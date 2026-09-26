import sys

def main():
    check_and_return_pattern(path(),pattern())

def absolute_or_relative_path_checker():
    """This checks whether the file is a relative or absolute file in a simple manner
    by checking if the following files belong to the c drive"""
    for i in sys.argv:
        if 'c:' in i.lower():
            return ('absolute',sys.argv.index(i))
            break
    else:
        return ('relative',-1)
        

def path_corrector(absolute_or_relative_path_checker):
    """This is a safety measure , incase there is an absolute path with spaces included
    then to avoid problems due to sys.argv functionality"""
    if absolute_or_relative_path_checker[0]=='absolute':
        correct_path=" ".join(sys.argv[absolute_or_relative_path_checker[1]:])
    else:
        correct_path=sys.argv[absolute_or_relative_path_checker[1]]

    return correct_path




def pattern():
    index_finder=absolute_or_relative_path_checker()[1]
    """joins the sys.argv with 1 white space to represent a singular pattern"""
    pattern=" ".join((sys.argv[1:index_finder]))
    return pattern


def path():
    """path() function directly calls the first system arguement that is the path"""
    name_of_file=path_corrector(absolute_or_relative_path_checker())
    return name_of_file

def check_and_return_pattern(file,pattern):
    """Check and return pattern takes two arguement, the file path and the pattern"""
    try:
        with open(rf"{file}",'r') as f:
            for line in f:
                if pattern.lower() in line.lower().strip():
                    print(f"{line.strip()}")
                else:
                    continue

    except FileNotFoundError:
        print("File doesnt exist.")


if __name__=="__main__":
    main()
