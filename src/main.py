
def main():
    read_file(path())



def path():
    """path() function asks the user for the file name and returns the name name
     I am doing this in order to support modularity , by allowing easy access to constant file calling or path calling if necessary. """
    name_of_file=input("Enter file name: ")
    return name_of_file

def read_file(file):
    "file_read(file) is pretty self explanatory, it reads the file for you."
    try:
        with open(rf"{file}",'r') as f:
            for line in f:
                print(line.strip())

    except FileNotFoundError:
        print("File doesnt exist.")


if __name__=="__main__":
    main()
