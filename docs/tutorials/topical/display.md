V5 Brain Display (LVGL)
=======================

Interacting with the touchscreen on the V5 Brain is made possible
through [LVGL](https://littlevgl.com). LVGL is a full-featured C
graphics library (it's accessible in C++ projects too under the same
API).

The first step to getting started with LVGL is to include `pros/apix.h`
in your `main.h` file or other header files. This includes the full LVGL
feature set as described in their documentation:
<https://littlevgl.com/>

You can follow along with any of the LVGL
[tutorials](https://github.com/littlevgl/lv_examples/tree/master/lv_tutorial)
or [wiki](https://docs.littlevgl.com/#Objects). There is no need to port
or initialize LVGL, you can simply start creating objects.

> **note**
>
> Custom LVGL code cannot be displayed at the same time as the [LLEMU](./llemu.html).
> :   As a result, you must remove the LLEMU code (`pros::lcd`) that is
>     present in `initialize.cpp` by default in a new project.
>

