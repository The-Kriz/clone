
import socket
import cv2
import numpy as np
import struct

ipAddress = input("Enter Server Ip Address: ")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ipAddress, 8080))
server.listen()
conn, addr = server.accept()
print("Client connected.")


img_size = (640, 480)
img_dtype = np.uint8
img_shape = (img_size[1], img_size[0], 3)


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
      return frame
    else:
        print("Error: could not decode frame.")
        return None
  except socket.error as e:
    print("Error: ", e)
    cv2.destroyAllWindows()
    conn.close()
    server.close() 
