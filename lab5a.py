# Add comments before you do anything else.
#!/usr/bin/env python3
# Author: Anita Ko
# Date: oct 19, 2026
# Purpose: Read a text file.
# Usage: ./lab5a.py

# TO DO 1: Create data2.txt.
# TO DO 2: Complete the functions below.
def read_file_lineByLine(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            print(line.strip())
    # Takes file_name as a string, reads the file in a loop one line at a time and prints each line.
def read_file_list(file_name):
    lines = []
    with open(file_name, 'r') as file:
        for line in file:
            lines.append(line.rstrip('\n'))
    return lines
    # Takes a file_name as string, read file line by line and add the line in a list as a list element without new-line characters
    # Return the list.
def main():
    file_name = 'data2.txt'
    read_file_lineByLine(file_name)
    print(read_file_list(file_name))
if __name__ == "__main__":
    main()
