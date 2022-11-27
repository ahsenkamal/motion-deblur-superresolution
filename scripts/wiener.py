#!/usr/bin/python3
from funcs import *

# im = rgb2gray(plt.imread('lena.png'))
# f = loadImageAsArray('lena.png')

# b1 = blur(im, mode = 'motion', kernel_size = 15)
# b2 = blur(f, mode = 'motion', kernel_size = 15)

# # plt.imshow(im, cmap = 'gray')
# # plt.imshow(blurred_img, cmap = 'gray')
# # plt.show()

# h = Image.new('L', (512, 512))

# x = [200, 500]
# y = [300, 100]
# plt.plot(x, y, color="white", linewidth=3)
# plt.imshow(h)
# plt.show()

"""

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
        saveArrayAsImage(f, outPath)

"""


"""

file_name = os.path.join('lena512.jpg') 
img = rgb2gray(plt.imread(file_name))

blurred_img = blur(img, mode = 'motion', kernel_size = 3)

noisy_img = add_gaussian_noise(blurred_img, sigma = 20)

kernel = gaussian_kernel(3)

filtered_img = wiener_filter(noisy_img, kernel, K = 30)

display = [img, blurred_img, noisy_img, filtered_img]
label = ['Original Image', 'Motion Blurred Image', 'Motion Blurring + Gaussian Noise', 'Wiener Filter applied']

fig = plt.figure(figsize=(12, 10))

for i in range(len(display)):
    fig.add_subplot(2, 2, i+1)
    plt.imshow(display[i], cmap = 'gray')
    plt.title(label[i])

plt.show()

"""