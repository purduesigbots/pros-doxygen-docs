\page motors Motors

\note
For a full list of functions for interacting with the V5 Motors, see its
[C API](@ref c-motors) and [C++ API](@ref cpp-motors).

## Initialization

V5 Motors should be configured before use in your code. Configuration
options like the gearset and encoder units are important to address
first thing in your user program to ensure that functions like
`motor_move_velocity()`
will work as expected.

When declaring motors in C++, it is not necessary to set the
configuration for the motor with its constructor (beyond its port
number) more than once for the given port. You may also reverse motors by passing the port number of the motor, but negative. An example of this is given
below.

```{.cpp}
#define MOTOR_PORT 1
#define REVERSED_MOTOR_PORT -2
void opcontrol() {
	pros::Motor drive_left (MOTOR_PORT);
	// drive_left will have the same configuration as drive_left_initializer

	pros::Motor drive_right (REVERSED_MOTOR_PORT);
	// drive_right is the reversed version of the motor on port two
}
```

## Motor Groups

In C++, V5 Motors can be configured together within a motor group to perform actions together. When declaring motor groups, you can pass a vector of the ports that the motors exist at. Then you can call motor functions (such as move) for the entire motor group. An example of this is given below.

```{.cpp}
#define MOTOR_PORT 1
#define REVERSED_MOTOR_PORT -2
void opcontrol() {
	pros::MotorGroup my_motor_group ({MOTOR_PORT, REVERSED_MOTOR_PORT});
	my_motor_group.move(100);
	pros::delay(1000);
}
```

## Simple Usage

The easiest way to interact with the motors is through the
`motor_move()`function.

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
