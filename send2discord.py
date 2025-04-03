import pyautogui
import time
import pyperclip

# Define the delay between each command
delay = 2.5

# Read the commands from the file
with open('commands.txt', 'r') as file:
    # Strip whitespace and ignore empty lines
    commands = [line.strip() for line in file if line.strip()]

# Ask the user to position the cursor in the Discord message input field
input("Position the cursor in the Discord message input field and then press Enter...")

# Add a short delay to give the user time to focus the Discord window
time.sleep(delay)  

# Loop through the commands and send them one by one
for command in commands:
    # Debugging line to show the command being processed
    print(f"Processing command: {command}")  
    pyperclip.copy(command)  # Copy the command to the clipboard
    pyautogui.hotkey('ctrl', 'v')  # Paste the command
    time.sleep(2)
    pyautogui.press('enter')  # Press the 'enter' key to send the message
    time.sleep(delay)  # Wait for the specified delay before sending the next command

print("All commands have been sent.")
