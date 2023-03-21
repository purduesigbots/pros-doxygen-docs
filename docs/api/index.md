\page api API Home

This document covers the main PROS API.

## C API Headers

- \subpage c-adi        "C API for ADI Devices"
- \subpage c-distance   "C API for distance sensors"
- \subpage c-gps        "C API for GPS sensors"
- \subpage c-imu        "C API for IMU sensors"
- \subpage c-link       "C API for VEXLink"
- \subpage c-llemu      "C API for LLEMU (Legacy Lcd EMUlator)"
- \subpage c-misc       "C API for miscellaneous features"
- \subpage c-motors     "C API for motors"
- \subpage c-optical    "C API for optical sensors"
- \subpage c-rotation   "C API for rotation sensors"
- \subpage c-rtos       "C Real Time Operating System API"
- \subpage c-screen     "C API for the screen"
- \subpage c-serial     "C API for generic serial devices"
- \subpage c-vision     "C API for vision sensors"

## C++ API Headers

- \subpage cpp-adi      "C++ API for ADI Devices"
- \subpage cpp-distance "C++ API for distance sensors"
- \subpage cpp-gps      "C++ API for GPS sensors"
- \subpage cpp-imu      "C++ API for IMU sensors"
- \subpage cpp-link     "C++ API for VEXLink"
- \subpage cpp-llemu    "C++ API for LLEMU (Legacy Lcd EMUlator)"
- \subpage cpp-misc     "C++ API for miscellaneous features"
- \subpage cpp-motors   "C++ API for motors"
- \subpage cpp-optical  "C++ API for optical sensors"
- \subpage cpp-rotation "C++ API for rotation sensors"
- \subpage cpp-rtos     "C++ Real Time Operating System API"
- \subpage cpp-screen   "C++ API for the V5 screen"
- \subpage cpp-serial   "C++ API for generic serial devices"
- \subpage cpp-vision   "C++ API for vision sensors"

## LVGL

PROS also includes LVGL, a graphics library that enables users to create advanced
user interfaces on the V5's screen. For LVGL's features, please refer to LVGL's documentation:
 - [Official LVGL 8.3.x Documentation](https://docs.lvgl.io/master/index.html)
 - [Archive of the LVGL 5.3.x Documentation](https://gcec-2918.github.io/LVGL_v5-3_Documentation_Archive/)


## MISC.

To aid in transitioning from [PROS 2](https://pros.cs.purdue.edu/cortex/index.html) syntax to PROS 3, a \subpage api-legacy is provided. This header provides PROS 2 functionality in its original syntax.

For additional RTOS-related features, check out the @ref apix. Be warned, these features
are intended for advanced users only and may be very complex to use.
