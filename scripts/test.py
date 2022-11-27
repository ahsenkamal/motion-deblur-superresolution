from funcs import *

f = loadImageAsArray('f.png')
h = loadImageAsArray('h.png')
F = getDFT(f)
H = getDFT(h)
# saveSpectrum(F, './spectrums/F_mag.png', './spectrums/F_phase.png')
# saveSpectrum(H, './spectrums/H_mag.png', './spectrums/H_phase.png')
# f1 = getIDFT(F)
# h1 = getIDFT(H)
# saveArrayAsImage(f1, 'f1.png')
# saveArrayAsImage(h1, 'h1.png')

dummy = np.copy(f)
dummy = convolve2d(dummy, h, mode = 'valid')
saveArrayAsImage(dummy, 'dummy.png')
