'''
@file      motor_baechler_chappell_wimberley.py
@brief     sets up motor driver
@details   instantiates timer channels within constructor and sets motor duty cycle

@author    Jeremy Baechler
@author    Kendall Chappell
@author    Matthew Wimberley
@date      20-Jan-2022
'''

class MotorDriver():
    
    def __init__(self, en_pin, IN1, IN2, timer):
        self.ENA = en_pin
        self.IN1 = IN1
        self.IN2 = IN2
        self.timer = timer
        self.timchan1 = self.timer.channel (1, pyb.Timer.PWM, pin=self.IN1)
        self.timchan2 = self.timer.channel (1, pyb.Timer.PWM, pin=self.IN2)
    
    def set_duty(self, duty):
        self.ENA.high()
        if duty>0:
#             print('inside function')
            self.timchan1.pulse_width_percent(0)
            self.timchan2.pulse_width_percent(duty)
        elif duty<=0:
            self.timchan1.pulse_width_percent(abs(duty))
            self.timchan2.pulse_width_percent(0)

if __name__ == '__main__':
<<<<<<< HEAD
    '''@brief   testing block
    '''
    import pyb
    
    ENA = pyb.Pin (pyb.Pin.board.PA10, pyb.Pin.OUT_PP)
=======
    ENA = pyb.Pin (pyb.Pin.board.PA10, pyb.Pin.OPEN_DRAIN, pull=pyb.Pin.PULL_UP)
>>>>>>> 0142c1007d3044d87c702879d2fbf33138833afe
    IN1 = pyb.Pin (pyb.Pin.board.PB4, pyb.Pin.OUT_PP)
    IN2 = pyb.Pin (pyb.Pin.board.PB5, pyb.Pin.OUT_PP)
    tim3 = pyb.Timer (3, freq=20000)
    mot1 = MotorDriver(ENA, IN1, IN2, tim3)
    mot1.set_duty(50)
            
