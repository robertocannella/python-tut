# type anotation during fuction declarations
# -> return type:
def increment(number: int, by: int = 1) -> tuple:
    return (number, number + by)  # returns a tuple (not modifiable)


print(increment(3, by=4))  # keyword argument
print(increment(3))
