with open("dataFile/sampleText.txt") as file :
    file_line = file.readline()

    while file_line :
        print(file_line)
        file_line = file.readline()


     