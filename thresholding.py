import nibabel as nib
import numpy as np

def apply_threshold(nii_file_path, threshold):
    # Load the NIfTI file
    nii_image = nib.load(nii_file_path)

    # Get the image data as a numpy array
    image_data = nii_image.get_fdata()

    # Apply thresholding: Set values below the threshold to 0
    image_data[image_data < threshold] = 0

    # Create a new NIfTI image from the thresholded data
    new_image = nib.Nifti1Image(image_data, nii_image.affine, nii_image.header)

    # Save the new NIfTI image
    nib.save(new_image, 'thresholded_image.nii')

# Example usage
nii_file_path = '../MIP_script/BH0040.nii.gz'
threshold = 130  # Set your threshold value here
apply_threshold(nii_file_path, threshold)