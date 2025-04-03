## Script to generate a list of commands

# Read user IDs from a text file
amount = int(input('Enter the Amount to give: '))
with open('List_of_Ids.txt', 'r') as file:
    user_ids = [line.strip() for line in file]

# Generate commands and save them to a new text file
with open('commands.txt', 'w') as output_file:
    for user_id in user_ids:
        command = f'!add-money {user_id} {amount}\n'    
        output_file.write(command)

print("Commands have been generated and saved to commands.txt")