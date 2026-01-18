with open("file.txt","r") as file:
    for line in file:
        whitespaces=0
        strings=line.split(" ")
        whitespaces+=len(strings)
        for string in strings:
            if len(string)!=0:
                if string[len(string)-1]!="\n":
                    print(string[0].upper()+string[1:len(string)],end=" ")
                else:
                    print(string[0].upper()+string[1:len(string)],end="")
            else:
                print(end=" ")
    print("\nNo of whitespaces:",whitespaces)