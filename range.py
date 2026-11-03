"""A short guide to using range() in loops."""

# range(stop) counts from 0 to stop - 1. The stop value is not included.
for i in range(5):
	print(i)  # 0, 1, 2, 3, 4

# range(start, stop) counts from start to stop - 1.
for i in range(2, 6):   
	print(i)  # 2, 3, 4, 5

# range(start, stop, step) changes how much the count increases each time.
for i in range(0, 10, 2):
	print(i)  # 0, 2, 4, 6, 8

# A negative step counts backward.
for i in range(5, 0, -1):
	print(i)  # 5, 4, 3, 2, 1
