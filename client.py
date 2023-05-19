import socket
import cv2
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client_port = 8080

connected = False

while not connected:
    # Broadcast a message to find the server
    message = b'Hello Server:' + str(client_port).encode()
    client_socket.sendto(message, ('<broadcast>', client_port))

    # Listen for response from the server
    client_socket.settimeout(2)  # Set a timeout for receiving server response
    try:
        data, addr = client_socket.recvfrom(1024)
        if data == b'Server Found':
            print("Server found. Connection established.")
            connected = True
        else:
            print("Server not found. Retrying...")
    except socket.timeout:
        print("Server not found. Retrying...")

client_socket.settimeout(None)  # Reset the timeout to disable it

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


client_socket.close()
cap.release()
cv2.destroyAllWindows()
client.close()
