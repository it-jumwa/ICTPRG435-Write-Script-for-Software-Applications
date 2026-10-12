"""
Name: Jaimee Molina
ID: 202514907
Date Created: 12-10-2026

Requests the ISP speed in kbps from the user.
Calculates the download speed in KBps and outputs it to the terminal
"""
ISP_speed = input("Enter your ISP's speed in kbps: ")
ISP_speed = float(ISP_speed)

speed_in_bits = ISP_speed * 1000
speed_in_bytes = speed_in_bits / 8
speed_in_kilobytes = speed_in_bytes / 1024

print(f"Download Speed: {speed_in_kilobytes} KBps")
