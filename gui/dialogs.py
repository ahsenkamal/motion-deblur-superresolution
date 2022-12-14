import platform
import sys

from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory, askopenfilenames, asksaveasfilename

def ask_file():
  root = Tk()
  root.withdraw()
  root.wm_attributes('-topmost', 1)
  file = askopenfilename(parent=root)
  root.update()

  return file if bool(file) else None

def ask_save_as_image_file():
  root = Tk()
  root.withdraw()
  root.wm_attributes('-topmost', 1)
  file = asksaveasfilename(parent=root, defaultextension='.jpeg', filetypes=(
        ('JPEG', '.jpeg'), ('PNG', '.png'), ('BMP', '.bmp'), ('GIF', '.gif')
  ))
  root.update()

  return file if bool(file) else None