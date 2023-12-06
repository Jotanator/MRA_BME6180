## Update 11/15/2023

To run all you need is 2 folder:
    - an input folder with all the MRA images,
    - an output folder where you wish you have all the skull stripped MRAs

You should then edit the paths in main.sh to read the correct input and output folder

Then execute run main.sh

## Installation

To use BET simply download and set it up. Instruction found here: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FslInstallation.

Fot the N4 bias reduction implemented in python you need the following packages:

    - SimpleITK
    - nibabel
    - glob

For the High Pass Filter implemented in matlab you need the Image Processing ToolBox.

## Use

If you use the file main.sh it will perform both skull extraction and N4 bias reduction on those extracted brains.

You could also individually use the command line commands for BET, or execute the N4 bias correction python script individually aswell.

Lastly the matlab script so far only takes one image at a time so you have to manually change the file name that you wish to use this filter for.
