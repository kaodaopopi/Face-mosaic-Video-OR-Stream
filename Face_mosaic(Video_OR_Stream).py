import cv2

# Load the classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# video from the webcam.
#cap = cv2.VideoCapture(0)
# Use existing video
cap = cv2.VideoCapture('test.mp4')

#Mosaic
def do_mosaic(faces,x,y,w,h,neighbor = 10):
    fh,fw = img.shape[0],img.shape[1]
    if(y+h>fh)or (x+w>fw):
        return
    for i in range(0,h-neighbor,neighbor):
        for j in range(0,w-neighbor,neighbor):
            rect = [j+x,i+y,neighbor,neighbor]
            color = img[i+y][j+x].tolist()
            left_up = (rect[0],rect[1])
            right_down = (rect[0] + neighbor - 1, rect[1] + neighbor - 1)
            cv2.rectangle(img, left_up, right_down, color, -1)

while True:
    # Read the frame
    _, img = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect face
    faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=3,
    minSize=(25, 25))

    # Draw the box of the face part
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 1)
        do_mosaic(faces,x, y, w, h)
        
    # Show results
    cv2.imshow('img', img)
    #Calculate how many faces are found
    print("Find {0} face.".format(len(faces)))

    # Press ESC to end the program execution
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
    

# Release the VideoCapture object     
cap.release()
cv2.destroyAllWindows()