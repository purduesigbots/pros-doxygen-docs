\page aivision AI Vision Sensor

\note
For a full list of functions for interacting with the ADI, see its
: [C API](@ref c-aivision) and [C++ API](@ref cpp-aivision).

## Coordinate System
All objects found by the AI Vision Sensor will have x and y coordinates.
The origin of its coordinate system is the top left corner of the image, with
x increasing from left to right and y increasing from top to bottom. Object detected
based on color descriptors, code descriptors, and AI models 

## Color Descriptors
Similar to the Vision Sensor, the AI Vision Sensor can detect objects as color blobs.
Colors for blob detection can be specified to the AI Vision Sensor as color descriptors.
A color descriptor consists of an RGB color, a hue range, a saturation range, and an ID.
IDs can range from 1-7, hue range can range from 1-40, and saturation range can range from 0.1-1.
Color objects are returned by the AI Vision Sensor with type color and the same ID as the
matching color descriptor, as well as the x and y coordinates of the top-left corner of its
bounding box, the width and height of the bounding box, and the angle.

Example Code:

```cpp
void opcontrol() {
    pros::AIVision aivision(2);
    aivision.reset();
    aivision.enable_detection_types(pros::AivisionModeType::colors);
    pros::AIVision::Color color = {.id = 1, .red = 32, .green = 142, .blue = 194, .hue_range = 20, .saturation_range = 0.5};
	pros::AIVision::Color color2 = {.id = 2, .red = 236, .green = 28, .blue = 95, .hue_range = 20, .saturation_range = 0.5};
	pros::AIVision::Color color3 = {.id = 3, .red = 146, .green = 216, .blue = 85, .hue_range = 20, .saturation_range = 0.5};
	aivision.set_color(color);
	aivision.set_color(color2);
	aivision.set_color(color3);
    while (true) {
        auto objects = aivision.get_all_objects();
        for (auto &object : objects) {
            if (pros::AIVision::is_type(object, pros::AivisionDetectType::color)) {
				printf("color\n");
				printf("id %d\n", object.id);
				printf("%d %d %d %d %d\n", object.object.color.xoffset, object.object.color.yoffset, object.object.color.width, object.object.color.height, object.object.color.angle);
			}
        }
        pros::delay(20);
    }
}
```

## Code Descriptors
The AI Vision Sensor allows blobs of different colors close to each other to be detected
as a single object by using code descriptors. Code descriptors tell the AI Vision Sensor
which color descriptors it should combine. Code descriptors consist of an ID, the number of
color descriptors to combine, and the IDs of the color descriptors. IDs can range from 1-5,
and the number of color descriptors to combine can range from 2-5.
Code objects are returned by the AI Vision Sensor with type code, and are otherwise identical
to color objects.

Example Code:

```cpp
void opcontrol() {
    pros::AIVision aivision(2);
    aivision.reset();
    aivision.enable_detection_types(pros::AivisionModeType::colors);
    pros::AIVision::Color color = {.id = 1, .red = 32, .green = 142, .blue = 194, .hue_range = 20, .saturation_range = 0.5};
	pros::AIVision::Color color2 = {.id = 2, .red = 236, .green = 28, .blue = 95, .hue_range = 20, .saturation_range = 0.5};
	aivision.set_color(color);
	pros::AIVision::Code code = {.id = 1, .length = 2, .c1 = 1, .c2 = 2};
	aivision.set_code(code);
    while (true) {
        auto objects = aivision.get_all_objects();
        for (auto &object : objects) {
            if (pros::AIVision::is_type(object, pros::AivisionDetectType::code)) {
				printf("code\n");
				printf("id %d\n", object.id);
				printf("%d %d %d %d %d\n", object.object.color.xoffset, object.object.color.yoffset, object.object.color.width, object.object.color.height, object.object.color.angle);
			}
        }
        pros::delay(20);
    }
}
```

## AI Model Object Detection
The AI Vision Sensor can also detect objects using an AI model, which can be more robust
than simple color descriptors. There is no method for uploading your own AI model, but the
model on the AI Vision Sensor can be switched between competition and classroom elements by
using VEXCode V5. Objects detected using the AI model are returned by the AI Vision Sensor
with type object and the ID of the object class, as well as the x and y coordinates of the top-left
corner of its bounding box, the width and height of the bounding box, and the score of the detection.
Score is reported as a percentage, from 0-100, with higher indicating the model has higher confidence 
in the detection.

Example Code:

```cpp
void opcontrol() {
    pros::AIVision aivision(2);
    aivision.reset();
    aivision.enable_detection_types(pros::AivisionModeType::objects);
    while (true) {
        auto objects = aivision.get_all_objects();
        for (auto &object : objects) {
            if (pros::AIVision::is_type(object, pros::AivisionDetectType::object)) {
				printf("object\n");
                printf("id %d\n", object.id);
				printf("%d %d %d %d %d\n", object.object.element.xoffset, object.object.element.yoffset, object.object.element.width, object.object.element.height, object.object.element.score);
			}
        }
        pros::delay(20);
    }
}
```

## AprilTag Detection
The AI Vision Sensor can detect AprilTags of four different families.
AprilTags detected by the AI Vision Sensor are returned with type tag and the ID of the AprilTag,
as well as the x and y coordinates of the four corners of the AprilTag.

Example Code:

```cpp
void opcontrol() {
    pros::AIVision aivision(2);
    aivision.reset();
    aivision.enable_detection_types(pros::AivisionModeType::tags);
    aivision.set_tag_family(pros::AivisionTagFamily::tag_16H5);
    while (true) {
        auto objects = aivision.get_all_objects();
        for (auto &object : objects) {
            if (pros::AIVision::is_type(object, pros::AivisionDetectType::tag)) {
				printf("tag\n");
                printf("id %d\n", object.id);
				printf("%d %d %d %d %d %d %d %d\n", object.object.tag.x0, object.object.tag.y0, object.object.tag.x1, object.object.tag.y1, object.object.tag.x2, object.object.tag.y2, object.object.tag.x3, object.object.tag.y3);
			}
        }
        pros::delay(20);
    }
}
```
