import cv2

def draw_label(img, text, pos, bg_color):
    font_face = cv2.FONT_HERSHEY_DUPLEX
    scale = 1
    color = (255, 255, 255)
    thickness = 1
    margin = 2

    txt_size = cv2.getTextSize(text, font_face, scale, thickness)

    end_x = pos[0] + txt_size[0][0] + margin
    end_y = pos[1] - txt_size[0][1] + margin

    cv2.rectangle(img, pos, (end_x, end_y), bg_color, thickness)
    cv2.putText(img, text, pos, font_face, scale, color, 1, cv2.LINE_AA)

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
state = int(input("TextOverlay on webcam feed or file, 0 for webcam and 1 for file>>>"))
if state == 0:
  cap = cv2.VideoCapture(0)

if state == 1:
  path = input("Enter full path of file>>> ")
  cap = cv2.VideoCapture(path)
# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")

text = input("Enter the text to be displayed >>>")
position = int(input("Enter position (Default = Bottom-middle). Options: Bottom-left(0) Top-Left(2) Bottom-middle(4)>>>"))
pos_arr = [9, 467, 9, 30, 233, 458]
if position != 0 and position != 2 and position != 4:
  position = 4
# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
    
    draw_label(frame, text, (pos_arr[position],pos_arr[position+1]), (255,255,255))
    
    # Display the resulting frame
    cv2.imshow('Frame',frame)

    # Press Q on keyboard to  exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

  # Break the loop
  else: 
    break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()