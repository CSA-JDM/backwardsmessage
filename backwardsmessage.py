# Jacob Meadows
# Computer Programming, 4th Period
# November 3rd, 2017
"""
Write a function that takes a string as an argument and displays the letters backward, one per line.
-Ask the user for a word
-Print it backwards
"""
def backwardsv1():
	count = -1
	isa = input("What word would you like reversed?: ")
	while count >= -len(isa):
		print(isa[count])
		count -= 1
def backwardsv2():
        count = 1
        isa = input("What word would you like reversed?: ")
        while count <= len(isa):
                print(isa[-count])
                count += 1
def backwardsv3():
        word = []
        count = 1
        isa = input("What word would you like reversed?: ")
        while "".join(word) != isa:
                print(isa[-count])
                word.append(isa[count - 1])
                count += 1
backwardsv1()
