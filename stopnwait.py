import time
def stop_and_wait_protocol(num_frames):
    i = 1
    j = 1
    while num_frames > 0:
        print(f"Sending frame {i}")
        if i % 2 == 0:
            print(f"Waiting for 1 second... (simulating a timeout for frame {i})")
            time.sleep(1)
            print(f"Resending frame {i}")
        print(f"Acknowledgment for frame {j}")
        num_frames -= 1
        i += 1
        j += 1
    print("End of Stop-and-Wait protocol")

num_frames = int(input("Enter the number of frames to send: "))
stop_and_wait_protocol(num_frames)
