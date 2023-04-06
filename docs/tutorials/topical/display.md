\page display V5 Brain Display (LVGL)

Interacting with the touchscreen on the V5 Brain is made possible
through [LVGL](https://lvgl.io/). LVGL is a full-featured C
graphics library (it's accessible in C++ projects too under the same
API).

The first step to getting started with LVGL is to include `pros/apix.h`
in your `main.h` file or other header files. This includes the full LVGL
feature set as described in their documentation:
<https://docs.lvgl.io/master/index.html>

You can follow along with any of the LVGL
[tutorials](https://docs.lvgl.io/master/get-started/index.html)
or [wiki](https://docs.lvgl.io/master/overview/index.html). There is no need to port
or initialize LVGL, you can simply start creating objects.

\note
Custom LVGL code cannot be displayed at the same time as the [LLEMU](./llemu.html).
As a result, you must remove the LLEMU code (`pros::lcd`) that is
present in `main.cpp` by default in a new project.
