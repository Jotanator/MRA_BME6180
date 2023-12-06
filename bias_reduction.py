import nibabel as nib
import SimpleITK as sitk
import glob
import os
import argparse
import os

def correct_image(nii_file_path, output_folder):
    nii_image = nib.load(nii_file_path)
    image_data = nii_image.get_fdata()
    sitk_img = sitk.GetImageFromArray(image_data)


    transformed = sitk.RescaleIntensity(sitk_img, 0, 255)
    transformed = sitk.LiThreshold(sitk_img, 0, 1)
    head_mask = transformed

    shrinkFactor = 1
    inputImage = sitk.Shrink(sitk_img, [shrinkFactor] * sitk_img.GetDimension())
    maskImage = sitk.Shrink(head_mask, [shrinkFactor] * sitk_img.GetDimension())

    bias_corrector = sitk.N4BiasFieldCorrectionImageFilter()
    corrected_img = bias_corrector.Execute(inputImage, maskImage)

    output_filename = os.path.join(output_folder, os.path.basename(nii_file_path).replace('.nii', '_after_n4_correction.nii'))
    sitk.WriteImage(corrected_img, output_filename)


if __name__ == "__main__":
    # Create the parser
    parser = argparse.ArgumentParser(description='Process some folders.')

    # Add the arguments
    parser.add_argument('InputFolder',
                        metavar='input_folder',
                        type=str,
                        help='the path to the input folder')

    parser.add_argument('OutputFolder',
                        metavar='output_folder',
                        type=str,
                        help='the path to the output folder')

    # Execute the parse_args() method
    args = parser.parse_args()
    print(args)
    for nii_file_path in glob.glob(args.InputFolder + '/*.nii.gz'):
        print(nii_file_path)
        if '_mask' not in os.path.basename(nii_file_path):
            correct_image(nii_file_path, args.OutputFolder)
