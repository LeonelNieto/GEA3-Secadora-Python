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
        "0": "EStarOption_Disabled",
        "1": "EStarOption_Enabled",
        "2": "EStarOption_Max",
        "255": "EStarOption_DontCare"
    }.get(Erd_EStarSensorDryRequested)
    ERDS_LIST.append(Erd_EStarSensorDryRequested)

    Erd_RamCycleHistoryRecord_drynessOptionAtStart = ERDS[3]
    Erd_RamCycleHistoryRecord_drynessOptionAtStart = {
        "0": "DrynessOption_Disabled",
        "1": "DrynessOption_Minimum",
        "2": "DrynessOption_LessDry",
        "3": "DrynessOption_Dry",
        "4": "DrynessOption_MoreDry",
        "5": "DrynessOption_ExtraDry",
        "6": "DrynessOption_Max",
        "255": "DrynessOption_DontCare"
    }.get(Erd_RamCycleHistoryRecord_drynessOptionAtStart)
    ERDS_LIST.append(Erd_RamCycleHistoryRecord_drynessOptionAtStart)

    Erd_RamCycleHistoryRecord_drynessOptionAtEnd = ERDS[4]
    Erd_RamCycleHistoryRecord_drynessOptionAtEnd = {
        "0": "DrynessOption_Disabled",
        "1": "DrynessOption_Minimum",
        "2": "DrynessOption_LessDry",
        "3": "DrynessOption_Dry",
        "4": "DrynessOption_MoreDry",
        "5": "DrynessOption_ExtraDry",
        "6": "DrynessOption_Max",
        "255": "DrynessOption_DontCare"
    }.get(Erd_RamCycleHistoryRecord_drynessOptionAtEnd)
    ERDS_LIST.append(Erd_RamCycleHistoryRecord_drynessOptionAtEnd)

    Erd_RamCycleHistoryRecord_temperatureOptionAtStart = ERDS[5]
    Erd_RamCycleHistoryRecord_temperatureOptionAtStart = {
        "0": "TemperatureOption_Disabled",
        "1": "TemperatureOption_NoHeat",
        "2": "TemperatureOption_ExtraLow",
        "3": "TemperatureOption_Low",
        "4": "TemperatureOption_Medium",
        "5": "TemperatureOption_High",
        "6": "TemperatureOption_Max",
        "255": "TemperatureOption_DontCare"   
    }.get(Erd_RamCycleHistoryRecord_temperatureOptionAtStart)
    ERDS_LIST.append(Erd_RamCycleHistoryRecord_temperatureOptionAtStart)

    Erd_RamCycleHistoryRecord_temperatureOptionAtEnd = ERDS[6]
    Erd_RamCycleHistoryRecord_temperatureOptionAtEnd = {
        "0": "TemperatureOption_Disabled",
        "1": "TemperatureOption_NoHeat",
        "2": "TemperatureOption_ExtraLow",
        "3": "TemperatureOption_Low",
        "4": "TemperatureOption_Medium",
        "5": "TemperatureOption_High",
        "6": "TemperatureOption_Max",
        "255": "TemperatureOption_DontCare"       
    }.get(Erd_RamCycleHistoryRecord_temperatureOptionAtEnd)
    ERDS_LIST.append(Erd_RamCycleHistoryRecord_temperatureOptionAtEnd)

    Erd_CurrentInletTemperature = ERDS[6]
    ERDS_LIST.append(Erd_CurrentInletTemperature)

    

    return ERDS_LIST