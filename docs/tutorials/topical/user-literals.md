\page user-literals User Literals

# Literals Provided By PROS

PROS provides the ability for users to create devices using C++'s user-literals
syntax:

```{.cpp}
// In order to use the user literals, we need to be using the pros::literals
// namespace. 
using namespace pros::literals;

pros::Motor front_motor = 1_mtr;   // Constructs a motor on port 1
pros::Motor back_motor = -2_motor; // Constructs a motor on port 2, and reverses it
pros::Imu imu = 12_imu;            // Constructs an IMU object on port 12
```

Using these literals function no differently than constructing the objects as 
normal C++ objects:

```{.cpp}
pros::Motor front_motor(1);   // Constructs a motor on port 1
pros::Motor back_motor(-2);   // Constructs a motor on port 2, and reverses it
pros::Imu imu(12);            // Constructs an IMU object on port 12
```

However, we felt this was a neat addition to add to the API so that users could
utilize whichever method they saw fit. Every V5 device has a literal that can 
be used to construct the object. Thise are listed on the API page for each
device class (\ref api). 

## List of PROS Literals:


# Defining Your Own User Literals

