from textwrap import wrap
from tkinter.filedialog import *
import tkinter as tk
from turtle import color

def saveFile():
   new_file = asksaveasfile(mode = 'w', filetypes = [('text files', '.txt')])
   if new_file is None:
      return
   text = str(entry.get(1.0, tk.END))
   new_file.write(text)
   new_file.close()
   
def openFile():
   file = askopenfile(mode = 'r', filetypes = [('text files', '*.txt')])
   if file is not None:
      content = file.read()
   entry.insert(tk.INSERT, content)
   
def clearFile():
   entry.delete(1.0, tk.END)

canvas = tk.Tk()
canvas.geometry('400x600')
canvas.title('Notepad')
canvas.config(bg = '#1a1a1a')
top = tk.Frame(canvas)
top.pack(padx = 10, pady = 5, anchor = 'nw')

b1 = tk.Button(canvas, text = 'Open', bg = 'white', command = openFile)   
b1.pack(in_ =top, side = tk.LEFT)

b2 = tk.Button(canvas, text = 'Save', bg = 'white', command = saveFile)
b2.pack(in_ = top, side = tk.LEFT)

b3 = tk.Button(canvas, text = 'Clear', bg = 'white', command = clearFile)
b3.pack(in_ = top, side = tk.LEFT)

b4 = tk.Button(canvas, text = 'Exit', bg = 'white', command = exit)
b4.pack(in_ = top, side = tk.LEFT)

entry = tk.Text(canvas, wrap = tk.WORD, bg = "white", font = ('poppins', 15),)
entry.pack(padx = 10, pady = 5, expand = True, fill = tk.BOTH)

canvas.mainloop()