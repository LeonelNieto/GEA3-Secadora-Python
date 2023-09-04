def ERDS_TO_WRITE(ERDS):
    ERDS_LIST = []

    Erd_CurrentSystemState = int(ERDS[0], 16)
    Erd_CurrentSystemState = {                                           
        0: "StartUp",
        1: "Idle",
        2: "Standby",
        3: "Run",
        4: "Pause",
        5: "EndOfCycle",
        6: "DelayRun",
        7: "DelayPause",
        8: "Commissioning",
        9: "Max"                               
    }.get(Erd_CurrentSystemState)
    ERDS_LIST.append(Erd_CurrentSystemState)

    Erd_CycleSelected = int(ERDS[1], 16)
    Erd_CycleSelected = {
        0:  "NotDefined",
        1:  "BasketClean",
        2:  "DrainSpin",
        3:  "QuickRinse",
        4:  "BulkyItems",
        5:  "Sanitize",
        6:  "TowelsSheets",
        7:  "WasherSteamRefresh",
        8:  "NormalOrMixedLoad",
        9:  "Whites",
        10: "DarkColors",
        11: "Jeans",
        12: "HandWash",
        13: "Delicates",
        14: "SpeedWash",
        15: "HeavyDuty",
        16: "Allergen",
        17: "PowerClean",
        18: "RinseSpin",
        19: "SingleItem",
        20: "Colors",
        21: "ColdWash",
        22: "WaterOnDemand",
        23: "TubClean",
        24: "CasualsWithSteam",
        25: "StainWashWithSteam",
        26: "DeepClean",
        128: "Cottons",
        129: "EasyCare",
        130: "ActiveWear",
        131: "TimedDry",
        132: "DeWrinkle",
        133: "Airfluff",
        134: "SteamRefresh",
        135: "SteamDewrinkle",
        136: "SpeedDry",
        137: "Mixed",
        138: "QuickDry",
        139: "Casuals",
        140: "WarmUp",
        141: "EnergySaver",
        142: "Antibacterial",
        143: "RackDry",
        144: "BabyCare",
        145: "AutoDry",
        146: "TimedDryWithNoHeat",
        147: "PermPress",
        148: "WasherLink"
    }.get(Erd_CycleSelected)
    ERDS_LIST.append(Erd_CycleSelected)
    
    Erd_EStarSensorDryRequested = int(ERDS[2], 16)
    Erd_EStarSensorDryRequested = {
        0: "Disabled",
        1: "Enabled",
        2: "Max",
        255: "DontCare"
    }.get(Erd_EStarSensorDryRequested)
    ERDS_LIST.append(Erd_EStarSensorDryRequested)

    Erd_RamCycleHistoryRecord_drynessOptionAtStart = int(ERDS[3], 16)
    Erd_RamCycleHistoryRecord_drynessOptionAtStart = {
        0: "Disabled",
        1: "Minimum",
        2: "LessDry",
        3: "Dry",
        4: "MoreDry",
        5: "ExtraDry",
        6: "Max",
        255: "DontCare"
    }.get(Erd_RamCycleHistoryRecord_drynessOptionAtStart)
    ERDS_LIST.append(Erd_RamCycleHistoryRecord_drynessOptionAtStart)

    Erd_RamCycleHistoryRecord_drynessOptionAtEnd = int(ERDS[4], 16)
    Erd_RamCycleHistoryRecord_drynessOptionAtEnd = {
        0: "Disabled",
        1: "Minimum",
        2: "LessDry",
        3: "Dry",
        4: "MoreDry",
        5: "ExtraDry",
        6: "Max",
        255: "DontCare"
    }.get(Erd_RamCycleHistoryRecord_drynessOptionAtEnd)
    ERDS_LIST.append(Erd_RamCycleHistoryRecord_drynessOptionAtEnd)

    Erd_RamCycleHistoryRecord_temperatureOptionAtStart = int(ERDS[5], 16)
    Erd_RamCycleHistoryRecord_temperatureOptionAtStart = {
        0: "Disabled",
        1: "NoHeat",
        2: "ExtraLow",
        3: "Low",
        4: "Medium",
        5: "High",
        6: "Max",
        255: "DontCare"   
    }.get(Erd_RamCycleHistoryRecord_temperatureOptionAtStart)
    ERDS_LIST.append(Erd_RamCycleHistoryRecord_temperatureOptionAtStart)

    Erd_RamCycleHistoryRecord_temperatureOptionAtEnd = int(ERDS[6], 16)
    Erd_RamCycleHistoryRecord_temperatureOptionAtEnd = {
        0: "Disabled",
        1: "NoHeat",
        2: "ExtraLow",
        3: "Low",
        4: "Medium",
        5: "High",
        6: "Max",
        255: "DontCare"       
    }.get(Erd_RamCycleHistoryRecord_temperatureOptionAtEnd)
    ERDS_LIST.append(Erd_RamCycleHistoryRecord_temperatureOptionAtEnd)

    Erd_CurrentInletTemperature = int(ERDS[7], 16)
    ERDS_LIST.append(str(Erd_CurrentInletTemperature))

    Erd_CurrentOutletTemperature = int(ERDS[8], 16)
    ERDS_LIST.append(str(Erd_CurrentOutletTemperature))

    Erd_OverTemperatureMaxInletTemperature = int(ERDS[9], 16)
    ERDS_LIST.append(str(Erd_OverTemperatureMaxInletTemperature))

    Erd_HeaterRelay1 = int(ERDS[10], 16)
    ERDS_LIST.append(str(Erd_HeaterRelay1))
    
    Erd_HeaterRelay2 = int(ERDS[11], 16)
    ERDS_LIST.append(str(Erd_HeaterRelay2))

    Erd_MaxTemperatureSlope = int(ERDS[12], 16)
    ERDS_LIST.append(str(Erd_MaxTemperatureSlope))

    Erd_MinimumFilteredVoltageFromMc = int(ERDS[13], 16)
    ERDS_LIST.append(str(Erd_MinimumFilteredVoltageFromMc))

    Erd_FilteredMoistureSensor = int(ERDS[14], 16)
    ERDS_LIST.append(str(Erd_FilteredMoistureSensor))
    
    Erd_SmoothMoistureReading = int(ERDS[15], 16)
    ERDS_LIST.append(str(Erd_SmoothMoistureReading))

    Erd_CalculatedCurvature = int(ERDS[16], 16)
    ERDS_LIST.append(str(Erd_CalculatedCurvature))

    Erd_CurvatureOccurredCount = int(ERDS[17], 16)
    ERDS_LIST.append(str(Erd_CurvatureOccurredCount))    

    Erd_TrimmerInhibitRelay1 = int(ERDS[18], 16)
    Erd_TrimmerInhibitRelay1 = {
        0: "False",
        1: "True"
    }.get(Erd_TrimmerInhibitRelay1)
    ERDS_LIST.append(Erd_TrimmerInhibitRelay1)

    Erd_TrimmerInhibitRelay2 = int(ERDS[19], 16)
    Erd_TrimmerInhibitRelay2 = {
        0: "False",
        1: "True"
    }.get(Erd_TrimmerInhibitRelay2)
    ERDS_LIST.append(Erd_TrimmerInhibitRelay2)

    Erd_TrimmerBothCoilInhibitRequest = int(ERDS[20], 16)
    Erd_TrimmerBothCoilInhibitRequest = {
        0: "False",
        1: "True"
    }.get(Erd_TrimmerBothCoilInhibitRequest)
    ERDS_LIST.append(Erd_TrimmerBothCoilInhibitRequest)

    Erd_DrumMotorState = int(ERDS[21], 16)
    Erd_DrumMotorState = {
        0: "Off",
        1: "Normal",
        2: "Reverse",
        3: "Max"       
    }.get(Erd_DrumMotorState)
    ERDS_LIST.append(Erd_DrumMotorState)

    Erd_FallbackHeatControlMethodStatus = int(ERDS[22], 16)
    Erd_FallbackHeatControlMethodStatus = {
        0: "False",
        1: "True"
    }.get(Erd_FallbackHeatControlMethodStatus)
    ERDS_LIST.append(Erd_FallbackHeatControlMethodStatus)    

    Erd_ApplicationVersion = ERDS[23]
    Erd_ApplicationVersion_criticalMajor = str(int(Erd_ApplicationVersion[0:2], 16))
    Erd_ApplicationVersion_criticalMinor = str(int(Erd_ApplicationVersion[2:4], 16))
    Erd_ApplicationVersion_major = str(int(Erd_ApplicationVersion[4:6], 16))
    Erd_ApplicationVersion_minor = str(int(Erd_ApplicationVersion[6:8], 16))
    ERDS_LIST.append(Erd_ApplicationVersion_criticalMajor + "." + Erd_ApplicationVersion_criticalMinor + "." + Erd_ApplicationVersion_major + "." + Erd_ApplicationVersion_minor)

    Erd_ParametricVersion = ERDS[24]
    Erd_ParametricVersion_criticalMajor = str(int(Erd_ParametricVersion[0:2], 16))
    Erd_ParametricVersion_criticalMinor = str(int(Erd_ParametricVersion[2:4], 16))
    Erd_ParametricVersion_major = str(int(Erd_ParametricVersion[4:6], 16))
    Erd_ParametricVersion_minor = str(int(Erd_ParametricVersion[6:8], 16))
    ERDS_LIST.append(Erd_ParametricVersion_criticalMajor + "." + Erd_ParametricVersion_criticalMinor + "." + Erd_ParametricVersion_major + "." + Erd_ParametricVersion_minor)

    Erd_Personality = int(ERDS[25], 16)
    ERDS_LIST.append(str(Erd_Personality))

    Erd_DrynessOption = int(ERDS[26], 16)
    Erd_DrynessOption = {
        0: "Disabled",
        1: "Minimum",
        2: "LessDry",
        3: "Dry",
        4: "MoreDry",
        5: "ExtraDry",
        6: "Max",
        255: "DontCare"
    }.get(Erd_DrynessOption)
    ERDS_LIST.append(Erd_DrynessOption)

    Erd_VentRestriction = int(ERDS[27], 16)
    Erd_VentRestriction = {
        0: "Unknown",
        1: "Small",
        2: "Large"
    }.get(Erd_VentRestriction)
    ERDS_LIST.append(Erd_VentRestriction)    

    Erd_LoadSizeByAggregation = int(ERDS[28], 16)
    Erd_LoadSizeByAggregation = {
        0: "Unknown",
        1: "Small",
        2: "Large"
    }.get(Erd_LoadSizeByAggregation)
    ERDS_LIST.append(Erd_LoadSizeByAggregation) 

    Erd_LoadSizeByContact = int(ERDS[29], 16)
    Erd_LoadSizeByContact = {
        0: "Unknown",
        1: "Small",
        2: "Large"
    }.get(Erd_LoadSizeByContact)
    ERDS_LIST.append(Erd_LoadSizeByContact) 

    Erd_LoadSizeByTemperature = int(ERDS[30], 16)
    Erd_LoadSizeByTemperature = {
        0: "Unknown",
        1: "Small",
        2: "Large"
    }.get(Erd_LoadSizeByTemperature)
    ERDS_LIST.append(Erd_LoadSizeByTemperature) 

    Erd_TargetMoistureVoltageHasBeenReached = int(ERDS[31], 16)
    Erd_TargetMoistureVoltageHasBeenReached = {
        0: "False",
        1: "True"
    }.get(Erd_TargetMoistureVoltageHasBeenReached)
    ERDS_LIST.append(Erd_TargetMoistureVoltageHasBeenReached)
    
    Erd_TargetMoistureVoltage = int(ERDS[32], 16)
    ERDS_LIST.append(str(Erd_TargetMoistureVoltage))
    
    Erd_TotalDryTimeCalculatorTimeMultiplierX100 = int(ERDS[33], 16)
    ERDS_LIST.append(str(Erd_TotalDryTimeCalculatorTimeMultiplierX100))

    Erd_TotalDryTimeCalculatorTimeAdderSeconds = int(ERDS[34], 16)
    ERDS_LIST.append(str(Erd_TotalDryTimeCalculatorTimeAdderSeconds))
        
    Erd_TimeToReachTargetVoltageSeconds = int(ERDS[35], 16)
    ERDS_LIST.append(str(Erd_TimeToReachTargetVoltageSeconds))

    Erd_SensingCycleTotalDryingTimeSeconds = int(ERDS[36], 16)
    ERDS_LIST.append(str(Erd_SensingCycleTotalDryingTimeSeconds))

    Erd_DrumGroundWatchdogResult = int(ERDS[37], 16)
    Erd_DrumGroundWatchdogResult = {
        0: "Unknown",
        1: "NotExpired",
        2: "Expired"
    }.get(Erd_DrumGroundWatchdogResult)
    ERDS_LIST.append(Erd_DrumGroundWatchdogResult)

    Erd_ClothDampnessCheckResult = int(ERDS[38], 16)
    Erd_ClothDampnessCheckResult = {
        0: "Undefined",
        1: "Disabled",
        2: "Idle",
        3: "WaitForFilteredVoltageReset",
        4: "Sensing",
        5: "Paused",
        6: "PausedWhileWaitingForFilteredVoltageReset",
        7: "TargetVoltageReached",
        8: "TargetVoltageReachedByExpiredWatchdog"
    }.get(Erd_ClothDampnessCheckResult)
    ERDS_LIST.append(Erd_ClothDampnessCheckResult)

    Erd_Fault_DrumGroundWatchdogDetection = int(ERDS[39], 16)
    Erd_Fault_DrumGroundWatchdogDetection = {
        0: "False",
        1: "True"
    }.get(Erd_Fault_DrumGroundWatchdogDetection)
    ERDS_LIST.append(Erd_Fault_DrumGroundWatchdogDetection)

    Erd_SteamValveCycleCountRam = int(ERDS[40], 16)
    ERDS_LIST.append(str(Erd_SteamValveCycleCountRam))

    Erd_SteamValveOnTimeDurationInSecondsRam = int(ERDS[41], 16)
    ERDS_LIST.append(str(Erd_SteamValveOnTimeDurationInSecondsRam))   

    Erd_CoolDownStepStatus = int(ERDS[42], 16)
    Erd_CoolDownStepStatus = {
        0: "Unknown",
        1: "Initialized",
        2: "Selected",
        3: "Deselected",
        4: "Started",
        5: "Stopped",
        6: "Paused",
        7: "Resumed",
        8: "Completed",
        9: "Max"
    }.get(Erd_CoolDownStepStatus)
    ERDS_LIST.append(Erd_CoolDownStepStatus)    

    Erd_ExtendedTumbleStepStatus = int(ERDS[43], 16)
    Erd_ExtendedTumbleStepStatus = {
        0: "Unknown",
        1: "Initialized",
        2: "Selected",
        3: "Deselected",
        4: "Started",
        5: "Stopped",
        6: "Paused",
        7: "Resumed",
        8: "Completed",
        9: "Max"
    }.get(Erd_ExtendedTumbleStepStatus)
    ERDS_LIST.append(Erd_ExtendedTumbleStepStatus)    

    Erd_SteamStepStatus = int(ERDS[44], 16)
    Erd_SteamStepStatus = {
        0: "Unknown",
        1: "Initialized",
        2: "Selected",
        3: "Deselected",
        4: "Started",
        5: "Stopped",
        6: "Paused",
        7: "Resumed",
        8: "Completed",
        9: "Max"
    }.get(Erd_SteamStepStatus)
    ERDS_LIST.append(Erd_SteamStepStatus) 

    Erd_EndOfCycleReason = int(ERDS[45], 16)
    Erd_EndOfCycleReason = {
        0: "NA",
        1: "EmptyDrum",
        2: "DryLoad",
        3: "CoolDownPaused",
        4: "ExtendedTumblePaused",
        5: "KnobChange",
        6: "PowerButtonPressed",
        7: "CycleComplete",
        8: "EventSequenceCommunicationIssue",
        9: "CriticalFault",
        10: "RemoteStop",
        11: "ExtremeHeatDetected",
        255: "DontCare"
    }.get(Erd_EndOfCycleReason)
    ERDS_LIST.append(Erd_EndOfCycleReason)
    
    Erd_ModelNumber = str(bytes.fromhex(ERDS[46]).decode('utf-8').replace('\x00', ''))
    ERDS_LIST.append(Erd_ModelNumber)
    
    Erd_SerialNumber = str(bytes.fromhex(ERDS[47]).decode('utf-8').replace('\x00', ''))
    ERDS_LIST.append(Erd_SerialNumber)
    
    Erd_AppliancePersonality = int(ERDS[48], 16)
    ERDS_LIST.append(str(Erd_AppliancePersonality))

    Erd_MachineStatus = int(ERDS[49], 16)
    Erd_MachineStatus = {
        0: "MachineStatus_Idle",
        1: "MachineStatus_Standby",
        2: "MachineStatus_Run",
        3: "MachineStatus_Pause",
        4: "MachineStatus_EndOfCycle",
        5: "MachineStatus_DSMDelayRun",
        6: "MachineStatus_DelayRun",
        7: "MachineStatus_DelayPause",
        8: "MachineStatus_DrainTimeOut",
        9: "MachineStatus_Commissioning",
        128: "MachineStatus_CleanSpeak"
    }.get(Erd_MachineStatus)
    ERDS_LIST.append(Erd_MachineStatus)
    
    Erd_MachineSubCycle = int(ERDS[50], 16)
    Erd_MachineSubCycle = {
        0: "MachineSubCycle_NotApplicable",
        128: "MachineSubCycle_Drying",
        129: "MachineSubCycle_MistSteam",
        130: "MachineSubCycle_CoolDown",
        131: "MachineSubCycle_ExtendedTumble",
        132: "MachineSubCycle_Damp",
        133: "MachineSubCycle_AirFluff"
    }.get(Erd_MachineSubCycle)
    ERDS_LIST.append(Erd_MachineSubCycle)
    
    Erd_ReduceStaticOption = int(ERDS[51], 16)
    Erd_ReduceStaticOption = {
        0: "ReduceStaticOption_Disabled",
        1: "ReduceStaticOption_Enabled",
        2: "ReduceStaticOption_Max",
        255: "ReduceStaticOption_DontCare"
    }.get(Erd_ReduceStaticOption)
    ERDS_LIST.append(Erd_ReduceStaticOption)

    Erd_EcoDryOption = int(ERDS[52], 16)
    Erd_EcoDryOption = {
        0: "EcoDryOption_Disabled",
        1: "EcoDryOption_Enabled",
        2: "EcoDryOption_Max",
        255: "EcoDryOption_DontCare"
    }.get(Erd_EcoDryOption)
    ERDS_LIST.append(Erd_EcoDryOption)

    Erd_TemperatureOption = int(ERDS[53], 16)
    Erd_TemperatureOption = {
        0: "TemperatureOption_Disabled",
        1: "TemperatureOption_NoHeat",
        2: "TemperatureOption_ExtraLow",
        3: "TemperatureOption_Low",
        4: "TemperatureOption_Medium",
        5: "TemperatureOption_High",
        6: "TemperatureOption_Max",
        255: "TemperatureOption_DontCare"
    }.get(Erd_TemperatureOption)
    ERDS_LIST.append(Erd_TemperatureOption)

    Erd_ExtendedTumbleOption = int(ERDS[54], 16)
    Erd_ExtendedTumbleOption = {
        0: "ExtendedTumbleOption_Disabled",
        1: "ExtendedTumbleOption_Enabled",
        2: "ExtendedTumbleOption_Max",
        255: "ExtendedTumbleOption_DontCare"
    }.get(Erd_ExtendedTumbleOption)
    ERDS_LIST.append(Erd_ExtendedTumbleOption)

    Erd_ScentOption = int(ERDS[55], 16)
    Erd_ScentOption = {
        0: "ScentOption_Off",
        1: "ScentOption_Auto",
        2: "ScentOption_More",
        3: "ScentOption_Less",
        4: "ScentOption_Max",
        255: "ScentOption_DontCare"
    }.get(Erd_ScentOption)
    ERDS_LIST.append(Erd_ScentOption)

    Erd_DetangleOption = int(ERDS[56], 16)
    Erd_DetangleOption = {
        0: "DetangleOption_Disabled",
        1: "DetangleOption_Enabled",
        2: "DetangleOption_Max",
        255: "DetangleOption_DontCare"
    }.get(Erd_DetangleOption)
    ERDS_LIST.append(Erd_DetangleOption)

    Erd_SanitizeOption = int(ERDS[57], 16)
    Erd_SanitizeOption = {
        0: "SanitizeOption_Disabled",
        1: "SanitizeOption_Enabled",
        2: "SanitizeOption_Max",
        255: "SanitizeOption_DontCare"
    }.get(Erd_SanitizeOption)
    ERDS_LIST.append(Erd_SanitizeOption)

    Erd_TimeLevelOption = int(ERDS[58], 16)
    Erd_TimeLevelOption = {
        0: "TimeLevelOption_Disabled",
        1: "TimeLevelOption_1",
        2: "TimeLevelOption_2",
        3: "TimeLevelOption_3",
        4: "TimeLevelOption_4",
        5: "TimeLevelOption_5",
        6: "TimeLevelOption_Max",
        255: "TimeLevelOption_DontCare"
    }.get(Erd_TimeLevelOption)
    ERDS_LIST.append(Erd_TimeLevelOption)

    Erd_AlertVolumeOption = int(ERDS[59], 16)
    Erd_AlertVolumeOption = {
        0: "VolumeOption_Off",
        1: "VolumeOption_Low",
        2: "VolumeOption_Medium",
        3: "VolumeOption_High",
        4: "VolumeOption_HighExtendedAlert",
        5: "VolumeOption_Max",
        255: "VolumeOption_DontCare"
    }.get(Erd_AlertVolumeOption)
    ERDS_LIST.append(Erd_AlertVolumeOption)

    Erd_SteamCycleOption = int(ERDS[60], 16)
    Erd_SteamCycleOption = {
        0: "SteamCycleOption_Disabled",
        1: "SteamCycleOption_SteamRefresh",
        2: "SteamCycleOption_SteamDewrinkle",
        3: "SteamCycleOption_Max",
        255: "SteamCycleOption_DontCare"
    }.get(Erd_SteamCycleOption)
    ERDS_LIST.append(Erd_SteamCycleOption)

    return ERDS_LIST

def System_State(ERD):
    Erd_CurrentSystemState = int(ERD, 16)
    return {                                           
        0: "STARTUp",
        1: "IDLE",
        2: "STANDBY",
        3: "RUN",
        4: "PAUSE",
        5: "ENDOFCYCLE",
        6: "DELAYRUN",
        7: "DELAYPAUSE",
        8: "COMMISSIONING",
        9: "MAX"                               
    }.get(Erd_CurrentSystemState)