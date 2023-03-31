
import socket
import cv2
import numpy as np
import struct

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('192.168.1.2', 8080))
server.listen()

conn, addr = server.accept()
print("Client connected.")

img_size = (640, 480)
img_dtype = np.uint8
img_shape = (img_size[1], img_size[0], 3)

# video_writer = cv2.VideoWriter('received_video.avi', cv2.VideoWriter_fourcc(*'MJPG'), 30, img_size)

while True:
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
            cv2.imshow('Received Video', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            # Write image to video file
            # video_writer.write(frame)
        else:
            print("Error: could not decode frame.")
    except socket.error as e:
        print("Error: ", e)
        conn.close()
        break

cv2.destroyAllWindows()
conn.close()
server.close()
