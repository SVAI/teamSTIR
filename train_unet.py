"""Train a simple Unet"""


import torch

from torchvision.transforms import Compose, Normalize, ToTensor
from nf_dataset import NFDataset

data_transform = Compose([  ToTensor(),
                            Normalize([0.], [300.]),
                            Normalize([.5], [.5]),
                            ])

target_transform = ToTensor()

import os, glob
subject_folders = sorted([os.path.basename(folder) for folder in glob.glob("/home/michael/nf_dataset")])

test_folders = subject_folders[-10:]
train_folders = subject_folders[:-10]

nfdataset = NFDataset("/home/michael/nf_dataset",
                        data_transform=data_transform,
                        exclude_subjects=test_folders)
#                        target_transform=target_transform)
nfdataset_test = NFDataset("/home/michael/nf_dataset",
                        data_transform=data_transform,
                        exclude_subjects=train_folders)
#
sampler = torch.utils.data.sampler.SubsetRandomSampler(
                                nfdataset.positive_counts)

dataloader = torch.utils.data.DataLoader(
                nfdataset, sampler=sampler, batch_size=32)


from unet.unet_model import UNet

unet = UNet(1, 1)

n_epochs = 10

n_samples_per_epoch = 100000


all_epoch_avg_losses = []

unet = unet.cuda()

optimizer = torch.optim.Adam(unet.parameters())
import sys

import numpy as np

for e in range(n_epochs):
    losses = []
    for (x, y), ii in zip(dataloader, range(n_samples_per_epoch)):
        x = x.cuda()
        y = y.cuda()[..., 0]
        yy = y.type(torch.float) * 2 - 1

        p = unet.forward(x)[:, 0]
        loss = -torch.nn.LogSigmoid()(p * yy).mean()
        losses.append(loss.detach().cpu().numpy())
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        print(f"{ii:05d}/{n_samples_per_epoch} {losses[-1]:0.3f} {np.mean(losses[-10:]):0.3f} {np.mean(losses):0.3f}", end="\r")
        sys.stdout.flush()
    torch.save(unet, f"unet0_cp{e:02d}.th")
    print("\n")
    all_epoch_avg_losses.append(np.mean(losses))
