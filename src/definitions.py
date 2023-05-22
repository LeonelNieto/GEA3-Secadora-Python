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

    Erd_HeatControlParametric = ERDS[13]
    Erd_HeatControlParametricheaterData0_inletTemperatureLowerLimit = str(int(Erd_HeatControlParametric[0:4], 16))
    ERDS_LIST.append(Erd_HeatControlParametricheaterData0_inletTemperatureLowerLimit)
    Erd_HeatControlParametric_heaterData0_inletTemperatureUpperLimit = str(int(Erd_HeatControlParametric[4:8], 16))
    ERDS_LIST.append(Erd_HeatControlParametric_heaterData0_inletTemperatureUpperLimit)
    Erd_HeatControlParametric_heaterData0_outletTemperatureLowerLimit = str(int(Erd_HeatControlParametric[8:12], 16))
    ERDS_LIST.append(Erd_HeatControlParametric_heaterData0_outletTemperatureLowerLimit)
    Erd_HeatControlParametric_heaterData0_outletTemperatureUpperLimit = str(int(Erd_HeatControlParametric[12:16], 16))
    ERDS_LIST.append(Erd_HeatControlParametric_heaterData0_outletTemperatureUpperLimit)
    Erd_HeatControlParametric_heaterData0_onTimeSeconds = str(int(Erd_HeatControlParametric[16:18], 16))
    ERDS_LIST.append(Erd_HeatControlParametric_heaterData0_onTimeSeconds)
    Erd_HeatControlParametric_heaterData0_offTimeSeconds = str(int(Erd_HeatControlParametric[18:20], 16))
    ERDS_LIST.append(Erd_HeatControlParametric_heaterData0_offTimeSeconds)
    Erd_HeatControlParametric_heaterData0_relayIsEnabled = int(Erd_HeatControlParametric[20:22], 16)
    Erd_HeatControlParametric_heaterData0_relayIsEnabled = {
        0: "False",
        1: "True"
    }.get(Erd_HeatControlParametric_heaterData0_relayIsEnabled)
    ERDS_LIST.append(Erd_HeatControlParametric_heaterData0_relayIsEnabled)
    Erd_HeatControlParametric_heaterData1_inletTemperatureLowerLimit = str(int(Erd_HeatControlParametric[24:28], 16))
    ERDS_LIST.append(Erd_HeatControlParametric_heaterData1_inletTemperatureLowerLimit)
    Erd_HeatControlParametric_heaterData1_inletTemperatureUpperLimit = str(int(Erd_HeatControlParametric[28:32], 16))
    ERDS_LIST.append(Erd_HeatControlParametric_heaterData1_inletTemperatureUpperLimit)
    Erd_HeatControlParametric_heaterData1_outletTemperatureLowerLimit = str(int(Erd_HeatControlParametric[32:36], 16))
    ERDS_LIST.append(Erd_HeatControlParametric_heaterData1_outletTemperatureLowerLimit)
    Erd_HeatControlParametric_heaterData1_outletTemperatureUpperLimit = str(int(Erd_HeatControlParametric[36:40], 16))
    ERDS_LIST.append(Erd_HeatControlParametric_heaterData1_outletTemperatureUpperLimit)
    Erd_HeatControlParametric_heaterData1_onTimeSeconds = str(int(Erd_HeatControlParametric[40:42], 16))
    ERDS_LIST.append(Erd_HeatControlParametric_heaterData1_onTimeSeconds)
    Erd_HeatControlParametric_heaterData1_offTimeSeconds = str(int(Erd_HeatControlParametric[42:44], 16))
    ERDS_LIST.append(Erd_HeatControlParametric_heaterData1_offTimeSeconds)
    Erd_HeatControlParametric_heaterData1_relayIsEnabled = int(Erd_HeatControlParametric[44:46], 16)
    Erd_HeatControlParametric_heaterData1_relayIsEnabled = {
        0: "False",
        1: "True"
    }.get(Erd_HeatControlParametric_heaterData1_relayIsEnabled)
    ERDS_LIST.append(Erd_HeatControlParametric_heaterData1_relayIsEnabled)

    Erd_MinimumFilteredVoltageFromMc = int(ERDS[14], 16)
    ERDS_LIST.append(str(Erd_MinimumFilteredVoltageFromMc))

    Erd_FilteredMoistureSensor = int(ERDS[15], 16)
    ERDS_LIST.append(str(Erd_FilteredMoistureSensor))
    
    Erd_SmoothMoistureReading = int(ERDS[16], 16)
    ERDS_LIST.append(str(Erd_SmoothMoistureReading))

    Erd_CalculatedCurvature = int(ERDS[17], 16)
    ERDS_LIST.append(str(Erd_CalculatedCurvature))

    Erd_CurvatureOccurredCount = int(ERDS[18], 16)
    ERDS_LIST.append(str(Erd_CurvatureOccurredCount))    

    Erd_TrimmerInhibitRelay1 = int(ERDS[19], 16)
    Erd_TrimmerInhibitRelay1 = {
        0: "False",
        1: "True"
    }.get(Erd_TrimmerInhibitRelay1)
    ERDS_LIST.append(Erd_TrimmerInhibitRelay1)

    Erd_TrimmerInhibitRelay2 = int(ERDS[20], 16)
    Erd_TrimmerInhibitRelay2 = {
        0: "False",
        1: "True"
    }.get(Erd_TrimmerInhibitRelay2)
    ERDS_LIST.append(Erd_TrimmerInhibitRelay2)

    Erd_TrimmerBothCoilInhibitRequest = int(ERDS[21], 16)
    Erd_TrimmerBothCoilInhibitRequest = {
        0: "False",
        1: "True"
    }.get(Erd_TrimmerBothCoilInhibitRequest)
    ERDS_LIST.append(Erd_TrimmerBothCoilInhibitRequest)

    Erd_DrumMotorState = int(ERDS[22], 16)
    Erd_DrumMotorState = {
        0: "Off",
        1: "Normal",
        2: "Reverse",
        3: "Max"       
    }.get(Erd_DrumMotorState)
    ERDS_LIST.append(Erd_DrumMotorState)

    Erd_FallbackHeatControlMethodStatus = int(ERDS[23], 16)
    Erd_FallbackHeatControlMethodStatus = {
        0: "False",
        1: "True"
    }.get(Erd_FallbackHeatControlMethodStatus)
    ERDS_LIST.append(Erd_FallbackHeatControlMethodStatus)    

    Erd_ApplicationVersion = ERDS[24]
    Erd_ApplicationVersion_criticalMajor = str(int(Erd_ApplicationVersion[0:2], 16))
    Erd_ApplicationVersion_criticalMinor = str(int(Erd_ApplicationVersion[2:4], 16))
    Erd_ApplicationVersion_major = str(int(Erd_ApplicationVersion[4:6], 16))
    Erd_ApplicationVersion_minor = str(int(Erd_ApplicationVersion[6:8], 16))
    ERDS_LIST.append(Erd_ApplicationVersion_criticalMajor + "." + Erd_ApplicationVersion_criticalMinor + "." + Erd_ApplicationVersion_major + "." + Erd_ApplicationVersion_minor)

    Erd_ParametricVersion = ERDS[25]
    Erd_ParametricVersion_criticalMajor = str(int(Erd_ParametricVersion[0:2], 16))
    Erd_ParametricVersion_criticalMinor = str(int(Erd_ParametricVersion[2:4], 16))
    Erd_ParametricVersion_major = str(int(Erd_ParametricVersion[4:6], 16))
    Erd_ParametricVersion_minor = str(int(Erd_ParametricVersion[6:8], 16))
    ERDS_LIST.append(Erd_ParametricVersion_criticalMajor + "." + Erd_ParametricVersion_criticalMinor + "." + Erd_ParametricVersion_major + "." + Erd_ParametricVersion_minor)

    Erd_Personality = int(ERDS[26], 16)
    ERDS_LIST.append(str(Erd_Personality))

    Erd_DrynessOption = int(ERDS[27], 16)
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

    Erd_VentRestriction = int(ERDS[28], 16)
    Erd_VentRestriction = {
        0: "Unknown",
        1: "Small",
        2: "Large"
    }.get(Erd_VentRestriction)
    ERDS_LIST.append(Erd_VentRestriction)    

    Erd_LoadSizeByAggregation = int(ERDS[29], 16)
    Erd_LoadSizeByAggregation = {
        0: "Unknown",
        1: "Small",
        2: "Large"
    }.get(Erd_LoadSizeByAggregation)
    ERDS_LIST.append(Erd_LoadSizeByAggregation) 

    Erd_LoadSizeByContact = int(ERDS[30], 16)
    Erd_LoadSizeByContact = {
        0: "Unknown",
        1: "Small",
        2: "Large"
    }.get(Erd_LoadSizeByContact)
    ERDS_LIST.append(Erd_LoadSizeByContact) 

    Erd_LoadSizeByTemperature = int(ERDS[31], 16)
    Erd_LoadSizeByTemperature = {
        0: "Unknown",
        1: "Small",
        2: "Large"
    }.get(Erd_LoadSizeByTemperature)
    ERDS_LIST.append(Erd_LoadSizeByTemperature) 

    Erd_TargetMoistureVoltageHasBeenReached = int(ERDS[32], 16)
    Erd_TargetMoistureVoltageHasBeenReached = {
        0: "False",
        1: "True"
    }.get(Erd_TargetMoistureVoltageHasBeenReached)
    ERDS_LIST.append(Erd_TargetMoistureVoltageHasBeenReached)
    
    Erd_TargetMoistureVoltage = int(ERDS[33], 16)
    ERDS_LIST.append(str(Erd_TargetMoistureVoltage))
    
    Erd_TotalDryTimeCalculatorTimeMultiplierX100 = int(ERDS[34], 16)
    ERDS_LIST.append(str(Erd_TotalDryTimeCalculatorTimeMultiplierX100))

    Erd_TotalDryTimeCalculatorTimeAdderSeconds = int(ERDS[35], 16)
    ERDS_LIST.append(str(Erd_TotalDryTimeCalculatorTimeAdderSeconds))

    Erd_SensorDryTemperatureMultiplierx100_temperatureMultiplierEcoDry = str(int(ERDS[36], 16))
    ERDS_LIST.append(Erd_SensorDryTemperatureMultiplierx100_temperatureMultiplierEcoDry)

    Erd_SensorDryTemperatureMultiplierx100_temperatureMultiplierExtraLow = str(int(ERDS[37], 16))
    ERDS_LIST.append(Erd_SensorDryTemperatureMultiplierx100_temperatureMultiplierExtraLow)
    
    Erd_SensorDryTemperatureMultiplierx100_temperatureMultiplierLow = str(int(ERDS[38], 16))
    ERDS_LIST.append(Erd_SensorDryTemperatureMultiplierx100_temperatureMultiplierLow)
    
    Erd_SensorDryTemperatureMultiplierx100_temperatureMultiplierMedium = str(int(ERDS[39], 16))
    ERDS_LIST.append(Erd_SensorDryTemperatureMultiplierx100_temperatureMultiplierMedium)
    
    Erd_SensorDryTemperatureMultiplierx100_temperatureMultiplierHigh = str(int(ERDS[40], 16))
    ERDS_LIST.append(Erd_SensorDryTemperatureMultiplierx100_temperatureMultiplierHigh)
        
    Erd_TimeToReachTargetVoltageSeconds = int(ERDS[41], 16)
    ERDS_LIST.append(str(Erd_TimeToReachTargetVoltageSeconds))

    Erd_SensingCycleTotalDryingTimeSeconds = int(ERDS[42], 16)
    ERDS_LIST.append(str(Erd_SensingCycleTotalDryingTimeSeconds))

    Erd_DrumGroundWatchdogResult = int(ERDS[43], 16)
    Erd_DrumGroundWatchdogResult = {
        0: "Unknown",
        1: "NotExpired",
        2: "Expired"
    }.get(Erd_DrumGroundWatchdogResult)
    ERDS_LIST.append(Erd_DrumGroundWatchdogResult)

    Erd_ClothDampnessCheckResult = int(ERDS[44], 16)
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

    Erd_Fault_DrumGroundWatchdogDetection = int(ERDS[45], 16)
    Erd_Fault_DrumGroundWatchdogDetection = {
        0: "False",
        1: "True"
    }.get(Erd_Fault_DrumGroundWatchdogDetection)
    ERDS_LIST.append(Erd_Fault_DrumGroundWatchdogDetection)

    Erd_SteamValveCycleCountRam = int(ERDS[46], 16)
    ERDS_LIST.append(str(Erd_SteamValveCycleCountRam))

    Erd_SteamValveOnTimeDurationInSecondsRam = int(ERDS[47], 16)
    ERDS_LIST.append(str(Erd_SteamValveOnTimeDurationInSecondsRam))   

    Erd_CoolDownStepStatus = int(ERDS[48], 16)
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

    Erd_ExtendedTumbleStepStatus = int(ERDS[49], 16)
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

    Erd_SteamStepStatus = int(ERDS[50], 16)
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

    Erd_EndOfCycleReason = int(ERDS[51], 16)
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
    
    Erd_ModelNumber = ERDS[52]
    ERDS_LIST.append(Erd_ModelNumber)
    
    Erd_SerialNumber = ERDS[53]
    ERDS_LIST.append(Erd_SerialNumber)
    
    Erd_AppliancePersonality = int(ERDS[54], 16)
    ERDS_LIST.append(str(Erd_AppliancePersonality))

    Erd_MachineStatus = int(ERDS[55], 16)
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
    
    Erd_MachineSubCycle = int(ERDS[56], 16)
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
    
    Erd_EcoDryOptionRequest = int(ERDS[57], 16)
    Erd_EcoDryOptionRequest = {
        0: "EcoDryOption_Disabled",
        1: "EcoDryOption_Enabled",
        2: "EcoDryOption_Max",
        255: "EcoDryOption_DontCare"
    }.get(Erd_EcoDryOptionRequest)
    ERDS_LIST.append(Erd_EcoDryOptionRequest)
    
    Erd_ReduceStaticOption = int(ERDS[58], 16)
    Erd_ReduceStaticOption = {
        0: "ReduceStaticOption_Disabled",
        1: "ReduceStaticOption_Enabled",
        2: "ReduceStaticOption_Max",
        255: "ReduceStaticOption_DontCare"
    }.get(Erd_ReduceStaticOption)
    ERDS_LIST.append(Erd_ReduceStaticOption)
    
    Erd_ExtendedTumbleAllowable = str(bin(int(ERDS[59], 16)))
    Erd_ExtendedTumbleAllowable_ExtendedTumbleAllowablesBit_Disabled = Erd_ExtendedTumbleAllowable[2:3]
    Erd_ExtendedTumbleAllowable_ExtendedTumbleAllowablesBit_Enabled = Erd_ExtendedTumbleAllowable[3:4]
    ERDS_LIST.append(Erd_ExtendedTumbleAllowable_ExtendedTumbleAllowablesBit_Disabled)
    ERDS_LIST.append(Erd_ExtendedTumbleAllowable_ExtendedTumbleAllowablesBit_Enabled)
    
    Erd_DetangleAllowable = str(bin(int(ERDS[60], 16)))
    Erd_DetangleAllowable_DetangleAllowablesBit_Disabled = Erd_DetangleAllowable[2:3]
    Erd_DetangleAllowable_DetangleAllowablesBit_Enabled = Erd_DetangleAllowable[3:4]
    ERDS_LIST.append(Erd_DetangleAllowable_DetangleAllowablesBit_Disabled)
    ERDS_LIST.append(Erd_DetangleAllowable_DetangleAllowablesBit_Enabled)
    
    Erd_MyCycleAllowable = str(bin(int(ERDS[61], 16)))
    Erd_MyCycleAllowable_MyCycleAllowablesBit_Disabled = Erd_MyCycleAllowable[2:3]
    Erd_MyCycleAllowable_MyCycleAllowablesBit_Enabled = Erd_MyCycleAllowable[3:4]
    ERDS_LIST.append(Erd_MyCycleAllowable_MyCycleAllowablesBit_Disabled)
    ERDS_LIST.append(Erd_MyCycleAllowable_MyCycleAllowablesBit_Enabled)
    
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