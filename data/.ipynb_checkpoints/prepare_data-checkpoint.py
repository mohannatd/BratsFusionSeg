from os import mkdir, path
import shutil
import nibabel as nib
import numpy as np
from model.fusion import Fusion
# import imutils

# Constants
NUM_SLICES = 155

# Function to normalize image data

def normalize_image(image):
    """Normalize the image data to a 0-255 scale."""
    img_min = np.min(image)
    img_max = np.max(image)
    normalized_image = (image - img_min) / (img_max - img_min) * 255
    # normalized_image = imutils.rotate(normalized_image, angle=180)
    return normalized_image

# Function to fuse images using zero learning fusion

def fuse_images(input_images):
    """Fuse multiple images into one using zero learning fusion."""
    fusion = Fusion(input_images)
    return fusion.fuse()

# Function to save NIfTI images

def save_nifti_image(data, filename):
    """Save the image data as a NIfTI file."""
    nifti_image = nib.Nifti1Image(data, np.eye(4))
    nifti_image.header.get_xyzt_units()
    nifti_image.to_filename(path.join(filename))

def rename_files():
    """Rename files in the input directory."""
    nnUNet_raw = path.join('nnUNet_raw')
    try:
        mkdir(nnUNet_raw)
    except:
        pass
    shutil.copy(path.join("fused_t1c_t1n.nii.gz"), path.join(nnUNet_raw, 'Brain_0000.nii.gz'))
    shutil.copy(path.join("rotate_t2f.nii.gz"), path.join(nnUNet_raw, 'Brain_0001.nii.gz'))
    shutil.copy(path.join("fused_t1c_t2w.nii.gz"), path.join(nnUNet_raw, 'Brain_0002.nii.gz'))
    shutil.copy(path.join("fused_t1c_t2f.nii.gz"), path.join(nnUNet_raw, 'Brain_0003.nii.gz'))

# Main function to prepare the dataset

def prepare_dataset(t1c_path, t1n_path, t2w_path, t2f_path):
    """Prepare the dataset by normalizing, fusing, and saving images."""
    t1c = nib.load(t1c_path).get_fdata()
    t1n = nib.load(t1n_path).get_fdata()
    t2f = nib.load(t2f_path).get_fdata()
    t2w = nib.load(t2w_path).get_fdata()

    for slice_num in range(NUM_SLICES):
        norm_t1c = normalize_image(t1c[:, :, slice_num])
        norm_t1n = normalize_image(t1n[:, :, slice_num])
        norm_t2f = normalize_image(t2f[:, :, slice_num])
        norm_t2w = normalize_image(t2w[:, :, slice_num])

        if slice_num == 0:
            fused_t1c_t1n = fuse_images([norm_t1c, norm_t1n])
            fused_t1c_t2f = fuse_images([norm_t1c, norm_t2f])
            fused_t1c_t2w = fuse_images([norm_t1c, norm_t2w])
            rotate_t2f = norm_t2f
        else:
            fused_t1c_t1n = np.dstack((fused_t1c_t1n, fuse_images([norm_t1c, norm_t1n])))
            fused_t1c_t2f = np.dstack((fused_t1c_t2f, fuse_images([norm_t1c, norm_t2f])))
            fused_t1c_t2w = np.dstack((fused_t1c_t2w, fuse_images([norm_t1c, norm_t2w])))
            rotate_t2f = np.dstack((rotate_t2f, norm_t2f))

    save_nifti_image(fused_t1c_t1n, 'fused_t1c_t1n.nii.gz')
    save_nifti_image(fused_t1c_t2f, 'fused_t1c_t2f.nii.gz')
    save_nifti_image(rotate_t2f, 'rotate_t2f.nii.gz')
    save_nifti_image(fused_t1c_t2w, 'fused_t1c_t2w.nii.gz')
    rename_files()
