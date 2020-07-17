\page adi ADI (3 Wire Ports)

\note 
For a full list of functions for interacting with the ADI, see its
: [C API](../../api/c/adi.html) and [C++ API](../../api/cpp/adi.html).

## Analog Sensors

While computers, microcontrollers, and other devices that interface with
VEX robots are digital systems, most of the real world operates as
analog components, where a range of possible values exist instead of
simply an arrangement of 1s and 0s. Analog sensors like potentiometers
and line trackers are used to communicate with these analog real-world
systems. These sensors return a number within a preset range of values
in accordance with their input, as opposed to a digit sensor which
simply returns an on or off state.

To take these analog inputs and convert them to information that the
Cortex can actually use, ADCs (Analog to Digital Converters) are used on
each of the Analog In ports to convert the analog input signals (varying
voltage signals) to 12 bit integers. As a result, the range of all
analog sensors when used with the Cortex is 0 to 4095 (the range of a 12
bit unsigned integer).

### Initialization

As with all ADI sensors, the first step to using the sensor is to set
the configuration for its ADI port.

Additionally, it is often worthwhile to calibrate analog sensors before
using them in the `initialize()` function. The
[analog_calibrate](../../api/c/adi.html#adi-analog-calibrate) function
collects approximately 500 data samples over a period of half a second
and returns the average value received over the sampling period. This
average value can be used to account for variations like ambient light
for line trackers.

### Potentiometer

Potentiometers measure angular position and can be used to determine the
direction of rotation of its input. Potentiometers are best used in
applications such as lifts where the sensor is not at risk of being
rotated beyond its 250-degree physical constraint. Potentiometers
typically do not need to be calibrated, although it may be desired as it
helps account for possible shifting in the potentiometer mounting and to
find the actual range of the potentiometer due to its mechanical stops
as that range may be closer to 5-4090 instead of 0-4095. If the
potentiometer is not calibrated, the
[analog_read](../../api/c/adi.html#adi-analog-read) function may be
used to obtain the raw input value of the potentiometer. If the sensor
was calibrated, the
[analog_read_calibrated](../../api/c/adi.html#adi-analog-read-calibrated)
function should be used, as it will account for the sensor's calibration
and return more accurate results. The input to both of these functions
is the channel number of the sensor, and an integer is returned.

Thus an example of use on a lift would look like:

### Line Tracker

VEX Line Trackers operate by measuring the amount of light reflected to
the sensor and determining the existence of lines from the difference in
light reflected by the white tape and the dark tiles. The Line Trackers
return a value between 0 and 4095, with 0 being the lightest reading and
4095 the darkest. It is recommended that Line Trackers be calibrated to
account for changes in ambient light.

An example of Line Tracker use:

### Accelerometer

The VEX Accelerometer measures acceleration on the x, y, and z axes
simultaneously. Accelerometers can be used to infer velocity and
displacement, but due to the error induced by such integration it is
recommended that simply the acceleration data be used. By design of the
VEX Accelerometer each axis is treated as its own analog sensors. Due to
this the VEX Accelerometer requires three analog input ports on the
Cortex.

Example accelerometer use:

## Digital Sensors

### Initialization

As with all ADI sensors, the first step to using the sensor is to set
the configuration for its ADI port.

From there, using a digital sensor is fairly straightforward. Digital
Sensors always return a true or false (boolean) value.

### Quad Encoder

Quadrature encoders can measure the rotation of the attached axle on
your robot. Most common uses of this sensor type are to track distance
traveled by attaching them to your robots drivetrain and monitoring how
much the axle spins.

With these sensors 1 measured tick is 1 degree of revolution.

\note
Encoders must be plugged into the ADI such that the top wire
is in an odd numbered port (1, 3, 5, 7 or 'A', 'C', 'E', or 'G'),
and then the bottom wire must be in the next highest port number.
Encoders are initialized as such:
```{.c}
 void initialize() {
   encoder = adi_encoder_init(QUAD_TOP_PORT, QUAD_BOTTOM_PORT, false);
 }
 ```

And then used in the following manner:

### Ultrasonic

Ultrasonic sensors are used in a manner that is very similar to
encoders, given that they are both two-wire sensors.

\note
Ultrasonic sensors must be plugged into the ADI such that the PING wire
(the orange OUTPUT cable) is in an odd numbered port (1, 3, 5, 7
or 'A', 'C', 'E', or 'G'), and then the ECHO wire (the yellow
INPUT cable) must be in the next highest port number.
Ultrasonic sensors are initialized as such:
 ```{.c}
void initialize() {
   ultrasonic = adi_ultrasonic_init(ULTRA_PING_PORT, ULTRA_ECHO_PORT);
 }
```

And then used in the following manner:

### Pneumatics

Pneumatics in VEX provide two-state linear actuation. They differ from
other digital sensors in that they are output signals. Therefore, the
default digital sensor configuration is insufficient.

And then the pneumatics are used as such:
