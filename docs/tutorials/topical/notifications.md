\page notifications Task Notifications

\note
For a full list of functions for interacting with Tasks, see its
[C API](../../api/c/rtos.html) and [C++ API](../../api/cpp/rtos.html).
 Task notifications are a powerful new feature in PROS 3 which allows
direct-to-task synchronization. Each task has a 32-bit notification
value. Each task can block on its own notification (wait for it to
become non-zero) and any task can update the notification value. Task
notifications have a broad range of applications, are simple to use, and
have significant memory and speed advantages when compared to
traditional semaphore-based synchronization mechanisms.

The simplest application of task notifications does not care about the
task notification value:
