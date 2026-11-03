"""Teach loops using familiar beginner concepts: print, variables, and input."""

print("Let's learn loops!")
print("A loop repeats code, so you don't have to write the same line many times.\n")

name = input("What's your name? ")
print("Hi,", name + "!")

print("\nFOR LOOP: repeat a known number of times")
print("This loop prints your name three times:")
for _ in range(3):
	print("Hello,", name + "!")

print("\nRANGE: count through a sequence of numbers")
for number in range(1, 4):
	print("Number:", number)

print("\nWHILE LOOP: repeat while a condition is true")
count = 1
while count <= 3:
	print("Count is", count)
	count = count + 1  # Updating count makes the condition eventually false.

print("\nQuick recap:")
print("- Use for when you know how many times to repeat.")
print("- Use while when repetition depends on a condition.")
print("- Always make sure a while loop can reach a stopping condition.")
