import os, sys, eel
from PIL import Image

import dialogs
import utils

image_cache = {}

eel.init('views')

@eel.expose
def initialize():
  print('inited')
  return []

@eel.expose
def ask_file():
  return dialogs.ask_file()

@eel.expose
def motion_deblur(image_path, angle, strength, snr):
  image = None
  if image_path in image_cache:
    image = image_cache[image_path]
  else:
    image = Image.open(image_path)
    image_cache[image_path] = image

  img_base64_str = utils.image_to_base64(image)
  eel.displayIUT(img_base64_str)

@eel.expose
def generateVerilog(projectLocation, adderName, N):
  eel.putMessageInOutput("Yay!")()


def start():
  eel.start('index.html', size=(1024, 768), port=10123)


if __name__ == "__main__":
  start()