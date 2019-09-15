# by @eickenberg

import numpy as np
import torch
from sklearn.feature_extraction.image import extract_patches
from torch.utils.data import Dataset

class PatchDataset(Dataset):

    def __init__(self, image3d, patch_size=64, transform=None,
                    add_color_axis=True):
        self.image3d = image3d
        self.patch_size = patch_size
        self.transform = transform
        self.add_color_axis = add_color_axis

        self.build()

    def build(self):

        # assume last axis indexes images
        patch_shape = (self.patch_size, self.patch_size, 1)
        self.patches = extract_patches(self.image3d, patch_shape)

    def __len__(self):
        return np.prod(self.patches.shape[:3])

    def __getitem__(self, i):
        indices = tuple(np.unravel_index(i, self.patches.shape[:3])) + (slice(None), slice(None), 0)
        output = self.patches[indices]
        if self.add_color_axis:
            output = output[:, :, np.newaxis]
        if self.transform is not None:
            return self.transform(output)
        return output

if __name__ == "__main__":
    import nibabel
    fname = "Imaging Data/WBMRI010/DICOM/Series29-.104.0--/Series29-.104.0--_SPINE_20070619152260_29.nii"
    data = nibabel.load(fname).get_data()

    patch_dataset = PatchDataset(data)
