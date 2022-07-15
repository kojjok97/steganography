from PIL import Image,ImageTk 

def convert_main_image(self,id,image_label,color_label,number_label):
    colors = {0:'NORMAL',1:'RED', 2:'GREEN', 3:'BLUE',4:'ALPHA',5:'FULL RED',6:'FULL GREEN',7:'FULL BLUE'}
    colors_channel = {'RED':'R','GREEN':'G','BLUE':'B','ALPHA':'A', 'FULL RED':'FULL R', 'FULL GREEN':'FULL G', 'FULL BLUE':'FULL B'}

    number = int(number_label['text'])
    color = color_label['text']
    color_num = None
    for x in colors:
        if colors[x] == color:
            color_num = x

    if id == '+':
        if number == 7:
            number_label.config(text=str(0))
            number = 0
        else:
            number_label.config(text=str(number+1))
            number += 1


        
    elif id == '-':
        if number == 0:
            number_label.config(text=str(7))
            number = 7
        else:
            number_label.config(text=str(number-1))
            number -= 1



    elif id == '++':
        if colors.get(7) == color:
            color_label.config(text='NORMAL')
            color = 'NORMAL'
        else:
        
            color_label.config(text=colors.get(color_num+1))
        
            color = colors.get(color_num+1)


    elif id == '--':
        if colors.get(0) == color:
            color_label.config(text='FULL BLUE')
            color = 'FULL BLUE'
        else:

            color_label.config(text=colors.get(color_num-1))
        
            color = colors.get(color_num-1)

    else : 
        pass
    

    if color == 'NORMAL':

        converted_img = self.img    
    else:
        converted_img =convert_image(number+1,colors_channel[color],self.img)
    

    self.new_img = ImageTk.PhotoImage(converted_img)
    image_label.config(image=self.new_img)

    self.current_img = converted_img 



def convert_image(number,color,img):



    if color in img.mode:
        return plane_bit_converter(number,color,img)
    
    elif 'FULL' in color:
        return full_color_converter(color[5:],img)

    else:
        return Image.new('1',img.size) 

def plane_bit_converter(number,color,img):
    
    new_img = Image.new('1',img.size)
    new_img_data = new_img.load()
    img_data = img.load()

    channel_index = img.mode.index(color)
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            color = img_data[x,y]
            channel = color[channel_index]
            plane = bin(channel)[2:].zfill(8)

            try:
                new_img_data[x,y] = 255*int(plane[abs(number-8)])
            except IndexError:
                pass
    
    return new_img

def full_color_converter(color,img):
    
    
    new_img = Image.new('RGB',img.size)
    new_img_data = new_img.load()
    img_data = img.load() 
    try:
        channel_index = img.mode.index(color)
    except:
        return new_img

    for x in range(img.size[0]):
        for y in range(img.size[1]):
            

            color = img_data[x,y][channel_index]
            new_color = [0,0,0]
            new_color[channel_index] = color


            new_img_data[x,y] = tuple(new_color)

    return new_img






def combine_image(numbers,colors,img):

    images = [convert_image(numbers[i],colors[i],img) for i in range(len(numbers))]
    new_img = Image.new('1',img.size,'#fff')
    new_img_data = new_img.load()
    for i in images:
        i_data = i.load()
        for x in range(img.size[0]):
            for y in range(img.size[1]):
                pixel = i_data[x,y]
                if pixel == 0:
                     new_img_data[x,y] = 0
                    

    print(pixel)


    return new_img
        
def hex_value_to_binary(self):
    temp_buffer = ''
    
    for x in self.file:
        temp_buffer += bin(x)

    self.file = temp_buffer

def make_one_bpp_steganography_image(number,color,img,file):
    self.hex_value_to_binary(self)
    
    img = Image.open('123.png')

    channel = img.mode.index(color[:2])

    file_count = 0 
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            pixel = img.getpixel((x,y))

            bin(pixel[channel])

            file_count += 1 


