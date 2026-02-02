def count_whitespaces(file_content):
    count = 0
    for character in file_content:
        if character == " ":
            count += 1
    return count


new_file_content = ""
with open("file.txt", "r") as file:
    for line in file:
        strings = line.split(" ")
        for string in strings:
            if len(string) != 0:
                if string[len(string) - 1] != "\n":
                    new_file_content += (
                        string[0].upper() + string[1 : len(string)] + " "
                    )
                else:
                    new_file_content += string[0].upper() + string[1 : len(string)]
            else:
                new_file_content += " "
    whitespaces = count_whitespaces(new_file_content)
    new_file_content += "\nNo of Whitespaces: " + str(whitespaces)
with open("newfile.txt", "w") as newFile:
    newFile.write(new_file_content)
