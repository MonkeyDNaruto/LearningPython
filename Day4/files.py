print("Files")
print("Note: Files are important in python, it's store the data in files.")
with open("test.txt", "w") as F: ## write mode
    F.write("Hello, I'm Nischal and I'm learning python.")
    F.close()
with open("test.txt", "r") as File: ## read mode
    content = File.read()
    print(content)
    File.close()
print("Data type of content is", type(content)) ## append mode
with open("test.txt", "a") as F:
    F.write("\nI'm learning python code in udemy")
    F.write("\nThis is a new line")
    F.write("\nThis is a new line")
    F.close()
with open("test.txt", "r") as File:
    print("File name => ", File.name)
    content = File.readlines()
    print(content)
    print("Data type of content is", type(content))
    print(File.tell())
    File.close()
