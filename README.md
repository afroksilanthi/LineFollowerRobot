# Documentation for Line Follower
Robot for following a line using simple parts and best performance.<br>
Written in [micropython](https://docs.micropython.org/en/latest/).

## Getting Started
### Setup
### Usage
### Parts
* Maker Pi RP2040
* Tracker Sensor (5 Channel IR sensor)
* 2pcs DC Electric Motor & tire wheel
* Battery box with 4 compartments
* 4 Batteries Alkaline AA 1.5V
* Casper wheel
* Plywood Chassis

## Algorithm
#### 💡 PID controller algorithm

The **P**roportional-**I**ntegral-**D**erivative **(PID)** algorithm, describes how the error term is handled.
The PID controller is used for reading the sensor, then compute the desired actuator output by calculating *proportional*, *integral*, and *derivative* responses and summing those three components to compute the output.<br><br>
These are the three non-negative tuning parameters that are summed to calculate the output of the PID controller:
   - **Kp :** proportional gain.
   - **Ki :** integral gain.
   - **Kd :** derivative gain.

&nbsp; The **proportional** term produces an output value that is proportional to the current error value. The proportional response can be adjusted by multiplying the error by a constant *Kp*, called the proportional gain constant.<br>
  
&nbsp;  The **integral** in a PID controller is the sum of the instantaneous error over time and gives the accumulated offset that should have been corrected previously. The accumulated error is then multiplied by the integral gain *(Ki)* and added to the controller output.<br>

&nbsp; The **derivative** of the process error is calculated by determining the slope of the error over time and multiplying this rate of change by the derivative gain *Kd*.<br>

All these, helped the robot to act faster, find the errors and move acurate when it comes to following a line.
## Functions
#### 📝 Function documentation
**code.py:**
- **percentage()**<br>
*Function that converts the speed value of the wheels, to an integer percentage value.*<br>
 Parameters: *percent* <br>
 Returns: *integer value of the speed percentage*

- **MotorsInit()**<br>
*Function that initialize the motors, connect them with the board pins and sets PWM to desired frequency.*<br>
 Parameters: *None*<br>
 Returns: *None*

- **MotorsValue()**<br>
*Function that sets the speed value of the motors.*<br>
 Parameters: *l,r*<br>
 Returns: *None*

- **runCalibration()**<br>
*Calibrates for better performance.*<br>
 Parameters: *None*<br>
 Returns: *None*

**TrackerSensor.py:**
