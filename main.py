#open file and read it contents
file = open('coding.txt', 'r')
print(file.read())
file.close()

#open file and read its begining 8 characters
file = open('coding.txt', 'r')
print("\n Read in parts \n")
print(file.read(8))
file.close()

#append your name and age in the file
file = open('coding.txt', 'a')
file.write("Hi! I am Penguin and I am 1yr old")
file.close()