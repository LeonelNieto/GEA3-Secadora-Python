def ERDS_TO_WRITE(ERDS):
    ERDS_LIST = []

    Erd_CurrentSystemState = ERDS[0]
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

    Erd_CycleSelected = ERDS[1]
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
    
    Erd_EStarSensorDryRequested = ERDS[2]
    Erd_EStarSensorDryRequested = {
        0: "EStarOption_Disabled",
        1: "EStarOption_Enabled",
        2: "EStarOption_Max",
        255: "EStarOption_DontCare"
    }.get(Erd_EStarSensorDryRequested)
    ERDS_LIST.append(Erd_EStarSensorDryRequested)

    Erd_RamCycleHistoryRecord_drynessOptionAtStart = ERDS[3]
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

    Erd_RamCycleHistoryRecord_drynessOptionAtEnd = ERDS[4]
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

    Erd_RamCycleHistoryRecord_temperatureOptionAtStart = ERDS[5]
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

    Erd_RamCycleHistoryRecord_temperatureOptionAtEnd = ERDS[6]
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

    Erd_CurrentInletTemperature = ERDS[7]
    ERDS_LIST.append(str(Erd_CurrentInletTemperature))

    Erd_CurrentOutletTemperature = ERDS[8]
    ERDS_LIST.append(str(Erd_CurrentOutletTemperature))

    Erd_OverTemperatureMaxInletTemperature = ERDS[9]
    ERDS_LIST.append(str(Erd_OverTemperatureMaxInletTemperature))

    Erd_HeaterRelay1 =ERDS[10]
    ERDS_LIST.append(str(Erd_HeaterRelay1))
    
    Erd_HeaterRelay2 =ERDS[11]
    ERDS_LIST.append(str(Erd_HeaterRelay2))

    Erd_MaxTemperatureSlope = ERDS[12]
    ERDS_LIST.append(str(Erd_MaxTemperatureSlope))
 
    Erd_HeatControlParametric = ERDS[13]
    ERDS_LIST.append(str(Erd_HeatControlParametric))

    Erd_MinimumFilteredVoltageFromMc = ERDS[14]
    ERDS_LIST.append(str(Erd_MinimumFilteredVoltageFromMc))

    Erd_FilteredMoistureSensor = ERDS[15]
    ERDS_LIST.append(str(Erd_FilteredMoistureSensor))
    
    Erd_SmoothMoistureReading = ERDS[16]
    ERDS_LIST.append(str(Erd_SmoothMoistureReading))

    Erd_CalculatedCurvature = ERDS[17]
    ERDS_LIST.append(str(Erd_CalculatedCurvature))

    Erd_CurvatureOccurredCount = ERDS[18]
    ERDS_LIST.append(str(Erd_CurvatureOccurredCount))    

    Erd_TrimmerInhibitRelay1 = ERDS[19]
    Erd_TrimmerInhibitRelay1 = {
        0: "False",
        1: "True"
    }.get(Erd_TrimmerInhibitRelay1)
    ERDS_LIST.append(Erd_TrimmerInhibitRelay1)

    Erd_TrimmerInhibitRelay2 = ERDS[20]
    Erd_TrimmerInhibitRelay2 = {
        0: "False",
        1: "True"
    }.get(Erd_TrimmerInhibitRelay2)
    ERDS_LIST.append(Erd_TrimmerInhibitRelay2)

    Erd_TrimmerBothCoilInhibitRequest = ERDS[21]
    Erd_TrimmerBothCoilInhibitRequest = {
        0: "False",
        1: "True"
    }.get(Erd_TrimmerBothCoilInhibitRequest)
    ERDS_LIST.append(Erd_TrimmerBothCoilInhibitRequest)

    Erd_DrumMotorState = ERDS[22]
    Erd_DrumMotorState = {
        0: "DrumMotorState_Off",
        1: "DrumMotorState_Normal",
        2: "DrumMotorState_Reverse",
        3: "DrumMotorState_Max"       
    }.get(Erd_DrumMotorState)
    ERDS_LIST.append(Erd_DrumMotorState)

    Erd_FallbackHeatControlMethodStatus = ERDS[23]
    Erd_FallbackHeatControlMethodStatus = {
        0: "False",
        1: "True"
    }.get(Erd_FallbackHeatControlMethodStatus)
    ERDS_LIST.append(Erd_FallbackHeatControlMethodStatus)    

    Erd_ApplicationVersion = ERDS[24]
    ERDS_LIST.append(str(Erd_ApplicationVersion))

    Erd_ParametricVersion = ERDS[25]
    ERDS_LIST.append(str(Erd_ParametricVersion))

    Erd_Personality = ERDS[26]
    ERDS_LIST.append(str(Erd_Personality))

    Erd_DrynessOption = ERDS[27]
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

    Erd_VentRestriction = ERDS[28]
    Erd_VentRestriction = {
        0: "VentRestriction_Unknown",
        1: "VentRestriction_Small",
        2: "VentRestriction_Large"
    }.get(Erd_VentRestriction)
    ERDS_LIST.append(Erd_VentRestriction)    

    Erd_LoadSizeByAggregation = ERDS[29]
    Erd_LoadSizeByAggregation = {
        0: "LoadSize_Unknown",
        1: "LoadSize_Small",
        2: "LoadSize_Large"
    }.get(Erd_LoadSizeByAggregation)
    ERDS_LIST.append(Erd_LoadSizeByAggregation) 

    Erd_LoadSizeByContact = ERDS[30]
    Erd_LoadSizeByContact = {
        0: "LoadSize_Unknown",
        1: "LoadSize_Small",
        2: "LoadSize_Large"
    }.get(Erd_LoadSizeByContact)
    ERDS_LIST.append(Erd_LoadSizeByContact) 

    Erd_LoadSizeByTemperature = ERDS[31]
    Erd_LoadSizeByTemperature = {
        0: "LoadSize_Unknown",
        1: "LoadSize_Small",
        2: "LoadSize_Large"
    }.get(Erd_LoadSizeByTemperature)
    ERDS_LIST.append(Erd_LoadSizeByTemperature) 

    Erd_TargetMoistureVoltageHasBeenReached = ERDS[32]
    Erd_TargetMoistureVoltageHasBeenReached = {
        0: "False",
        1: "True"
    }.get(Erd_TargetMoistureVoltageHasBeenReached)
    ERDS_LIST.append(Erd_TargetMoistureVoltageHasBeenReached)
    
    Erd_TargetMoistureVoltage = ERDS[33]
    ERDS_LIST.append(str(Erd_TargetMoistureVoltage))
    
    Erd_TotalDryTimeCalculatorTimeMultiplierX100 = ERDS[34]
    ERDS_LIST.append(str(Erd_TotalDryTimeCalculatorTimeMultiplierX100))

    Erd_TotalDryTimeCalculatorTimeAdderSeconds = ERDS[35]
    ERDS_LIST.append(str(Erd_TotalDryTimeCalculatorTimeAdderSeconds))

    #TODO
    Erd_SensorDryTemperatureMultiplierx100 = ERDS[36]
    ERDS_LIST.append(Erd_SensorDryTemperatureMultiplierx100)

    Erd_TimeToReachTargetVoltageSeconds = ERDS[37]
    ERDS_LIST.append(str(Erd_TimeToReachTargetVoltageSeconds))

    Erd_SensingCycleTotalDryingTimeSeconds = ERDS[38]
    ERDS_LIST.append(str(Erd_SensingCycleTotalDryingTimeSeconds))

    Erd_DrumGroundWatchdogResult = ERDS[9]
    Erd_DrumGroundWatchdogResult = {
        0: "DrumGroundWatchdogResult_Unknown",
        1: "DrumGroundWatchdogResult_NotExpired",
        2: "DrumGroundWatchdogResult_Expired"
    }.get(Erd_DrumGroundWatchdogResult)
    ERDS_LIST.append(Erd_DrumGroundWatchdogResult)


    return ERDS_LIST

print(ERDS_TO_WRITE([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))