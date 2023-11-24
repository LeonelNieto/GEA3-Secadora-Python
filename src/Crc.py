def crc16_ccitt(data_hex):
    data = bytearray.fromhex(data_hex)                                   
    poly = 0x1021                                                          
    crc = 0x1021                                                           
    for byte in data:
        for i in range(8):
            bit = (byte >> (7-i) & 1) == 1
            c15 = (crc >> 15 & 1) == 1
            crc <<= 1
            if c15 ^ bit:
                crc ^= poly
    crc &= 0xffff
    crcStr = "{:04x}".format(crc)
    
    return crcStr

def Is_Crc_Correct(data_frame):
    frame_to_calculate_crc = data_frame[2:-6]
    crc_calculated = crc16_ccitt(frame_to_calculate_crc).upper()
    crc_frame_read = data_frame[-6:-2]

    return crc_calculated == crc_frame_read