import os, sys, eel

import dialogs
import utils

eel.init('views')

@eel.expose
def initialize():
  print('inited')
  return []


@eel.expose
def ask_file():
  return dialogs.ask_file()


@eel.expose
def generateVerilog(projectLocation, adderName, N):
  eel.putMessageInOutput("Yay!")()


def start():
  eel.start('index.html', size=(1024, 768), port=10123)


if __name__ == "__main__":
  start()