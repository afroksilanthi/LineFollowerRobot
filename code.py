import machine, time

#Left Motor
LMotorRedPin = machine.Pin(10, machine.Pin.OUT)#Forwards
LMotorBlackPin = machine.Pin(11, machine.Pin.OUT)#Backwards

#speed L
pwmLeftMotorR = machine.PWM(LMotorRedPin) #red, forwards
pwmLeftMotorR.freq(50)
pwmLeftMotorB = machine.PWM(LMotorBlackPin) #black, backwards
pwmLeftMotorB.freq(50)


#Right Motor
RMotorRedPin = machine.Pin(8, machine.Pin.OUT)#Front
RMotorBlackPin = machine.Pin(9, machine.Pin.OUT)#Back

#speed R
pwmRightMotorR = machine.PWM(RMotorRedPin) #red, forwards
pwmRightMotorR.freq(50)
pwmRightMotorB = machine.PWM(RMotorBlackPin) #black, backwards
pwmRightMotorB.freq(50)



while True:
# 1/4 speed
  #LEFT
   #front
#    LMotorRedPin.low()
    pwmLeftMotorR.duty_u16(16383)
    time.sleep(2)
   #back
   # LMotorBlackPin.low()
    pwmLeftMotorB.duty_u16(16383)
    time.sleep(2)

  #RIGHT
   #front
   # RMotorRedPin.low()
    pwmRightMotorR.duty_u16(16383)
    time.sleep(2)
   #back
  #  RMotorBlackPin.low()
    pwmRightMotorB.duty_u16(16383)
    time.sleep(2)


#1/2 speed: #32767
#full: #65535

def RForward():
    RMotorRedPin.value(1)
    RMotorBlackPin.value(0)
    
def RBackward():
    RMotorRedPin.value(0)
    RMotorBlackPin.value(1)

def RStop():
    RMotorRedPin.value(0)
    RMotorBlackPin.value(0)

def LForward():
    LMotorRedPin.value(1)
    LMotorBlackPin.value(0)
    
def LBackward():
    LMotorRedPin.value(0)
    LMotorBlackPin.value(1)

def LStop():
    LMotorRedPin.value(0)
    LMotorBlackPin.value(0)

#while True:
  #  RForward()
   # LForward()
    #time.sleep(0.3)

    #RStop()
    #LStop()
    #time.sleep(1)

   # RBackward()
   # LBackward()
   # time.sleep(0.3)

   # RStop()
   # LStop()
    #time.sleep(1)
