def countWhitespaces(fileContent):
    count = 0
    for character in fileContent:
        if character == " ":
            count += 1
    return count


newFileContent = ""
with open("file.txt", "r") as file:
    for line in file:
        strings = line.split(" ")
        for string in strings:
            if len(string) != 0:
                if string[len(string) - 1] != "\n":
                    newFileContent += string[0].upper() + string[1 : len(string)] + " "
                else:
                    newFileContent += string[0].upper() + string[1 : len(string)]
            else:
                newFileContent += " "
    whitespaces = countWhitespaces(newFileContent)
    print("No of whitespaces:", whitespaces)
    newFileContent += "\nNo of Whitespaces: " + str(whitespaces)
with open("newfile.txt", "w") as newFile:
    newFile.write(newFileContent)
