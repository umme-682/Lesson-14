#open the file in read mode
file_read = open('coding.txt', 'r')
print("File in Read Mode -")
print(file_read.read())
file_read.close()

#open the file in write mode
file_write = open('coding.txt', 'w')
#write in the file
file_write.write("File in write mode....")
file_write.write("Hi! I am Penguin and I am 1yr old")
file_write.close()

#open the file in append mode
file_append = open('coding.txt', 'a')
#append in te file
file_append.write("\n File in append mode....")
file_append.write("Hi! I am Penguin and I am 1yr old")
file_append.close()