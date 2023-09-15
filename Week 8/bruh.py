import csv

str_category = "Category"
file_infile = open("Google Play Store.csv", "r")
csv_dict_reader = csv.DictReader(file_infile)

for lst_cols in csv_dict_reader:
    print(lst_cols)

file_infile.close()
