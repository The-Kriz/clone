import socket
import cv2
import struct
import time

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('192.168.1.2',8080))
print("connected")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: could not read frame from camera.")
        break
    
    frame = cv2.resize(frame, (640, 480))
    encoded_frame = cv2.imencode('.jpg', frame)[1].tobytes()
    size = struct.pack('<L', len(encoded_frame))

    try:
        client.sendall(size + encoded_frame)
    except socket.error as e:
        print("Error: ", e)
        client.close()
        break
    
#    cv2.imshow('frame', frame)
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break
        
#    time.sleep(0.1)

cap.release()
cv2.destroyAllWindows()
client.close()
