import machine, time

def percentage(percent):
    return int(65565 * (percent / 100))

# --- Parameters ---
# DC Motors
LMPins = { "RED" : 10, "BLACK" : 11 }
LMRed = pwmLMRed = LMBlack = pwmLMBlack = None
RMPins = { "RED" : 8,  "BLACK" : 9 }
RMRed = pwmRMRed = RMBlack = pwmRMBlack = None
MFreq = 200

# IR Sensors
IRPins = { "LEFT" : 17, "RIGHT" : 26 }
RInfrared = LInfrared = None

# PID
Kp = 6.5     # Curve smoothness
Ki = 0.0001  # Reduce oscillation
Kd = 0.6     # Tight curve

# --- Initialization ---
def MotorsInit():
    # Initialize motors and setup PWM to the desired frequency.
    global LMRed, pwmLMRed, LMBlack, pwmLMBlack
    global RMRed, pwmRMRed, RMBlack, pwmRMBlack
    
    # Left Motor (Red = Forward, Black = Backward)
    LMRed = machine.Pin(LMPins["RED"], machine.Pin.OUT)
    pwmLMRed = machine.PWM(LMRed, freq=MFreq, duty_u16=0)
    LMBlack = machine.Pin(LMPins["BLACK"], machine.Pin.OUT)
    pwmLMBlack = machine.PWM(LMBlack, freq=MFreq, duty_u16=0)
    
    # Right Motor (Red = Forward, Black = Backward)
    RMRed = machine.Pin(RMPins["RED"], machine.Pin.OUT)
    pwmRMRed = machine.PWM(RMRed, freq=MFreq, duty_u16=0)
    RMBlack = machine.Pin(RMPins["BLACK"], machine.Pin.OUT)
    pwmRMBlack = machine.PWM(RMBlack, freq=MFreq, duty_u16=0)

def InfraredInit():
    # Initialize all infrared sensor pins with default state set to 0.
    global RInfrared, LInfrared
    
    # Right IR Sensor
    RInfrared = machine.Pin(IRPins["RIGHT"], machine.Pin.IN, machine.Pin.PULL_DOWN)
    # Left IR Sensor
    LInfrared = machine.Pin(IRPins["LEFT"], machine.Pin.IN, machine.Pin.PULL_DOWN)

# Run init functions
MotorsInit()
InfraredInit()

# --- Sensor readings ---
def IRPosition():
    # If black line is on the center then return 0
    # If black line is on the right then return 1
    # If black line is on the left then return -1
    return (RInfrared.value() - LInfrared.value())

# Initial values
I = 0
LMSpeed = RMSpeed = 0
lastError = 0

# Main loop
while True:
    error = IRPosition()
    #print(f'Error: {error}')
    time.sleep(0.1)
    
    P = error
    I = I + error
    D = error - lastError
    lastError = error

    motorSpeed = P*Kp + I*Ki + D*Kd
    #print(f'PID: {motorSpeed}')
    
    LMSpeed_per = LMSpeed + motorSpeed
    if LMSpeed_per > 100:
        LMSpeed_per = 100
    elif LMSpeed_per < 0:
        LMSpeed_per = 0
    #print(f'Speed Left: {LMSpeed_per}')

    RMSpeed_per = RMSpeed - motorSpeed
    if RMSpeed_per > 100:
        RMSpeed_per = 100
    elif RMSpeed_per < 0:
        RMSpeed_per = 0
    #print(f'Speed Right: {RMSpeed_per}')

    LMSpeed = LMSpeed_per
    pwmLMRed.duty_u16(percentage(LMSpeed))
    pwmLMBlack.duty_u16(0)
    
    RMSpeed = RMSpeed_per
    pwmRMRed.duty_u16(percentage(RMSpeed))
    pwmRMBlack.duty_u16(0)

