from tkinter import * 
import tkinter.ttk as ttk
from image_io import image_io
import tkinter.messagebox as msg
from PIL import Image, ImageTk
from convert_image import convert_image, extract_image
import os
import time
import binascii


def add(color_label,number_label,option_listbox):
    if color_label['text'] == 'NORMAL':
        msg.showwarning('경고', 'NORMAL이미지는 추가할 수 없습니다.')
        return

    if 'FULL' in color_label['text']:
        msg.showwarning('경고', '{}이미지는 추가할 수 없습니다.'.format(color_label['text']))
        return
    
    option_listbox.insert(END,'{}:{}'.format(number_label['text'],color_label['text']))
    
def delete(option_listbox):
    for index in reversed(option_listbox.curselection()):
        option_listbox.delete(index)

def view(self,option_listbox,image_label):
    image_convert_list = option_listbox.get(0,END)
    numbers, colors = [],[]
    for image_convert in image_convert_list:
        number, color = image_convert.split(':')
        numbers.append(int(number)+1)
        colors.append(color[:1])
    
    
    self.current_img = convert_image.combine_image(numbers,colors,self.img)
    self.new_img = ImageTk.PhotoImage(self.current_img)
    image_label.config(image=self.new_img)



def reset(self,color_label,number_label,option_listbox,image_label):
    color_label['text'] = 'NORMAL'
    number_label['text'] = 0

    
    option_listbox.delete(0,END)
    
    self.new_img = ImageTk.PhotoImage(self.img)
    image_label.config(image=self.new_img)

def two_bpp_extract_window(img):

    two_bpp_extract_window = Toplevel()
    two_bpp_extract_window.geometry('600x300')
    two_bpp_extract_window.title('2BPP LSB Steganography')

    rgb_list = ['Red','Green','Blue']
    plane_bit_list = [x for x in range(1,9)]


    bottom_frame = Frame(two_bpp_extract_window)
    bottom_frame.pack(side='top',fill='x')

    first_bit_plane_frame = LabelFrame(bottom_frame, text='First Planes')
    first_bit_plane_frame.pack(side='left',padx=10,pady=10,expand=True)


    first_bit_first_rgb_combobox = ttk.Combobox(first_bit_plane_frame, height=3, values=rgb_list, state='readonly')
    first_bit_first_rgb_combobox.current(0) 
    first_bit_first_rgb_combobox.pack()

    first_bit_first_plane_combobox = ttk.Combobox(first_bit_plane_frame, height=8, values=plane_bit_list, state='readonly')
    first_bit_first_plane_combobox.current(0)
    first_bit_first_plane_combobox.pack()

    first_bit_second_rgb_combobox = ttk.Combobox(first_bit_plane_frame, height=3, values=rgb_list, state='readonly')
    first_bit_second_rgb_combobox.current(0) 
    first_bit_second_rgb_combobox.pack()

    first_bit_second_plane_combobox = ttk.Combobox(first_bit_plane_frame, height=8, values=plane_bit_list, state='readonly')
    first_bit_second_plane_combobox.current(0)
    first_bit_second_plane_combobox.pack()


    second_bit_plane_frame = LabelFrame(bottom_frame, text='Second Planes')
    second_bit_plane_frame.pack(side='right',padx=10,pady=10,expand=True)

    second_bit_first_rgb_combobox = ttk.Combobox(second_bit_plane_frame, height=3, values=rgb_list, state='readonly')
    second_bit_first_rgb_combobox.current(0) 
    second_bit_first_rgb_combobox.pack()

    second_bit_first_plane_combobox = ttk.Combobox(second_bit_plane_frame, height=8, values=plane_bit_list, state='readonly')
    second_bit_first_plane_combobox.current(0)
    second_bit_first_plane_combobox.pack()

    second_bit_second_rgb_combobox = ttk.Combobox(second_bit_plane_frame, height=3, values=rgb_list, state='readonly')
    second_bit_second_rgb_combobox.current(0) 
    second_bit_second_rgb_combobox.pack()

    second_bit_second_plane_combobox = ttk.Combobox(second_bit_plane_frame, height=8, values=plane_bit_list, state='readonly')
    second_bit_second_plane_combobox.current(0)
    second_bit_second_plane_combobox.pack()


    order_setting_frame = LabelFrame(bottom_frame,text='order_setting')
    order_setting_frame.pack(side='right',padx=10,pady=10,expand=True)

    extract_by_label = Label(order_setting_frame, text='Extract by')
    row_column_var = StringVar()
    row_radio = Radiobutton(order_setting_frame, text='Row', value='ROW', variable=row_column_var)
    row_radio.select()
    column_radio = Radiobutton(order_setting_frame, text='Column', value='COLUMN', variable=row_column_var)

    extract_by_label.grid(row=0, column=0)
    row_radio.grid(row=0, column=1)
    column_radio.grid(row=0, column=2)


    btn_frame = Frame(two_bpp_extract_window)
    btn_frame.pack(side='bottom',fill='x',padx=5,pady=5,expand=True)
    

    save_text_btn = Button(btn_frame, width=10, height=1, text='Save Text', command=lambda : image_io.save_text_two_bpp(row_column_var.get(),[first_bit_first_rgb_combobox.get(),
                                                                                                                       first_bit_second_rgb_combobox.get(),
                                                                                                                       second_bit_first_rgb_combobox.get(),
                                                                                                                       second_bit_second_rgb_combobox.get()],
                                                                                                                      [[first_bit_first_plane_combobox.get(),
                                                                                                                       first_bit_second_plane_combobox.get()],
                                                                                                                       [second_bit_first_plane_combobox.get(),
                                                                                                                       second_bit_second_plane_combobox.get()]],img))


    
    save_text_btn.grid(row= 5, column= 2, padx=5, pady=5, sticky=N+E+W+S)

    two_bpp_extract_window.mainloop()



def one_bpp_extract_window(img):

    one_bpp_extract_window = Toplevel()
    one_bpp_extract_window.geometry('450x300')
    one_bpp_extract_window.title('1BPP LSB Steganography')
    rgb_list = ['Red','Green','Blue']
    plane_bit_list = [x for x in range(1,9)]


    bottom_frame = Frame(one_bpp_extract_window)
    bottom_frame.pack(side='top',fill='x')

    bit_plane_frame = LabelFrame(bottom_frame, text='Planes')
    bit_plane_frame.pack(side='left',padx=10,pady=10,expand=True)


    rgb_combobox = ttk.Combobox(bit_plane_frame, height=3, values=rgb_list, state='readonly')
    rgb_combobox.current(0) 
    rgb_combobox.pack()

    plane_combobox = ttk.Combobox(bit_plane_frame, height=8, values=plane_bit_list, state='readonly')
    plane_combobox.current(0)
    plane_combobox.pack()


    order_setting_frame = LabelFrame(bottom_frame,text='order_setting')
    order_setting_frame.pack(side='right',padx=10,pady=10,expand=True)

    extract_by_label = Label(order_setting_frame, text='Extract by')
    row_column_var = StringVar()
    row_radio = Radiobutton(order_setting_frame, text='Row', value='ROW', variable=row_column_var)
    row_radio.select()
    column_radio = Radiobutton(order_setting_frame, text='Column', value='COLUMN', variable=row_column_var)

    extract_by_label.grid(row=0, column=0)
    row_radio.grid(row=0, column=1)
    column_radio.grid(row=0, column=2)


    btn_frame = Frame(one_bpp_extract_window)
    btn_frame.pack(side='bottom',fill='x',padx=5,pady=5,expand=True)
    

    save_text_btn = Button(btn_frame, width=10, height=1, text='Save Text',command=lambda : image_io.save_text_one_bpp(row_column_var.get(),rgb_combobox.get(),plane_combobox.get(),img))

    
    save_text_btn.grid(row= 5, column= 2, padx=5, pady=5, sticky=N+E+W+S)

    one_bpp_extract_window.mainloop()     
   



def main():
    
    img_file_name = './img.png'
    img_save_obj = type('Img',(object,),dict(img=Image.new('RGBA',(680,400),color='#fff'),current_img=None,open_image=image_io.open_image,save_image=image_io.save_image,convert_main_image=convert_image.convert_main_image,add=add,delete=delete,view=view,reset=reset))
    img_save_obj.img.save('./img.png','png')


    
    
    img_save_obj.current_img = img_save_obj.img

    root = Tk() 
    root.title('Stegarnography')
    root.geometry('640x480')

    image_view= PhotoImage(file=img_file_name) 
    os.remove('./img.png')
    image_label = Label(root, image=image_view)
    image_label.pack(fill='both')

    # 1~7 선택 버튼 
    number_frame = Frame(root)
    number_frame.pack(side='right', padx=5, pady=5)

    number_label = Label(number_frame,height=1,text='0',width=3)
    number_label.grid(row=1,column=0)

    color_frame = Frame(root)
    color_frame.pack(side='right', padx=5, pady=5)

    color_label = Label(color_frame,height=1,text='NORMAL', width=12)
    color_label.grid(row=1,column=0)

    up_image = PhotoImage(file='./ui/upButton.png')
    down_image = PhotoImage(file='./ui/downButton.png')
    number_up = Button(number_frame, image=up_image, text='',width=40, height=10, command=lambda:img_save_obj.convert_main_image(img_save_obj,'+',image_label,color_label,number_label))
    number_up.grid(row=0,column=0, padx=1,pady=1)

    number_down = Button(number_frame, image=down_image, text='',width=40, height=10,command=lambda:img_save_obj.convert_main_image(img_save_obj,'-',image_label,color_label,number_label))
    number_down.grid(row=2,column=0, padx=1, pady=1)

    # 색 선택 버튼


    color_up_image = PhotoImage(file='./ui/colorUp.png')
    color_down_image = PhotoImage(file='./ui/colorDown.png')
    color_up = Button(color_frame, image=color_up_image, text='',width=104, height=10,command=lambda:img_save_obj.convert_main_image(img_save_obj,'++',image_label,color_label,number_label))
    color_up.grid(row=0,column=0, padx=1,pady=1)

    color_up = Button(color_frame, image=color_down_image, text='',width=104, height=10,command=lambda:img_save_obj.convert_main_image(img_save_obj,'--',image_label,color_label,number_label))
    color_up.grid(row=2,column=0, padx=1, pady=1)




    # 선택된 옵션 확인 

    option_listbox_frame = Frame(root)
    option_listbox_frame.pack(side='left', padx=5, pady=1)

    option_listbox_scroll = Scrollbar(option_listbox_frame) 
    option_listbox_scroll.pack(side='right',fill='y')
    option_listbox = Listbox(option_listbox_frame,selectmode='extended',width=40 ,height=3, yscrollcommand=option_listbox_scroll.set)
    option_listbox.pack(side='left',fill='both',expand=True)


    # 버튼 프레임
    btn_frame = Frame(root)
    btn_frame.pack(side='right', padx=5, pady=5)

    add_btn = Button(btn_frame, text='add',width=8,height=1,command=lambda : img_save_obj.add(color_label,number_label,option_listbox))
    add_btn.grid(row=0,column=0,padx=2,pady=2,sticky=N+E+W+S)

    del_btn = Button(btn_frame, text='del',width=8,height=1, command=lambda : img_save_obj.delete(option_listbox))
    del_btn.grid(row=0,column=1,padx=2,pady=2,sticky=N+E+W+S)

    view_btn = Button(btn_frame, text='view',width=8,height=1, command=lambda : img_save_obj.view(img_save_obj,option_listbox,image_label))
    view_btn.grid(row=1,column=0,padx=2,pady=2,sticky=N+E+W+S)

    reset_btn = Button(btn_frame, text='reset',width=8,height=1, command=lambda : img_save_obj.reset(img_save_obj,color_label,number_label,option_listbox,image_label))
    reset_btn.grid(row=1,column=1,padx=2,pady=2,sticky=N+E+W+S)



    menu = Menu(root)
    menu_file = Menu(menu, tearoff=0)
    menu_file.add_command(label='Open File',command=lambda :img_save_obj.open_image(img_save_obj,root,image_label,color_label,number_label,option_listbox))
    menu_file.add_command(label='Save File',command=lambda : img_save_obj.save_iamge(img_save_obj))
    menu_file.add_separator()
    menu_file.add_command(label='Exit', command=root.quit)

    menu_analyse = Menu(menu, tearoff=0)
    menu_analyse.add_command(label='2bpp Steganography',command=lambda : two_bpp_extract_window(img_save_obj.img))
    menu_analyse.add_command(label='1bpp Steganography',command=lambda : one_bpp_extract_window(img_save_obj.img))


    menu.add_cascade(label='File', menu= menu_file)
    menu.add_cascade(label='Analyse', menu= menu_analyse)


    root.config(menu=menu)
    root.mainloop()
    

if __name__=="__main__":
    main() 