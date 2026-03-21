import customtkinter as ctk
import converter as cv
import os
from datetime import datetime
from tkinter import filedialog
from pathlib import Path
#variables
total_converted = 0
failed_converted = 0 
files = ()
#functions
def writeLogs(name: str, logs : str, op : bool):
    with open("logs.txt", "a", encoding="utf-8") as f:
            date = datetime.now()
            date = date.strftime("%d/%m/%Y %H:%M:%S")
            if op:
                f.write(f"{date} - Status: converted to {name} with filename ({logs})\n")
            else:
                f.write(f"{date} - Status: [ERROR] - failed to convert filename ({name}) with error: {logs}\n")

def browse_single_files():
    path = filedialog.askopenfilename(title="Choose an image",filetypes=[("Image files", "*.png *.jpg *.webp *.gif *.tiff *.bmp *.pdf *.svg *.ico")])
    if path:
        # wprint(path)
        entry_filename.delete(0,ctk.END)
        entry_filename.insert(0,path)

def browse_multi_files():
    global files
    files = filedialog.askopenfilenames(title="Choose an image",filetypes=[("Image files", "*.png *.jpg *.webp *.gif *.tiff *.bmp *.pdf *.svg *.ico")])
    multifiles_label.configure(text=f"{len(files)} Files selected")

def buttonsp_event():
    os.system("start https://discord.com/invite/Bz5C2Gt6rZ")

def button1_event():
    global total_converted
    global failed_converted
    #print(op_value.get())
    #print(total_converted)
    if entry_filename2.get() == "":
        output = Path(entry_filename.get()).stem
    else:
        output = entry_filename2.get()
    converted,logs = cv.converter(op_menu.get(),entry_filename.get(),output)
    if converted:
        total_converted += 1
        if total_converted == 1:
            converted_label.pack(pady=10)
        converted_label.configure(text=f"({total_converted}x) Converted!!!",text_color="green")
        writeLogs(op_menu.get(),logs,True)
    else:
        failed_converted += 1
        if failed_converted == 1:
            converted_label.pack(pady=10)
        converted_label.configure(text=f"({failed_converted}x) Failed to convert\nCheck logs!",text_color="red")
        writeLogs(entry_filename.get(),logs,False)

def button2_event():
    global total_converted
    global failed_converted
    temp_total = total_converted
    temp_failed = failed_converted
    global files
    if len(files) == 0:
        failed_converted += 1
        converted_label.pack(pady=10)
        converted_label.configure(text=f"({failed_converted}x) Failed to convert\nCheck logs!",text_color="red")
        writeLogs("","No file selected",False)
    else:
        for file in files:
            output = Path(file).stem
            converted,logs = cv.converter(op_menu.get(),file,output)
            if converted:
                total_converted += 1
                writeLogs(op_menu.get(),logs,True)
            else:
                failed_converted += 1
                writeLogs(output,logs,False)
        if temp_failed == failed_converted:
            converted_label.pack(pady=10)
            converted_label.configure(text=f"({total_converted}x) Converted!!!",text_color="green")
        elif temp_failed < failed_converted:
            converted_label.pack(pady=10)
            converted_label.configure(text=f"(Converted({total_converted-temp_total}x) - {failed_converted-temp_failed}x) Failed\nCheck logs!",text_color="red")



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
one_entry_text.pack(pady=(15,6))
entry_text = ctk.CTkLabel(frame1, text="Input Path:",width=100,font=("Inter",14))
entry_text.pack(padx=10)
entry_filename = ctk.CTkEntry(frame1, placeholder_text="example: resources/image.svg",width=200)
entry_filename.pack(pady=(0,5),padx=40) 
browse_button = ctk.CTkButton(frame1, text="Browse files",command=browse_single_files)
browse_button.pack(padx=10,pady=(0,10))

entry_text2 = ctk.CTkLabel(frame1, text="Output file name (optional):",width=100,font=("Inter",14))
entry_text2.pack(padx=10)
entry_filename2 = ctk.CTkEntry(frame1, placeholder_text="example: image1 (without .png)",width=200)
entry_filename2.pack(padx=40) 

#left frame2
frame2 = ctk.CTkFrame(left_frame,width=350,height=220)
frame2.pack(side="top",padx=20,pady=10)
frame2.pack_propagate(False)
#label_dev = ctk.CTkLabel(frame2,text="In development...",font=("Inter",18,"bold"))
#label_dev.pack(pady=50)
label_multi = ctk.CTkLabel(frame2,text="Multi File Conversion",font=("Inter",18,"bold"))
label_multi.pack(pady=(20,0))
multifiles_label = ctk.CTkLabel(frame2,text="0 Files selected", font=("Inter",15))
multifiles_label.pack(pady=(30,14))
brwose_button_2 = ctk.CTkButton(frame2,text="Browse files", command=browse_multi_files)
brwose_button_2.pack()

#right frame
frame3 = ctk.CTkFrame(right_frame,width=200,height=300)
frame3.pack(pady=(70,0),padx=15)
frame3.pack_propagate(False)
op_values = ["png","jpg","webp","gif","tiff","bmp","pdf","svg","ico"]
op_value = ctk.StringVar(value="png")
label_op = ctk.CTkLabel(frame3,text="Output format:",font=("Inter",14))
label_op.pack(pady=(60,0))
op_menu = ctk.CTkOptionMenu(frame3,values=op_values,variable=op_value)
op_menu.pack(pady=(0,50))
button1 = ctk.CTkButton(frame3,text="Convert Single!",command=button1_event)
button1.pack()
button2 = ctk.CTkButton(frame3,text="Convert Multi!",command=button2_event)
button2.pack(pady=(10,0))
converted_label = ctk.CTkLabel(frame3,font=("Inter",14,"bold"))

#support/credits
support_button = ctk.CTkButton(right_frame,text="Support/Updates",fg_color="blue",hover_color="#000d61",command=buttonsp_event)
support_button.pack(pady=(30,0))

#app main loop
app.mainloop()
