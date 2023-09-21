from datetime import datetime
import definitions
import FileCsv
import ReadorWrite
import os
import serial
import sys
import time
import verifylength as vrlen

class DisconnectedWire(Exception):
    pass

def SetBoard():
    """
    Configure serial port and autoconnect it
    """                                                      
    global ser
    ser = serial.Serial()
    ser.baudrate = 230400                                                               
    ser.bytesize = serial.EIGHTBITS
    ser.parity = serial.PARITY_NONE                                                          
    ser.timeout = 0.5                                                                                                
    ser.port = "/dev/ttyUSB0"                                              
    ser.open()
    
def ReadERD(dst:str, ERD:str) -> str:
    """
    Function to read ERDs.
    
    Args:
        dst: Mc destination
        ERD: Erd to read
    
    Return:
        Dato: Data of ERD read
    """                                    
    Erd = vrlen.longitudERD(ERD)             
    while True:
        complete_frame = ""  
        lectura = ReadorWrite.ReadErd(Erd, dst)        
        ser.write(lectura)                                       
        while True:
            reading = ser.read(1)                 
            concatenate = reading.hex()                                     
            complete_frame += concatenate                                        
            if reading == b'\xE3':                               
                break                   
            if reading == b'':   
                complete_frame = "Verifica conexiones"   
                return "None"
        complete_frame = complete_frame.upper()             
        Byte_ERD = complete_frame[14:18]
        Byte_OK = complete_frame[12:14]
        if (Byte_ERD == ERD) and (Byte_OK == "00"):
            Longitud_Dato_hex = complete_frame[18:20]
            Longitud_Dato_int = int(Longitud_Dato_hex, 16) * 2
            Dato = complete_frame[20:(20 + Longitud_Dato_int)]
            break
    return Dato     

########################################   HEADERS   ############################################

HEADERS = ["Fecha", "Hora", "Erd_CurrentSystemState", "Erd_CycleSelected", "Erd_EStarSensorDryRequested","Erd_RamCycleHistoryRecord.drynessOptionAtStart", 
                    "Erd_RamCycleHistoryRecord.drynessOptionAtEnd", "Erd_RamCycleHistoryRecord.temperatureOptionAtStart", "Erd_RamCycleHistoryRecord.temperatureOptionAtEnd", "Erd_CurrentInletTemperature","Erd_CurrentOutletTemperature", "Erd_OverTemperatureMaxInletTemperature","Erd_HeaterRelay1", "Erd_HeaterRelay2", "Erd_MaxTemperatureSlope","Erd_MinimumFilteredVoltageFromMc", "Erd_FilteredMoistureSensor", "Erd_SmoothMoistureReading", "Erd_CalculatedCurvature", "Erd_CurvatureOccurredCount", "Erd_TrimmerInhibitRelay1", "Erd_TrimmerInhibitRelay2", "Erd_TrimmerBothCoilInhibitRequest", "Erd_DrumMotorState", "Erd_FallbackHeatControlMethodStatus", "Erd_ApplicationVersion", "Erd_ParametricVersion", 
                    "Erd_Personality", "Erd_DrynessOption", "Erd_VentRestriction", "Erd_LoadSizeByAggregation", "Erd_LoadSizeByContact", "Erd_LoadSizeByTemperature","Erd_TargetMoistureVoltageHasBeenReached", "Erd_TargetMoistureVoltage", "Erd_TotalDryTimeCalculatorTimeMultiplierX100", "Erd_TotalDryTimeCalculatorTimeAdderSeconds", "Erd_TimeToReachTargetVoltageSeconds", "Erd_SensingCycleTotalDryingTimeSeconds", "Erd_DrumGroundWatchdogResult", "Erd_ClothDampnessCheckResult", "Erd_Fault_DrumGroundWatchdogDetection", "Erd_SteamValveCycleCountRam","Erd_SteamValveOnTimeDurationInSecondsRam", "Erd_CoolDownStepStatus", "Erd_ExtendedTumbleStepStatus", "Erd_SteamStepStatus", "Erd_EndOfCycleReason", "Erd_ModelNumber", "Erd_SerialNumber", "Erd_AppliancePersonality", "Erd_MachineStatus", "Erd_MachineSubCycle", "Erd_ReduceStaticOption", "Erd_EcoDryOption", "Erd_TemperatureOption", "Erd_ExtendedTumbleOption", "Erd_ScentOption", "Erd_DetangleOption", "Erd_SanitizeOption", 
                    "Erd_TimeLevelOption", "Erd_AlertVolumeOption", "Erd_SteamCycleOption"]  

file_name_System_State = "System_State" + ".csv"
Executable_Path = sys.argv[0]
Actual_Path = os.path.dirname(os.path.abspath(Executable_Path))
file_System_State = os.path.join(Actual_Path, file_name_System_State)

File_Name_Erds = "Unidad_1" + ".csv"
File_Data_Erds = os.path.join(Actual_Path, File_Name_Erds)
if not os.path.exists(File_Data_Erds):
    FileCsv.Write_Data_CSV(File_Data_Erds, HEADERS)

######################################## AGREGAR ERDS ############################################
ERD_List = ["F01B", "200A", "F11F", "F15E", "F301", "F302", "F705", "F30C", "F30D", "F0AE", "F0AC", "F303", "F322", "F11A", "F119", "F07F", "F080", "F073", "F311",
            "F075", "003A", "003B", "FF01", "204D", "F0B2", "F0AF", "F0AB", "F0AD", "F0A9", "F0A8", "F1A5", "F1A6", "F0BC", "F0A7", "F0C7", "F0BA", "FD98",
            "F1A0", "F1A1", "F0ED", "F116", "F137", "F0AA", "0001", "0002", "0035", "2000", "2001", "205E", "2046", "2050", "2053", "2099", "2076",
            "207A", "2077", "F074", "208C"]

def main():
    while True:
        try:
            Count_EndOfCycle = 0
            System_State = ""
            Erd_CurrentSystemState = ""
            tiempo_referencia = time.time()
            FirstCall = True
            contWireDisconnect = 0
            while True:
                SetBoard()
                while True:
                    try:
                        State = ReadERD("C0", "F01B")
                        if State == "None":
                            raise DisconnectedWire("Some wire was disconnected, Verify conections")
                        
                        if contWireDisconnect > 0:
                            if State in ["03", "04", "05"]:
                                FileCsv.Write_Data_System_State(file_System_State, definitions.System_State(State))
                                contWireDisconnect = 0
                                
                            if State not in ["03", "04", "05"]:
                                FileCsv.Write_Data_System_State(file_System_State, "ENDOFCYCLE")
                                contWireDisconnect = 0
                        
                        if (State != System_State) and (State in ["03", "04", "05"]):
                            FileCsv.Write_Data_System_State(file_System_State, definitions.System_State(State))
                            contWireDisconnect = 0

                        if (State != System_State) and (State not in ["03", "04", "05"]):
                            FileCsv.Write_Data_System_State(file_System_State, "ENDOFCYCLE")
                            contWireDisconnect = 0
                        
                        System_State = State
                        
                        if State not in ["03", "04", "05"]:
                            FirstCall = True
                        
                        if (State == "03") or (State == "04") or (((Erd_CurrentSystemState == "05") or (State == "05")) and Count_EndOfCycle == 0):
                            tiempo_actual = time.time()
                            ERDS = []
                            for ERD in ERD_List:
                                Dato = ReadERD("C0", ERD)
                                ERDS.append(Dato)

                            Erd_CurrentSystemState, Erd_CycleSelected, Erd_EStarSensorDryRequested, Erd_RamCycleHistoryRecord, Erd_CurrentInletTemperature, Erd_CurrentOutletTemperature, Erd_OverTemperatureMaxInletTemperature, Erd_HeaterRelay1, Erd_HeaterRelay2, Erd_MaxTemperatureSlope, Erd_MinimumFilteredVoltageFromMc, Erd_FilteredMoistureSensor, Erd_SmoothMoistureReading, Erd_CalculatedCurvature, Erd_CurvatureOccurredCount, Erd_TrimmerInhibitRelay1, Erd_TrimmerInhibitRelay2, Erd_TrimmerBothCoilInhibitRequest, Erd_DrumMotorState, Erd_FallbackHeatControlMethodStatus, Erd_ApplicationVersion, Erd_ParametricVersion, Erd_Personality, Erd_DrynessOption, Erd_VentRestriction, Erd_LoadSizeByAggregation, Erd_LoadSizeByContact, Erd_LoadSizeByTemperature, Erd_TargetMoistureVoltageHasBeenReached, Erd_TargetMoistureVoltage, Erd_TotalDryTimeCalculatorTimeMultiplierX100, Erd_TotalDryTimeCalculatorTimeAdderSeconds, Erd_TimeToReachTargetVoltageSeconds, Erd_SensingCycleTotalDryingTimeSeconds, Erd_DrumGroundWatchdogResult, Erd_ClothDampnessCheckResult, Erd_Fault_DrumGroundWatchdogDetection, Erd_SteamValveCycleCountRam, Erd_SteamValveOnTimeDurationInSecondsRam, Erd_CoolDownStepStatus, Erd_ExtendedTumbleStepStatus, Erd_SteamStepStatus, Erd_EndOfCycleReason, Erd_ModelNumber, Erd_SerialNumber, Erd_AppliancePersonality, Erd_MachineStatus, Erd_MachineSubCycle, Erd_ReduceStaticOption, Erd_EcoDryOption, Erd_TemperatureOption, Erd_ExtendedTumbleOption, Erd_ScentOption, Erd_DetangleOption,Erd_SanitizeOption, Erd_TimeLevelOption, Erd_AlertVolumeOption, Erd_SteamCycleOption = ERDS                                                             
                            
                            Erd_RamCycleHistoryRecord_drynessOptionAtStart = Erd_RamCycleHistoryRecord[100:102]
                            Erd_RamCycleHistoryRecord_drynessOptionAtEnd = Erd_RamCycleHistoryRecord[102:104]
                            Erd_RamCycleHistoryRecord_temperatureOptionAtStart = Erd_RamCycleHistoryRecord[104:106]
                            Erd_RamCycleHistoryRecord_temperatureOptionAtEnd = Erd_RamCycleHistoryRecord[106:108]

                            DATA_TO_WRITE = [Erd_CurrentSystemState, Erd_CycleSelected, Erd_EStarSensorDryRequested, Erd_RamCycleHistoryRecord_drynessOptionAtStart, Erd_RamCycleHistoryRecord_drynessOptionAtEnd, Erd_RamCycleHistoryRecord_temperatureOptionAtStart, Erd_RamCycleHistoryRecord_temperatureOptionAtEnd, Erd_CurrentInletTemperature,Erd_CurrentOutletTemperature, Erd_OverTemperatureMaxInletTemperature, Erd_HeaterRelay1, Erd_HeaterRelay2, Erd_MaxTemperatureSlope, Erd_MinimumFilteredVoltageFromMc, Erd_FilteredMoistureSensor, Erd_SmoothMoistureReading, Erd_CalculatedCurvature, Erd_CurvatureOccurredCount, Erd_TrimmerInhibitRelay1, Erd_TrimmerInhibitRelay2, Erd_TrimmerBothCoilInhibitRequest, Erd_DrumMotorState, Erd_FallbackHeatControlMethodStatus, Erd_ApplicationVersion, Erd_ParametricVersion, Erd_Personality, Erd_DrynessOption, Erd_VentRestriction, Erd_LoadSizeByAggregation, Erd_LoadSizeByContact, Erd_LoadSizeByTemperature, Erd_TargetMoistureVoltageHasBeenReached, Erd_TargetMoistureVoltage, Erd_TotalDryTimeCalculatorTimeMultiplierX100, Erd_TotalDryTimeCalculatorTimeAdderSeconds,Erd_TimeToReachTargetVoltageSeconds, Erd_SensingCycleTotalDryingTimeSeconds, Erd_DrumGroundWatchdogResult, Erd_ClothDampnessCheckResult, Erd_Fault_DrumGroundWatchdogDetection, Erd_SteamValveCycleCountRam, Erd_SteamValveOnTimeDurationInSecondsRam, Erd_CoolDownStepStatus, Erd_ExtendedTumbleStepStatus, Erd_SteamStepStatus, Erd_EndOfCycleReason, Erd_ModelNumber, Erd_SerialNumber, Erd_AppliancePersonality, Erd_MachineStatus, Erd_MachineSubCycle, Erd_ReduceStaticOption, Erd_EcoDryOption, Erd_TemperatureOption, Erd_ExtendedTumbleOption, Erd_ScentOption, Erd_DetangleOption, Erd_SanitizeOption, Erd_TimeLevelOption, Erd_AlertVolumeOption, Erd_SteamCycleOption]
                            
                            if (tiempo_actual - tiempo_referencia >= 60) or FirstCall or (Count_EndOfCycle == 0 and Erd_CurrentSystemState == "05"):
                                TimeS = datetime.now().strftime("%H:%M")
                                DiaS = datetime.now().strftime("%d-%m-%Y") 
                                try:
                                    DATA_TO_CSV = [DiaS] + [TimeS] + definitions.ERDS_TO_WRITE(DATA_TO_WRITE)
                                    print(DATA_TO_CSV)
                                    FileCsv.Write_Data_CSV(File_Data_Erds, DATA_TO_CSV) 
                                    tiempo_referencia = tiempo_actual
                                    FirstCall = False
                                    if Erd_CurrentSystemState == "05":
                                        Count_EndOfCycle = 1
                                    else:
                                        Count_EndOfCycle = 0
                                    
                                except ValueError:
                                    print("ValueError")
                                            
                    except DisconnectedWire:
                        if contWireDisconnect > 3:
                            FileCsv.Write_Data_System_State(file_System_State, "WIREDISCONNECT")
                            print("Some wire was disconnected")
                        contWireDisconnect += 1
                        System_State = State
                        time.sleep(1)
                        
        except (serial.SerialException, OSError):
            FileCsv.Write_Data_System_State(file_System_State, "PORTDISCONNECT")
            print("No se pudo conectar al puerto")
            time.sleep(3) 

if __name__ == "__main__":
    main()
