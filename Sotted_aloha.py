import time
import random

def send_frames(total_frames):
    frames_to_send = total_frames
    frames_sent = 0
    frame_id = 0

    while frames_sent < frames_to_send:
        print("\nWaiting for the next time slot...")
        time.sleep(1)  # Simulate time slot
        print(f"Attempting to send frame {frame_id} at the start of the slot.")

        if random.choice([True, False]):  # Randomly decide success or collision
            print(f"Frame {frame_id} sent successfully.")
            frames_sent += 1
            frame_id += 1
        else:
            print(f"Collision occurred for frame {frame_id}.")
            backoff_time = random.randint(1, 5)  # Random backoff time
            print(f"Waiting for a backoff period of {backoff_time} seconds...")
            time.sleep(backoff_time)

    print("\nAll frames sent successfully.")

# Example usage
f = int(input("Enter the number of frames to send: "))
send_frames(f)
