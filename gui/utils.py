import os, sys, re
import platform

import base64, io

def open_output_folder(folder):
  folder_directory = os.path.abspath(folder)
  if platform.system() == 'Windows':
    os.startfile(folder_directory, 'explore')
  elif platform.system() == 'Linux':
    os.system('xdg-open "' + folder_directory + '"')
  elif platform.system() == 'Darwin':
    os.system('open "' + folder_directory + '"')
  else:
    return False
  return True

def image_to_base64(image):
  buffered = io.BytesIO()
  image.save(buffered, format="PNG")
  img_base64_str = "data:image/png;base64," + base64.b64encode(buffered.getvalue()).decode()
  return img_base64_str
