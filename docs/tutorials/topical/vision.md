Vision Sensor
=============

> **note**
>
> For a full list of functions for interacting with the V5 Vision Sensor, see its
> :   [C API](../../api/c/vision.html) and [C++
>     API](../../api/cpp/vision.html).
>
Setting Signatures
------------------

The first step to using the vision sensor is setting color signatures
for the sensor to recognize as objects. This is done through the V5
Vision Utility program.

Retrieving Objects
------------------

The primary function of the vision sensor is returning objects, or blobs
of color detected by the sensor. The characteristics of an object are
defined in
[vision\_object\_s\_t](../../api/c/vision.html#vision_object_s_t).

### By Size

The simplest way to interact with the vision sensor is to get an object
by its size. 0 is the largest object detected by the sensor.

### By Signature

If you have multiple signatures saved to the vision signature, you will
most likely want to only look for objects of a particular signature. The
`get_by_sig()` function implements this functionality.

Changing the Object Coordinates
-------------------------------

Each returned object from the vision sensor comes with a set of
coordinates telling where the object was found in the vision sensor's
field of view. The default behavior is to return the coordinates as a
function of distance from the top left corner of the field of view - so
positive y is downward and positive x is right. With the PROS API, you
can change this behavior so that the center of the Field Of View is the
(0,0) point for object coordinates. Positive y is still downward and
positive x is still right, but negative y is upward of center and
negative x is left of center in this configuration.

Exposure Setting
----------------

In PROS Kernel 3.1.4 and earlier, the vision sensor exposure parameter
was in the range [0,58]. In PROS Kernel 3.1.5 and newer, the parameter
is scaled to be in the range [0,150] to match the Vision Sensor utility.
As a result, there is a loss of information in this translation since
multiple integers on the scale [0,150] map to the scale [0,58].
