"""
Name: Jaimee Molina
ID: 202514907
Date Created: 12-10-2026

Accepts 4 Windows commands from the user and executes them
"""
import os

commands = []

first_command = input("Enter first Windows command: ")
commands.append(first_command)

second_command = input("Enter second Windows command: ")
commands.append(second_command)

third_command = input("Enter third Windows command: ")
commands.append(third_command)

fourth_command = input("Enter fourth Windows command: ")
commands.append(fourth_command)

for cmd in commands:
    print(f"\n======================\n"
          f"Command {commands.index(cmd) + 1}: {cmd}\n"
          f"======================")
    os.system(cmd)
    print("\n")
    os.system("pause")
