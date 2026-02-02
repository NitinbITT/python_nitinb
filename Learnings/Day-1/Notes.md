# Modules
* Modules are programs which can be imported and used in any program 
* It helps to keep program organized.
* It keeps all similar files in single module
* it is a single python file.
* there are diff type of modules
    * User-defined
    * Built-in
    * external : modules downloaded using pip or anyother package installer
    * Package-module: These are modules which is present in a package.

**Ways of importing a module** :
* import *module* as *alias*
* import *module*
* from *module* import *function*
* from *module* import *   

**__name__** : tells if the file is run directly or it is imported.
 * for a file being run directly it will show **__main__**
 * else it will show the file name

 ## pycache directory:
 * the pycache directory is used to store the compiled code of python files.They contain bytecode
 * it helps to run code faster.
 * it is created only for imported files. 

 # Packages:
 * Packages are folders containing modules which keep the modules grouped.
 Eg : a module can store different functions like, add,sub,mul,div etc as simple math in a module and contain complex calculations in another module and these modules will come under a single package as Math.
 * To make a folder as a package it must contain __init__.py file.
 * this file contains the functions that must be directly imported from modules
 * __all__ this variable is used to say what are all the functions that must be imported to the file when using * .

 # Exception:
 * Exception is where an exception is provided to an execution.
 * They can be handled.

 ## Exception handling:
 * try and except
 * finally
 * else 

**try block:** try block is where an operation is tried even it makes exception 
**except block:** This is the handling place where if the try fails then this blocks gets executed.
**else block:** Else block is where the block gets executed when the try runs successfully.
**finally block:**This is the block where even if any one block runs this block will run.

- SyntaxError	
- NameError	
- TypeError	
- ValueError	
- ZeroDivisionError	
- ImportError	
- IOError / OSError	
- IndexError	
- KeyError	
- AttributeError	
- MemoryError	
- KeyboardInterrupt

**Raising an exception:**
* an raise any exception explicitly without the compiler.
eg:
```
try:
    n=2
    if n<5:
        raise Exception("Value less than 5")
except Exception as e:
    print(e,"Exception")
```

**User-defined exception:**
* Exeption which is raised for business logics.
* They must be raied explicitly.
Eg :
```
class InvalidValueException(Exception):
    pass

try:
    n=2
    if n<5:
        raise InvalidValueException("Value less than 5")
except InvalidValueException as e:
    print(e,"Exception")
```