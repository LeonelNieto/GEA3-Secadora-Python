def ERDS_TO_WRITE(ERDS):
    ERDS_LIST = []

    Erd_CurrentSystemState = int(ERDS[0], 16)
    Erd_CurrentSystemState = {                                           
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
    ERDS_LIST.append(Erd_CurrentSystemState)

    Erd_CycleSelected = int(ERDS[1], 16)
    Erd_CycleSelected = {
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
    ERDS_LIST.append(Erd_CycleSelected)
    
    Erd_EStarSensorDryRequested = int(ERDS[2], 16)
    Erd_EStarSensorDryRequested = {
        0: "EStarOption_Disabled",
        1: "EStarOption_Enabled",
        2: "EStarOption_Max",
        255: "EStarOption_DontCare"
    }.get(Erd_EStarSensorDryRequested)
    ERDS_LIST.append(Erd_EStarSensorDryRequested)

    Erd_RamCycleHistoryRecord_drynessOptionAtStart = int(ERDS[3], 16)
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
    ERDS_LIST.append(Erd_RamCycleHistoryRecord_drynessOptionAtStart)

    Erd_RamCycleHistoryRecord_drynessOptionAtEnd = int(ERDS[4], 16)
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
    ERDS_LIST.append(Erd_RamCycleHistoryRecord_drynessOptionAtEnd)

    Erd_RamCycleHistoryRecord_temperatureOptionAtStart = int(ERDS[5], 16)
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
    ERDS_LIST.append(Erd_RamCycleHistoryRecord_temperatureOptionAtStart)

    Erd_RamCycleHistoryRecord_temperatureOptionAtEnd = int(ERDS[6], 16)
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
        0: "DrumMotorState_Off",
        1: "DrumMotorState_Normal",
        2: "DrumMotorState_Reverse",
        3: "DrumMotorState_Max"       
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
        0: "DrynessOption_Disabled",
        1: "DrynessOption_Minimum",
        2: "DrynessOption_LessDry",
        3: "DrynessOption_Dry",
        4: "DrynessOption_MoreDry",
        5: "DrynessOption_ExtraDry",
        6: "DrynessOption_Max",
        255: "DrynessOption_DontCare"
    }.get(Erd_DrynessOption)
    ERDS_LIST.append(Erd_DrynessOption)

    Erd_VentRestriction = int(ERDS[28], 16)
    Erd_VentRestriction = {
        0: "VentRestriction_Unknown",
        1: "VentRestriction_Small",
        2: "VentRestriction_Large"
    }.get(Erd_VentRestriction)
    ERDS_LIST.append(Erd_VentRestriction)    

    Erd_LoadSizeByAggregation = int(ERDS[29], 16)
    Erd_LoadSizeByAggregation = {
        0: "LoadSize_Unknown",
        1: "LoadSize_Small",
        2: "LoadSize_Large"
    }.get(Erd_LoadSizeByAggregation)
    ERDS_LIST.append(Erd_LoadSizeByAggregation) 

    Erd_LoadSizeByContact = int(ERDS[30], 16)
    Erd_LoadSizeByContact = {
        0: "LoadSize_Unknown",
        1: "LoadSize_Small",
        2: "LoadSize_Large"
    }.get(Erd_LoadSizeByContact)
    ERDS_LIST.append(Erd_LoadSizeByContact) 

    Erd_LoadSizeByTemperature = int(ERDS[31], 16)
    Erd_LoadSizeByTemperature = {
        0: "LoadSize_Unknown",
        1: "LoadSize_Small",
        2: "LoadSize_Large"
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
        0: "DrumGroundWatchdogResult_Unknown",
        1: "DrumGroundWatchdogResult_NotExpired",
        2: "DrumGroundWatchdogResult_Expired"
    }.get(Erd_DrumGroundWatchdogResult)
    ERDS_LIST.append(Erd_DrumGroundWatchdogResult)

    Erd_ClothDampnessCheckResult = int(ERDS[44], 16)
    Erd_ClothDampnessCheckResult = {
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
    ERDS_LIST.append(Erd_CoolDownStepStatus)    

    Erd_ExtendedTumbleStepStatus = int(ERDS[49], 16)
    Erd_ExtendedTumbleStepStatus = {
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
    ERDS_LIST.append(Erd_ExtendedTumbleStepStatus)    

    Erd_SteamStepStatus = int(ERDS[50], 16)
    Erd_SteamStepStatus = {
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
    ERDS_LIST.append(Erd_SteamStepStatus) 

    Erd_EndOfCycleReason = int(ERDS[51], 16)
    Erd_EndOfCycleReason = {
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
    ERDS_LIST.append(Erd_EndOfCycleReason) 

    return ERDS_LIST

# print(ERDS_TO_WRITE([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0102010201020102010002030400010200010202010202010201020010201200010100010100001010102000010010101010", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0102034055010910", "010203405501091", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0 ,0, 0, 0]))