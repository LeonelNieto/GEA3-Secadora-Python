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
        complete_frame = complete_frame.upper()             
        Byte_ERD = complete_frame[14:18]
        if Byte_ERD == ERD:
            Longitud_Dato_hex = complete_frame[18:20]
            Longitud_Dato_int = int(Longitud_Dato_hex, 16) * 2
            Dato = complete_frame[20:(20 + Longitud_Dato_int)]
            Is_Correct = False
    return Dato     

########################################   HEADERS   ############################################
def check_file(my_file):
    with open(my_file, mode="a") as file:  
        file = csv.writer(file, delimiter=",",
                quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        file.writerow(["Dia", "Hora", "Erd_CurrentSystemState", "Erd_CycleSelected", "Erd_EStarSensorDryRequested", "Erd_SteamCycleOptionRequest",
                    "Erd_RamCycleHistoryRecord.drynessOptionAtStart", "Erd_RamCycleHistoryRecord.drynessOptionAtEnd", "Erd_RamCycleHistoryRecord.temperatureOptionAtStart", 
                    "Erd_RamCycleHistoryRecord.temperatureOptionAtEnd", "Erd_CurrentInletTemperature","Erd_CurrentOutletTemperature", "Erd_OverTemperatureMaxInletTemperature",
                    "Erd_HeaterRelay1", "Erd_HeaterRelay2", "Erd_MaxTemperatureSlope", "Erd_HeatControlParametric", "Erd_MinimumFilteredVoltageFromMc", "Erd_FilteredMoistureSensor",
                    "Erd_SmoothMoistureReading", "Erd_CalculatedCurvature", "Erd_CurvatureOccurredCount", "Erd_TrimmerInhibitRelay1", "Erd_TrimmerInhibitRelay2",
                    "Erd_TrimmerBothCoilInhibitRequest", "Erd_DrumMotorState", "Erd_FallbackHeatControlMethodStatus", "Erd_ApplicationVersion", "Erd_ParametricVersion", 
                    "Erd_Personality", "Erd_DrynessOption", "Erd_VentRestriction", "Erd_LoadSizeByAggregation", "Erd_LoadSizeByContact", "Erd_LoadSizeByTemperature",
                    "Erd_TargetMoistureVoltageHasBeenReached", "Erd_TargetMoistureVoltage", "Erd_TotalDryTimeCalculatorTimeMultiplierX100", "Erd_TotalDryTimeCalculatorTimeAdderSeconds",
                    "Erd_SensorDryTemperatureMultiplierx100", "Erd_TimeToReachTargetVoltageSeconds", "Erd_SensingCycleTotalDryingTimeSeconds", "Erd_DrumGroundWatchdogResult", "Erd_ClothDampnessCheckResult", "Erd_Fault_DrumGroundWatchdogDetection", "Erd_SteamValveCycleCountRam",
                    "Erd_SteamValveOnTimeDurationInSecondsRam", "Erd_CoolDownStepStatus", "Erd_ExtendedTumbleStepStatus", "Erd_SteamStepStatus", "Erd_EndOfCycleReason", "\n"])     

TimeStr = datetime.now().strftime("%H-%M-%S")
diaStr = datetime.now().strftime("%d-%m-%Y")
file_name = "Prueba" + diaStr + "_" + TimeStr + ".txt"
my_file = Path("/home/pi/Desktop/" + file_name)
check_file(my_file)

######################################## AGREGAR ERDS ############################################
ERD_List = ["F01B", "200A", "F11F", "F187", "F15E", "F301", "F302", "F705", "F30C", "F30D", "F0AE", "F06D", "F0AC", "F303", "F322", "F11A", "F119", "F07F", "F080", "F073", "F311",
            "F075", "003A", "003B", "FF01", "204D", "F0B2", "F0AF", "F0AB", "F0AD", "F0A9", "F0A8", "F1A5", "F1A6", "F816", "F0BC", "F0A7", "F0C7", "F0BA", "FD98",
            "F1A0", "F1A1", "F0ED", "F116", "F137", "F0AA"]

def main():
    while True:
        SetBoard()
        ERDS = []
        TimeS = datetime.now().strftime("%H:%M:%S")
        diaS = datetime.now().strftime("%d-%m-%Y")
        for ERD in ERD_List:
            Dato = ReadButton("C0", ERD)
            print(Dato)
            ERDS.append(Dato)
            
        Erd_CurrentSystemState, Erd_CycleSelected, Erd_EStarSensorDryRequested, Erd_SteamCycleOptionRequest, Erd_RamCycleHistoryRecord, Erd_CurrentInletTemperature,Erd_CurrentOutletTemperature, Erd_OverTemperatureMaxInletTemperature, Erd_HeaterRelay1, Erd_HeaterRelay2, Erd_MaxTemperatureSlope, Erd_HeatControlParametric, Erd_MinimumFilteredVoltageFromMc, Erd_FilteredMoistureSensor, Erd_SmoothMoistureReading, Erd_CalculatedCurvature, Erd_CurvatureOccurredCount, Erd_TrimmerInhibitRelay1, Erd_TrimmerInhibitRelay2, Erd_TrimmerBothCoilInhibitRequest, Erd_DrumMotorState, Erd_FallbackHeatControlMethodStatus, Erd_ApplicationVersion, Erd_ParametricVersion, Erd_Personality, Erd_DrynessOption, Erd_VentRestriction, Erd_LoadSizeByAggregation, Erd_LoadSizeByContact, Erd_LoadSizeByTemperature, Erd_TargetMoistureVoltageHasBeenReached, Erd_TargetMoistureVoltage, Erd_TotalDryTimeCalculatorTimeMultiplierX100, Erd_TotalDryTimeCalculatorTimeAdderSeconds, Erd_SensorDryTemperatureMultiplierx100, Erd_TimeToReachTargetVoltageSeconds, Erd_SensingCycleTotalDryingTimeSeconds,Erd_DrumGroundWatchdogResult, Erd_ClothDampnessCheckResult, Erd_Fault_DrumGroundWatchdogDetection, Erd_SteamValveCycleCountRam, Erd_SteamValveOnTimeDurationInSecondsRam, Erd_CoolDownStepStatus, Erd_ExtendedTumbleStepStatus, Erd_SteamStepStatus, Erd_EndOfCycleReason = ERDS                                                             

        Erd_RamCycleHistoryRecord_drynessOptionAtStart = Erd_RamCycleHistoryRecord[100:102]
        Erd_RamCycleHistoryRecord_drynessOptionAtEnd = Erd_RamCycleHistoryRecord[102:104]
        Erd_RamCycleHistoryRecord_temperatureOptionAtStart = Erd_RamCycleHistoryRecord[104:106]
        Erd_RamCycleHistoryRecord_temperatureOptionAtEnd = Erd_RamCycleHistoryRecord[106:108]

        with open(my_file, "a") as file: 
            file = csv.writer(file, delimiter=",",
                                quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            file.writerow([diaS, TimeS, Erd_CurrentSystemState, Erd_CycleSelected, Erd_EStarSensorDryRequested, Erd_SteamCycleOptionRequest, Erd_RamCycleHistoryRecord_drynessOptionAtStart, Erd_RamCycleHistoryRecord_drynessOptionAtEnd, Erd_RamCycleHistoryRecord_temperatureOptionAtStart, Erd_RamCycleHistoryRecord_temperatureOptionAtEnd, Erd_CurrentInletTemperature,Erd_CurrentOutletTemperature, Erd_OverTemperatureMaxInletTemperature, Erd_HeaterRelay1, Erd_HeaterRelay2, Erd_MaxTemperatureSlope, Erd_HeatControlParametric, Erd_MinimumFilteredVoltageFromMc, Erd_FilteredMoistureSensor, Erd_SmoothMoistureReading, Erd_CalculatedCurvature, Erd_CurvatureOccurredCount, Erd_TrimmerInhibitRelay1, Erd_TrimmerInhibitRelay2, Erd_TrimmerBothCoilInhibitRequest, Erd_DrumMotorState, Erd_FallbackHeatControlMethodStatus, Erd_ApplicationVersion, Erd_ParametricVersion, Erd_Personality, Erd_DrynessOption, Erd_VentRestriction, Erd_LoadSizeByAggregation, Erd_LoadSizeByContact, Erd_LoadSizeByTemperature, Erd_TargetMoistureVoltageHasBeenReached, Erd_TargetMoistureVoltage, Erd_TotalDryTimeCalculatorTimeMultiplierX100, Erd_TotalDryTimeCalculatorTimeAdderSeconds, Erd_SensorDryTemperatureMultiplierx100, Erd_TimeToReachTargetVoltageSeconds, Erd_SensingCycleTotalDryingTimeSeconds, Erd_DrumGroundWatchdogResult, Erd_ClothDampnessCheckResult, Erd_Fault_DrumGroundWatchdogDetection, Erd_SteamValveCycleCountRam, Erd_SteamValveOnTimeDurationInSecondsRam, Erd_CoolDownStepStatus, Erd_ExtendedTumbleStepStatus, Erd_SteamStepStatus, Erd_EndOfCycleReason, "\n"])      

        time.sleep(59.74)
            
if __name__ == "__main__":
    main()
