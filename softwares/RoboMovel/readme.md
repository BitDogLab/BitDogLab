# 🤖 Robô Móvel Skid-Steer — BitDogLab

Este projeto implementa o controle completo de um **robô móvel 4x4 tipo Skid-Steer** desenvolvido para a **placa BitDogLab (v6 ou v7)**.  
O robô é controlado via **Bluetooth** por aplicativos Android e utiliza um **Raspberry Pi Pico / Pico W** programado em **MicroPython**.

---

> ⚠️ **Importante:**  
> O arquivo no repositório se chama:
> ```
> movimentacaoBluetooth_buzina_luz.py
> ```
>  
> Ao enviar para a placa BitDogLab usando o **Thonny**, salve o arquivo com o nome:
> ```
> main.py
> ```
> Assim, o código será executado automaticamente quando o robô for ligado.

---

## 🧩 Lista de componentes

| Componente | Descrição |
|-------------|------------|
| **Placa BitDogLab** | Versão v6 ou v7 com Raspberry Pi Pico / Pico W |
| **Motores TT DC** | 4 motores 3–6 V com redutor e rodas de 68 mm |
| **Conexões dos motores** | 2 traseiros (master) → JST-SH 2P + jumpers fêmea soldados<br>2 dianteiros (slave) → jumpers macho soldados |
| **Chassis** | Impressão 3D em ABS — modelo v4 |
| **Mãos-francesas (suportes laterais)** | Impressas em ABS — modelo v3<br>Fixadas com **fita dupla-face** |
| **Parafusos e porcas** | 4x M3x25 + 4x M3 |
| **Ponte H** | Módulo **TB6612FNG** (integrado à PCB BitDogLab) |
| **Cabo flat IDC 2x7** | Conecta placa BitDogLab à ponte H |
| **Suporte de bateria** | 2x células 18650 Li-ion |
| **Baterias** | 2x 18650 (3.7 V) — total ~7.4 V |
| **Conector de energia** | XT30 macho |
| **Módulo Bluetooth** | HC-05 |
| **Adesivo dupla-face** | Para fixação dos suportes |

---

## 📱 Aplicativos Android compatíveis

O robô é controlado via **Bluetooth UART** usando os seguintes aplicativos (disponíveis no Google Play):

- **Arduino Bluetooth Controller** (por *Giristudio*)  
- **BT Car Controller - Arduino/ESP** (por *Giristudio*)

Ao apertar botões no aplicativo, ambos enviam comandos seriais simples (`F`, `B`, `L`, `R`, etc.) via Bluetooth.

---

## 🧠 Funcionalidades principais

| Função | Descrição |
|--------|------------|
| 🔄 **Movimento Skid-Steer 4x4** | Controle diferencial de dois lados independentes (esquerdo e direito). |
| 💡 **Controle de LEDs NeoPixel** | Iluminação RGB com ajuste de brilho e modos de luz. |
| 🔊 **Buzina sonora** | Alterna entre sons “Beep Beep” e “Foon Foon”. |
| 🔌 **Comunicação Bluetooth (UART)** | Recebe comandos em tempo real de um app Android. |
| ⚙️ **Controle de velocidade** | Ajustável de 0 a 9 (PWM). |

---

## 🪄 Sub-rotinas principais no código

O código **`movimentacaoBluetooth_buzina_luz.py`** é estruturado em funções que organizam o comportamento do robô.  
Algumas das subrotinas mais relevantes são:

| Função | Descrição |
|---------|-----------|
| `configura_pwm_motores()` | Inicializa o PWM dos motores e define o duty cycle padrão. |
| `move_frente()`, `move_tras()`, `vira_esquerda()`, `vira_direita()` | Controlam os quatro motores de forma coordenada. |
| `para_motores()` | Envia duty 0 para todos os motores (freio eletrônico). |
| `beep()` e `foon()` | Geram dois tipos distintos de som no buzzer PWM. |
| `alterna_som()` | Alterna entre os modos de buzina (“Beep” ↔ “Foon”). |
| `acende_leds(cor, brilho)` | Define a cor e intensidade dos LEDs NeoPixel. |
| `alterna_modo_luz()` | Cicla entre quatro modos de iluminação: apagado → fraco → apagado → forte. |
| `ajusta_brilho(delta)` | Aumenta ou diminui o brilho manualmente via comandos `+` e `-`. |
| `processa_comando_uart(cmd)` | Lê e executa os comandos recebidos via Bluetooth. |

---

## 🔤 Comandos via Bluetooth

| Comando | Ação |
|----------|------|
| `F` | Avança |
| `B` | Recuo |
| `L` | Vira à esquerda |
| `R` | Vira à direita |
| `S` | Para |
| `0–9` | Define velocidade (PWM) |
| `W` | Liga luz branca |
| `i` | Desliga luz |
| `I` / `X` | Alterna modos de luz |
| `+` / `-` | Ajusta brilho manualmente |
| `Y` | Alterna som da buzina |

---

## 🧱 Modelos 3D (impressão)

Os arquivos STL do robô estão disponíveis para **impressão 3D em ABS**:

| Arquivo | Função |
|----------|--------|
| `ABS_1.0070_chassis_para_4x4_v4.STL` | Chassis principal |
| `ABS_dir_1.0071_suporteBitDog_MaoFrancesa_v3.STL` | Suporte lateral direito (“mão francesa”) |
| `ABS_esq_1.0071_suporteBitDog_MaoFrancesa_v3.STL` | Suporte lateral esquerdo (“mão francesa”) |

As mãos francesas são fixadas ao chassis com **fita dupla-face**.

---

## ⚡ Alimentação

- 2x baterias **Li-ion 18650 (3.7 V)** em série → **7.4 V nominal**
- Conector **XT30**
- Corrente típica: 0.5–2 A total
- Pode ser recarregado externamente com carregador balanceado ou módulo BMS

---

## 🧰 Como gravar o programa

1. Abra o **Thonny IDE**.  
2. Conecte o Raspberry Pi Pico (BitDogLab).  
3. Abra o arquivo `movimentacaoBluetooth_buzina_luz.py`.  
4. Salve-o no dispositivo com o nome **`main.py`**.  
   - Menu: *Arquivo → Salvar como... → Raspberry Pi Pico → main.py*  
5. Reinicie a BitDogLab — o programa iniciará automaticamente.

---

## 🧪 Teste rápido

1. Conecte o módulo **HC-05** ao smartphone Android.  
2. Abra um dos aplicativos Bluetooth acima.  
3. Aperte botões da buzina e luz
4. Observe a resposta luminosa/sonora do robô.
5. Se funcionar, então você pode usar a movimentação normalmente.

---

## 🧑‍🔬 Créditos

**Projeto BitDogLab — Robô Móvel Skid-Steer**  
Campinas – SP 🇧🇷  
