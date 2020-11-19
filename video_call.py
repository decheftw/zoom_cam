import cv2
width = 350/2
height = 350/2
cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)
mouseX = 0
mouseY = 0
clicked = 0
max_x = 640
max_y= 480
faceCascade = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")

def calculate_x(x):
    top_x = 0
    bottom_x = 0
    if x+width > max_x:
        top_x = max_x
        bottom_x = max_x - width * 2
        return top_x, bottom_x
    if x-height < 0:
        top_x = 0 + width * 2
        bottom_x = 0
        return top_x, bottom_x
    return x+width, x-width

def calculate_y(y):
    top_y = 0
    bottom_y = 0
    if y+height > max_y:
        top_y = max_y
        bottom_y = max_y - height * 2
        return top_y, bottom_y
    if y-height < 0:
        top_y = 0 + height * 2
        bottom_y = 0
        return top_y, bottom_y
    return y+height, y-height

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
    )
    x = 0
    y = 0
    if len(faces) == 1:
        for (left, top, w, h) in faces:
            x = left + w/2
            y = top + h/2
        top_y, bottom_y = calculate_y(y)
        top_x, bottom_x = calculate_x(x)
        cropped = frame[int(bottom_y):int(top_y), int(bottom_x):int(top_x)]
    else:
        cropped = frame
    cv2.imshow("preview", cropped)
    rval, frame = vc.read()

    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
cv2.destroyWindow("preview")