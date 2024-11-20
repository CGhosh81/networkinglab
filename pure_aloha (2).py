import random
import time
total_frames = 3  
successful_frames = 0  
frame_id = 0  
def send_frame(frame_id):
    print(f"Sending frame {frame_id}...")
    
    return random.choice([True, False])
def wait_for_ack():
    time.sleep(0.5)  
    return send_frame(frame_id)

while successful_frames < total_frames:
    ack_received = wait_for_ack()
    if ack_received:
        print(f"Frame {frame_id} transmitted successfully.")
        successful_frames += 1
        frame_id += 1
    else:
        print(f"Collision occurred for frame {frame_id}.")
        backoff_time = random.randint(1, 3)
        print(f"Waiting for backoff period: {backoff_time} seconds...")
        time.sleep(backoff_time)
print("All frames transmitted successfully!")
