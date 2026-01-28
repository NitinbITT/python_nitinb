# REST API:
* Rspresentaional State Transfer
* It is used to communicate between servers.
* Eg: Forntend server communicating between backend server
* Preferrred as they are simple to implement and keeps the servers independent
* There are methods in REST API which helps in getting, setting and updating the data.
    * GET
    * PUT
    * PATCH
    * DELETE
    * POST
* They also provide status codes which helps to understand whether the required task is done.

## Principles:
* The endpoints of rest api must be noun and not verb 
* The methods of REST API is verb
* They are be stateless
* servers must be independent
* cachebility : Browsers help in cacheing
Why preferred than other languages
* Easy to implement
* Provides loose coupling.

Types of data handling 
* Parameters
Eg : GET /user/20

* Query paramater:
Eg : GET /user?name=abc&password=156789

* Request Body:
    Sending data through body

## Idempotent:
* It is where the state doesnt change eventhough performing the same operation repeatedly

**Safe methods**
* GET
* HEAD
* OPTIONS
* TRACE

**Idempotent methods :**
* PUT
* DELETE

**Non-idempotent methods :**
* POST

* Idempotent helps to keep consistent data across the application.

## Pagination:
* it is where the limiting of data which is being sent from the server to client.
    * Offset pagination
    * Seek pagination
    * Keyset pagination