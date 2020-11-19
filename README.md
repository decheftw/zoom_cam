# Zoom Cam

## To run:
1. Clone repo
2. run python3 video_call.py
3. Press escape to close the window

## What it does:
The app displays a live webcam feed and searches for a face. If it detects 1 face, it will focus on that face and crop the image so that the face is always in the center of the screen, even when it moves. The tracking is fairly responsive, so test it out with some head bops!

## How it works:
I'm using opencv to read in frames from the device webcam. Then, opencv's CascadeClassifier with the xml file found here: https://github.com/opencv/opencv/tree/master/data/haarcascades returns the x and y in which the detected face starts. I half of my constant height and width to that to find the center of the face. I use the center of my face to calculate the substrings in which to crop the opencv frame.

## Limitations:
Currently only works with 1 face in the frame. Detecting 2 faces or 0 faces will set the camera to default width and height.

## Next Steps:
1. Integration with Windows Direct Show SDK so I can emulate a webcam with this filter. Then apps like Zoom, Google Hangouts, etc. will detect this app's output as an additional camera.
2. Zooming in and out. When the subject's face moves forward or backward, the frame should zoom in and out so the same percentage of the image is taken up by the face.
3. Default frame. When there is no face, the frame should stay the same size and with a default zoom instead of resetting to maximum size.
4. Incorporating multiple faces.
