# Define the number of rows
rows = 5

# ASCII value for 'A'
ascii_value_A = 65

# Outer loop for rows
for i in range(rows):
    # Inner loop for printing characters
    for j in range(i+1):
        # Get the character based on ASCII value and print
        character = chr(ascii_value_A + i)
        print(character, end="")
    print()  # Move to the next line after each row

