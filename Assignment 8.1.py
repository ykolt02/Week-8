import os

def main():
    directory = input("Enter the directory that you want to save the file : ")
    filename = input("Enter the filename : ")
    name = input("Enter your name : ")
    address = input("Enter your address : ")
    phone_number = input("Enter your phone number : ")
    #checking if the directory exists
    if os.path.isdir(directory):
        #createing and opening the file to write
        writeFile = open(os.path.join(directory,filename),'w')
        #writing the data by comma seperated
        writeFile.write(name+','+address+','+phone_number+'\n')
        #close the file after writing is done
        writeFile.close()
        print("File is located at: " + directory + "\\" + filename + "\n")
        print("\nFile contents:\n")
        #reading the file for proof of storing
        readFile = open(os.path.join(directory,filename),'r')
        for line in readFile:
            print(line)
        readFile.close()
    elif not(os.path.isdir(directory)): #executes if directory not found
        os.system("mkdir " + directory)
        writeFile = open(os.path.join(directory,filename),'w')
        #writing the data by comma seperated
        writeFile.write(name+','+address+','+phone_number+'\n')
        #close the file after writing is done
        writeFile.close()
        print("File is located at: " + directory + "\\" + filename + "\n")
        print("\nFile contents:")
        #reading the file for proof of storing
        readFile = open(os.path.join(directory,filename),'r')
        for line in readFile:
            print(line)
        readFile.close()

    else:
        print("Sorry that directory is not exists...")
main()