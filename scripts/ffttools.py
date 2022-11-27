#!/usr/bin/python3
import sys
import numpy as np
from PIL import Image


def getDFT(f):
    f = np.copy(f)
    M, N = f.shape

    # shift spectrum to center of the array
    for i in range(M):
        for j in range(N):
            f[i, j] *= (-1)**(i+j)
    
    # do dft
    F = np.fft.fft2(f)

    return F


def getIDFT(F):
    F = np.copy(F)
    M, N = F.shape

    f = np.fft.ifft2(F)

    # undo shifting
    for i in range(M):
        for j in range(N):
            f[i, j] *= (-1)**(i+j)

    return f.real


def saveArrayAsImage(arr, outPath):
    M, N = arr.shape

    out = Image.new('L', (M, N))
    pix = out.load()

    for i in range(M):
        for j in range(N):
            pix[i, j] = int(arr[i, j])
    
    out.save(outPath)


def loadImageAsArray(imPath):
    im = Image.open(imPath).convert('L')
    return np.array(list(im.getdata()), dtype=np.float64).reshape(im.size)


def saveMagSpectrum(F, outPath):
    F = abs(F)

    # log normalization
    Fn = np.array(list(map(lambda x: np.log(1+x), F)))

    # normalize the range to [0..255]
    Fn *= 255/np.log(1+255*F.size)

    # save the spectrum as an image
    saveArrayAsImage(Fn, outPath)


def savePhaseSpectrum(F, outPath):
    F = np.angle(F) + np.pi
    F *= 255/(2*np.pi)

    saveArrayAsImage(F, outPath)


def saveSpectrum(F, magSpecPath, phaseSpecPath):
    saveMagSpectrum(F, magSpecPath)
    savePhaseSpectrum(F, phaseSpecPath)


def loadMagSpectrum(specPath):
    Fn = loadImageAsArray(specPath)
    
    Fn *= np.log(1+255*Fn.size)/255

    F = np.array(list(map(lambda x: np.exp(x)-1, Fn)))

    return F


def loadPhaseSpectrum(specPath):
    F = loadImageAsArray(specPath)
    
    F *= 2*np.pi/255
    F -= np.pi

    return F


def combineMagAndPhaseSpectrum(Fm, Fp):
    F = Fm * np.exp(1j * Fp)
    return F


def loadSpectrum(magSpecPath, phaseSpecPath):
    magSpec = loadMagSpectrum(magSpecPath)
    phaseSpec = loadPhaseSpectrum(phaseSpecPath)
    return combineMagAndPhaseSpectrum(magSpec, phaseSpec)


if __name__ == "__main__":
    mode = sys.argv[1].strip().lower()
    imPath = sys.argv[2].strip()
    
    imName, imExt = imPath.split(".")
    magSpecPath = imName + ".magspec." + imExt
    phaseSpecPath = imName + ".phasespec." + imExt

    if mode == "dft":
        f = loadImageAsArray(imPath)
        F = getDFT(f)
        saveSpectrum(F, magSpecPath, phaseSpecPath)
    elif mode == "idft":
        F = loadSpectrum(magSpecPath, phaseSpecPath)
        f = getIDFT(F)
        
        outPath = imName + ".idft." + imExt
        saveArrayAsImage(f1, outPath)