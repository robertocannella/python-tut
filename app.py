from types import coroutine


string = "This is A String"

# String indexing
print(len(string))
print(string[0])
print(string[-1])

# Slicing strings
print(string[0:3])
print(string[:3])  # excluding a start index, python will imply 0index

# Escape sequences (inherited from C language)
# \'  \"  \\ \n
msg: str = "Python \"Programming\""
print(msg)

# Concatination
first: str = "Roberto"
last: str = "Cannella"
full: str = first + " " + last
print(full)

# String Formatting {expressions can be handled inside curly braces}
alternative_full: str = f"{first} {last}"
print(alternative_full)

course: str = "Python Programming"
print(course.upper())  # UPPERCASE
print(course.lower())  # lowercase
print(course.title())  # Title Case
print(course.count("P"))  # counts occurrances
print(course.strip())  # remove white space
print(course.find("Pro"))  # search (returns -1 if false)
print(course.replace("P", "-"))  # replace
print("Programming" in course)  # returns boolean
print("Programming" not in course)  # returns boolean
