import sys
import numpy as np
from PIL import Image
from numpy.fft import fft2, ifft2
from scipy.signal import gaussian, convolve2d
import matplotlib.pyplot as plt
import os

def rgb2gray(rgb):
	return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])


def blur(img, mode = 'box', kernel_size = 3):
    # mode = 'box' or 'gaussian' or 'motion'
    dummy = np.copy(img)
    if mode == 'box':
        h = np.ones((kernel_size, kernel_size)) / kernel_size ** 2
    elif mode == 'gaussian':
        h = gaussian(kernel_size, kernel_size / 3).reshape(kernel_size, 1)
        h = np.dot(h, h.transpose())
        h /= np.sum(h)
    elif mode == 'motion':
        h = np.eye(kernel_size) / kernel_size
    dummy = convolve2d(dummy, h, mode = 'valid')
    return dummy


def add_gaussian_noise(img, sigma):
    gauss = np.random.normal(0, sigma, np.shape(img))
    noisy_img = img + gauss
    noisy_img[noisy_img < 0] = 0
    noisy_img[noisy_img > 255] = 255
    return noisy_img


def wiener_filter(img, kernel, K):
    kernel /= np.sum(kernel)
    dummy = np.copy(img)
    dummy = fft2(dummy)
    kernel = fft2(kernel, s = img.shape)
    kernel = np.conj(kernel) / (np.abs(kernel) ** 2 + K)
    dummy = dummy * kernel
    dummy = np.abs(ifft2(dummy))
    return dummy


def gaussian_kernel(kernel_size = 3):
    h = gaussian(kernel_size, kernel_size / 3).reshape(kernel_size, 1)
    h = np.dot(h, h.transpose())
    h /= np.sum(h)
    return h


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
            pix[i, j] = int(arr[j, i])
    
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