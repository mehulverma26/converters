# requirements
# pip install pandas openpyxl
import pandas as pd
import os


def get_file_name(file_path):
    file_path_components = file_path.split("\\")
    file_name_and_extension = file_path_components[-1].rsplit(".", 1)
    return file_name_and_extension[0]


a = input("enter the location of the file with extension: ")
if os.path.exists(a):
    new_dataFrame = pd.read_csv(a)
    b = input("enter the path where you want to save the pdf: ")
    c = input("enter the name of the pdf that you want to save: ")
    if c == "":
        c = get_file_name(a)
    d = b + "\\"
    e = d + c + ".xlsx"
    new_dataFrame.to_excel(e, index=False)
else:
    print("file does not exist")
