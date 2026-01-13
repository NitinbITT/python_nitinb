### Valid Variable:
    * Start with underscore
    * Start with any letter
    * Must not contain anyother special character other than underscore
    * Cannot start with a number

### Global vairables:
    * Global vairables are where the variables are visible to every other local places in the program.
    * They are not visible outside the program

### Namespaces:
    * Namespaces are identifiers for variables and methods.
    * They uniquely identify by using scope and name.
    * They bind objects like dictionaries.
     Eg : Take different folders have a file in the same name, and each directory is the uniqueness of each file.

### Data Types:
    * int 
    * str
    * float
    * complex (it is a combination of real and imaginary numbers, where imaginary numbers are denaoted along with 'j')

    **type()** -> helps to find the type of a variable

### Type Casting:
    * Type casting is where a data of a variable is converted from one type to another 
        - int()
        - float()
        - str()

### Flow Control
    **pass** - used as a placeholder.
             - used only to fill a place.
    ```
    if number>5:
        pass
    else
        print("Number Greater than 5")
    ```

### Operators
    - Arithmetic (+, -, *, /, //, %, **)
    - Assignment (=, +=, -=, /=, *=, %=, //=, **=, &=, |=, ^=, >>=, <<=)
    - Comparison (==, <=, >=, <, >, !=)
    - Logical (and, or, not)
    - Identity (is, is not): used to check objects 
    - Membership (in, not in) : used to check whether a value is present in an Object
    - Bitwise (&, |, >>, <<, ^, ~)