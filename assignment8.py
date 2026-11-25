with open("input.txt", "r") as file:   # used to Open the input file and read all lines
    lines = file.readlines()

line_count = len(lines)   # used to Count the number of lines

first_two_lines = lines[:2]   # Extract the first two lines

with open("output.txt", "w") as file:    # Write the first two lines into a new file
    file.writelines(first_two_lines)

print("Total number of lines:", line_count)
print("First two lines written to output.txt")
