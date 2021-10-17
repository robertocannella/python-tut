# for x in "Python":
#     print(x)

# for x in ['a', 'b', 'c']:
#     print(x)

# interate thru range (for i loop)
for x in range(5):
    print(x)

    # start / end
for x in range(2, 5):
    print(x)

    # start / end / step
for x in range(0, 10, 2):
    print(x)

    # range objects  (low memory vs lists)
print(type(range(5)))
