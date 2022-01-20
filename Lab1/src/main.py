'''
@file main.py
'''

import pyb, utime

ENA = pyb.Pin (pyb.Pin.board.PA10, pyb.Pin.OPEN_DRAIN, pull=pyb.Pin.PULL_UP)
IN1 = pyb.Pin (pyb.Pin.board.PB4, pyb.Pin.OUT_PP)
IN2 = pyb.Pin (pyb.Pin.board.PB5, pyb.Pin.OUT_PP)
# pinB6 = pyb.Pin (pyb.Pin.board.PB6, pyb.Pin.IN)
# pinB7 = pyb.Pin (pyb.Pin.board.PB7, pyb.Pin.IN)
# pinC6 = pyb.Pin (pyb.Pin.board.PC6, pyb.Pin.IN)
# pinC7 = pyb.Pin (pyb.Pin.board.PC7, pyb.Pin.IN)
ENA.high()

tim3 = pyb.Timer (3, freq=20000)
t3ch1 = tim3.channel (1, pyb.Timer.PWM, pin=IN1)
t3ch2 = tim3.channel (2, pyb.Timer.PWM, pin=IN2)

# tim4 = pyb.Timer (4, prescaler=1, period = 65535)
# t4ch1 = tim4.channel (1, pyb.Timer.ENC_AB, pin=pinB6)
# t4ch2 = tim4.channel (2, pyb.Timer.ENC_AB, pin=pinB7)
# 
# tim8 = pyb.Timer (8, prescaler=1, period = 65535)
# t8ch1 = tim8.channel (1, pyb.Timer.ENC_AB, pin=pinC6)
# t8ch2 = tim8.channel (2, pyb.Timer.ENC_AB, pin=pinC7)

t3ch1.pulse_width_percent(0)
t3ch2.pulse_width_percent(100)

# while True:
#     print(tim8.counter())
#     utime.sleep_ms(10)


# tim3 = pyb.Timer (3, freq=20000)
# t3ch1 = tim3.channel(1, pyb.Timer.PWM, pin=ENA)
