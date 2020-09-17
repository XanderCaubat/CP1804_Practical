import os

print("The files and folders in {} are:".format(os.getcwd()))
items = os.listdir('../prac03')
for item in items:
    print(item)