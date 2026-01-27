import customtkinter as ctk
import tkinter
import main_app as cv
import os

#variables
total_converted = 0
failed_converted = 0 
#functions
def buttonsp_event():
    os.system("start https://discord.com/invite/Bz5C2Gt6rZ")
def button1_event():
    global total_converted
    global failed_converted
    #print(op_value.get())
    #print(total_converted)


    converted = cv.converter(op_menu.get(),entry_filename.get(),entry_filename2.get())
    if converted:
        total_converted += 1
        if total_converted == 1:
            converted_label.pack(pady=10)
        converted_label.configure(text=f"({total_converted}x) Converted!!!",text_color="green")
    else:
        failed_converted += 1
        if failed_converted == 1:
            converted_label.pack(pady=10)
        converted_label.configure(text=f"({failed_converted}x) Failed to convert\nCheck logs!",text_color="red")
#apearence
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("_internal/themes/midnight.json")


#app object
app = ctk.CTk()
app.geometry("640x480")
app.title("Image Converter - By NoNameiqz")
app.iconbitmap("_internal/icon.ico")

#frame and widgets

#main frames
left_frame = ctk.CTkFrame(app,width=400,fg_color="transparent")
left_frame.pack(side="left",fill="y")
right_frame = ctk.CTkFrame(app,width=240,fg_color="transparent")
right_frame.pack(side="right",fill="y")


#left frame1
frame1 = ctk.CTkFrame(left_frame,width=350,height=220)
frame1.pack(side="top",padx=20,pady=10)
frame1.pack_propagate(False)
one_entry_text = ctk.CTkLabel(frame1,text="Single File Conversion",font=("Inter",18,"bold"))
one_entry_text.pack(pady=(15,10))
entry_text = ctk.CTkLabel(frame1, text="Input Path:",width=100,font=("Inter",14))
entry_text.pack(padx=10)
entry_filename = ctk.CTkEntry(frame1, placeholder_text="example: resources/image.svg",width=200)
entry_filename.pack(pady=(0,25),padx=40) 

entry_text2 = ctk.CTkLabel(frame1, text="Output Path (optional):",width=100,font=("Inter",14))
entry_text2.pack(padx=10)
entry_filename2 = ctk.CTkEntry(frame1, placeholder_text="example: image1 (without .png)",width=200)
entry_filename2.pack(padx=40) 

#left frame2
frame2 = ctk.CTkFrame(left_frame,width=350,height=220)
frame2.pack(side="top",padx=20,pady=10)
frame2.pack_propagate(False)
label_dev = ctk.CTkLabel(frame2,text="In development...",font=("Inter",18,"bold"))
label_dev.pack(pady=50)


#right frame
frame3 = ctk.CTkFrame(right_frame,width=200,height=300)
frame3.pack(pady=(70,0),padx=15)
frame3.pack_propagate(False)
op_values = ["png","jpg","webp","gif","tiff","bmp","pdf","svg","ico"]
op_value = ctk.StringVar(value="png")
label_op = ctk.CTkLabel(frame3,text="Output format:",font=("Inter",14))
label_op.pack(pady=(60,0))
op_menu = ctk.CTkOptionMenu(frame3,values=op_values,variable=op_value)
op_menu.pack(pady=(0,100))
button1 = ctk.CTkButton(frame3,text="Convert!",command=button1_event)
button1.pack()
converted_label = ctk.CTkLabel(frame3,font=("Inter",14,"bold"))

#support/credits
support_button = ctk.CTkButton(right_frame,text="Support/Updates",fg_color="blue",hover_color="#000d61",command=buttonsp_event)
support_button.pack(pady=(30,0))

#app main loop
app.mainloop()
