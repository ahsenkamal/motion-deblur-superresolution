# wget https://public-asai-dl-models.s3.eu-central-1.amazonaws.com/ISR/rdn-C6-D20-G64-G064-x2/ArtefactCancelling/rdn-C6-D20-G64-G064-x2_ArtefactCancelling_epoch219.hdf5
# mkdir weights && mv *.hdf5 weights

import numpy as np
from PIL import Image
from ISR.models import RDN

def super_resolve(img_arr: np.array):
    rdn = RDN(arch_params={'C':6, 'D':20, 'G':64, 'G0':64, 'x':2})
    rdn.model.load_weights('weights/rdn-C6-D20-G64-G064-x2_ArtefactCancelling_epoch219.hdf5')
    sr_img = rdn.predict(img_arr)

    return sr_img

def get_img_from_path(img_path):
    return np.array(Image.open(img_path))

def save_img_to_path(img_path, img_arr):
    Image.fromarray(img_arr).save(img_path)

if __name__ == '__main__':
    img_arr = get_img_from_path('../samples/flower.png')
    sr_img = super_resolve(img_arr)
    save_img_to_path('../samples/flower-resolved.png', sr_img)
