APPLICATION PROGRAMMING INTERFACE (API)
====================================
This is a set fo routines, protocols and tools for building software applications.
- They specify how software components should interact
- They are used when programmind graphical user interface components

Examples of Popular APIs
------------------------
- Google Maps API
- YouTube API
- Flickr API
- Amazon Product Advertising API

Representational State Transfer (REST) API
-------------------------------------------
- Is a way for two computer systems to communicate using the HTTP technologies found in the web browsers and servers
- They enable Real Time Data Sharing
- Operates on a set of Recommendations for creating web services including: 
	- Client Server Architecture
	- Statelessness
	- Cacheability
	- Layered System

Consideration for implementation
--------------------------------
- Endpoint consensus
- Versioning
- Authentication
- Security and Handling multiple requests

MICROSERVICES?
================
This is an architectural approach where a large application is broken down into smaller, independent services.
Each service:
- Performs a specific business function
- Communicates with other sevices via APIs
- Can be developed, deployed and scaled independently.

KEY COMPONENTS OF AN API
==========================
1. Endpoints: URLS through which API requests are sent. Each endpoint corresponds to a specific functionality or resource within the API
2. Requesdts and Responses:
	- Requests: sent by the client to interact with the API. They usually include an HTTP method (GET, POST, PUT, DELETE), headers and sometimes body.
	- Responses: Returned by the server. They contain the requested data or status messages and typically formatted in JSON or XML
3. Methods: Actions can be performed via the API.
Common HTTP methods include
- GET: retrieve data
- POST: send data to create a resource
- PUT: update and existing resource
- DELETE: Remove a resource
4. Authentication; to ensure only authorized users can access and manipulate the data. This might involve API keys, OAuth tokens, or other methods
5. Rate LimitingL Controls the number of requwsts a user can make to an API within a givent time frame to prevent abuse
6. Data Formats: typically use data formats like JSON OR XML to structure the data exchanged between clients and servers.
