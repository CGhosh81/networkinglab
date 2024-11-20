import time
import random

class StopAndWait:
    def __init__(self):
        self.timeout = 3  # Timeout in seconds
        self.sequence_number = 0  # Sequence number for packets (0 or 1)

    def send_packet(self, packet):
        """Simulate sending a packet."""
        print(f"Sending {packet} with sequence {self.sequence_number}")
        return self.sequence_number

    def receive_ack(self):
        """Simulate receiving acknowledgment."""
        if random.random() < 0.8:  # 80% chance of receiving acknowledgment
            return self.sequence_number
        return None  # Simulate acknowledgment loss

    def sender(self, packets):
        """Send packets and wait for acknowledgment."""
        for packet in packets:
            while True:  # Keep sending until acknowledgment is received
                seq_sent = self.send_packet(packet)  # Send the packet

                # Wait for acknowledgment
                if self.receive_ack() == seq_sent:
                    print(f"Acknowledgment received for {packet}")
                    break  # Move to the next packet if acknowledgment is received
                else:
                    print(f"Timeout! Retransmitting {packet}...")  # Retransmit if no acknowledgment

            # Alternate sequence number for the next packet
            self.sequence_number = 1 - self.sequence_number

# Example usage
packets_to_send = ["Packet1", "Packet2", "Packet3","Packet4","Packet5"]
stop_and_wait = StopAndWait()
stop_and_wait.sender(packets_to_send)
