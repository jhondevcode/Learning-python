fruits = ["Banana", "Apple", "Orange"]

print(fruits)

fruits.append("Strawberry")
print(fruits)
fruits.append("Cherry")
print(fruits)
fruits.append("Carrot")
print(fruits)

fruits.pop()
print(fruits)

# with for loop
for fr in fruits:
    print(fr)

print()

index = 0
while index < len(fruits):
    print(fruits[index])
    index += 1
