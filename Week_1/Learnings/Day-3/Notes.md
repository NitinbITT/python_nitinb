### Data Types:
* int 
* str
* float
* complex (it is a combination of real and imaginary numbers, where imaginary numbers are denoted along with 'j')
* Bool - It is a type where it says whether true or false. (True, False)
* **List** 
    - They are allowed to change. i.e., mutable
    - They are allowed to have duplicate elements.
    ```
    a=[4,3,5,2]
    ```
* **Tuple**
    - They are not allowed to change.
    - They can have duplicate elements.
    ```
    a=(2,6,1,3,4)
    ```
* **Range**
    - They are not allowed to change and have duplicates.
    ```
    a=range(1,5)
    ```

* **Set**
    - They do not maintain the order of insertion or initialization
    - There is no indexing
    - They cannot have duplicates
    - They are mutable.
    ```
    a={1,5,3,7}
    ```
* **Frozenset**
    - They are similar to set but, it cannot change.
    ```
    a=frozenset(*List*)
    
    a=frozenset([1,5,4,2,4,3,5,5,3,3,3,5,3])
    ```
* **Dictionary**:
    - They are used to store values by knowing what they are.
    Syntax:
    ```
    employee={
        "name":"person",
        "Age":28
    }
    ```
    ```
    employee=dict("name"="person","age"=28)
    ```

    to get value: 
    ```
    employee["name"]
    ```
    or
    ```
    employee.get("name")
    ```
    **Methods**:
    - get()
    - values()
    - keys()
    - items()
    - update()

    **Using the get method is the safest way to retrieve value.**
**type()** -> helps to find the type of a variable

### Type Casting:
* Type casting is where a data of a variable is converted from one type to another 
* There 2 types of conversion
    - implicit 
        * It is where the type of the value is changed indirectly.
        ```
        a=10
        b=2.5
        c=a+b
        print(c)    # 12.5
        ```
    - explicit

        * int()
        * float()
        * str()
        * bool()
        * list()
        * set()
        * tuple()

**Converting Binary String to Integer**
* We can convert binary string to an integer
    ```
    a="101"
    b=int(a,2)
    print(b)
    ```

**Arrays**
* There is no arrays in python, instead list is used.
* List has same way of working as array.
* List store values as a pointer to a value and they are not continous.
    * **Methods:**
        - append()
        - insert()
        - pop()
        - remove()
        - reverse()
        - sort()
        - clear()
        - extend() 

**Numpy Arrays:**
* Numpy arrays are continues, uses less memory space and provides direct memory access rather then lists.
    ```
    import numpy from np
    a=np.array([1,2,3])
    print(a)   #[1 2 3]
    ```
- To get user input we cannot directly do in numpy array, we must convert list to numpy array.
    Eg:
    ```
    import numpy from np 

    a=list(map(int,input("Enter values").split(" ")))
    print(a)
    ```

    **split()** : Used to split the single string into multiple strings

    **input()** : Input method

    **map()** : They are used to perform a specific tash on the given values. Here, it is used to change the type of each values to mentioned data type
    
    **list()** : Type conversion to list type