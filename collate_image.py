"""
Script to take all years of a make/model and collate
the images into one make/model folder.  Operates on the
VMMRdb dataset:  http://vmmrdb.cecsresearch.org/
"""

import os
import glob
import shutil

new_datadir = 'vmmrdb_dataset_dir'

dirs = [x[0] for x in os.walk('VMMRdb')]

os.makedirs(new_datadir, exist_ok=True)

dirs_tmp = [d[:-5] for d in dirs]

for d in dirs_tmp:
    os.makedirs(os.path.join(new_datadir, os.path.basename(d)), exist_ok=True)


for d in dirs:
    # Specific to data folder names in this dataset
    tmp_dir = d[:-5]
    imgs = glob.glob(d+os.sep+"*.jpg")
    for img in imgs:
        shutil.copy(img, os.path.join(new_datadir, os.path.basename(tmp_dir), os.path.basename(img)))


