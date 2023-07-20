# this is a work in progress
import pandas as pd

a = input("enter the location of the file with extension: ")
if os.path.exists(a):
    new_dataFrame = pd.read_csv(a)
    b = input("enter the path where you want to save the pdf: ")
    c = input("enter the name of the pdf that you want to save: ")
    new_dataFrame.to_excel("SampleExcelFile.xlsx", sheet_name="Subjects", index=False)
else:
    print("file does not exist")
