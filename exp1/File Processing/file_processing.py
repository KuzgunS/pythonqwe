


def main():

    found = False # flag var

    search = input("Enter a description to search for: ") # get the search val

    coffee_file = open('coffee.txt', 'r') # open coffee.txt file in read mode

    descr = coffee_file.readline() #read the 1st record's description field

    #read the rest of the file
    while descr != '':

        qty = float(coffee_file.readline()) # read the quantity field

        descr = descr.rstrip('\n') # strip the \n from the description. 

        if descr == search:
            #display the record
            print('Description: ',descr)
            print('Quantity: ',qty )
            print()

            found = True

        descr = coffee_file.readline() # read the next description. Eğer '' ise while'a tekrar giremiyor

    coffee_file.close() # close the file

    if not found:
        print('That item wasn\'t wfound in the file.')

# call main func to run
main()

