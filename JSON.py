#JSON : JSON is text, written with JavaScript object notation syntax for storing and exchanging data
# Python has a built-in package called json, which can be used to work with JSON data

# Convert from JSON to Python : using the json.loads() method.
import json
x =  '{ "name":"John", "age":30, "city":"New York"}' # some JSON:
y = json.loads(x)
print(y["age"]) # the result is a Python dictionary:

# Convert from Python to JSON : using the json.dumps() method.
import json
x = { # a Python object (dict):
  "name": "John",
  "age": 30,
  "city": "New York"
}
y = json.dumps(x) # convert into JSON:
print(y) # the result is a JSON string:

import json
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))