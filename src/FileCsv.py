import csv
from pathlib import Path
from datetime import datetime

def File_CSV(Name_File, Ubication_File):
    TimeStr = datetime.now().strftime("%H-%M-%S")
    diaStr = datetime.now().strftime("%d-%m-%Y")
    file_name = Name_File + "_" + diaStr + "_" + TimeStr + ".csv"
    file_Erd = Path(Ubication_File + file_name)
    return file_Erd

def Write_Data_CSV(PathFile, Data):
    with open(PathFile, "a") as file: 
        file = csv.writer(file, delimiter=",",
                            quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        file.writerow(Data)
