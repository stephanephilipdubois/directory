import os

def main():
    directory = input("Please enter the directory that you want to save the file: ")
    filename = input("Plase enter the file name: ")
    name = input("Please enter your name: ")
    address = input("Please enter your address: ")
    phone_number = input("Please enter your phone number: ")
    #checking if the directory exists
    if os.path.isdir(directory):
        writeFile = open(os.path.join(directory,filename),'w')
        writeFile.write(name+','+address+','+phone_number+'\n')
        writeFile.close()

        print("File contents:")
        readFile = open(os.path.join(directory,filename),'r')
        for line in readFile:
            print(line)
        readFile.close()
    else:
        print("Sorry, that directory does not exist")
main()
