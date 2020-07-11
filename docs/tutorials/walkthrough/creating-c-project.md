Creating a C Project
====================

By default, a new PROS project contains C++ source files and the C++
API. If you would prefer to program in C instead, change the extension
of the source files (prior to PROS kernel 3.2.0: `initialize.cpp`,
`autonomous.cpp`, and `opcontrol.cpp`; after PROS kernel 3.2.0:
`main.cpp`) to `.c`.

\note Testing Notes

\warning Testing Warning

> **warning**
>
> Do not change any of the PROS header files in this process. That will cause the wrong files to be
> :   included in your project, and will likely prevent compilation.
>     Only modify the extensions of the `.cpp` files.
>
This will compile your PROS project as C code, and will give you access
to the [C API](../../api/c/index.html).

If you're interested in combining C and C++, you should read through the
[Combining C and C++ tutorial](../general/combining-c-cpp.html). Please
note that it is typically a complicated matter to combine the two, and
rarely a good idea.
