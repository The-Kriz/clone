import socket
import cv2
import time

ipAddress = input("Enter Server Ip Address: ")


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #  AF_INET = IP address , SOCK_STREAM = TCP
client.connect((ipAddress,8080))  #127.0.0.1 , port
print("connected")

cap = cv2.VideoCapture(0) # connect to the first camera connected to the Pi

while True:
    if not cap.isOpened():
        print("Error: could not open camera.")
        exit()
    else:
        ret, frame = cap.read() # read a frame from the camera
        frame = cv2.resize(frame, (640, 480)) # resize the frame to a smaller size for faster transfer
        encoded_frame = cv2.imencode('.jpg', frame)[1].tobytes() # encode the frame as a jpeg and convert to bytes

        lenn =  len(encoded_frame).to_bytes(4, byteorder='little')

        client.send(lenn) # send the size of the encoded frame as 4 bytes in little endian order
        client.send(encoded_frame) # send the encoded frame

        #cv2.imshow('frame', frame) # show the frame on the client side
        if cv2.waitKey(1) & 0xFF == ord('q'): # exit loop if 'q' is pressed
            break
    time.sleep(0)

cap.release()
cv2.destroyAllWindows()
client.close()
