import ReadorWrite
import verifylength as vrlen
import serial
import serial.tools.list_ports
import csv
from pathlib import Path
from datetime import datetime
import time

def SetBoard():                                                      
    global ser
    ser = serial.Serial()
    ser.baudrate = 230400                                                               
    ser.bytesize = serial.EIGHTBITS
    ser.parity = serial.PARITY_NONE                                                          
    ser.timeout = 0.5                                                                                                
    ser.port = "/dev/ttyUSB0"                                                
    ser.open()    
    
def ReadButton(dst, ERD):                                    
    longitud_ERD = vrlen.longitudERD(ERD)             
    Is_Correct = True
    while Is_Correct:
        complete_frame = ""  
        lectura = ReadorWrite.ReadErd(longitud_ERD, dst)        
        ser.write(lectura)                                       
        while True:
            reading = ser.read(1)                 
            concatenate = reading.hex()                                     
            complete_frame += concatenate                                        
            if reading == b'\xE3':                               
                break                   
            if reading == b'':   
                complete_frame = "Verifica conexiones"   
                break
        Dato = complete_frame 
        print(Dato) 
        complete_frame = complete_frame.upper()             
        Byte_ERD = complete_frame[14:18]
        if Byte_ERD == ERD:
            Longitud_Dato_hex = complete_frame[18:20]
            Longitud_Dato_int = int(Longitud_Dato_hex) * 2
            Dato = complete_frame[20:(20 + Longitud_Dato_int)]
            Is_Correct = False
    return Dato     

ERD_List = ["F01B", "2000", "F7D0"]

def check_file(my_file):
    with open(my_file, mode="a") as file:  
        file = csv.writer(file, delimiter=",",
                quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        file.writerow(["Dia", "Hora", "ERD1", "ERD2", "ERD3", 
                    "ERD4", "ERD5", "ERD6", "ERD7", "ERD8","\n"])

TimeStr = datetime.now().strftime("%H-%M-%S")
diaStr = datetime.now().strftime("%d-%m-%Y")
file_name = "Prueba" + diaStr + "_" + TimeStr + ".csv"
my_file = Path("/home/pi/Desktop/GEA3-Secadora-Python/Data CSV/" + file_name)
check_file(my_file)

def main():
    while True:
        SetBoard()
        ERDS = []
        TimeS = datetime.now().strftime("%H:%M:%S")
        diaS = datetime.now().strftime("%d-%m-%Y")
        for ERD in ERD_List:
            Dato = ReadButton("C0", ERD)
            ERDS.append(Dato)
            
        ERD_F01B, ERD_2000, ERD_F7D0 = ERDS
        try:      
            with open(my_file, "a") as file: 
                file = csv.writer(file, delimiter=",",
                                    quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
                file.writerow([diaS, TimeS, ERD_F01B, ERD_2000, ERD_F7D0, "\n"])
            print(ERDS)
            time.sleep(1)
        
        except PermissionError:
            print(f'El archivo "{file_name}" está abierto esperando a que se cierre')
            time.sleep(1)
            
if __name__ == "__main__":
    main()