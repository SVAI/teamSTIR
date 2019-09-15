# by @eickenberg

import torch
import numpy as np

from patch_dataset import PatchDataset
from torch.utils.data import ConcatDataset

import glob
import os
import nibabel

class ZipDataset(torch.utils.data.Dataset):

    def __init__(self, *datasets):
        self.datasets = datasets

    def __len__(self):
        return min(len(dataset) for dataset in self.datasets)

    def __getitem__(self, i):
        return tuple(dataset[i] for dataset in self.datasets)



class NFDataset(torch.utils.data.Dataset):

    def __init__(self, keys=(), exclude_subjects=(),
                    data_transform=None,
                    target_transform=None):
        self.keys = keys
        self.exclude_subjects = exclude_subjects
        self.data_transform = data_transform
        self.target_transform = target_transform
        self.data_transform = data_transform

        self.build()

    def build(self):
        subject_folders = sorted(glob.glob(os.path.join(self.nf_folder, "WBMRI*")))
        for ex in self.exclude_subjects:
            for i, s in enumerate(subject_folders):
                if ex in s:
                    del subject_folders[i]
        self.subject_folders = subject_folders

        self.stir_patch_datasets = []
        self.annotation_patch_datasets = []
        
        self.count64_lengths = []
        self.positive_counts = []
        self.random_negative_counts = []
        
        counter = 0
        self.distrib = np.zeros(3000, dtype=int)

        for subject_folder in subject_folders:
            stir_file = os.path.join(subject_folder, "STIR_file.nii")
            stir_vol = nibabel.load(stir_file).get_data()
            stir_vol[stir_vol >= 3000] = 0
            self.distrib += np.bincount(stir_vol.ravel(), minlength=3000)
            self.stir_patch_datasets.append(
                    PatchDataset(stir_vol[:, ::-1].astype('float32'), 
                        transform=self.data_transform))
                    # ^note the axis flip

            annotation_file = os.path.join(subject_folder, "annotation_file.nii.gz")
            annotation_vol = (nibabel.load(annotation_file).get_data() > 0).astype('bool') # <- note the axis flip
            self.annotation_patch_datasets.append(
                    PatchDataset(annotation_vol,
                        transform=self.target_transform))

            count64_file = os.path.join(subject_folder, "count64_file.nii.gz")
            count64_vol = nibabel.load(count64_file)
            count64_data = count64_vol.get_data()
            self.count64_lengths.append(count64_data.size)

            positive_counts = np.where(count64_data.ravel() > 0)[0]
            negative_counts = np.random.choice(np.where(count64_data.ravel() == 0)[0],
                                                len(positive_counts), replace=False)
            self.positive_counts.append(positive_counts + counter)
            self.random_negative_counts.append(negative_counts + counter)
            counter += self.count64_lengths[-1]

        self.positive_counts = np.concatenate(self.positive_counts)
        self.random_negative_counts = np.concatenate(self.random_negative_counts)

        self.subset_indices = np.stack((self.positive_counts, self.random_negative_counts),
                axis=1).ravel()


        self.stir_patches = ConcatDataset(self.stir_patch_datasets)
        self.annotation_patches = ConcatDataset(self.annotation_patch_datasets)

        self.dataset = ZipDataset(self.stir_patches, self.annotation_patches)

    def __getitem__(self, i):
        return self.dataset[i]

    def __len__(self):
        return len(self.dataset)





if __name__ == "__main__":

    from torchvision.transforms import Compose, Normalize, ToTensor

    data_transform = Compose([  ToTensor(),
                                Normalize([0.], [300.]),
                                Normalize([.5], [.5]),
                                ])

    #target_transform = ToTensor()
    nfdataset = NFDataset("/home/michael/nf_dataset",
                            data_transform=data_transform,
                            target_transform=target_transform)

    sampler = torch.utils.data.sampler.SubsetRandomSampler(
                                    nfdataset.positive_counts)

    dataloader = torch.utils.data.DataLoader(
                    nfdataset, sampler=sampler, batch_size=32)
