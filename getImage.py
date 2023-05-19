import socket
import cv2
import numpy as np
import struct

server_port = 8080
Connection = False

img_size = (640, 480)
img_dtype = np.uint8
img_shape = (img_size[1], img_size[0])
# video_writer = cv2.VideoWriter('received_video.avi', cv2.VideoWriter_fourcc(*'MJPG'), 30, img_size)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', server_port))
server_socket.listen(1)
print("Server is running. Waiting for a client to connect...")

# Listen for broadcasted message from the client
client_ip = ''
client_port = 0
while True:
    data, addr = server_socket.recvfrom(1024)
    if data == b'Hello Server':
        client_ip = addr[0]
        client_port = int(data.decode().split(':')[1])
        break

# Accept the connection from the client
conn, addr = server_socket.accept()
print("Client connected. Client address:", addr)

# Receive client's initial message
data = conn.recv(1024)

if data == b'Hello Server':
    # Valid client
    conn.send(b'Server Found')
    print("Valid client. Connection established.")
    # Perform further actions with the connected client
else:
    # Invalid client
    conn.send(b'Invalid Client')
    print("Invalid client. Connection rejected.")


def sendimage():
  try:
  # Receive size of encoded frame
    size_data = b''
    while len(size_data) < 4:
        size_data += conn.recv(4 - len(size_data))

    # Decode size of encoded frame
    size = struct.unpack('<L', size_data)[0]

    # Receive encoded frame data
    frame_data = b''
    while len(frame_data) < size:
        frame_data += conn.recv(size - len(frame_data))

    # Decode encoded frame data
    frame = cv2.imdecode(np.frombuffer(frame_data, dtype=img_dtype), cv2.IMREAD_COLOR)

    # Check if frame is valid
    if frame is not None:
        # Display received image
        # cv2.imshow('Received Video', frame)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

        # Write image to video file
        # video_writer.write(frame)
      return frame
    else:
        print("Error: could not decode frame.")
        return None
  except socket.error as e:
    print("Error: ", e)
    cv2.destroyAllWindows()
    conn.close()
    server_socket.close()
