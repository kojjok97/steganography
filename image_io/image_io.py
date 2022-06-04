from tkinter import * 
from tkinter import filedialog
from convert_image import extract_image
from PIL import Image, ImageTk 
import binascii


def open_image(self,root,image_label,color_label,number_label,option_listbox):
    
    file = filedialog.askopenfilename(title='이미지 파일을 선택하세요', filetypes=(('모든 파일', '*.*'),('png','*.png'),('jpeg','*.jpg')), initialdir='./')

#    try :
#        img_file_name = PhotoImage(file=file)
#        img.config(image=img_file_name)
#    except :
#        msg.showwarning('파일 포멧 에러', '이미지 파일을 선택해주세요')
#        return 

    self.img = Image.open(file)

    self.current_img = self.img
    width, height = self.img.size

    if width < 640:
        width = 640
    
    if height < 440:
        height = 400
    
    height += 80

    root.geometry(f'{str(width)}x{str(height)}')
    
    self.new_img= ImageTk.PhotoImage(self.img)
    image_label.config(image=self.new_img)
    color_label['text'] = 'NORMAL'
    number_label['text'] = 0
    option_listbox.delete(0,END)

            


def save_image(self):
    file = filedialog.asksaveasfilename(title='저장할 디렉토리를 선택하세요', filetypes=(('png','*.png*'),('모든 파일','*.*')), initialdir='./')
    self.current_img.save(file)

    
def save_text_two_bpp(row_column,rgb_list,plane_list,img):
    file = filedialog.asksaveasfilename(title='저장할 디렉토리를 선택하세요', filetypes=(('txt','*.txt*'),('png','*.png*'),('jpeg','*.jpg*'),('모든 파일','*.*')), initialdir='./')
    hex_data= extract_image.two_bpp_extract(plane_list,rgb_list,row_column,img)
    with open(file,'wb') as f:
        f.write(binascii.unhexlify(hex_data))

def save_text_one_bpp(row_column,rgb,plane,img):
    file= filedialog.asksaveasfilename(title='저장할 디렉토리를 선택하세요', filetypes=(('txt','*.txt*'),('png','*.png*'),('jpeg','*.jpg*'),('모든 파일','*.*')), initialdir='./')
    hex_data = extract_image.one_bpp_extract(row_column,rgb,plane,img)
    with open(file,'wb') as f:
        f.write(binascii.unhexlify(hex_data))