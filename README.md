## TkinterColourPicker
This is a basic colour picker inspired by w3school color picker 

# Objective
1.The main objective of the application is to give the hexcode for the selected colour from the template.                               
2.This application also have an inbuild windows color picker.                                                                
3.This application also copies the selected color's hexcode.                                                                             
4.This application has dynamic color changing widgets to have preview of what that color looks like.

# Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages.

```bash
pip install pyperclip
pip install pillow
```
# Visuals

![colorpicker](https://user-images.githubusercontent.com/24393343/58766203-728f5f80-8599-11e9-863d-2a929a243f4e.jpg)
 
# Run Locally
1. Method-1
* Clone the repo.
* Open the file and extract it.
* Edit the .py File in any editor and run it.

2. Method-2
* Go to this website : https://absanthosh01.wixsite.com/pythonist
* Download the application and run the portable .exe file!!

# Requirnments

```bash
import re
import PIL
import pyperclip

from tkinter import *
from PIL     import Image
from io      import BytesIO
from base64  import b16encode
from base64  import b64decode
from tkinter.colorchooser import *


```
    
