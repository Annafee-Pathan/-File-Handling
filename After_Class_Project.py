# File Handling in Different Modes

# 1. Write mode ("w")
f = open("sample.txt", "w")
f.write("This is the first line.\n")
f.write("Writing to file using 'w' mode.\n")
f.close()

# 2. Read mode ("r")
f = open("sample.txt", "r")
print("Reading file in 'r' mode:")
print(f.read())
f.close()

# 3. Append mode ("a")
f = open("sample.txt", "a")
f.write("This line is added using 'a' mode.\n")
f.close()

# 4. Read + Write mode ("r+")
f = open("sample.txt", "r+")
print("\nReading and writing using 'r+' mode:")
content = f.read()
print(content)
f.write("Extra text written using 'r+' mode.\n")
f.close()

# 5. Append + Read mode ("a+")
f = open("sample.txt", "a+")
f.write("Appending and reading using 'a+' mode.\n")
f.seek(0)  # move cursor to start for reading
print("\nContents after using 'a+':")
print(f.read())
f.close()
