'''!
@file main.py
@author Jeremy Baechler
@author Kendall Chappell
@author Matt Wimberley
'''

import utime

def led_setup():
    global ch1
    pinA0 = pyb.Pin (pyb.Pin.board.PA0, pyb.Pin.OUT_PP)
    tim2 = pyb.Timer (2, freq=20000)
    ch1 = tim2.channel (1, pyb.Timer.PWM_INVERTED, pin=pinA0)

def led_brightness(bright):
    ch1.pulse_width_percent(bright)

    
if __name__ == '__main__':
    current_time = utime.ticks_us()
    led_setup()
    while True:
        new_time = utime.ticks_us()
        diff = utime.ticks_diff(new_time, current_time)/1000000
        if diff >= 0 and diff < 5:
            bright = 20*(diff)
            led_brightness(bright)
        elif diff >=5 and diff < 10:
            bright = 100- 20*(diff-5)
            led_brightness(bright)
        else:
            current_time = utime.ticks_us()
        print(bright, diff)
            