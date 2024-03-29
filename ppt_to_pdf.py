# run pip install pywin32 before using
import sys
import os
import glob
import win32com.client


def convert(files, formatType=32):
    powerpoint = win32com.client.Dispatch("Powerpoint.Application")
    powerpoint.Visible = 1
    for filename in files:
        newname = os.path.splitext(filename)[0] + ".pdf"
        deck = powerpoint.Presentations.Open(filename)
        deck.SaveAs(newname, formatType)
        deck.Close()
    powerpoint.Quit()


files = glob.glob(input("enter the location of ppt: "))
convert(files)
