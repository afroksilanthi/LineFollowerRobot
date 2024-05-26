# Documentation for Line Follower
![Static Badge](https://img.shields.io/badge/MicroPython-%232b2728?style=flat-square&logo=micropython)
![Static Badge](https://img.shields.io/badge/Raspberry%20Pi%20Pico-%23a22846?style=flat-square&logo=raspberrypi)

Robot for following a line using simple parts and best performance.<br>
Written in [micropython](https://docs.micropython.org/en/latest/).

## Getting Started
### 💻 Setup
Install the approriate firmware on your Pico microcontroller from [here](https://micropython.org/download/).

Using [Thonny](https://thonny.org/), you may copy the files in the microcontroller and rename **code.py** to **main.py**.

### 📍 Use
Before powering up the board, place the robot on top of the track. After turning on, there is a 2 seconds calibration delay that assigns the white and black values.

### ⚙️ Parts
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
 Returns: *Number*

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

- **class TrackerSensor()**<br>
*Library to communicate with the Waveshare Tracker Sensor*<br>
 Parameters: *ArrayPins*<br>
 
    - **calibrate()**<br>
       *Assign sensor min and max values*<br>
       Parameters: *None*<br>
       Returns: *None*

     - **read_calibrated()**<br>
       *Calibrates and normalizes sensor values according to min and max in range 0-1000*<br>
       Parameters: *None*<br>
       Returns: *List*

     - **read_line()**<br>
       *Calculates the position of the line*<br>
       Parameters: *None*<br>
       Returns: *Number*

     - **read_stopped()**<br>
       *Checks if the robot sees a stopping line*<br>
       Parameters: *None*<br>
       Returns: *Boolean*

     - **read_white()**<br>
       *Checks if the robot is located in a white space*<br>
       Parameters: *None*<br>
       Returns: *Boolean*
