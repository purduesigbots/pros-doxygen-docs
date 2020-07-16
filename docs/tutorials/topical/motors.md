# Motors

> **note**
>
> For a full list of functions for interacting with the V5 Motors, see its
> : [C API](../../api/c/motors.html) and [C++
> API](../../api/cpp/motors.html).

## Initialization

V5 Motors should be configured before use in your code. Configuration
options like the gearset and encoder units are important to address
first thing in your user program to ensure that functions like
[motor_move_velocity](../../api/c/motors.html#motor-move-velocity)
will work as expected.

When declaring motors in C++, it is not necessary to set the
configuration for the motor with its constructor (beyond its port
number) more than once for the given port. An example of this is given
below.

> > ```{.cpp}
> > #define MOTOR_PORT 1
> >
> > void opcontrol() {
> >   pros::Motor drive_left (MOTOR_PORT);
> >   // drive_left will have the same configuration as drive_left_initializer
> > }
> > ```

## Simple Usage

The easiest way to interact with the motors is through the
[motor_move](../../api/c/motors.html#motor-move) function. This is
analogous to the [motorSet](../../../cortex/api/index.html#motorSet)
function from PROS 2.

## Autonomous Movement

The V5 Motors can move in a number of different ways that are better
suited towards autonomous movement than the simple `motor_move()`
example shown above.

### Profile Movements

Profile movements are movements to a given position that are executed by
the motor's firmware. There are two functions that achieve this,
`motor_move_absolute()` and `motor_move_relative()`. These two functions
are practically similar, but `motor_move_relative()` takes into account
the zero position of the motor's encoder.

These functions are very well suited to movement in autonomous.

For further reading material on the algorithms that create these
profiled movement, see [Mathematics of Motion Control
Profiles](https://pdfs.semanticscholar.org/a229/fdba63d8d68abd09f70604d56cc07ee50f7d.pdf)
for the
[Feedforward](<https://en.wikipedia.org/wiki/Feed_forward_(control)>)
control, and [George Gillard's PID
Explanation](http://georgegillard.com/documents/2-introduction-to-pid-controllers)
for the
[feedback](https://en.wikipedia.org/wiki/Control_theory#PID_feedback_control)
control.

### Velocity Controller Movement

The final `move` function available with the PROS Motor API is
`motor_move_velocity()`. This ensures consistent velocity output from
the motor through the use of
[PID](http://georgegillard.com/documents/2-introduction-to-pid-controllers).

## Telemetry

The V5 motors return a plethora of diagnostic information about their
performance. The motors return the following parameters:

Parameter C Function C++ Function

---

Position [motorggetpposition](../../api/c/motors.html#motor-get-position) [pros::Motor::get_position](get_position_)
Velocity [motorggetaactualvvelocity](../../api/c/motors.html#motor-get-actual-velocity) [pros::Motor::get_actual_velocity](get_actual_velocity_)
Current [motorggetccurrentddraw](../../api/c/motors.html#motor-get-current-draw) [pros::Motor::get_current_draw](get_current_draw_)
Efficiency [motorggeteefficiency](../../api/c/motors.html#motor-get-efficiency) [pros::Motor::get_efficiency](get_efficiency_)
Power [motorggetppower](../../api/c/motors.html#motor-get-power) [pros::Motor::get_power](get_power_)
Temperature [motorggetttemperature](../../api/c/motors.html#motor-get-temperature) [pros::Motor::get_temperature](get_temperature_)
Torque [motorggetttorque](../../api/c/motors.html#motor-get-torque) [pros::Motor::get_torque](get_torque_)
Voltage [motorggetvvoltage](../../api/c/motors.html#motor-get-voltage) [pros::Motor::get_voltage](get_voltage_)
Direction [motorggetddirection](../../api/c/motors.html#motor-get-direction) [pros::Motor::get_direction](get_direction_)
