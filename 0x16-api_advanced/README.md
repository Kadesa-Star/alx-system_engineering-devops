0x16. API advanced
==================

Objectives
-----------
- Learn how to navigate API documentation to find relevant endpoint sand understand their parameters using the Reddit Documentation as a guide
- Using an API with Pagination - understanding how to handle APIs that return paginated results. This typically involves making multiple requests to retrieve all available data
for instance if a Reddit endpoint  returns results in pages you will need to handle pagination to collect all results
- Parsing JSON results
Extract and manipulate data from JSON responses. JSON is the format used for most API responses.
For instance use pythons `json` module to parse and process the JSON data returned by Reddit 
- Making Recursive API calls
----------------------------
Implement recursive functions to handle cases where data needs to be fetched in a recursive manner, such as traversing nested data or handling paginated responses.
If Reddit provides a "next" link for further pages use recursion to follow these links and collect data.
- Sorting a Dictionary by Value
==============================
- learn how to sort dictionaries based on their values which can be useful for organizing results
if you are aggregating data from Reddit and need to sort it, use Python's sorting functions
