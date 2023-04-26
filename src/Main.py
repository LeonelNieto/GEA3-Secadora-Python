import ReadorWrite
import verifylength as vrlen
import serial
from datetime import datetime
import time
import FileCsv
import definitions

def SetBoard():                                                      
    global ser
    ser = serial.Serial()
    ser.baudrate = 230400                                                               
    ser.bytesize = serial.EIGHTBITS
    ser.parity = serial.PARITY_NONE                                                          
    ser.timeout = 0.5                                                                                                
    ser.port = 'COM1'                                               
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
        Byte_OK = complete_frame[12:14]
        if (Byte_ERD == ERD) and (Byte_OK == "00"):
            Longitud_Dato_hex = complete_frame[18:20]
            Longitud_Dato_int = int(Longitud_Dato_hex, 16) * 2
            Dato = complete_frame[20:(20 + Longitud_Dato_int)]
            Is_Correct = False
    return Dato     

TimeStr = datetime.now().strftime("%H-%M-%S")
diaStr = datetime.now().strftime("%d-%m-%Y")
path = "C:/Users/LNLMEXID/Desktop/Pruebas Archivos/"

######################################################### CREATE FILES ####################################################################
file_Erd_CurrentSystemState = FileCsv.File_CSV("Erd_CurrentSystemState", path)
file_Erd_Erd_CycleSelected = FileCsv.File_CSV("Erd_CycleSelected", path)
file_Erd_Erd_EStarSensorDryRequested = FileCsv.File_CSV("Erd_EStarSensorDryRequested", path)
file_Erd_Erd_RamCycleHistoryRecord = FileCsv.File_CSV("Erd_RamCycleHistoryRecord", path)
file_Erd_Erd_CurrentInletTemperature = FileCsv.File_CSV("Erd_CurrentInletTemperature", path)
file_Erd_Erd_CurrentOutletTemperature = FileCsv.File_CSV("Erd_CurrentOutletTemperature", path)
file_Erd_Erd_OverTemperatureMaxInletTemperature = FileCsv.File_CSV("Erd_OverTemperatureMaxInletTemperature", path)
file_Erd_Erd_HeaterRelay1 = FileCsv.File_CSV("Erd_HeaterRelay1", path)
file_Erd_Erd_HeaterRelay2 = FileCsv.File_CSV("Erd_HeaterRelay2", path)
file_Erd_Erd_MaxTemperatureSlope = FileCsv.File_CSV("Erd_MaxTemperatureSlope", path)
file_Erd_Erd_HeatControlParametric = FileCsv.File_CSV("Erd_HeatControlParametric", path)
file_Erd_Erd_MinimumFilteredVoltageFromMc = FileCsv.File_CSV("Erd_MinimumFilteredVoltageFromMc", path)
file_Erd_Erd_FilteredMoistureSensor = FileCsv.File_CSV("Erd_FilteredMoistureSensor", path)
file_Erd_Erd_SmoothMoistureReading = FileCsv.File_CSV("Erd_SmoothMoistureReading", path)
file_Erd_Erd_CalculatedCurvature = FileCsv.File_CSV("Erd_CalculatedCurvature", path)
file_Erd_Erd_CurvatureOccurredCount = FileCsv.File_CSV("Erd_CurvatureOccurredCount", path)
file_Erd_Erd_TrimmerInhibitRelay1 = FileCsv.File_CSV("Erd_TrimmerInhibitRelay1", path)
file_Erd_Erd_TrimmerInhibitRelay2 = FileCsv.File_CSV("Erd_TrimmerInhibitRelay2", path)
file_Erd_Erd_TrimmerBothCoilInhibitRequest = FileCsv.File_CSV("Erd_TrimmerBothCoilInhibitRequest", path)
file_Erd_Erd_DrumMotorState = FileCsv.File_CSV("Erd_DrumMotorState", path)
file_Erd_Erd_FallbackHeatControlMethodStatus = FileCsv.File_CSV("Erd_FallbackHeatControlMethodStatus", path)
file_Erd_Erd_ApplicationVersion = FileCsv.File_CSV("Erd_ApplicationVersion", path)
file_Erd_Erd_ParametricVersion = FileCsv.File_CSV("Erd_ParametricVersion", path)
file_Erd_Erd_Personality = FileCsv.File_CSV("Erd_Personality", path)
file_Erd_Erd_DrynessOption = FileCsv.File_CSV("Erd_DrynessOption", path)
file_Erd_Erd_VentRestriction = FileCsv.File_CSV("Erd_VentRestriction", path)
file_Erd_Erd_LoadSizeByAggregation = FileCsv.File_CSV("Erd_LoadSizeByAggregation", path)
file_Erd_Erd_LoadSizeByContact = FileCsv.File_CSV("Erd_LoadSizeByContact", path)
file_Erd_Erd_LoadSizeByTemperature = FileCsv.File_CSV("Erd_LoadSizeByTemperature", path)
file_Erd_Erd_TargetMoistureVoltageHasBeenReached = FileCsv.File_CSV("Erd_TargetMoistureVoltageHasBeenReached", path)
file_Erd_Erd_TargetMoistureVoltage = FileCsv.File_CSV("Erd_TargetMoistureVoltage", path)
file_Erd_Erd_TotalDryTimeCalculatorTimeMultiplierX100 = FileCsv.File_CSV("Erd_TotalDryTimeCalculatorTimeMultiplierX100", path)
file_Erd_Erd_TotalDryTimeCalculatorTimeAdderSeconds = FileCsv.File_CSV("Erd_TotalDryTimeCalculatorTimeAdderSeconds", path)
file_Erd_Erd_SensorDryTemperatureMultiplierx100 = FileCsv.File_CSV("Erd_SensorDryTemperatureMultiplierx100", path)
file_Erd_Erd_TimeToReachTargetVoltageSeconds = FileCsv.File_CSV("Erd_TimeToReachTargetVoltageSeconds", path)
file_Erd_Erd_SensingCycleTotalDryingTimeSeconds = FileCsv.File_CSV("Erd_SensingCycleTotalDryingTimeSeconds", path)
file_Erd_Erd_DrumGroundWatchdogResult = FileCsv.File_CSV("Erd_DrumGroundWatchdogResult", path)
file_Erd_Erd_ClothDampnessCheckResult = FileCsv.File_CSV("Erd_ClothDampnessCheckResult", path)
file_Erd_Erd_Fault_DrumGroundWatchdogDetection = FileCsv.File_CSV("Erd_Fault_DrumGroundWatchdogDetection", path)
file_Erd_Erd_SteamValveCycleCountRam = FileCsv.File_CSV("Erd_SteamValveCycleCountRam", path)
file_Erd_Erd_SteamValveOnTimeDurationInSecondsRam = FileCsv.File_CSV("Erd_SteamValveOnTimeDurationInSecondsRam", path)
file_Erd_Erd_CoolDownStepStatus = FileCsv.File_CSV("Erd_CoolDownStepStatus", path)
file_Erd_Erd_ExtendedTumbleStepStatus = FileCsv.File_CSV("Erd_ExtendedTumbleStepStatus", path)
file_Erd_Erd_SteamStepStatus = FileCsv.File_CSV("Erd_SteamStepStatus", path)
file_Erd_Erd_EndOfCycleReason = FileCsv.File_CSV("Erd_EndOfCycleReason", path)

######################################################### CREATE HEADERS ##################################################################
FileCsv.Write_Data_CSV(file_Erd_CurrentSystemState, ["Fecha", "Hora", "Erd_CurrentSystemState"])
FileCsv.Write_Data_CSV(file_Erd_Erd_CycleSelected, ["Fecha", "Hora", "Erd_CycleSelected"])
FileCsv.Write_Data_CSV(file_Erd_Erd_EStarSensorDryRequested, ["Fecha", "Hora", "Erd_EStarSensorDryRequested"])
FileCsv.Write_Data_CSV(file_Erd_Erd_RamCycleHistoryRecord, ["Fecha", "Hora", "Erd_RamCycleHistoryRecord_drynessOptionAtStart", "Erd_RamCycleHistoryRecord_drynessOptionAtEnd", "Erd_RamCycleHistoryRecord_temperatureOptionAtStart", "Erd_RamCycleHistoryRecord_temperatureOptionAtEnd"])
FileCsv.Write_Data_CSV(file_Erd_Erd_CurrentInletTemperature, ["Fecha", "Hora", "Erd_CurrentInletTemperature"])
FileCsv.Write_Data_CSV(file_Erd_Erd_CurrentOutletTemperature, ["Fecha", "Hora", "Erd_CurrentOutletTemperature"])
FileCsv.Write_Data_CSV(file_Erd_Erd_OverTemperatureMaxInletTemperature, ["Fecha", "Hora", "Erd_OverTemperatureMaxInletTemperature"])
FileCsv.Write_Data_CSV(file_Erd_Erd_HeaterRelay1, ["Fecha", "Hora", "Erd_HeaterRelay1"])
FileCsv.Write_Data_CSV(file_Erd_Erd_HeaterRelay2, ["Fecha", "Hora", "Erd_HeaterRelay2"])
FileCsv.Write_Data_CSV(file_Erd_Erd_MaxTemperatureSlope, ["Fecha", "Hora", "Erd_MaxTemperatureSlope"])
FileCsv.Write_Data_CSV(file_Erd_Erd_HeatControlParametric, ["Fecha", "Hora", "Erd_HeatControlParametric"])
FileCsv.Write_Data_CSV(file_Erd_Erd_MinimumFilteredVoltageFromMc, ["Fecha", "Hora", "Erd_MinimumFilteredVoltageFromMc"])
FileCsv.Write_Data_CSV(file_Erd_Erd_FilteredMoistureSensor, ["Fecha", "Hora", "Erd_FilteredMoistureSensor"])
FileCsv.Write_Data_CSV(file_Erd_Erd_SmoothMoistureReading, ["Fecha", "Hora", "Erd_SmoothMoistureReading"])
FileCsv.Write_Data_CSV(file_Erd_Erd_CalculatedCurvature, ["Fecha", "Hora", "Erd_CalculatedCurvature"])
FileCsv.Write_Data_CSV(file_Erd_Erd_CurvatureOccurredCount, ["Fecha", "Hora", "Erd_CurvatureOccurredCount"])
FileCsv.Write_Data_CSV(file_Erd_Erd_TrimmerInhibitRelay1, ["Fecha", "Hora", "Erd_TrimmerInhibitRelay1"])
FileCsv.Write_Data_CSV(file_Erd_Erd_TrimmerInhibitRelay2, ["Fecha", "Hora", "Erd_TrimmerInhibitRelay2"])
FileCsv.Write_Data_CSV(file_Erd_Erd_TrimmerBothCoilInhibitRequest, ["Fecha", "Hora", "Erd_TrimmerBothCoilInhibitRequest"])
FileCsv.Write_Data_CSV(file_Erd_Erd_DrumMotorState, ["Fecha", "Hora", "Erd_DrumMotorState"])
FileCsv.Write_Data_CSV(file_Erd_Erd_FallbackHeatControlMethodStatus, ["Fecha", "Hora", "Erd_FallbackHeatControlMethodStatus"])
FileCsv.Write_Data_CSV(file_Erd_Erd_ApplicationVersion, ["Fecha", "Hora", "Erd_ApplicationVersion"])
FileCsv.Write_Data_CSV(file_Erd_Erd_ParametricVersion, ["Fecha", "Hora", "Erd_ParametricVersion"])
FileCsv.Write_Data_CSV(file_Erd_Erd_Personality, ["Fecha", "Hora", "Erd_Personality"])
FileCsv.Write_Data_CSV(file_Erd_Erd_DrynessOption, ["Fecha", "Hora", "Erd_DrynessOption"])
FileCsv.Write_Data_CSV(file_Erd_Erd_VentRestriction, ["Fecha", "Hora", "Erd_VentRestriction"])
FileCsv.Write_Data_CSV(file_Erd_Erd_LoadSizeByAggregation, ["Fecha", "Hora", "Erd_LoadSizeByAggregation"])
FileCsv.Write_Data_CSV(file_Erd_Erd_LoadSizeByContact, ["Fecha", "Hora", "Erd_LoadSizeByContact"])
FileCsv.Write_Data_CSV(file_Erd_Erd_LoadSizeByTemperature, ["Fecha", "Hora", "Erd_LoadSizeByTemperature"])
FileCsv.Write_Data_CSV(file_Erd_Erd_TargetMoistureVoltageHasBeenReached, ["Fecha", "Hora", "Erd_TargetMoistureVoltageHasBeenReached"])
FileCsv.Write_Data_CSV(file_Erd_Erd_TargetMoistureVoltage, ["Fecha", "Hora", "Erd_TargetMoistureVoltage"])
FileCsv.Write_Data_CSV(file_Erd_Erd_TotalDryTimeCalculatorTimeMultiplierX100, ["Fecha", "Hora", "Erd_TotalDryTimeCalculatorTimeMultiplierX100"])
FileCsv.Write_Data_CSV(file_Erd_Erd_TotalDryTimeCalculatorTimeAdderSeconds, ["Fecha", "Hora", "Erd_TotalDryTimeCalculatorTimeAdderSeconds"])
FileCsv.Write_Data_CSV(file_Erd_Erd_SensorDryTemperatureMultiplierx100, ["Fecha", "Hora", "Erd_SensorDryTemperatureMultiplierx100"])
FileCsv.Write_Data_CSV(file_Erd_Erd_TimeToReachTargetVoltageSeconds, ["Fecha", "Hora", "Erd_TimeToReachTargetVoltageSeconds"])
FileCsv.Write_Data_CSV(file_Erd_Erd_SensingCycleTotalDryingTimeSeconds, ["Fecha", "Hora", "Erd_SensingCycleTotalDryingTimeSeconds"])
FileCsv.Write_Data_CSV(file_Erd_Erd_DrumGroundWatchdogResult, ["Fecha", "Hora", "Erd_DrumGroundWatchdogResult"])
FileCsv.Write_Data_CSV(file_Erd_Erd_ClothDampnessCheckResult, ["Fecha", "Hora", "Erd_ClothDampnessCheckResult"])
FileCsv.Write_Data_CSV(file_Erd_Erd_Fault_DrumGroundWatchdogDetection, ["Fecha", "Hora", "Erd_Fault_DrumGroundWatchdogDetection"])
FileCsv.Write_Data_CSV(file_Erd_Erd_SteamValveCycleCountRam, ["Fecha", "Hora", "Erd_SteamValveCycleCountRam"])
FileCsv.Write_Data_CSV(file_Erd_Erd_SteamValveOnTimeDurationInSecondsRam, ["Fecha", "Hora", "Erd_SteamValveOnTimeDurationInSecondsRam"])
FileCsv.Write_Data_CSV(file_Erd_Erd_CoolDownStepStatus, ["Fecha", "Hora", "Erd_CoolDownStepStatus"])
FileCsv.Write_Data_CSV(file_Erd_Erd_ExtendedTumbleStepStatus, ["Fecha", "Hora", "Erd_ExtendedTumbleStepStatus"])
FileCsv.Write_Data_CSV(file_Erd_Erd_SteamStepStatus, ["Fecha", "Hora", "Erd_SteamStepStatus"])
FileCsv.Write_Data_CSV(file_Erd_Erd_EndOfCycleReason, ["Fecha", "Hora", "Erd_EndOfCycleReason"])

######################################################## ERD LIST #########################################################################
ERD_List = ["F01B", "200A", "F11F", "F15E", "F301", "F302", "F705", "F30C", "F30D", "F0AE", "F06D", "F0AC", "F303", "F322", "F11A", "F119", "F07F", "F080", "F073", "F311",
            "F075", "003A", "003B", "FF01", "204D", "F0B2", "F0AF", "F0AB", "F0AD", "F0A9", "F0A8", "F1A5", "F1A6", "F816", "F0BC", "F0A7", "F0C7", "F0BA", "FD98",
            "F1A0", "F1A1", "F0ED", "F116", "F137", "F0AA"]

def main():
    while True:
        Tiempo_Inicio = time.time()
        SetBoard()
        ERDS = []
        for ERD in ERD_List:
            Dato = ReadButton("C0", ERD)
            ERDS.append(Dato)
        diaS = datetime.now().strftime("%d-%m-%Y")
        TimeS = datetime.now().strftime("%H:%M:%S") 
        Erd_CurrentSystemState, Erd_CycleSelected, Erd_EStarSensorDryRequested, Erd_RamCycleHistoryRecord, Erd_CurrentInletTemperature,Erd_CurrentOutletTemperature, Erd_OverTemperatureMaxInletTemperature, Erd_HeaterRelay1, Erd_HeaterRelay2, Erd_MaxTemperatureSlope, Erd_HeatControlParametric, Erd_MinimumFilteredVoltageFromMc, Erd_FilteredMoistureSensor, Erd_SmoothMoistureReading, Erd_CalculatedCurvature, Erd_CurvatureOccurredCount, Erd_TrimmerInhibitRelay1, Erd_TrimmerInhibitRelay2, Erd_TrimmerBothCoilInhibitRequest, Erd_DrumMotorState, Erd_FallbackHeatControlMethodStatus, Erd_ApplicationVersion, Erd_ParametricVersion, Erd_Personality, Erd_DrynessOption, Erd_VentRestriction, Erd_LoadSizeByAggregation, Erd_LoadSizeByContact, Erd_LoadSizeByTemperature, Erd_TargetMoistureVoltageHasBeenReached, Erd_TargetMoistureVoltage, Erd_TotalDryTimeCalculatorTimeMultiplierX100, Erd_TotalDryTimeCalculatorTimeAdderSeconds, Erd_SensorDryTemperatureMultiplierx100, Erd_TimeToReachTargetVoltageSeconds, Erd_SensingCycleTotalDryingTimeSeconds,Erd_DrumGroundWatchdogResult, Erd_ClothDampnessCheckResult, Erd_Fault_DrumGroundWatchdogDetection, Erd_SteamValveCycleCountRam, Erd_SteamValveOnTimeDurationInSecondsRam, Erd_CoolDownStepStatus, Erd_ExtendedTumbleStepStatus, Erd_SteamStepStatus, Erd_EndOfCycleReason = ERDS                                                             
    
        FileCsv.Write_Data_CSV(file_Erd_CurrentSystemState, [diaS] + [TimeS] + [definitions.CurrentSystemState(Erd_CurrentSystemState)])
        FileCsv.Write_Data_CSV(file_Erd_Erd_CycleSelected, [diaS] + [TimeS] + [definitions.CycleSelected(Erd_CycleSelected)])
        FileCsv.Write_Data_CSV(file_Erd_Erd_EStarSensorDryRequested, [diaS] + [TimeS] + [definitions.EStarSensorDryRequested(Erd_EStarSensorDryRequested)])
        FileCsv.Write_Data_CSV(file_Erd_Erd_RamCycleHistoryRecord, [diaS] + [TimeS] + definitions.RamCycleHistoryRecord(Erd_RamCycleHistoryRecord))
        FileCsv.Write_Data_CSV(file_Erd_Erd_CurrentInletTemperature, [diaS] + [TimeS] + [definitions.CurrentInletTemperature(Erd_CurrentInletTemperature)])
        FileCsv.Write_Data_CSV(file_Erd_Erd_CurrentOutletTemperature, [diaS] + [TimeS] + [definitions.CurrentOutletTemperature(Erd_CurrentOutletTemperature)])
        FileCsv.Write_Data_CSV(file_Erd_Erd_OverTemperatureMaxInletTemperature, [diaS] + [TimeS] + [definitions.OverTemperatureMaxInletTemperature(Erd_OverTemperatureMaxInletTemperature)])
        FileCsv.Write_Data_CSV(file_Erd_Erd_HeaterRelay1, [diaS] + [TimeS] + [definitions.HeaterRelay1(Erd_HeaterRelay1)])
        FileCsv.Write_Data_CSV(file_Erd_Erd_HeaterRelay2, [diaS] + [TimeS] + [definitions.HeaterRelay2(Erd_HeaterRelay2)])
        FileCsv.Write_Data_CSV(file_Erd_Erd_MaxTemperatureSlope, [diaS] + [TimeS] + [definitions.MaxTemperatureSlope(Erd_MaxTemperatureSlope)])
        FileCsv.Write_Data_CSV(file_Erd_Erd_HeatControlParametric, [diaS] + [TimeS] + definitions.HeatControlParametric(Erd_HeatControlParametric))
        FileCsv.Write_Data_CSV(file_Erd_Erd_MinimumFilteredVoltageFromMc, [diaS] + [TimeS] + [definitions.MinimumFilteredVoltageFromMC(Erd_MinimumFilteredVoltageFromMc)])
        FileCsv.Write_Data_CSV(file_Erd_Erd_FilteredMoistureSensor, [diaS] + [TimeS] + [definitions.FilteredMoistureSensor(Erd_FilteredMoistureSensor)])
        FileCsv.Write_Data_CSV(file_Erd_Erd_SmoothMoistureReading, [diaS] + [TimeS] + [definitions.SmoothMoistureReading(Erd_SmoothMoistureReading)])
        FileCsv.Write_Data_CSV(file_Erd_Erd_CalculatedCurvature, [diaS] + [TimeS] + [definitions.CalculatedCurvature(Erd_CalculatedCurvature)])
        FileCsv.Write_Data_CSV(file_Erd_Erd_CurvatureOccurredCount, [diaS] + [TimeS] + [definitions.CurvatureOccurredCount(Erd_CurvatureOccurredCount)])
        FileCsv.Write_Data_CSV(file_Erd_Erd_TrimmerInhibitRelay1, [diaS] + [TimeS] + [definitions.TrimmerInhibitRelay1(Erd_TrimmerInhibitRelay1)])
        FileCsv.Write_Data_CSV(file_Erd_Erd_TrimmerInhibitRelay2, [diaS] + [TimeS] + [definitions.TrimmerInhibitRelay2(Erd_TrimmerInhibitRelay2)])
        FileCsv.Write_Data_CSV(file_Erd_Erd_TrimmerBothCoilInhibitRequest, [diaS] + [TimeS] + [definitions.TrimmerBothCoilInhibitRequest(Erd_TrimmerBothCoilInhibitRequest)])
        FileCsv.Write_Data_CSV(file_Erd_Erd_DrumMotorState, [diaS] + [TimeS] + [definitions.DrumMotorState(Erd_DrumMotorState)])
        FileCsv.Write_Data_CSV(file_Erd_Erd_FallbackHeatControlMethodStatus, [diaS] + [TimeS] + [definitions.FallbackHeatControlMethodStatus(Erd_FallbackHeatControlMethodStatus)])
        FileCsv.Write_Data_CSV(file_Erd_Erd_ApplicationVersion, [diaS] + [TimeS] + [definitions.ApplicationVersion(Erd_ApplicationVersion)])
        FileCsv.Write_Data_CSV(file_Erd_Erd_ParametricVersion, [diaS] + [TimeS] + [definitions.ParametricVersion(Erd_ParametricVersion)])
        FileCsv.Write_Data_CSV(file_Erd_Erd_Personality, [diaS] + [TimeS] + [definitions.Personality(Erd_Personality)])
        FileCsv.Write_Data_CSV(file_Erd_Erd_DrynessOption, [diaS] + [TimeS] + [definitions.DrynessOption(Erd_DrynessOption)])
        FileCsv.Write_Data_CSV(file_Erd_Erd_VentRestriction, [diaS] + [TimeS] + [definitions.VentRestriction(Erd_VentRestriction)])
        FileCsv.Write_Data_CSV(file_Erd_Erd_LoadSizeByAggregation, [diaS] + [TimeS] + [definitions.LoadSizeByAggregation(Erd_LoadSizeByAggregation)])
        FileCsv.Write_Data_CSV(file_Erd_Erd_LoadSizeByContact, [diaS] + [TimeS] + [definitions.LoadSizeByContact(Erd_LoadSizeByContact)])
        FileCsv.Write_Data_CSV(file_Erd_Erd_LoadSizeByTemperature, [diaS] + [TimeS] + [definitions.LoadSizeByTemperature(Erd_LoadSizeByTemperature)]) 
        FileCsv.Write_Data_CSV(file_Erd_Erd_TargetMoistureVoltageHasBeenReached, [diaS] + [TimeS] + [definitions.TargetMoistureVoltageHasBeenReached(Erd_TargetMoistureVoltageHasBeenReached)])
        FileCsv.Write_Data_CSV(file_Erd_Erd_TargetMoistureVoltage, [diaS] + [TimeS] + [definitions.TargetMoistureVoltage(Erd_TargetMoistureVoltage)])
        FileCsv.Write_Data_CSV(file_Erd_Erd_TotalDryTimeCalculatorTimeMultiplierX100, [diaS] + [TimeS] + [definitions.TotalDryTimeCalculatorTimeMultiplierX100(Erd_TotalDryTimeCalculatorTimeMultiplierX100)])
        FileCsv.Write_Data_CSV(file_Erd_Erd_TotalDryTimeCalculatorTimeAdderSeconds, [diaS] + [TimeS] + [definitions.TotalDryTimeCalculatorTimeAdderSeconds(Erd_TotalDryTimeCalculatorTimeAdderSeconds)])
        FileCsv.Write_Data_CSV(file_Erd_Erd_SensorDryTemperatureMultiplierx100, [diaS] + [TimeS] + [definitions.SensorDryTemperatureMultiplierx100(Erd_SensorDryTemperatureMultiplierx100)])
        FileCsv.Write_Data_CSV(file_Erd_Erd_TimeToReachTargetVoltageSeconds, [diaS] + [TimeS] + definitions.TimeToReachTargetVoltageSeconds(Erd_TimeToReachTargetVoltageSeconds))
        FileCsv.Write_Data_CSV(file_Erd_Erd_SensingCycleTotalDryingTimeSeconds, [diaS] + [TimeS] + [definitions.SensingCycleTotalDryingTimeSeconds(Erd_SensingCycleTotalDryingTimeSeconds)])
        FileCsv.Write_Data_CSV(file_Erd_Erd_DrumGroundWatchdogResult, [diaS] + [TimeS] + [definitions.DrumGroundWatchdogResult(Erd_DrumGroundWatchdogResult)])
        FileCsv.Write_Data_CSV(file_Erd_Erd_ClothDampnessCheckResult, [diaS] + [TimeS] + [definitions.ClothDampnessCheckResult(Erd_ClothDampnessCheckResult)])
        FileCsv.Write_Data_CSV(file_Erd_Erd_Fault_DrumGroundWatchdogDetection, [diaS] + [TimeS] + [definitions.Fault_DrumGroundWatchdogDetection(Erd_Fault_DrumGroundWatchdogDetection)])
        FileCsv.Write_Data_CSV(file_Erd_Erd_SteamValveCycleCountRam, [diaS] + [TimeS] + [definitions.SteamValveCycleCountRam(Erd_SteamValveCycleCountRam)])
        FileCsv.Write_Data_CSV(file_Erd_Erd_SteamValveOnTimeDurationInSecondsRam, [diaS] + [TimeS] + [definitions.SteamValveOnTimeDurationInSecondsRam(Erd_SteamValveOnTimeDurationInSecondsRam)])
        FileCsv.Write_Data_CSV(file_Erd_Erd_CoolDownStepStatus, [diaS] + [TimeS] + [definitions.CoolDownStepStatus(Erd_CoolDownStepStatus)])
        FileCsv.Write_Data_CSV(file_Erd_Erd_ExtendedTumbleStepStatus, [diaS] + [TimeS] + [definitions.ExtendedTumbleStepStatus(Erd_ExtendedTumbleStepStatus)])
        FileCsv.Write_Data_CSV(file_Erd_Erd_SteamStepStatus, [diaS] + [TimeS] + [definitions.SteamStepStatus(Erd_SteamStepStatus)])
        FileCsv.Write_Data_CSV(file_Erd_Erd_EndOfCycleReason, [diaS] + [TimeS] + [definitions.EndOfCycleReason(Erd_EndOfCycleReason)])

        Tiempo_Restante = 1 - (time.time() - Tiempo_Inicio) 
        if Tiempo_Inicio > 0:
            time.sleep(Tiempo_Restante)
            
if __name__ == "__main__":
    main()