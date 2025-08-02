file = open('a.txt','r')
print(file.read())
file.close()

file_w=open('a.txt','w')
file_w.write("Hello")
file_w.close()

file_append = open('a.txt','a')
file_append.write("\n File in append mode .....")
file_append.write("My name is penguin")
file_append.close()