from PIL import Image 

def two_bpp_extract(numbers,colors,row_column,img):
    solve_data_hex = ''
    img_data = img.load()

    channel_indexes = [img.mode.index(c[:1]) for c in colors]


    if row_column == 'ROW':
        width,height = img.size
    else:
        height,width = img.size

    new_data_hex = ''
    for x in range(width):
        
        for y in range(height): 
            if row_column == 'ROW':
                pixel = img_data[x,y]
            else :
                pixel = img_data[y,x]
            
            plane_first = None
            plane_second = None


            channel = [pixel[channel_indexes[v]] for v in range(4)]

            plane_first = int((bin(channel[0])[2:].zfill(8))[abs(int(numbers[0][0])-8)]) ^ int((bin(channel[1])[2:].zfill(8))[abs(int(numbers[0][1])-8)])
            plane_second = int((bin(channel[2])[2:].zfill(8))[abs(int(numbers[1][0])-8)]) ^ int((bin(channel[3])[2:].zfill(8))[abs(int(numbers[1][1])-8)])

    
                
            new_data_hex += str(plane_first) + str(plane_second) 
            
            
            if len(new_data_hex) == 8:

                solve_data_hex += hex(int(new_data_hex,2))[2:].zfill(2)
                


                new_data_hex = ''
    
    
    return solve_data_hex
                        

def one_bpp_extract(row_column,rgb,plane,img):
    solve_data_hex = ''
    img_data = img.load()
    channel_index = img.mode.index(rgb[:1])

    
    if row_column == 'ROW':
        width,height = img.size
    else :
        height,width = img.size
    new_hex_data = ''
    for x in range(width):
        for y in range(height): 
            if row_column == 'ROW':
                pixel = img_data[x,y]
            else:
                pixel = img_data[y,x]

            plane_bit = pixel[channel_index]

            bin_pixel = bin(plane_bit)[2:].zfill(8)
            new_hex_data +=bin_pixel[abs(int(plane)-8)]

            if len(new_hex_data) == 8:

                
                solve_data_hex += hex(int(bin_pixel,2))[2:].zfill(2)
                new_hex_data = ''

    


    return solve_data_hex
