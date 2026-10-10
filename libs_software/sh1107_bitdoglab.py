# ============================================================
# sh1107_bitdoglab.py
#                        versão: outubro de 2026 - Fruett
# Driver MicroPython para OLED SH1107 128x128
# BitDogLab
#
# Interface:
#   I2C
#
# Configuração BitDogLab:
#   I2C1
#   SDA = GP2
#   SCL = GP3
#   endereco = 0x3C
#
# ============================================================

import framebuf
from time import sleep_ms


class SH1107_I2C(framebuf.FrameBuffer):

    def __init__(
        self,
        width,
        height,
        i2c,
        addr=0x3C,
        rotate_180=False,
        column_offset=0
    ):

        self.width = width
        self.height = height

        self.i2c = i2c
        self.addr = addr

        self.rotate_180 = rotate_180
        self.column_offset = column_offset


        # ====================================================
        # FRAMEBUFFER
        #
        # 128 x 128 / 8 = 2048 bytes
        # ====================================================

        self.buffer = bytearray(
            self.width
            * self.height
            // 8
        )


        super().__init__(
            self.buffer,
            self.width,
            self.height,
            framebuf.MONO_VLSB
        )


        # ====================================================
        # POWER-UP
        # ====================================================

        sleep_ms(
            150
        )


        # inicializa controlador
        self.init_display()


        # ====================================================
        # PRIMEIRA LIMPEZA
        # ====================================================

        self.fill(
            0
        )

        self.show()


        sleep_ms(
            30
        )


        # ====================================================
        # DISPLAY ON
        # ====================================================

        self.poweron()


        sleep_ms(
            80
        )


        # ====================================================
        # REFORÇA REGISTRADORES CRÍTICOS
        # ====================================================

        self.force_state()


        # ====================================================
        # SEGUNDA LIMPEZA
        # ====================================================

        self.fill(
            0
        )

        self.show()


        sleep_ms(
            30
        )


    # ========================================================
    # ENVIA COMANDO
    # ========================================================

    def write_cmd(
        self,
        cmd
    ):

        self.i2c.writeto(
            self.addr,
            bytes(
                (
                    0x00,
                    cmd
                )
            )
        )


    # ========================================================
    # ENVIA UMA PÁGINA COMPLETA
    #
    # 1 byte de controle + 128 bytes
    # ========================================================

    def write_page(
        self,
        data
    ):

        pacote = bytearray(
            len(data) + 1
        )


        # byte de controle:
        # próximos bytes são dados
        pacote[0] = 0x40


        pacote[1:] = data


        self.i2c.writeto(
            self.addr,
            pacote
        )


    # ========================================================
    # CONFIGURA COLUNA
    # ========================================================

    def set_column(
        self,
        coluna
    ):

        coluna += self.column_offset


        # nibble inferior
        self.write_cmd(
            0x00
            | (
                coluna
                & 0x0F
            )
        )


        # nibble superior
        self.write_cmd(
            0x10
            | (
                (
                    coluna
                    >> 4
                )
                & 0x0F
            )
        )


    # ========================================================
    # FORÇA ESTADO PRINCIPAL DO SH1107
    # ========================================================

    def force_state(
        self
    ):

        # ----------------------------------------------------
        # Memory Mode / Page Addressing
        # ----------------------------------------------------

        self.write_cmd(
            0x20
        )


        # ----------------------------------------------------
        # Display Start Line = 0
        #
        # SH1107:
        # 0xDC + valor
        # ----------------------------------------------------

        self.write_cmd(
            0xDC
        )

        self.write_cmd(
            0x00
        )


        # ----------------------------------------------------
        # Display Offset = 0
        # ----------------------------------------------------

        self.write_cmd(
            0xD3
        )

        self.write_cmd(
            0x00
        )


        # ----------------------------------------------------
        # Orientação
        # ----------------------------------------------------

        if self.rotate_180:

            self.write_cmd(
                0xA1
            )

            self.write_cmd(
                0xC8
            )

        else:

            self.write_cmd(
                0xA0
            )

            self.write_cmd(
                0xC0
            )


        # ----------------------------------------------------
        # mostra conteúdo da RAM
        # ----------------------------------------------------

        self.write_cmd(
            0xA4
        )


        # ----------------------------------------------------
        # modo normal
        # ----------------------------------------------------

        self.write_cmd(
            0xA6
        )


        # ----------------------------------------------------
        # página inicial
        # ----------------------------------------------------

        self.write_cmd(
            0xB0
        )


        # ----------------------------------------------------
        # coluna inicial
        # ----------------------------------------------------

        self.set_column(
            0
        )


    # ========================================================
    # INICIALIZAÇÃO COMPLETA
    # ========================================================

    def init_display(
        self
    ):

        # ====================================================
        # DISPLAY OFF
        # ====================================================

        self.write_cmd(
            0xAE
        )

        sleep_ms(
            30
        )


        # ====================================================
        # MEMORY MODE
        #
        # Page Addressing Mode
        # ====================================================

        self.write_cmd(
            0x20
        )


        # ====================================================
        # CLOCK
        # ====================================================

        self.write_cmd(
            0xD5
        )

        self.write_cmd(
            0x50
        )


        # ====================================================
        # CONTRASTE
        # ====================================================

        self.write_cmd(
            0x81
        )

        self.write_cmd(
            0x80
        )


        # ====================================================
        # MULTIPLEX
        #
        # 128 linhas -> 0x7F
        # ====================================================

        self.write_cmd(
            0xA8
        )

        self.write_cmd(
            0x7F
        )


        # ====================================================
        # DISPLAY START LINE = 0
        #
        # IMPORTANTE:
        #
        # SH1107 usa:
        #
        # 0xDC
        # 0x00
        # ====================================================

        self.write_cmd(
            0xDC
        )

        self.write_cmd(
            0x00
        )


        # ====================================================
        # DISPLAY OFFSET = 0
        # ====================================================

        self.write_cmd(
            0xD3
        )

        self.write_cmd(
            0x00
        )


        # ====================================================
        # DC-DC INTERNO
        # ====================================================

        self.write_cmd(
            0xAD
        )

        self.write_cmd(
            0x8B
        )


        sleep_ms(
            50
        )


        # ====================================================
        # ORIENTAÇÃO
        # ====================================================

        if self.rotate_180:

            # segment remap
            self.write_cmd(
                0xA1
            )

            # COM scan invertido
            self.write_cmd(
                0xC8
            )

        else:

            self.write_cmd(
                0xA0
            )

            self.write_cmd(
                0xC0
            )


        # ====================================================
        # PRE-CHARGE
        # ====================================================

        self.write_cmd(
            0xD9
        )

        self.write_cmd(
            0x22
        )


        # ====================================================
        # VCOM DESELECT
        # ====================================================

        self.write_cmd(
            0xDB
        )

        self.write_cmd(
            0x35
        )


        # ====================================================
        # DISPLAY RAM
        # ====================================================

        self.write_cmd(
            0xA4
        )


        # ====================================================
        # NORMAL DISPLAY
        # ====================================================

        self.write_cmd(
            0xA6
        )


        # ====================================================
        # PÁGINA ZERO
        # ====================================================

        self.write_cmd(
            0xB0
        )


        # ====================================================
        # COLUNA ZERO
        # ====================================================

        self.set_column(
            0
        )


        sleep_ms(
            30
        )


    # ========================================================
    # SHOW
    #
    # 128 linhas / 8 = 16 páginas
    #
    # Cada página:
    #   128 bytes
    # ========================================================

    def show(
        self
    ):

        pages = (
            self.height
            // 8
        )


        for page in range(
            pages
        ):

            # ------------------------------------------------
            # seleciona página
            # ------------------------------------------------

            self.write_cmd(
                0xB0
                | page
            )


            # ------------------------------------------------
            # volta explicitamente à coluna inicial
            # ------------------------------------------------

            self.set_column(
                0
            )


            # ------------------------------------------------
            # trecho do framebuffer
            # ------------------------------------------------

            inicio = (
                page
                * self.width
            )

            fim = (
                inicio
                + self.width
            )


            # ------------------------------------------------
            # envia página inteira em uma única transação
            # ------------------------------------------------

            self.write_page(
                self.buffer[
                    inicio:fim
                ]
            )


    # ========================================================
    # RECUPERA CONTROLADOR
    # ========================================================

    def recover(
        self
    ):

        try:

            # display off
            self.poweroff()


            sleep_ms(
                100
            )


            # reinicializa registradores
            self.init_display()


            # limpa RAM
            self.fill(
                0
            )

            self.show()


            sleep_ms(
                30
            )


            # liga novamente
            self.poweron()


            sleep_ms(
                100
            )


            # força novamente o estado
            self.force_state()


            self.fill(
                0
            )

            self.show()


            return True


        except Exception as e:

            print(
                "Erro recover SH1107:",
                e
            )

            return False


    # ========================================================
    # CONTRASTE
    # ========================================================

    def contrast(
        self,
        value
    ):

        value = max(
            0,
            min(
                255,
                value
            )
        )


        self.write_cmd(
            0x81
        )

        self.write_cmd(
            value
        )


    # ========================================================
    # INVERTE DISPLAY
    # ========================================================

    def invert(
        self,
        invert=True
    ):

        if invert:

            self.write_cmd(
                0xA7
            )

        else:

            self.write_cmd(
                0xA6
            )


    # ========================================================
    # DISPLAY OFF
    # ========================================================

    def poweroff(
        self
    ):

        self.write_cmd(
            0xAE
        )


    # ========================================================
    # DISPLAY ON
    # ========================================================

    def poweron(
        self
    ):

        self.write_cmd(
            0xAF
        )
