import os

print("The files and folders in {} are:".format(os.getcwd()))
items = os.listdir('../Prac03')
for item in items:
    print(item)