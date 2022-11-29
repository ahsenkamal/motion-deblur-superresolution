import os, sys, re
import platform

import cv2
import numpy as np
import base64

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
  retval, image_buffer = cv2.imencode('.png', image)
  img_base64_str = "data:image/png;base64," + base64.b64encode(image_buffer).decode()
  return img_base64_str

def base64_to_image(image_base64_str):
  image_base64_str = image_base64_str[22:] # strip "data:image/png;base64,"
  image_buffer = np.fromstring(base64.b64decode(image_base64_str), np.uint8)
  image = cv2.imdecode(image_buffer, cv2.IMREAD_ANYCOLOR)
  return image

