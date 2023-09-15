import csv # import csv library
'''This code takes a file input and header input
the function utilises those inputs to open the file then checks the header
the header is added to a dictionary called unique_list and stores the count of the header
it then gets printed'''

# a function that takes the file and header and checks it adding the selected header into a list and the count of the header into a dictionary
def read_and_check(file, header): 
    unique_list = {} # initiates a unique list
    file_infile = open(file, "r") # open file
    csv_dict_reader = csv.DictReader(file_infile) # reads the file and store in dictionary

    for lst_cols in csv_dict_reader: #iterates through the list of columns
        if lst_cols[header] not in unique_list:
            unique_list[lst_cols[header]] = 1 # if the value is not in unique_list add it with the value 1
        else:
            unique_list[lst_cols[header]] += 1 # if the value is is in unique_list increase value by 1
                  
    print(unique_list)
  
    file_infile.close() #close the file

# Testing
read_and_check("Google Play Store.csv", "Category")
read_and_check("Google Play Store.csv", "Rating")