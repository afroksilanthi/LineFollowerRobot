from machine import Pin, PWM
from time import sleep, ticks_ms
from TrackerSensor import TrackerSensor

def percentage(percent):
    return int(65565 * (percent / 100))

# --- Parameters ---
# DC Motors
LMPins = { "RED" : 10, "BLACK" : 11 }
LMRed = pwmLMRed = LMBlack = pwmLMBlack = None
RMPins = { "RED" : 8,  "BLACK" : 9 }
RMRed = pwmRMRed = RMBlack = pwmRMBlack = None
MFreq = 200
MMax = 100 #90  # Maximum speed in percents

# IR Sensor array
ArrPins = {"IR2" : 28, "IR3" : 27, "IR4" : 26}
pins = [ArrPins["IR2"], ArrPins["IR3"], ArrPins["IR4"]]
sensor = TrackerSensor(pins)

# LED (for calibration status)
LEDPin = 0
led = Pin(LEDPin, Pin.OUT)

# --- Initialization ---
def MotorsInit():
    # Initialize motors and setup PWM to the desired frequency.
    global LMRed, pwmLMRed, LMBlack, pwmLMBlack
    global RMRed, pwmRMRed, RMBlack, pwmRMBlack
    
    # Left Motor (Red = Forward, Black = Backward)
    LMRed = Pin(LMPins["RED"], Pin.OUT)
    pwmLMRed = PWM(LMRed, freq=MFreq, duty_u16=0)
    LMBlack = Pin(LMPins["BLACK"], Pin.OUT)
    pwmLMBlack = PWM(LMBlack, freq=MFreq, duty_u16=0)
    
    # Right Motor (Red = Forward, Black = Backward)
    RMRed = Pin(RMPins["RED"], Pin.OUT)
    pwmRMRed = PWM(RMRed, freq=MFreq, duty_u16=0)
    RMBlack = Pin(RMPins["BLACK"], Pin.OUT)
    pwmRMBlack = PWM(RMBlack, freq=MFreq, duty_u16=0)
    
def MotorsValue(l, r):
    # Left Motor
    pwmLMRed.duty_u16(percentage(l))
    pwmLMBlack.duty_u16(0)
    # Right Motor
    pwmRMRed.duty_u16(percentage(r))
    pwmRMBlack.duty_u16(0)

def runCalibration():
    print("Calibrating...")
    led.value(1)
    start = ticks_ms()
    while (ticks_ms() - start < 2000):
        sensor.calibrate()
    led.value(0)
    print("Calibration complete")

# Run init functions
MotorsInit()
runCalibration()

# PID
Kp = 0.2  # Curve smoothness
Ki = 0#0.0001 #0.0005    # Add lag
Kd = 0.45    # Tight curve

# Init values
I = lastError = 0
LMSpeed = RMSpeed = 0

# Main
while True:
    if sensor.read_stopped() == True:
        sleep(0.1)
        if sensor.read_white() == True:
            pwmLMRed.duty_u16(0)
            pwmRMRed.duty_u16(0)
            break
    else:    
        # [-1000, 1000] where 0 means center
        error = sensor.read_line() - 1000
        
        P = error
        I = I + error
        D = error - lastError
        lastError = error
        pwr_diff = P*Kp + I*Ki + D*Kd
        
        # Check if the increase/reduction is above max
        if (pwr_diff > MMax):
            pwr_diff = MMax
        if (pwr_diff < -MMax):
            pwr_diff = -MMax
        
        # Increase / Reduce the motors
        if (pwr_diff < 0):
            LMSpeed = int(MMax + pwr_diff)
            RMSpeed = MMax
        else:
            LMSpeed = MMax
            RMSpeed = int(MMax - pwr_diff)
    
    MotorsValue(LMSpeed, RMSpeed)
    #print(f"L/R: {LMSpeed} / {RMSpeed}")
    
    sleep(0.01)

