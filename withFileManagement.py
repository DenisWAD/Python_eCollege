with open("dataFile/sampleText.txt") as file :
    file_line = file.readline()

    while file_line :
        print(file_line)
        file_line = file.readline()


# Uses .readline() in a while loop to loop through every line in the file and quits loop when reaches end of file