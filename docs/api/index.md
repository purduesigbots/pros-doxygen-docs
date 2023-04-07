\page api API Home

This document covers the main PROS API.

## C API Headers

- \subpage c-adi        "C API for ADI Devices"
- \subpage c-distance   "C API for Distance Sensors"
- \subpage c-gps        "C API for GPS Sensors"
- \subpage c-imu        "C API for IMU Sensors"
- \subpage c-link       "C API for VEXLink"
- \subpage c-llemu      "C API for LLEMU (Legacy Lcd EMUlator)"
- \subpage c-misc       "C API for Miscellaneous Features"
- \subpage c-motors     "C API for Motors"
- \subpage c-optical    "C API for Optical Sensors"
- \subpage c-rotation   "C API for Rotation Sensors"
- \subpage c-rtos       "C Real Time Operating System API"
- \subpage c-screen     "C API for the V5 Screen"
- \subpage c-serial     "C API for Generic Serial Devices"
- \subpage c-vision     "C API for Vision Sensors"

## C++ API Headers

- \subpage cpp-adi                  "C++ API for ADI Devices"
- \subpage cpp-distance             "C++ API for Distance Sensors"
- \subpage cpp-gps                  "C++ API for GPS Sensors"
- \subpage cpp-imu                  "C++ API for IMU Sensors"
- \subpage cpp-link                 "C++ API for VEXLink"
- \subpage cpp-llemu                "C++ API for LLEMU (Legacy Lcd EMUlator)"
- \subpage cpp-misc                 "C++ API for Miscellaneous Features"
- \subpage cpp-motors               "C++ API for Motors"
- \subpage cpp-motor-group          "C++ API for Motor Groups"
- \subpage cpp-optical              "C++ API for Optical Sensors"
- \subpage cpp-rotation             "C++ API for Rotation Sensors"
- \subpage cpp-rtos                 "C++ Real Time Operating System API"
- \subpage cpp-screen               "C++ API for the V5 Screen"
- \subpage cpp-serial               "C++ API for Generic Serial Devices"
- \subpage cpp-vision               "C++ API for Vision Sensors"

## C++ Abstract Classes (For Template/Library Writers)

- \subpage cpp-abstract-motor       "C++ API for Abstract Motors"

## LVGL

PROS also includes LVGL, a graphics library that enables users to create advanced
user interfaces on the V5's screen. For LVGL's features, please refer to LVGL's documentation:
 - [Official LVGL 8.3.x Documentation](https://docs.lvgl.io/master/index.html)
 - [Archive of the LVGL 5.3.x Documentation](https://gcec-2918.github.io/LVGL_v5-3_Documentation_Archive/)


## MISC.

To aid in transitioning from [PROS 2](https://pros.cs.purdue.edu/cortex/index.html) syntax to PROS 3, a \subpage api-legacy is provided. This header provides PROS 2 functionality in its original syntax.

For additional RTOS-related features, check out the @ref apix. Be warned, these features
are intended for advanced users only and may be very complex to use.
