# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a demo of file handling in Python.\n")
    file.write("We are writing multiple lines to this file.\n")
    file.write("This is the third line.\n")

print("Data written to file successfully.")

# Reading from the file
with open("example.txt", "r") as file:
    print("\nReading data from the file:")
    content = file.read()
    print(content)
