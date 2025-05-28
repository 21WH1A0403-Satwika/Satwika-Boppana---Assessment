
#Write into the file
with open("sample.txt", "w") as f:
    f.write("Hello,\n")
    f.write("I'm\n")
    f.write("Satwika Boppana\n")

#Append
with open("sample.txt", "a+") as f:
    f.write("from\n")
    f.write("ECE\n")
    f.seek(0)
    print("\nContent in sample file is:")
    print(f.read())
