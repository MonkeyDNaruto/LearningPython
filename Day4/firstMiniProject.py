#Ask for a sentence
#print the length of a sentence
#ask for a file name
#write a file using file nae and aadd sentence in it
#run
sentence = input("Enter a sentence: ")
print("The length of the entered sentence is: ", len(sentence))
file_name = input("Enter a file name: ")
file_name = f"{file_name}.txt"
with open(file_name, "w") as F:
    F.write(sentence)
    sentenceLength = "\nThe length of the sentence is: " + str(len(sentence))
    print(sentenceLength)
    F.write(sentenceLength)
    print("File created sucessfully.")
    F.close()