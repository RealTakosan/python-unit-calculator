from tkinter import *
import ctypes
import base64

icon64 = "AAABAAEAICAAAAEAIACoEAAAFgAAACgAAAAgAAAAQAAAAAEAIAAAAAAAABAAAMMOAADDDgAAAAAAAAAAAAAUFBT/FBQU/xQUFP8UFBT/EhIS/zAwMP/j4+P//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////xQUFP8UFBT/FBQU/xQUFP8SEhL/LS0t/8rKyv/o6Oj//Pz8//////////////////////////////////////////////////////////////////z8/P/m5ub/4+Pj/+Pj4//j4+P/4+Pj/+Pj4//j4+P/5ubm//z8/P//////EhIS/xISEv8UFBT/FBQU/xQUFP8XFxf/Kysr/0lJSf/m5ub/////////////////////////////////////////////////////////////////5ubm/0lJSf8uLi7/Ly8v/y8vL/8vLy//Ly8v/y4uLv9JSUn/5ubm//////8wMDD/LS0t/xcXF/8UFBT/FBQU/xQUFP8RERH/Kysr/8rKyv/o6Oj//Pz8///////////////////////////////////////////////////////i4uL/Li4u/xQUFP8sLCz/Ly8v/y8vL/8sLCz/FBQU/y4uLv/j4+P//////+Xl5f/Kysr/Kysr/xEREf8UFBT/FBQU/xQUFP8XFxf/Kysr/0lJSf/m5ub//////////////////////////////////////////////////////+Pj4/8vLy//Kysr/8rKyv/l5eX/5eXl/8rKyv8rKyv/Ly8v/+Pj4////////////+bm5v9JSUn/Kysr/xcXF/8UFBT/FBQU/xQUFP8RERH/Kysr/8rKyv/o6Oj//Pz8////////////////////////////////////////////4+Pj/y8vL/8vLy//4+Pj////////////4+Pj/y8vL/8vLy//4+Pj/////////////Pz8/+jo6P/Kysr/Kysr/xEREf8UFBT/FBQU/xQUFP8XFxf/Kysr/0lJSf/m5ub////////////////////////////////////////////j4+P/Ly8v/y8vL//j4+P////////////j4+P/Ly8v/y8vL//j4+P//////////////////////+bm5v9JSUn/Kysr/xcXF/8UFBT/FBQU/xQUFP8RERH/Kysr/8rKyv/o6Oj//Pz8/////////////////////////////////+Pj4/8vLy//Ly8v/+Pj4////////////+Pj4/8vLy//Ly8v/+Pj4////////////////////////Pz8/+jo6P/Kysr/Kysr/xEREf8UFBT/FBQU/xQUFP8XFxf/Kysr/0lJSf/m5ub/////////////////////////////////4+Pj/y8vL/8vLy//4+Pj////////////4+Pj/y8vL/8vLy//4+Pj/////////////////////////////////+bm5v9JSUn/Kysr/xcXF/8UFBT/FBQU/xQUFP8RERH/Kysr/8rKyv/o6Oj//Pz8///////////////////////j4+P/Ly8v/y8vL//j4+P////////////j4+P/Ly8v/y8vL//j4+P//////////////////////////////////Pz8/+jo6P/Kysr/Kysr/xEREf8UFBT/FBQU/xQUFP8XFxf/Kysr/0lJSf/m5ub//////////////////////+Li4v8tLS3/LS0t/+Li4v///////////+Li4v8tLS3/LS0t/+Pj4////////////////////////////////////////////+bm5v9JSUn/Kysr/xcXF/8UFBT/FBQU/xQUFP8RERH/Kysr/8rKyv/o6Oj//Pz8////////////5ubm/0dHR/9HR0f/5ubm////////////5ubm/0dHR/9HR0f/5ubm/////////////////////////////////////////////Pz8/+jo6P/Kysr/Kysr/xEREf8UFBT/FBQU/xQUFP8XFxf/Kysr/0lJSf/m5ub////////////8/Pz/5ubm/+bm5v/8/Pz////////////8/Pz/5ubm/+bm5v/8/Pz//////////////////////////////////////////////////////+bm5v9JSUn/Kysr/xcXF/8UFBT/FBQU/xQUFP8RERH/Kysr/8rKyv/o6Oj//Pz8/////////////////////////////////////////////Pz8/+bm5v/j4+P//////////////////////////////////////////////////Pz8/+jo6P/Kysr/Kysr/xEREf8UFBT/FBQU/xQUFP8XFxf/Kysr/0lJSf/m5ub////////////////////////////////////////////m5ub/SUlJ/y4uLv///////////////////////////////////////////////////////////+bm5v9JSUn/Kysr/xcXF/8UFBT/FBQU/xQUFP8RERH/Kysr/8rKyv/o6Oj//Pz8/////////////////////////////////+Li4v8uLi7/EBAQ/////////////////////////////////////////////////////////////Pz8/+jo6P/Kysr/Kysr/xEREf8UFBT/FBQU/xQUFP8XFxf/Kysr/0lJSf/m5ub/////////////////////////////////4+Pj/zAwMP8SEhL//////////////////////////////////////////////////////////////////////+bm5v9JSUn/Kysr/xcXF/8UFBT/FBQU/xQUFP8RERH/Kysr/8rKyv/o6Oj//Pz8///////////////////////j4+P/MDAw/xISEv///////////////////////////////////////////////////////////////////////Pz8/+jo6P/Kysr/Kysr/xEREf8UFBT/FBQU/xQUFP8XFxf/Kysr/0lJSf/m5ub//////////////////////+Pj4/8wMDD/EhIS///////8/Pz/5ubm/+Pj4//j4+P/4+Pj/+Pj4//j4+P/4+Pj/+bm5v/8/Pz//////////////////////+bm5v9JSUn/Kysr/xcXF/8UFBT/FBQU/xQUFP8RERH/Kysr/8rKyv/o6Oj//Pz8////////////4+Pj/zAwMP8SEhL//////+bm5v9JSUn/Li4u/y8vL/8vLy//Ly8v/y8vL/8tLS3/SEhI/+bm5v///////////////////////Pz8/+jo6P/Kysr/Kysr/xEREf8UFBT/FBQU/xQUFP8XFxf/Kysr/0lJSf/m5ub////////////j4+P/MDAw/xISEv//////4+Pj/y4uLv8UFBT/LCws/y8vL/8vLy//Ly8v/y0tLf9ISEj/5ubm/////////////////////////////////+bm5v9JSUn/Kysr/xcXF/8UFBT/FBQU/xQUFP8RERH/Kysr/8rKyv/l5eX/5eXl/8rKyv8tLS3/EhIS///////j4+P/Ly8v/ysrK//Kysr/5eXl/+Pj4//j4+P/4+Pj/+bm5v/8/Pz//////////////////////////////////Pz8/+jo6P/Kysr/Kysr/xEREf8UFBT/FBQU/xQUFP8XFxf/LS0t/zAwMP8wMDD/LS0t/xcXF/8UFBT//////+Pj4/8vLy//Ly8v/+Pj4////////////////////////////////////////////////////////////////////////////+bm5v9JSUn/Kysr/xcXF/8UFBT/FBQU/xQUFP8SEhL/EhIS/xISEv8SEhL/FBQU/xQUFP//////4+Pj/y8vL/8vLy//4+Pj/////////////////////////////////////////////////////////////////////////////Pz8/+jo6P/Kysr/Kysr/xEREf8UFBT/FBQU/xQUFP8UFBT/FBQU/xQUFP8UFBT/FBQU///////j4+P/Ly8v/y8vL//j4+P//////////////////////////////////////////////////////////////////////////////////////+bm5v9JSUn/Kysr/xcXF/8UFBT/FBQU/xQUFP8UFBT/FBQU/xQUFP8UFBT//////+Pj4/8vLy//Ly8v/+Pj4////////////////////////////////////////////////////////////////////////////////////////Pz8/+jo6P/Kysr/LS0t/xISEv8UFBT/FBQU/xQUFP8UFBT/FBQU/xQUFP//////4+Pj/y8vL/8rKyv/ysrK/+Xl5f/j4+P/4+Pj/+Pj4//m5ub//Pz8/////////////////////////////////////////////////////////////////+Pj4/8wMDD/EhIS/xQUFP8UFBT/FBQU/xQUFP8UFBT/FBQU///////j4+P/Li4u/xQUFP8sLCz/Ly8v/y8vL/8vLy//LS0t/0hISP/m5ub/////////////////////////////////////////////////////////////////4+Pj/zAwMP8SEhL/FBQU/xQUFP8UFBT/FBQU/xQUFP8UFBT//////+bm5v9JSUn/Li4u/y8vL/8vLy//Ly8v/y8vL/8tLS3/SEhI/+bm5v////////////z8/P/m5ub/4+Pj/+Pj4//j4+P/4+Pj/+Pj4//j4+P/4+Pj/+Xl5f/Kysr/LS0t/xISEv8UFBT/FBQU/xQUFP8UFBT/FBQU/xQUFP///////Pz8/+bm5v/j4+P/4+Pj/+Pj4//j4+P/4+Pj/+Pj4//m5ub//Pz8////////////5ubm/0lJSf8uLi7/MDAw/zAwMP8wMDD/MDAw/zAwMP8wMDD/MDAw/y0tLf8XFxf/FBQU/xQUFP8UFBT/FBQU/xQUFP8UFBT/FBQU///////////////////////////////////////////////////////////////////////i4uL/Ly8v/xAQEP8SEhL/EhIS/xISEv8SEhL/EhIS/xISEv8SEhL/EhIS/xQUFP8UFBT/FBQU/xQUFP8UFBT/FBQU/xQUFP8UFBT/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA="

root = Tk()

cur_usunit = StringVar()
cur_euunit = StringVar()

cur_usunit.set("c")
cur_euunit.set("c")

input_var = StringVar()
output_var = StringVar()

root['bg']='#141414'
root.resizable(False, False)
root.title("Convert Units")
root.geometry("300x400")

myappid = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
icon_data = base64.b64decode(icon64)
temp_icon = "temp_icon.ico"
with open(temp_icon, "wb") as tmp_file:
    tmp_file.write(icon_data)
root.iconbitmap(temp_icon)

def usunit_change():
    if cur_usunit.get()=="inch":
        cur_usunit.set("foot")
        usunit_btn.configure(text="From feet")
    elif cur_usunit.get()=="foot":
        cur_usunit.set("yard")
        usunit_btn.configure(text="From yards")
    elif cur_usunit.get()=="yard":
        cur_usunit.set("mile")
        usunit_btn.configure(text="From miles")
    elif cur_usunit.get()=="mile":
        cur_usunit.set("inch")
        usunit_btn.configure(text="From inches")
    elif cur_usunit.get()=="c":
        cur_usunit.set("inch")
        usunit_btn.configure(text="From inches")

def euunit_change():
    if cur_euunit.get()=="mm":
        cur_euunit.set("cm")
        euunit_btn.configure(text="To centimetres")
    elif cur_euunit.get()=="cm":
        cur_euunit.set("dm")
        euunit_btn.configure(text="To decimetres")
    elif cur_euunit.get()=="dm":
        cur_euunit.set("m")
        euunit_btn.configure(text="To metres")
    elif cur_euunit.get()=="m":
        cur_euunit.set("km")
        euunit_btn.configure(text="To kilometres")
    elif cur_euunit.get()=="km":
        cur_euunit.set("mm")
        euunit_btn.configure(text="To millimetres")
    elif cur_euunit.get()=="c":
        cur_euunit.set("mm")
        euunit_btn.configure(text="To millimetres")


def transfer():
    lus = cur_usunit.get()
    leu = cur_euunit.get()
    n = 0
    if lus == "c" or leu=="c":
        return
    else:
        iv = float(input_var.get())
    
    if lus == "mile" and leu == "mm":
        n = iv*1609344
        output_var.set(n)
    elif lus == "mile" and leu == "cm":
        n = iv*160934.4
        output_var.set(n)
    elif lus == "mile" and leu == "dm":
        n = iv*16093.44
        output_var.set(n)
    elif lus == "mile" and leu == "m":
        n = iv*1609.344
        output_var.set(n)
    elif lus == "mile" and leu == "km":
        n = iv*1.609344
        output_var.set(n)
    elif lus == "yard" and leu == "mm":
        n = iv*914.4
        output_var.set(n)
    elif lus == "yard" and leu == "cm":
        n = iv*91.44
        output_var.set(n)
    elif lus == "yard" and leu == "dm":
        n = iv*9.144
        output_var.set(n)
    elif lus == "yard" and leu == "m":
        n = iv*0.9144
        output_var.set(n)
    elif lus == "yard" and leu == "km":
        n = iv*0.0009144
        output_var.set(n)
    elif lus == "foot" and leu == "mm":
        n = iv*304.8
        output_var.set(n)
    elif lus == "foot" and leu == "cm":
        n = iv*30.48
        output_var.set(n)
    elif lus == "foot" and leu == "dm":
        n = iv*3.048
        output_var.set(n)
    elif lus == "foot" and leu == "m":
        n = iv*0.3048
        output_var.set(n)
    elif lus == "foot" and leu == "km":
        n = iv*0.0003048
        output_var.set(n)
    elif lus == "inch" and leu == "mm":
        n = iv*25.4
        output_var.set(n)
    elif lus == "inch" and leu == "cm":
        n = iv*2.54
        output_var.set(n)
    elif lus == "inch" and leu == "dm":
        n = iv*0.254
        output_var.set(n)
    elif lus == "inch" and leu == "m":
        n = iv*0.0254
        output_var.set(n)
    elif lus == "inch" and leu == "km":
        n = iv*0.0000254
        output_var.set(n)

input_label = Label(root, text="Input", font=25, height=1, width=15)
input_label.place(x=10,y=40)

input_entry = Entry(root, textvariable=input_var, font=25, width=20)
input_entry.place(x=10,y=80)

output_label = Label(root, text="Output", font=25, height=1, width=15)
output_label.place(x=10,y=120)

output_entry = Label(root, textvariable=output_var, font=25, width=20, anchor='w', justify=LEFT)
output_entry.place(x=10,y=160)

transfer_btn = Button(root, text="Transfer the units", font=25, height=1, width=15, anchor='w', justify=LEFT, command=transfer)
transfer_btn.place(x=10,y=340)

euunit_btn = Button(root, text="Choose", font=25, height=1, width=15, anchor='w', justify=LEFT, command=euunit_change)
euunit_btn.place(x=10,y=280)

usunit_btn = Button(root, text="Choose", font=25, height=1, width=15, anchor='w', justify=LEFT, command=usunit_change)
usunit_btn.place(x=10,y=230)

root.mainloop()