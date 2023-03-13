def longitudERD(ERD):
    numeroCaracteres = len(ERD)                
    return {                                           
        1 : "000" + ERD,                               
        2 :  "00" + ERD,                               
        3 :   "0" + ERD,                               
        4:          ERD                                
    }.get(numeroCaracteres, "Fallo")                   
