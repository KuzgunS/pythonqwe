def main():

    filename = input('Enter a filename: ') # get the name of the file to be opened
    #coffee.txt girersen olur. 
    try:
        infile = open(filename, 'r') # open the file

        contents = infile.read() # read the file's contents

        print(contents) # display the file's contents

        infile.close() # close the file

    except IOError:
        print('An error occurred trying to read the file',filename)


main()
