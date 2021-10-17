# not operator
name = " "

if not name.strip():
    print("Name is empty.")
else:
    print("Hello " + name)

# logical and
age = 22
if age > 18 and age < 65:
    print("Elegible")

# beter syntax of above

if 18 < age < 65:
    print("Elegible")
