from machine import Pin, SoftI2C
from time import sleep_ms
import exPWM

# O canal do PCA9685 a ser usado é o canal 5.
CHANNEL = 5

# Cria instância do ExpandedPWM!
i2c = SoftI2C(scl=Pin(1), sda=Pin(0))
expwm = exPWM.base.ExpandedPWM(i2c)

# Testa os componentes da placa extensora. Atenção: A placa deve estar conectada nos pinos especificados na linha 9!
if expwm.scan():
  print("Placa extensora funcionando corretamente!")

# Configura a frequência do sistema PWM.
expwm.freqPWM(500)

# Loop principal.
while True:
  # Aumenta a potência do LED e depois diminui, gradativamente.
  for i in range(0, 4096):
    expwm.dutyPWM(CHANNEL, i)
    sleep_ms(5)
  for i in range(0, 4096):
    expwm.dutyPWM(CHANNEL, 4096 - i)
    sleep_ms(5)