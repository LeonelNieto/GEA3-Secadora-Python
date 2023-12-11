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
    frame_filtered = separate_by_pair(data_frame)
    frame_to_calculate_crc = frame_filtered[2:-6]
    crc_calculated = crc16_ccitt(frame_to_calculate_crc).upper()
    crc_frame_read = data_frame[-6:-2]
    
    return crc_calculated == crc_frame_read

def separate_by_pair(frame_raw):
    """Separate by pairs to filter the data without E0

    Args:
        frame_raw (_str_): raw data of the erd read.

    Returns:
        _str_: data frame filtered without E0
    """
    crc_and_bitStop = frame_raw[-6:]
    frame_without_crc_and_bitStop = frame_raw[:-6]
    len_frame = len(frame_without_crc_and_bitStop)
    LEFT_SIDE = 0
    RIGHT_SIDE = 2
    filtered_data = ""
    
    while RIGHT_SIDE <= len_frame:
        data_in_pairs = frame_without_crc_and_bitStop[LEFT_SIDE:RIGHT_SIDE]
        LEFT_SIDE += 2
        RIGHT_SIDE += 2
        if data_in_pairs != "E0":
            filtered_data += data_in_pairs
    
    return filtered_data + crc_and_bitStop