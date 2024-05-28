from sys import argv

script,filename = argv

print(f"We are going to erase {filename}")
print("If you don't want that, hit CTRL-C.")
print("If you want that , hit Return.")
input("?")
print("Opening the file..")

target = open(filename,'w')

print("Truncating the file.Goodbye!")

target.truncate()

print("Now I am going to ask you to write three lines.")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line3 : ")

print("I'm going to write these lines to the file.")

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print("Finally, we close it")
target.close()







