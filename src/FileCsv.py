import csv

def Write_Data_CSV(PathFile, Data):
    with open(PathFile, "a") as file: 
        file = csv.writer(file, delimiter=",",
                            quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        file.writerow(Data)

def Write_Data_System_State(PathFile, Data):
    data = [[Data]]
    with open(PathFile, "w", newline='') as file:
        writer = csv.writer(file, delimiter=",", quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        writer.writerows(data)
