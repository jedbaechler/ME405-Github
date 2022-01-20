'''
@file      EncoderReader.py
@brief     sets up encoder to be able to read values past 65535
@details   holds onto last value at each read, so negative values 
           and very large values can be stored and read with no hard limit 

@author    Jeremy Baechler
@author    Kendall Chappell
@author    Matthew Wimberley
@date      20-Jan-2022
'''

import pyb
import motor_baechler_chappell_wimberley.py

class EncoderReader:


    '''@brief       sets up class encoder to be used locally by other programs
       @details     saves last value of each cycle to be added or subtracted
       '''
       
    current_position = 0
    delta = 0

    def __init__(self, enc_number):
        

        
        if enc_number == 1:
            '''@brief   sets up first encoder'''
            
            self.timer = pyb.Timer(4, prescaler = 0, period = 65535)
            self.ch1 = self.timer.channel(1, pyb.Timer.ENC_AB, pin = pyb.Pin.cpu.B6)
            self.ch2 = self.timer.channel(2, pyb.Timer.ENC_AB, pin = pyb.Pin.cpu.B7)
            
        elif enc_number ==2:
            '''@brief   sets up second encoder'''
        
            self.timer = pyb.Timer(8, prescaler = 0, period = 65535)
            self.ch1 = self.timer.channel(1, pyb.Timer.ENC_AB, pin = pyb.Pin.cpu.C6)
            self.ch2 = self.timer.channel(2, pyb.Timer.ENC_AB, pin = pyb.Pin.cpu.C7)  

    def read(self):

        
        '''@brief       needs at least 2 values in each period
           @details     if >=2 values then delta can be accurately recorded
                        saved and then subtracted from last known value '''
                        

        previous_position = self.current_position % 65535
        self.delta = self.timer.counter() - prev_position
        if self.delta < -65535/2:
            self.delta += 65535
        elif self.delta > 65535/2:
            self.delta -= 65535
        self.current_position += self.delta
        
    def zero(self):
        '''@brief       zeroes encoder position
        '''
        
        current_position = 0
        
if __name__ == "__main__":
    

    ENA = pyb.Pin (pyb.Pin.board.PA10, pyb.Pin.OUT_PP)
    IN1 = pyb.Pin (pyb.Pin.board.PB4, pyb.Pin.OUT_PP)
    IN2 = pyb.Pin (pyb.Pin.board.PB5, pyb.Pin.OUT_PP)
    tim3 = pyb.Timer (3, freq=20000)
    #motor = 
    moe = motor.MotorDriver(ENA, IN1, IN2, tim3)
    moe.set_duty_cycle(50)

    red = EncoderReader(1)
    red.read()