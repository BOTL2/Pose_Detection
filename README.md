Key capabilities
Cross-platform support Enjoy the same experience on both Android and iOS.
Full body tracking The model returns 33 key skeletal landmark points, including the positions of the hands and feet.
InFrameLikelihood score For each landmark, a measure that indicates the probability that the landmark is within the image frame. The score has a range of 0.0 to 1.0, where 1.0 indicates high confidence.
Two optimized SDKs The base SDK runs in real time on modern phones like the Pixel 4 and iPhone X. It returns results at the rate of ~30 and ~45 fps respectively. However, the precision of the landmark coordinates may vary. The accurate SDK returns results at a slower framerate, but produces more accurate coordinate values.
Z Coordinate for depth analysis This value can help determine whether parts of the users body are in front or behind the users' hips. For more information, see the Z Coordinate section below.
The Pose Detection API is similar to the Facial Recognition API in that it returns a set of landmarks and their location. However, while Face Detection also tries to recognize features such as a smiling mouth or open eyes, Pose Detection does not attach any meaning to the landmarks in a pose or the pose itself. You can create your own algorithms to interpret a pose. See Pose Classification Tips for some examples.

Pose detection can only detect one person in an image. If two people are in the image, the model will assign landmarks to the person detected with the highest confidence.

Z Coordinate
The Z Coordinate is an experimental value that is calculated for every landmark. It is measured in "image pixels" like the X and Y coordinates, but it is not a true 3D value. The Z axis is perpendicular to the camera and passes between a subject's hips. The origin of the Z axis is approximately the center point between the hips (left/right and front/back relative to the camera). Negative Z values are towards the camera; positive values are away from it. The Z coordinate does not have an upper or lower bound.
