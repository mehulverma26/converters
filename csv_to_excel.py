# requirements
# pip install pandas openpyxl
import pandas as pd
import os

a = input("enter the location of the file with extension: ")
if os.path.exists(a):
    new_dataFrame = pd.read_csv(a)
    b = input("enter the path where you want to save the pdf: ")
    c = input("enter the name of the pdf that you want to save: ")
    d = b + "\\"
    e = d + c + ".xlsx"
    new_dataFrame.to_excel(e, index=False)
else:
    print("file does not exist")
