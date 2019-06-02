import re
import PIL
import pyperclip

from tkinter import *
from PIL     import Image
from io      import BytesIO
from base64  import b16encode
from base64  import b64decode
from tkinter.colorchooser import *
global hexcodelow



root = Tk()
root.title("Colour-Picker")
def click(event):
    try:
        im = PIL.Image.open(BytesIO(b64decode(dats)))
        rgbIm = im.convert("RGB")
        r,g,b = rgbIm.getpixel((event.x, event.y))
        rgbcode=(int(r),int(g),int(b))
        hexcode =(b'#'+b16encode(bytes(rgbcode)))
        hexcodelow=hexcode.lower()
        pyperclip.copy(str(hexcodelow.decode("utf-8")))
        widgetf. config     (bg= hexcodelow)
        widgetf1. config     (bg= hexcodelow)
        hexlabel.config     (bg=hexcodelow)
        hexlabel.config     (text=hexcodelow)
        root.    configure  (background=hexcodelow)
        copycol.config(text="Copied\n"+hexcodelow.decode("utf-8"))
    except:
        pass



def getColor():
    try:
        color = askcolor() 
        cval=color[1]
        hexlabel.config(bg=cval)
        hexlabel.config     (text=cval)
        widgetf. config     (bg= cval)
        widgetf1. config     (bg= cval)
        pyperclip.copy(str(cval))
        copycol.config(text="Copied\n"+cval)
        inputbox.delete("1.0", "end")
        inputbox.insert('1.0',(cval))
        root.    configure  (background=cval)
        print (cval)
    except:
        pass


def hover(event):
    try:            
        x, y = event.x, event.y
        im = PIL.Image.open(BytesIO(b64decode(dats)))
        rgbIm = im.convert("RGB")
        r,g,b = rgbIm.getpixel((x,y))
        rgbcode=(int(r),int(g),int(b))
        hexcode =(b'#'+b16encode(bytes(rgbcode)))
        hexcodelow=hexcode.lower()
        pal.config(bg=hexcodelow)
        defpicker.config(bg=hexcodelow)
        quit.config(bg=hexcodelow)
    except Exception as err:
        pass
def exit():
    root.destroy()


def hover2(event):
    pal.config(bg="#ffffff") 

def colourvalue(event):
    inputbox.delete("1.0", "end")

def colorgetter(event):
    colourcode=inputbox.get('1.0','end')
    try:
        widgetf. config     (bg= colourcode)
        widgetf1. config     (bg= colourcode)
        hexlabel.config     (bg=colourcode)
        root.    configure  (background=colourcode)
    except:
        inputbox.delete("1.0", "end")
        inputbox.insert('1.0',("Invalid Code"))

dats1='''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'''
dats='''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'''
imagePath = PhotoImage(data=dats)
widgetf = Label(root,image=imagePath,  bg="#71daab")
widgetf.place(x=40, y=50)

imagePath1 = PhotoImage(data=dats1)
widgetf1 = Label(root,image=imagePath1,  bg="#71daab")
widgetf1.place(x=308, y=0)

pal= Label(root,height=2,width=20)
pal.place(x = 300,  y = 190)

inputbox= Text(root,height=1,width=13,font=("",15))
inputbox.place(x=299,y=238)
inputbox.insert('1.0', ("Color Value"))

hexlabel= Label(root,text='#000000',bg='#71daab',fg='#000000',font=("Gill Sans",20))
hexlabel.place(x = 112,  y = 268)

copycol = Label(root,  text ='Select\n  ' , height = 3,  width = 20, bg="#ed4d3e")
copycol.place(x = 300,  y = 130)

defpicker=Button(root,text='DCP', command=getColor,bg="#ed4d3e",bd=10)
defpicker.place(x=300,y=280)

quit= Button(root,text="Quit",bg="#ed4d3e",command=exit,bd=10)#,height = 2,  width = 7)
quit.place(x=395,y=280)

root.bind('<Button-1>', click)
inputbox.bind('<Button-1>', colourvalue)
root.bind('<Return>', colorgetter)
widgetf.bind('<Motion>', hover)
widgetf.bind("<Enter>", hover)
widgetf.bind("<Leave>", hover2)


root.configure(background="#71daab")
root.resizable(False,  False)
root.geometry("480x350")
root.update()
root.mainloop()