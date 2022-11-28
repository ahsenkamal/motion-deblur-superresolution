import os, sys, eel
import cv2

import dialogs
import utils

import motion_deblur

IUT = None # Image Under Test

eel.init('views')

@eel.expose
def ask_file():
  return dialogs.ask_file()

@eel.expose
def ask_and_save_image(image_base64_str):
  save_file_name = dialogs.ask_save_as_image_file()
  image = utils.base64_to_image(image_base64_str)
  if save_file_name:
    cv2.imwrite(save_file_name, image)

@eel.expose
def submit_iut_path(image_path):
  global IUT
  IUT = cv2.imread(image_path)

@eel.expose
def do_motion_deblur(angle, strength, snr, iut_already_displayed):
  image = IUT

  if not iut_already_displayed:
    img_base64_str = utils.image_to_base64(image)
    eel.displayIUT(img_base64_str)

  psf, res_image = motion_deblur.motion_deblur(image, angle, strength, snr)

  psf_base64_str = utils.image_to_base64(psf)
  eel.displayPSF(psf_base64_str)
  
  res_image_base64_str = utils.image_to_base64(res_image)
  eel.displayOUT(res_image_base64_str)


def start():
  eel.start('index.html', size=(1024, 768), port=10123)


if __name__ == "__main__":
  start()