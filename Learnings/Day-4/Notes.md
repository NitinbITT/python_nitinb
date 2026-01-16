## Python Functions:
* They help to write clean code and separates logic into different blocks
* It helps to avoid redundance.

Syntax:
```
def function_name():
    ...
```

* **Arguments**:
    * Arguments are the values which are passed to the function.
* **Parameters**:
    * Parameters are the variables which are in function definition.

### Default parameter
* Functions can have default paramters where it is used if there are no arguments passed
Eg:
```
def function_name(variable=value):
    .....
```

### Keyword arguement:
* It is were, it helps to avoid the order of the argumnets passed. AKA: *Kwargs*
* To specify that a function can accept only keyword arguements we have to mention '* ,' in the beginning
Eg:
```
def function(name,age):
    print(name,age)

function(age=12,name="Alex")
```
### Positional arguements: 
* They have to maintain order of the function definition.
* To mention a function must can have only positional arguements we have to specify ',/' in definition.

```
def function(name,/):
    print(name)

function("alex")
```

### *args and **kwargs:
* They are used in function definition, when we do not know how many inputs will be there in the arguement.
    * ***args** : They help for positional arguements. 
    Eg:
        ```
        def print_numbers(*args):
            for i in range args:
                print(i)
        
        print_numbers(1,2,3,4,5)
        ```
    * ****kwargs** : They help for keyword arguements. They help to accept n number of keyword arguements

**Use of ***:
* The * can be used to dereference while calling a function.
Eg:
```
def print_numbers(a,b,c):
    print(a,b,c)

number=[1,2,3]
print_numbers(*number)
```

* We will be using ** to unpack dictionaries.

## Anonymous functions:
* They are also called lambda functions
* They are used to write simple function in one line without any function name.
* They can have any number of arguements, but only one expression.

```
a=lambda x: x*2
```
## Recursion 
* recursion is where a function calls itself.
* the maximum recursion call in python is 1000.

## File handling:
* File handling in python is done by using functions open() and close.
* open() helps to open a file.
* open() returns an object if the file is opened
* close() help sto close the opened file

- **Methods:**
    * open()
    * close()
    * f.name()
    * f.mode()
    * f.closed()
    * write()
    * read()
* **Modes** :
    * w - write mode
    * r - read mode
    * a - append mode
    * x - create mode
    * t - text mode 
    * b - binary mode : used to read and write binary files like audio, video ,image etc.

**With**:
* The with keyword helps to automatically close the fil opened.
* It is the **best practice**.


