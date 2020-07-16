# Controller

> **note**
>
> For a full list of functions for interacting with the V5 Controller, see its
> : [C API](../../api/c/misc.html) and [C++
> API](../../api/cpp/misc.html).
>
> Feedback from the V5 Controller comes in two forms - analog and digital.
> The analog data comes from the
> [joysticks](https://en.wikipedia.org/wiki/Analog_stick), and the digital
> data comes from the buttons.

The analog data is a value in the range of [-127,127], and digital data
is either 1 or 0 (pressed or unpressed, respectively).

## Analog Data

Retrieve analog values from the V5 Controller in the following manner:

The controller returns a range of [-127,127] for analog data, which is
why the [motor_move](../../api/c/motors.html#motor-move) function is
appropriate for easy use with the controllers.

## Digital Data

Retrieve Digital Values from the V5 Controller in the following manner:
