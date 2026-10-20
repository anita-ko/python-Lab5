# Add comments before you do anything else.
#!/usr/bin/env python3
# Author: Anita Ko
# Date: oct 19, 2026
# Purpose: Process File data.
# Usage: ./lab5d.py

# TO DO 1: Copy the files pythonStatements.txt and machineCode.txt in folder.
# TO DO 2: Follow the instructions from the readme.me file to create the exact output.

with open("pythonStatements.txt", "r") as pythonFile, open("machineCode.txt", "r") as machineFile:
    with open("output.txt", "w") as outputFile:
        for pythonLine, machineLine in zip(pythonFile, machineFile):
            pythonCode = pythonLine.split("#")[0].strip()
            machineCode = machineLine.strip()
            outputFile.write(pythonCode + "\t" + machineCode + "\n")
with open("output.txt", "r") as outputFile:
    print(outputFile.read(), end="")
