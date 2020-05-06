"""
Augment (double data set) using imgaug
Note:  can also take bounding boxes and transform
imgaug info:  https://github.com/aleju/imgaug
"""
import numpy as np
import imgaug as ia
import imgaug.augmenters as iaa
import argparse
import matplotlib.pyplot as plt
import os
import glob

np.random.bit_generator = np.random._bit_generator

def main(data_dir):
    imagefiles = glob.glob(os.path.join(data_dir, "*.*"))
    # imagefiles = imagefiles[:int((len(imagefiles)*0.3))]
    images = []
    img_files = []
    for img_file in imagefiles:
        images.append(plt.imread(os.path.join(img_file)))
        img_files.append(img_file)

    # To sometimes apply aug
    sometimes = lambda aug: iaa.Sometimes(0.3, aug)

    # The transformations!!!
    seq = iaa.Sequential([
        iaa.Fliplr(1.0),
        iaa.Affine(translate_px={"x": (1, 5)}),
        sometimes(iaa.CropToSquare()),
        # sometimes(iaa.SigmoidContrast(cutoff=0.7)),
        # sometimes(iaa.AdditiveGaussianNoise(scale=0.05*255)),
        # sometimes(iaa.Fog()),
        # sometimes(iaa.Multiply(0.5)),
        # sometimes(iaa.Add(-10)),
        # sometimes(iaa.Pad(px=(256, 256, 0, 0))),
    ])

    images_aug = seq(images=images)

    # Save images
    for i in range(len(images)):
        img_file = img_files[i]
        # Create new file name and save
        name_spl = os.path.basename(img_file).split('.')
        ending = name_spl[-1]
        new_file_name = '.'.join(name_spl[0:-1]) + '_aug' + '.' + ending
        plt.imsave(os.path.join(data_dir, new_file_name), images_aug[i])
            
                
if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--data-dir', type=str, dest='data_dir',
        help='Data directory where classification images live.'
    )
    args = parser.parse_args()
    main(args.data_dir)