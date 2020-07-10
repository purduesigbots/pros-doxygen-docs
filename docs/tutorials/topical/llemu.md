LLEMU (Legacy LCD Emulator)
===========================

> **note**
>
> For a full list of functions for interacting with the LLEMU, see its
> :   [C API](../../api/c/llemu.html) and [C++
>     API](../../api/cpp/llemu.html).
>
Initialization
--------------

Initialization of the LLEMU is very simple, it's just a call to its
initialization function at whatever point in the program you would like
the LLEMU to start displaying (this will most likely be in
`initialize()`).

Initialization is done as such:

Writing to the LLEMU
--------------------

Writing to the LLEMU is nearly identical to writing to the LCD with
[PROS 2](../../cortex/tutorials/lcd.html). Most writing should be done
with the print function, which is analogous to
[printf](http://www.cplusplus.com/reference/cstdio/printf/).

Using the Buttons
-----------------

Using the buttons can be done in a similar method to [PROS
2](../../../cortex/tutorials/lcd.html) with the
[pros::lcd::read\_buttons](../../api/cpp/llemu.html#read-buttons)
function. See the above example for printing the button readings.

While this is sufficient for most applications, some tasks are easier to
perform using the
[pros::lcd::register\_btn\#\_cb](../../api/cpp/llemu.html#register-btn0-cb)
functions (where \# is replaced with 0, 1, or 2 for the left, center,
and right buttons respectively). With these function you can assign a
function to be called each time that the button is pressed.

> **note**
>
> Custom LVGL code cannot be displayed at the same time as LLEMU.
