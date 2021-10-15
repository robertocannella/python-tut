students_count = 1000   # Python is dynamically typed
print(type(students_count))
print(type("HELLO"))
print(type(1.1))
print(type(False))

age: int = 20   # installing mypy linter allows for type checking
# compiler error is shown though will not throw an error
age = "Python"
