import os, sys, re
import platform

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

