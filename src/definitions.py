def ERDS_TO_WRITE(ERDS):
    ERDS_LIST = []

    Erd_CurrentSystemState = int(ERDS[0], 16)
    Erd_CurrentSystemStateValue = str(Erd_CurrentSystemState)
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
    ERDS_LIST.append(Erd_CurrentSystemStateValue)
    
    Erd_CycleSelected = int(ERDS[1], 16)
    Erd_CycleSelectedValue = str(Erd_CycleSelected)
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
    ERDS_LIST.append(Erd_CycleSelectedValue)
    
    Erd_EStarSensorDryRequested = int(ERDS[2], 16)
    Erd_EStarSensorDryRequestedValue = str(Erd_EStarSensorDryRequested)
    Erd_EStarSensorDryRequested = {
        0: "Disabled",
        1: "Enabled",
        2: "Max",
        255: "DontCare"
    }.get(Erd_EStarSensorDryRequested)
    ERDS_LIST.append(Erd_EStarSensorDryRequested)
    ERDS_LIST.append(Erd_EStarSensorDryRequestedValue)

    Erd_RamCycleHistoryRecord_drynessOptionAtStart = int(ERDS[3], 16)
    Erd_RamCycleHistoryRecord_drynessOptionAtStartValue = str(Erd_RamCycleHistoryRecord_drynessOptionAtStart)
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
    ERDS_LIST.append(Erd_RamCycleHistoryRecord_drynessOptionAtStartValue)
    
    Erd_RamCycleHistoryRecord_drynessOptionAtEnd = int(ERDS[4], 16)
    Erd_RamCycleHistoryRecord_drynessOptionAtEndValue = str(Erd_RamCycleHistoryRecord_drynessOptionAtEnd)
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
    ERDS_LIST.append(Erd_RamCycleHistoryRecord_drynessOptionAtEndValue)

    Erd_RamCycleHistoryRecord_temperatureOptionAtStart = int(ERDS[5], 16)
    Erd_RamCycleHistoryRecord_temperatureOptionAtStartValue = str(Erd_RamCycleHistoryRecord_temperatureOptionAtStart)
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
    ERDS_LIST.append(Erd_RamCycleHistoryRecord_temperatureOptionAtStartValue)

    Erd_RamCycleHistoryRecord_temperatureOptionAtEnd = int(ERDS[6], 16)
    Erd_RamCycleHistoryRecord_temperatureOptionAtEndValue = str(Erd_RamCycleHistoryRecord_temperatureOptionAtEnd)
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
    ERDS_LIST.append(Erd_RamCycleHistoryRecord_temperatureOptionAtEndValue)

    Erd_CurrentInletTemperature = int(ERDS[7], 16)
    Erd_CurrentInletTemperatureValue = str(Erd_CurrentInletTemperature)
    ERDS_LIST.append(str(Erd_CurrentInletTemperature))
    ERDS_LIST.append(Erd_CurrentInletTemperatureValue)

    Erd_CurrentOutletTemperature = int(ERDS[8], 16)
    Erd_CurrentOutletTemperatureValue = str(Erd_CurrentOutletTemperature)
    ERDS_LIST.append(str(Erd_CurrentOutletTemperature))
    ERDS_LIST.append(Erd_CurrentOutletTemperatureValue)

    Erd_OverTemperatureMaxInletTemperature = int(ERDS[9], 16)
    Erd_OverTemperatureMaxInletTemperatureValue = str(Erd_OverTemperatureMaxInletTemperature)
    ERDS_LIST.append(str(Erd_OverTemperatureMaxInletTemperature))
    ERDS_LIST.append(Erd_OverTemperatureMaxInletTemperatureValue)

    Erd_HeaterRelay1 = int(ERDS[10], 16)
    Erd_HeaterRelay1Value = str(Erd_HeaterRelay1)
    ERDS_LIST.append(str(Erd_HeaterRelay1))
    ERDS_LIST.append(Erd_HeaterRelay1Value)
    
    Erd_HeaterRelay2 = int(ERDS[11], 16)
    Erd_HeaterRelay2Value = str(Erd_HeaterRelay2)
    ERDS_LIST.append(str(Erd_HeaterRelay2))
    ERDS_LIST.append(Erd_HeaterRelay2Value)

    Erd_MaxTemperatureSlope = int(ERDS[12], 16)
    Erd_MaxTemperatureSlopeValue = str(Erd_MaxTemperatureSlope)
    ERDS_LIST.append(str(Erd_MaxTemperatureSlope))
    ERDS_LIST.append(Erd_MaxTemperatureSlopeValue)
    
    Erd_MinimumFilteredVoltageFromMc = int(ERDS[13], 16)
    Erd_MinimumFilteredVoltageFromMcValue = str(Erd_MinimumFilteredVoltageFromMc)
    ERDS_LIST.append(str(Erd_MinimumFilteredVoltageFromMc))
    ERDS_LIST.append(Erd_MinimumFilteredVoltageFromMcValue)

    Erd_FilteredMoistureSensor = int(ERDS[14], 16)
    Erd_FilteredMoistureSensorValue = str(Erd_FilteredMoistureSensor)
    ERDS_LIST.append(str(Erd_FilteredMoistureSensor))
    ERDS_LIST.append(Erd_FilteredMoistureSensorValue)
    
    Erd_SmoothMoistureReading = int(ERDS[15], 16)
    Erd_SmoothMoistureReadingValue = str(Erd_SmoothMoistureReading)
    ERDS_LIST.append(str(Erd_SmoothMoistureReading))
    ERDS_LIST.append(Erd_SmoothMoistureReadingValue)

    Erd_CalculatedCurvature = int(ERDS[16], 16)
    Erd_CalculatedCurvatureValue = str(Erd_CalculatedCurvature)
    ERDS_LIST.append(str(Erd_CalculatedCurvature))
    ERDS_LIST.append(Erd_CalculatedCurvatureValue)

    Erd_CurvatureOccurredCount = int(ERDS[17], 16)
    Erd_CurvatureOccurredCountValue = str(Erd_CurvatureOccurredCount)
    ERDS_LIST.append(str(Erd_CurvatureOccurredCount))    
    ERDS_LIST.append(Erd_CurvatureOccurredCountValue)

    Erd_TrimmerInhibitRelay1 = int(ERDS[18], 16)
    Erd_TrimmerInhibitRelay1Value = str(Erd_TrimmerInhibitRelay1)
    Erd_TrimmerInhibitRelay1 = {
        0: "False",
        1: "True"
    }.get(Erd_TrimmerInhibitRelay1)
    ERDS_LIST.append(Erd_TrimmerInhibitRelay1)
    ERDS_LIST.append(Erd_TrimmerInhibitRelay1Value)

    Erd_TrimmerInhibitRelay2 = int(ERDS[19], 16)
    Erd_TrimmerInhibitRelay2Value = str(Erd_TrimmerInhibitRelay2)
    Erd_TrimmerInhibitRelay2 = {
        0: "False",
        1: "True"
    }.get(Erd_TrimmerInhibitRelay2)
    ERDS_LIST.append(Erd_TrimmerInhibitRelay2)
    ERDS_LIST.append(Erd_TrimmerInhibitRelay2Value)

    Erd_TrimmerBothCoilInhibitRequest = int(ERDS[20], 16)
    Erd_TrimmerBothCoilInhibitRequestValue = str(Erd_TrimmerBothCoilInhibitRequest)
    Erd_TrimmerBothCoilInhibitRequest = {
        0: "False",
        1: "True"
    }.get(Erd_TrimmerBothCoilInhibitRequest)
    ERDS_LIST.append(Erd_TrimmerBothCoilInhibitRequest)
    ERDS_LIST.append(Erd_TrimmerBothCoilInhibitRequestValue)

    Erd_DrumMotorState = int(ERDS[21], 16)
    Erd_DrumMotorStateValue = str(Erd_DrumMotorState)
    Erd_DrumMotorState = {
        0: "Off",
        1: "Normal",
        2: "Reverse",
        3: "Max"       
    }.get(Erd_DrumMotorState)
    ERDS_LIST.append(Erd_DrumMotorState)
    ERDS_LIST.append(Erd_DrumMotorStateValue)

    Erd_FallbackHeatControlMethodStatus = int(ERDS[22], 16)
    Erd_FallbackHeatControlMethodStatusValue = str(Erd_FallbackHeatControlMethodStatus)
    Erd_FallbackHeatControlMethodStatus = {
        0: "False",
        1: "True"
    }.get(Erd_FallbackHeatControlMethodStatus)
    ERDS_LIST.append(Erd_FallbackHeatControlMethodStatus)
    ERDS_LIST.append(Erd_FallbackHeatControlMethodStatusValue)    

    Erd_ApplicationVersion = ERDS[23]
    Erd_ApplicationVersion_criticalMajor = str(int(Erd_ApplicationVersion[0:2], 16))
    Erd_ApplicationVersion_criticalMinor = str(int(Erd_ApplicationVersion[2:4], 16))
    Erd_ApplicationVersion_major = str(int(Erd_ApplicationVersion[4:6], 16))
    Erd_ApplicationVersion_minor = str(int(Erd_ApplicationVersion[6:8], 16))
    ERDS_LIST.append(Erd_ApplicationVersion_criticalMajor + "." + Erd_ApplicationVersion_criticalMinor + "." + Erd_ApplicationVersion_major + "." + Erd_ApplicationVersion_minor)
    ERDS_LIST.append(ERDS[23])
    
    Erd_ParametricVersion = ERDS[24]
    Erd_ParametricVersion_criticalMajor = str(int(Erd_ParametricVersion[0:2], 16))
    Erd_ParametricVersion_criticalMinor = str(int(Erd_ParametricVersion[2:4], 16))
    Erd_ParametricVersion_major = str(int(Erd_ParametricVersion[4:6], 16))
    Erd_ParametricVersion_minor = str(int(Erd_ParametricVersion[6:8], 16))
    ERDS_LIST.append(Erd_ParametricVersion_criticalMajor + "." + Erd_ParametricVersion_criticalMinor + "." + Erd_ParametricVersion_major + "." + Erd_ParametricVersion_minor)
    ERDS_LIST.append(ERDS[24])
    
    Erd_Personality = int(ERDS[25], 16)
    Erd_PersonalityValue = str(Erd_Personality)
    ERDS_LIST.append(str(Erd_Personality))
    ERDS_LIST.append(Erd_PersonalityValue)

    Erd_DrynessOption = int(ERDS[26], 16)
    Erd_DrynessOptionValue = str(Erd_DrynessOption)
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
    ERDS_LIST.append(Erd_DrynessOptionValue)

    Erd_VentRestriction = int(ERDS[27], 16)
    Erd_VentRestrictionValue = str(Erd_VentRestriction)
    Erd_VentRestriction = {
        0: "Unknown",
        1: "Small",
        2: "Large"
    }.get(Erd_VentRestriction)
    ERDS_LIST.append(Erd_VentRestriction)
    ERDS_LIST.append(Erd_VentRestrictionValue)    

    Erd_LoadSizeByAggregation = int(ERDS[28], 16)
    Erd_LoadSizeByAggregationValue = str(Erd_LoadSizeByAggregation)
    Erd_LoadSizeByAggregation = {
        0: "Unknown",
        1: "Small",
        2: "Large"
    }.get(Erd_LoadSizeByAggregation)
    ERDS_LIST.append(Erd_LoadSizeByAggregation)
    ERDS_LIST.append(Erd_LoadSizeByAggregationValue) 

    Erd_LoadSizeByContact = int(ERDS[29], 16)
    Erd_LoadSizeByContactValue = str(Erd_LoadSizeByContact)
    Erd_LoadSizeByContact = {
        0: "Unknown",
        1: "Small",
        2: "Large"
    }.get(Erd_LoadSizeByContact)
    ERDS_LIST.append(Erd_LoadSizeByContact) 
    ERDS_LIST.append(Erd_LoadSizeByContactValue)

    Erd_LoadSizeByTemperature = int(ERDS[30], 16)
    Erd_LoadSizeByTemperatureValue = str(Erd_LoadSizeByTemperature)
    Erd_LoadSizeByTemperature = {
        0: "Unknown",
        1: "Small",
        2: "Large"
    }.get(Erd_LoadSizeByTemperature)
    ERDS_LIST.append(Erd_LoadSizeByTemperature) 
    ERDS_LIST.append(Erd_LoadSizeByTemperatureValue)

    Erd_TargetMoistureVoltageHasBeenReached = int(ERDS[31], 16)
    Erd_TargetMoistureVoltageHasBeenReachedValue = str(Erd_TargetMoistureVoltageHasBeenReached)
    Erd_TargetMoistureVoltageHasBeenReached = {
        0: "False",
        1: "True"
    }.get(Erd_TargetMoistureVoltageHasBeenReached)
    ERDS_LIST.append(Erd_TargetMoistureVoltageHasBeenReached)
    ERDS_LIST.append(Erd_TargetMoistureVoltageHasBeenReachedValue)
    
    Erd_TargetMoistureVoltage = int(ERDS[32], 16)
    Erd_TargetMoistureVoltageValue = str(Erd_TargetMoistureVoltage)
    ERDS_LIST.append(str(Erd_TargetMoistureVoltage))
    ERDS_LIST.append(Erd_TargetMoistureVoltageValue)
    
    Erd_TotalDryTimeCalculatorTimeMultiplierX100 = int(ERDS[33], 16)
    Erd_TotalDryTimeCalculatorTimeMultiplierX100Value = str(Erd_TotalDryTimeCalculatorTimeMultiplierX100)
    ERDS_LIST.append(str(Erd_TotalDryTimeCalculatorTimeMultiplierX100))
    ERDS_LIST.append(Erd_TotalDryTimeCalculatorTimeMultiplierX100Value)

    Erd_TotalDryTimeCalculatorTimeAdderSeconds = int(ERDS[34], 16)
    Erd_TotalDryTimeCalculatorTimeAdderSecondsValue = str(Erd_TotalDryTimeCalculatorTimeAdderSeconds)
    ERDS_LIST.append(str(Erd_TotalDryTimeCalculatorTimeAdderSeconds))
    ERDS_LIST.append(Erd_TotalDryTimeCalculatorTimeAdderSecondsValue)
        
    Erd_TimeToReachTargetVoltageSeconds = int(ERDS[35], 16)
    Erd_TimeToReachTargetVoltageSecondsValue = str(Erd_TimeToReachTargetVoltageSeconds)
    ERDS_LIST.append(str(Erd_TimeToReachTargetVoltageSeconds))
    ERDS_LIST.append(Erd_TimeToReachTargetVoltageSecondsValue)

    Erd_SensingCycleTotalDryingTimeSeconds = int(ERDS[36], 16)
    Erd_SensingCycleTotalDryingTimeSecondsValue = str(Erd_SensingCycleTotalDryingTimeSeconds)
    ERDS_LIST.append(str(Erd_SensingCycleTotalDryingTimeSeconds))
    ERDS_LIST.append(Erd_SensingCycleTotalDryingTimeSecondsValue)

    Erd_DrumGroundWatchdogResult = int(ERDS[37], 16)
    Erd_DrumGroundWatchdogResultValue = str(Erd_DrumGroundWatchdogResult)
    Erd_DrumGroundWatchdogResult = {
        0: "Unknown",
        1: "NotExpired",
        2: "Expired"
    }.get(Erd_DrumGroundWatchdogResult)
    ERDS_LIST.append(Erd_DrumGroundWatchdogResult)
    ERDS_LIST.append(Erd_DrumGroundWatchdogResultValue)

    Erd_ClothDampnessCheckResult = int(ERDS[38], 16)
    Erd_ClothDampnessCheckResultValue = str(Erd_ClothDampnessCheckResult)
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
    ERDS_LIST.append(Erd_ClothDampnessCheckResultValue)

    Erd_Fault_DrumGroundWatchdogDetection = int(ERDS[39], 16)
    Erd_Fault_DrumGroundWatchdogDetectionValue = str(Erd_Fault_DrumGroundWatchdogDetection)
    Erd_Fault_DrumGroundWatchdogDetection = {
        0: "False",
        1: "True"
    }.get(Erd_Fault_DrumGroundWatchdogDetection)
    ERDS_LIST.append(Erd_Fault_DrumGroundWatchdogDetection)
    ERDS_LIST.append(Erd_Fault_DrumGroundWatchdogDetectionValue)

    Erd_SteamValveCycleCountRam = int(ERDS[40], 16)
    Erd_SteamValveCycleCountRamValue = str(Erd_SteamValveCycleCountRam)
    ERDS_LIST.append(str(Erd_SteamValveCycleCountRam))
    ERDS_LIST.append(Erd_SteamValveCycleCountRamValue)

    Erd_SteamValveOnTimeDurationInSecondsRam = int(ERDS[41], 16)
    Erd_SteamValveOnTimeDurationInSecondsRamValue = str(Erd_SteamValveOnTimeDurationInSecondsRam)
    ERDS_LIST.append(str(Erd_SteamValveOnTimeDurationInSecondsRam))   
    ERDS_LIST.append(Erd_SteamValveOnTimeDurationInSecondsRamValue)

    Erd_CoolDownStepStatus = int(ERDS[42], 16)
    Erd_CoolDownStepStatusValue = str(Erd_CoolDownStepStatus)
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
    ERDS_LIST.append(Erd_CoolDownStepStatusValue)

    Erd_ExtendedTumbleStepStatus = int(ERDS[43], 16)
    Erd_ExtendedTumbleStepStatusValue = Erd_ExtendedTumbleStepStatus
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
    ERDS_LIST.append(Erd_ExtendedTumbleStepStatusValue)

    Erd_SteamStepStatus = int(ERDS[44], 16)
    Erd_SteamStepStatusValue = str(Erd_SteamStepStatus)
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
    ERDS_LIST.append(Erd_SteamStepStatusValue)

    Erd_EndOfCycleReason = int(ERDS[45], 16)
    Erd_EndOfCycleReasonValue = str(Erd_EndOfCycleReason)
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
    ERDS_LIST.append(Erd_EndOfCycleReasonValue)
    
    Erd_ModelNumber = str(bytes.fromhex(ERDS[46]).decode('utf-8').replace('\x00', ''))
    ERDS_LIST.append(Erd_ModelNumber)
    ERDS_LIST.append(ERDS[46])
    
    Erd_SerialNumber = str(bytes.fromhex(ERDS[47]).decode('utf-8').replace('\x00', ''))
    ERDS_LIST.append(Erd_SerialNumber)
    ERDS_LIST.append(ERDS[47])
    
    Erd_AppliancePersonality = int(ERDS[48], 16)
    Erd_AppliancePersonalityValue = str(Erd_AppliancePersonality)
    ERDS_LIST.append(str(Erd_AppliancePersonality))
    ERDS_LIST.append(Erd_AppliancePersonalityValue)

    Erd_MachineStatus = int(ERDS[49], 16)
    Erd_MachineStatusValue = str(Erd_MachineStatus)
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
    ERDS_LIST.append(Erd_MachineStatusValue)
    
    Erd_MachineSubCycle = int(ERDS[50], 16)
    Erd_MachineSubCycleValue = str(Erd_MachineSubCycle)
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
    ERDS_LIST.append(Erd_MachineSubCycleValue)
    
    Erd_ReduceStaticOption = int(ERDS[51], 16)
    Erd_ReduceStaticOptionValue = str(Erd_ReduceStaticOption)
    Erd_ReduceStaticOption = {
        0: "ReduceStaticOption_Disabled",
        1: "ReduceStaticOption_Enabled",
        2: "ReduceStaticOption_Max",
        255: "ReduceStaticOption_DontCare"
    }.get(Erd_ReduceStaticOption)
    ERDS_LIST.append(Erd_ReduceStaticOption)
    ERDS_LIST.append(Erd_ReduceStaticOptionValue)

    Erd_EcoDryOption = int(ERDS[52], 16)
    Erd_EcoDryOptionValue = str(Erd_EcoDryOption)
    Erd_EcoDryOption = {
        0: "EcoDryOption_Disabled",
        1: "EcoDryOption_Enabled",
        2: "EcoDryOption_Max",
        255: "EcoDryOption_DontCare"
    }.get(Erd_EcoDryOption)
    ERDS_LIST.append(Erd_EcoDryOption)
    ERDS_LIST.append(Erd_EcoDryOptionValue)

    Erd_TemperatureOption = int(ERDS[53], 16)
    Erd_TemperatureOptionValue = str(Erd_TemperatureOption)
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
    ERDS_LIST.append(Erd_TemperatureOptionValue)

    Erd_ExtendedTumbleOption = int(ERDS[54], 16)
    Erd_ExtendedTumbleOptionValue = str(Erd_ExtendedTumbleOption)
    Erd_ExtendedTumbleOption = {
        0: "ExtendedTumbleOption_Disabled",
        1: "ExtendedTumbleOption_Enabled",
        2: "ExtendedTumbleOption_Max",
        255: "ExtendedTumbleOption_DontCare"
    }.get(Erd_ExtendedTumbleOption)
    ERDS_LIST.append(Erd_ExtendedTumbleOption)
    ERDS_LIST.append(Erd_ExtendedTumbleOptionValue)

    Erd_ScentOption = int(ERDS[55], 16)
    Erd_ScentOptionValue = str(Erd_ScentOption)
    Erd_ScentOption = {
        0: "ScentOption_Off",
        1: "ScentOption_Auto",
        2: "ScentOption_More",
        3: "ScentOption_Less",
        4: "ScentOption_Max",
        255: "ScentOption_DontCare"
    }.get(Erd_ScentOption)
    ERDS_LIST.append(Erd_ScentOption)
    ERDS_LIST.append(Erd_ScentOptionValue)

    Erd_DetangleOption = int(ERDS[56], 16)
    Erd_DetangleOptionValue = str(Erd_DetangleOption)
    Erd_DetangleOption = {
        0: "DetangleOption_Disabled",
        1: "DetangleOption_Enabled",
        2: "DetangleOption_Max",
        255: "DetangleOption_DontCare"
    }.get(Erd_DetangleOption)
    ERDS_LIST.append(Erd_DetangleOption)
    ERDS_LIST.append(Erd_DetangleOptionValue)

    Erd_SanitizeOption = int(ERDS[57], 16)
    Erd_SanitizeOptionValue = str(Erd_SanitizeOption)
    Erd_SanitizeOption = {
        0: "SanitizeOption_Disabled",
        1: "SanitizeOption_Enabled",
        2: "SanitizeOption_Max",
        255: "SanitizeOption_DontCare"
    }.get(Erd_SanitizeOption)
    ERDS_LIST.append(Erd_SanitizeOption)
    ERDS_LIST.append(Erd_SanitizeOptionValue)

    Erd_TimeLevelOption = int(ERDS[58], 16)
    Erd_TimeLevelOptionValue = str(Erd_TimeLevelOption)
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
    ERDS_LIST.append(Erd_TimeLevelOptionValue)

    Erd_AlertVolumeOption = int(ERDS[59], 16)
    Erd_AlertVolumeOptionValue = str(Erd_AlertVolumeOption)
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
    ERDS_LIST.append(Erd_AlertVolumeOptionValue)

    Erd_SteamCycleOption = int(ERDS[60], 16)
    Erd_SteamCycleOptionValue = str(Erd_SteamCycleOption)
    Erd_SteamCycleOption = {
        0: "SteamCycleOption_Disabled",
        1: "SteamCycleOption_SteamRefresh",
        2: "SteamCycleOption_SteamDewrinkle",
        3: "SteamCycleOption_Max",
        255: "SteamCycleOption_DontCare"
    }.get(Erd_SteamCycleOption)
    ERDS_LIST.append(Erd_SteamCycleOption)
    ERDS_LIST.append(Erd_SteamCycleOptionValue)

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