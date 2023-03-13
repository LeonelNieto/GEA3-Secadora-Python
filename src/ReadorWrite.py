import Crc

def ReadErd(ERD, dst):
    bitInit = "E2"                                                                                      
    src = "E4"                                                                                          
    cmd = "A000"                                                                                        
    bitStop = "E3"                                                                                      
    longitud = int(((len(bitInit + dst + src + cmd + ERD + bitStop)) + 6) / 2)                          
    lenght = "{:02x}".format(longitud)                                                                  
    FrameToCalculateCrc = dst + lenght + src + cmd + ERD                                                
    crc = Crc.crc16_ccitt(FrameToCalculateCrc)                                                                                                                                            # Elimina "0x" del CRC
    frame = bitInit + FrameToCalculateCrc + crc + bitStop                                               
    data = bytes.fromhex(frame)                                                                         
    return data                                                                                         

def WriteErd(ERD, dato, dst):
    bitInit = "E2"                                                                                      
    src = "E4"                                                                                          
    cmd = "A200"                                                                                        
    ERD_Data_Size = int((len(dato)) / 2)                                                                
    ERD_Data_Size = "{:02x}".format(ERD_Data_Size)                                                      
    ESC = "E0"                                                                                          
    bitStop = "E3"                                                                                      
    longitud = int(((len(bitInit + dst + src + cmd + ERD + ERD_Data_Size + dato + bitStop)) + 6) / 2)  
    lenght = "{:02x}".format(longitud)                                                                  
    FrameToCalculateCrc = dst + lenght + src + cmd + ERD + ERD_Data_Size + dato                         
    crc = Crc.crc16_ccitt(FrameToCalculateCrc)                                                                                                                                
    if ERD != "0032":                                                                                   
        frame = bitInit + FrameToCalculateCrc + crc + bitStop                                           
    else:                                                                                               
        frame = bitInit + FrameToCalculateCrc + ESC + crc + bitStop                                     
    dataWrite = bytearray.fromhex(frame)                                                                
    return dataWrite                                                                                      

def Boatloader(dst, cmd, msg):
    bitInit = "E2"                                                                                  
    src = "E4"                                                                                       
    bitStop = "E3"                                                                                   
    longitud = int(((len(bitInit + dst + src + cmd + msg + bitStop)) + 6) / 2)                          
    lenght = "{:02x}".format(longitud)                                                               
    FrameToCalculateCrc = dst + lenght + src + cmd + msg                                              
    crc = Crc.crc16_ccitt(FrameToCalculateCrc)                                                         
    frame = bitInit + FrameToCalculateCrc + crc + bitStop                                              
    data = bytes.fromhex(frame)                                                                        
    return data                                                                                         

