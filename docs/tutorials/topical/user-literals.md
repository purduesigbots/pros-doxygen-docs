\page user-literals User Literals

# Literals Provided By PROS

PROS provides the ability for users to create devices using C++'s user-literals
syntax:

```{.cpp}
// In order to use the user literals, we need to be using the pros::literals
// namespace. Make sure to include the line "using namespace pros::literals"
// at the beginning of any file in which you want to use user literals.
using namespace pros::literals;

pros::Motor front_motor = 1_mtr;   // Constructs a motor on port 1
pros::Motor back_motor = 2_rmtr; // Constructs a motor on port 2, and reverses it
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

```{.cpp}
const pros::Rotation operator"" _rot(const unsigned long long int r);
const pros::Imu operator"" _imu(const unsigned long long int i);
const pros::Gps operator""_gps(const unsigned long long int g);
const pros::Optical operator"" _opt(const unsigned long long int o);
const pros::Distance operator"" _dist(const unsigned long long int d);
const pros::Motor operator"" _mtr(const unsigned long long int m); // For non-reversed motor
const pros::Motor operator"" _rmtr(const unsigned long long int m); // For reversed motor
const pros::Serial operator"" _ser(const unsigned long long int m);
```

