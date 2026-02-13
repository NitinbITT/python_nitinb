class ContextManager:
    def __init__(self,string1,string2):
        self.string1=string1
        self.string2=string2

    def __enter__(self):
        print("Entering context")

    def __exit__(self,exc_type,exc_value,exc_traceback):
        print(f"Exception type:{exc_type} Exception value:{exc_value}\n Traceback:{exc_traceback}")
        print("Exiting context")
        return True

with ContextManager("Hello","world") as c:
    raise ZeroDivisionError("division by 0 occured")
    print("This is inside with block")

# class FileOpen():
#     def __init__(self,filename,mode):
#         self.file=None
#         self.filename=filename
#         self.mode=mode
    
#     def __enter__(self):
#         self.file=open(self.filename,self.mode)
#         return self.file
    
#     def __exit__(self,exc_type,exc_value,exc_tracback):
#         file.close()

# with FileOpen("context-file.txt","w") as file:
#     file.write("Hello, world!")

# with FileOpen("context-file.txt","r") as file:
#     print(file.read())
