import csv # import csv library
'''This code figures out how many apps are last updated in 2018
it prints each lines year, month, day
then checks for the year 2018
and adds to the counter
the counter at the end is how many apps are last updated'''

counter = 0 #intialise the counter
file_infile = open("Google Play Store.csv", "r") #open the file google_play_store
csv_reader = csv.reader(file_infile) #splits using csvreader

for lst_cols in csv_reader: # iterates through each line
    print(lst_cols[10]) # index 11 in the list contains the date
    if "2018" in lst_cols[10]: # iterates through each line
        counter = counter + 1 
    print("There are " + str(counter) + " apps last updated in 2018") # prints the amount of apps last updated
 