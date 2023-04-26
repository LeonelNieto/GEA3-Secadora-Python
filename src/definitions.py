def CurrentSystemState(ERD):
    Erd_CurrentSystemState = int(ERD, 16)
    return {                                           
        0: "SystemState_StartUp",
        1: "SystemState_Idle",
        2: "SystemState_Standby",
        3: "SystemState_Run",
        4: "SystemState_Pause",
        5: "SystemState_EndOfCycle",
        6: "SystemState_DelayRun",
        7: "SystemState_DelayPause",
        8: "SystemState_Commissioning",
        9: "SystemState_Max"                               
    }.get(Erd_CurrentSystemState)

def CycleSelected(ERD):
    Erd_CycleSelected = int(ERD, 16)
    return {
        0:  "CycleSelected_NotDefined",
        1:  "CycleSelected_BasketClean",
        2:  "CycleSelected_DrainSpin",
        3:  "CycleSelected_QuickRinse",
        4:  "CycleSelected_BulkyItems",
        5:  "CycleSelected_Sanitize",
        6:  "CycleSelected_TowelsSheets",
        7:  "CycleSelected_WasherSteamRefresh",
        8:  "CycleSelected_NormalOrMixedLoad",
        9:  "CycleSelected_Whites",
        10: "CycleSelected_DarkColors",
        11: "CycleSelected_Jeans",
        12: "CycleSelected_HandWash",
        13: "CycleSelected_Delicates",
        14: "CycleSelected_SpeedWash",
        15: "CycleSelected_HeavyDuty",
        16: "CycleSelected_Allergen",
        17: "CycleSelected_PowerClean",
        18: "CycleSelected_RinseSpin",
        19: "CycleSelected_SingleItem",
        20: "CycleSelected_Colors",
        21: "CycleSelected_ColdWash",
        22: "CycleSelected_WaterOnDemand",
        23: "CycleSelected_TubClean",
        24: "CycleSelected_CasualsWithSteam",
        25: "CycleSelected_StainWashWithSteam",
        26: "CycleSelected_DeepClean",
        128: "CycleSelected_Cottons",
        129: "CycleSelected_EasyCare",
        130: "CycleSelected_ActiveWear",
        131: "CycleSelected_TimedDry",
        132: "CycleSelected_DeWrinkle",
        133: "CycleSelected_Airfluff",
        134: "CycleSelected_SteamRefresh",
        135: "CycleSelected_SteamDewrinkle",
        136: "CycleSelected_SpeedDry",
        137: "CycleSelected_Mixed",
        138: "CycleSelected_QuickDry",
        139: "CycleSelected_Casuals",
        140: "CycleSelected_WarmUp",
        141: "CycleSelected_EnergySaver",
        142: "CycleSelected_Antibacterial",
        143: "CycleSelected_RackDry",
        144: "CycleSelected_BabyCare",
        145: "CycleSelected_AutoDry",
        146: "CycleSelected_TimedDryWithNoHeat",
        147: "CycleSelected_PermPress",
        148: "CycleSelected_WasherLink"
    }.get(Erd_CycleSelected)

def EStarSensorDryRequested(ERD):
    Erd_EStarSensorDryRequested = int(ERD, 16)
    return {
        0: "EStarOption_Disabled",
        1: "EStarOption_Enabled",
        2: "EStarOption_Max",
        255: "EStarOption_DontCare"
    }.get(Erd_EStarSensorDryRequested)

def RamCycleHistoryRecord(ERD):
    ERD_LIST = []
    Erd_RamCycleHistoryRecord_drynessOptionAtStart = int(ERD[100:102], 16)
    Erd_RamCycleHistoryRecord_drynessOptionAtStart = {
        0: "DrynessOption_Disabled",
        1: "DrynessOption_Minimum",
        2: "DrynessOption_LessDry",
        3: "DrynessOption_Dry",
        4: "DrynessOption_MoreDry",
        5: "DrynessOption_ExtraDry",
        6: "DrynessOption_Max",
        255: "DrynessOption_DontCare"
    }.get(Erd_RamCycleHistoryRecord_drynessOptionAtStart)
    ERD_LIST.append(Erd_RamCycleHistoryRecord_drynessOptionAtStart)

    Erd_RamCycleHistoryRecord_drynessOptionAtEnd = int(ERD[102:104], 16)
    Erd_RamCycleHistoryRecord_drynessOptionAtEnd = {
        0: "DrynessOption_Disabled",
        1: "DrynessOption_Minimum",
        2: "DrynessOption_LessDry",
        3: "DrynessOption_Dry",
        4: "DrynessOption_MoreDry",
        5: "DrynessOption_ExtraDry",
        6: "DrynessOption_Max",
        255: "DrynessOption_DontCare"
    }.get(Erd_RamCycleHistoryRecord_drynessOptionAtEnd)
    ERD_LIST.append(Erd_RamCycleHistoryRecord_drynessOptionAtEnd)

    Erd_RamCycleHistoryRecord_temperatureOptionAtStart = int(ERD[104:106], 16)
    Erd_RamCycleHistoryRecord_temperatureOptionAtStart = {
        0: "TemperatureOption_Disabled",
        1: "TemperatureOption_NoHeat",
        2: "TemperatureOption_ExtraLow",
        3: "TemperatureOption_Low",
        4: "TemperatureOption_Medium",
        5: "TemperatureOption_High",
        6: "TemperatureOption_Max",
        255: "TemperatureOption_DontCare"   
    }.get(Erd_RamCycleHistoryRecord_temperatureOptionAtStart)
    ERD_LIST.append(Erd_RamCycleHistoryRecord_temperatureOptionAtStart)

    Erd_RamCycleHistoryRecord_temperatureOptionAtEnd = int(ERD[106:108], 16)
    Erd_RamCycleHistoryRecord_temperatureOptionAtEnd = {
        0: "TemperatureOption_Disabled",
        1: "TemperatureOption_NoHeat",
        2: "TemperatureOption_ExtraLow",
        3: "TemperatureOption_Low",
        4: "TemperatureOption_Medium",
        5: "TemperatureOption_High",
        6: "TemperatureOption_Max",
        255: "TemperatureOption_DontCare"       
    }.get(Erd_RamCycleHistoryRecord_temperatureOptionAtEnd)
    ERD_LIST.append(Erd_RamCycleHistoryRecord_temperatureOptionAtEnd)
    return ERD_LIST

def CurrentInletTemperature(ERD):
    return str(int(ERD, 16))

def CurrentOutletTemperature(ERD):
    return str(int(ERD, 16))

def OverTemperatureMaxInletTemperature(ERD):
    return str(int(ERD, 16))

def HeaterRelay1(ERD):
    return str(int(ERD, 16))

def HeaterRelay2(ERD):
    return str(int(ERD, 16))

def MaxTemperatureSlope(ERD):
    return str(int(ERD, 16))

def HeatControlParametric(ERD):
    ERD_LIST = []
    Erd_HeatControlParametricheaterData0_inletTemperatureLowerLimit = str(int(ERD[0:4], 16))
    ERD_LIST.append(Erd_HeatControlParametricheaterData0_inletTemperatureLowerLimit)
    Erd_HeatControlParametric_heaterData0_inletTemperatureUpperLimit = str(int(ERD[4:8], 16))
    ERD_LIST.append(Erd_HeatControlParametric_heaterData0_inletTemperatureUpperLimit)
    Erd_HeatControlParametric_heaterData0_outletTemperatureLowerLimit = str(int(ERD[8:12], 16))
    ERD_LIST.append(Erd_HeatControlParametric_heaterData0_outletTemperatureLowerLimit)
    Erd_HeatControlParametric_heaterData0_outletTemperatureUpperLimit = str(int(ERD[12:16], 16))
    ERD_LIST.append(Erd_HeatControlParametric_heaterData0_outletTemperatureUpperLimit)
    Erd_HeatControlParametric_heaterData0_onTimeSeconds = str(int(ERD[16:18], 16))
    ERD_LIST.append(Erd_HeatControlParametric_heaterData0_onTimeSeconds)
    Erd_HeatControlParametric_heaterData0_offTimeSeconds = str(int(ERD[18:20]))
    ERD_LIST.append(Erd_HeatControlParametric_heaterData0_offTimeSeconds)
    Erd_HeatControlParametric_heaterData0_relayIsEnabled = int(ERD[20:22], 16)
    Erd_HeatControlParametric_heaterData0_relayIsEnabled = {
        0: "False",
        1: "True"
    }.get(Erd_HeatControlParametric_heaterData0_relayIsEnabled)
    ERD_LIST.append(Erd_HeatControlParametric_heaterData0_relayIsEnabled)
    Erd_HeatControlParametric_heaterData1_inletTemperatureLowerLimit = str(int(ERD[24:28], 16))
    ERD_LIST.append(Erd_HeatControlParametric_heaterData1_inletTemperatureLowerLimit)
    Erd_HeatControlParametric_heaterData1_inletTemperatureUpperLimit = str(int(ERD[28:32], 16))
    ERD_LIST.append(Erd_HeatControlParametric_heaterData1_inletTemperatureUpperLimit)
    Erd_HeatControlParametric_heaterData1_outletTemperatureLowerLimit = str(int(ERD[32:36], 16))
    ERD_LIST.append(Erd_HeatControlParametric_heaterData1_outletTemperatureLowerLimit)
    Erd_HeatControlParametric_heaterData1_outletTemperatureUpperLimit = str(int(ERD[36:40], 16))
    ERD_LIST.append(Erd_HeatControlParametric_heaterData1_outletTemperatureUpperLimit)
    Erd_HeatControlParametric_heaterData1_onTimeSeconds = str(int(ERD[40:42], 16))
    ERD_LIST.append(Erd_HeatControlParametric_heaterData1_onTimeSeconds)
    Erd_HeatControlParametric_heaterData1_offTimeSeconds = str(int(ERD[42:44], 16))
    ERD_LIST.append(Erd_HeatControlParametric_heaterData1_offTimeSeconds)
    Erd_HeatControlParametric_heaterData1_relayIsEnabled = int(ERD[44:46], 16)
    Erd_HeatControlParametric_heaterData1_relayIsEnabled = {
        0: "False",
        1: "True"
    }.get(Erd_HeatControlParametric_heaterData1_relayIsEnabled)
    ERD_LIST.append(Erd_HeatControlParametric_heaterData1_relayIsEnabled)
    return ERD_LIST

def MinimumFilteredVoltageFromMC(ERD):
    return str(int(ERD, 16))

def FilteredMoistureSensor(ERD):
    return str(int(ERD, 16))

def SmoothMoistureReading(ERD):
    return (str(int(ERD, 16)))

def CalculatedCurvature(ERD):
    return (str(int(ERD, 16)))

def CurvatureOccurredCount(ERD):
    return (str(int(ERD, 16)))  

def TrimmerInhibitRelay1(ERD): 
    Erd_TrimmerInhibitRelay1 = int(ERD, 16)
    return {
        0: "False",
        1: "True"
    }.get(Erd_TrimmerInhibitRelay1)

def TrimmerInhibitRelay2(ERD): 
    Erd_TrimmerInhibitRelay2 = int(ERD, 16)
    return {
        0: "False",
        1: "True"
    }.get(Erd_TrimmerInhibitRelay2)

def TrimmerBothCoilInhibitRequest(ERD):
    Erd_TrimmerBothCoilInhibitRequest = int(ERD, 16)
    return {
        0: "False",
        1: "True"
    }.get(Erd_TrimmerBothCoilInhibitRequest)

def DrumMotorState(ERD):
    Erd_DrumMotorState = int(ERD, 16)
    return {
        0: "DrumMotorState_Off",
        1: "DrumMotorState_Normal",
        2: "DrumMotorState_Reverse",
        3: "DrumMotorState_Max"       
    }.get(Erd_DrumMotorState)

def FallbackHeatControlMethodStatus(ERD):
    Erd_FallbackHeatControlMethodStatus = int(ERD, 16)
    return {
        0: "False",
        1: "True"
    }.get(Erd_FallbackHeatControlMethodStatus)  

def ApplicationVersion(ERD):
    Erd_ApplicationVersion_criticalMajor = str(int(ERD[0:2], 16))
    Erd_ApplicationVersion_criticalMinor = str(int(ERD[2:4], 16))
    Erd_ApplicationVersion_major = str(int(ERD[4:6], 16))
    Erd_ApplicationVersion_minor = str(int(ERD[6:8], 16))
    return Erd_ApplicationVersion_criticalMajor + "." + Erd_ApplicationVersion_criticalMinor + "." + Erd_ApplicationVersion_major + "." + Erd_ApplicationVersion_minor

def ParametricVersion(ERD):
    Erd_ParametricVersion_criticalMajor = str(int(ERD[0:2]))
    Erd_ParametricVersion_criticalMinor = str(int(ERD[2:4]))
    Erd_ParametricVersion_major = str(int(ERD[4:6]))
    Erd_ParametricVersion_minor = str(int(ERD[6:8]))
    return Erd_ParametricVersion_criticalMajor + "." + Erd_ParametricVersion_criticalMinor + "." + Erd_ParametricVersion_major + "." + Erd_ParametricVersion_minor

def Personality(ERD):
    return str(int(ERD, 16))

def DrynessOption(ERD):
    Erd_DrynessOption = int(ERD, 16)
    return {
        0: "DrynessOption_Disabled",
        1: "DrynessOption_Minimum",
        2: "DrynessOption_LessDry",
        3: "DrynessOption_Dry",
        4: "DrynessOption_MoreDry",
        5: "DrynessOption_ExtraDry",
        6: "DrynessOption_Max",
        255: "DrynessOption_DontCare"
    }.get(Erd_DrynessOption)

def VentRestriction(ERD):
    Erd_VentRestriction = int(ERD, 16)
    return {
        0: "VentRestriction_Unknown",
        1: "VentRestriction_Small",
        2: "VentRestriction_Large"
    }.get(Erd_VentRestriction) 

def LoadSizeByAggregation(ERD):
    Erd_LoadSizeByAggregation = int(ERD, 16)
    return {
        0: "LoadSize_Unknown",
        1: "LoadSize_Small",
        2: "LoadSize_Large"
    }.get(Erd_LoadSizeByAggregation)

def LoadSizeByContact(ERD):
    Erd_LoadSizeByContact = int(ERD, 16)
    return {
        0: "LoadSize_Unknown",
        1: "LoadSize_Small",
        2: "LoadSize_Large"
    }.get(Erd_LoadSizeByContact)

def LoadSizeByTemperature(ERD):
    Erd_LoadSizeByTemperature = int(ERD, 16)
    return {
        0: "LoadSize_Unknown",
        1: "LoadSize_Small",
        2: "LoadSize_Large"
    }.get(Erd_LoadSizeByTemperature)

def TargetMoistureVoltageHasBeenReached(ERD):
    Erd_TargetMoistureVoltageHasBeenReached = int(ERD, 16)
    Erd_TargetMoistureVoltageHasBeenReached = {
        0: "False",
        1: "True"
    }.get(Erd_TargetMoistureVoltageHasBeenReached)

def TargetMoistureVoltage(ERD):    
    return str(int(ERD, 16))

def TotalDryTimeCalculatorTimeMultiplierX100(ERD):
    return str(int(ERD, 16))

def TotalDryTimeCalculatorTimeAdderSeconds(ERD):
    return str(int(ERD, 16))

def SensorDryTemperatureMultiplierx100(ERD):
    ERD_LIST = []
    Erd_SensorDryTemperatureMultiplierx100_temperatureMultiplierEcoDry = str(int(ERD[0:4], 16))
    ERD_LIST.append(Erd_SensorDryTemperatureMultiplierx100_temperatureMultiplierEcoDry)
    Erd_SensorDryTemperatureMultiplierx100_temperatureMultiplierExtraLow = str(int(ERD[4:8], 16))
    ERD_LIST.append(Erd_SensorDryTemperatureMultiplierx100_temperatureMultiplierExtraLow)
    Erd_SensorDryTemperatureMultiplierx100_temperatureMultiplierLow = str(int(ERD[8:12], 16))
    ERD_LIST.append(Erd_SensorDryTemperatureMultiplierx100_temperatureMultiplierLow)
    Erd_SensorDryTemperatureMultiplierx100_temperatureMultiplierMedium = str(int(ERD[12:16], 16))
    ERD_LIST.append(Erd_SensorDryTemperatureMultiplierx100_temperatureMultiplierMedium)
    Erd_SensorDryTemperatureMultiplierx100_temperatureMultiplierHigh = str(int(ERD[16:20], 16))
    ERD_LIST.append(Erd_SensorDryTemperatureMultiplierx100_temperatureMultiplierHigh)
    return ERD_LIST
    
def TimeToReachTargetVoltageSeconds(ERD):
    return str(int(ERD, 16))

def SensingCycleTotalDryingTimeSeconds(ERD):
    return str(int(ERD, 16))

def DrumGroundWatchdogResult(ERD):
    Erd_DrumGroundWatchdogResult = int(ERD, 16)
    return {
        0: "DrumGroundWatchdogResult_Unknown",
        1: "DrumGroundWatchdogResult_NotExpired",
        2: "DrumGroundWatchdogResult_Expired"
    }.get(Erd_DrumGroundWatchdogResult)

def ClothDampnessCheckResult(ERD):
    Erd_ClothDampnessCheckResult = int(ERD, 16)
    return {
        0: "ClothDampnessCheckResult_Undefined",
        1: "ClothDampnessCheckResult_Disabled",
        2: "ClothDampnessCheckResult_Idle",
        3: "ClothDampnessCheckResult_WaitForFilteredVoltageReset",
        4: "ClothDampnessCheckResult_Sensing",
        5: "ClothDampnessCheckResult_Paused",
        6: "ClothDampnessCheckResult_PausedWhileWaitingForFilteredVoltageReset",
        7: "ClothDampnessCheckResult_TargetVoltageReached",
        8: "ClothDampnessCheckResult_TargetVoltageReachedByExpiredWatchdog"
    }.get(Erd_ClothDampnessCheckResult)

def Fault_DrumGroundWatchdogDetection(ERD):
    Erd_Fault_DrumGroundWatchdogDetection = int(ERD, 16)
    return {
        0: "False",
        1: "True"
    }.get(Erd_Fault_DrumGroundWatchdogDetection)

def SteamValveCycleCountRam(ERD):
    return str(int(ERD, 16))

def SteamValveOnTimeDurationInSecondsRam(ERD):
    return str(int(ERD, 16))

def CoolDownStepStatus(ERD):
    Erd_CoolDownStepStatus = int(ERD, 16)
    return {
        0: "CycleStepState_Unknown",
        1: "CycleStepState_Initialized",
        2: "CycleStepState_Selected",
        3: "CycleStepState_Deselected",
        4: "CycleStepState_Started",
        5: "CycleStepState_Stopped",
        6: "CycleStepState_Paused",
        7: "CycleStepState_Resumed",
        8: "CycleStepState_Completed",
        9: "CycleStepState_Max"
    }.get(Erd_CoolDownStepStatus)
   
def ExtendedTumbleStepStatus(ERD):
    Erd_ExtendedTumbleStepStatus = int(ERD, 16)
    return {
        0: "CycleStepState_Unknown",
        1: "CycleStepState_Initialized",
        2: "CycleStepState_Selected",
        3: "CycleStepState_Deselected",
        4: "CycleStepState_Started",
        5: "CycleStepState_Stopped",
        6: "CycleStepState_Paused",
        7: "CycleStepState_Resumed",
        8: "CycleStepState_Completed",
        9: "CycleStepState_Max"
    }.get(Erd_ExtendedTumbleStepStatus)
  
def SteamStepStatus(ERD):
    Erd_SteamStepStatus = int(ERD, 16)
    return {
        0: "CycleStepState_Unknown",
        1: "CycleStepState_Initialized",
        2: "CycleStepState_Selected",
        3: "CycleStepState_Deselected",
        4: "CycleStepState_Started",
        5: "CycleStepState_Stopped",
        6: "CycleStepState_Paused",
        7: "CycleStepState_Resumed",
        8: "CycleStepState_Completed",
        9: "CycleStepState_Max"
    }.get(Erd_SteamStepStatus)

def EndOfCycleReason(ERD):
    Erd_EndOfCycleReason = int(ERD, 16)
    return {
        0: "EndOfCycleReason_NA",
        1: "EndOfCycleReason_EmptyDrum",
        2: "EndOfCycleReason_DryLoad",
        3: "EndOfCycleReason_CoolDownPaused",
        4: "EndOfCycleReason_ExtendedTumblePaused",
        5: "EndOfCycleReason_KnobChange",
        6: "EndOfCycleReason_PowerButtonPressed",
        7: "EndOfCycleReason_CycleComplete",
        8: "EndOfCycleReason_EventSequenceCommunicationIssue",
        9: "EndOfCycleReason_CriticalFault",
        10: "EndOfCycleReason_RemoteStop",
        11: "EndOfCycleReason_ExtremeHeatDetected",
        255: "EndOfCycleReason_DontCare"
    }.get(Erd_EndOfCycleReason)


# print(ERDS_TO_WRITE([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0102010201020102010002030400010200010202010202010201020010201200010100010100001010102000010010101010", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0102034055010910", "010203405501091", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0 ,0, 0, 0]))