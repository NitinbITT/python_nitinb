## Resource modeling
* **Resource** : it is the single piece of data which can be accessed by URI.
* Resource modeling is a strategy to model the URI for effective use.
    * Noun based URI
    * Heirarchical flow of nouns
    * Uniquely identifiable data
    * Each URI must return only minimal amount of data to avoid latency and bandwidth 

## URI:
* Uniform Resoucr Locator
* It is used to uniquely identity a resource
* It has 2 subclasses
    * URL - Uniform Resource Locator
    * URN - uniform Resource Name
* Syntax : 
```
URI = scheme ":" ["//" authority] path ["?" query] ["#" fragment]
```
* scheme and path is mandatory

## Query parameters:
* They are passed along with the URL.
* It helps to retrieve resources.
* They are used to sort, filter from the resources
* Things which are after ? are query parameter
* They are optional
Eg:
```
https://www.example.com/users/10234/orders?status=shipped 
```
## Path parameter:
* They are used to identify a specific resource
Eg:
```
users/post/1324
```
* 1324 is the path parameter

## Query VS Path parameters:
* Query is used to filter and sort data
* Path is used to uniquely identify a resource

### Filter and Sorting:
* **Filtering**:
    * passing values to query paramters:
    Eg :
    ```
    GET /items?state=active&seller_id=1234
    ```

    * Using greater and lesser than symbols
    * To specify opertors we must use LHS Brackets([] ->[lte][gte][regex][exists] etc)
    or RHS colon
    Eg :
    ```
    GET /items?price[gte]=10&price[lte]=100
    GET /items?price=gte:10&price=lte:100
    ```

    * Sorting can be done by specifying it as query params.
``` 
GET /users?sort_by=asc(email) and GET /users?sort_by=desc(email)
GET /users?sort_by=+email and GET /users?sort_by=-email
GET /users?sort_by=email.asc and GET /users?sort_by=email.desc
GET /users?sort_by=email&order_by=asc and GET /users?sort_by=email&order_by=desc
```

## Authentication:
* Authentication is where, we check whether the user is a valid user
* It is used during logging in 
* JWT token, Access Tokens, OAuth 2.0 are some authentication mechanisms

### Flow:
1. Send request to server by filiing the user data 
2. Server validating the data and verifying
3. Server sends token to the client

* This token is used to authenticate the client at each request
* It helps to reduce the no of authentication process it has to go at each request.

## Authorization:
* It is where, it is validated whether only the authorized person has the access.