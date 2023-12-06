% 3D FFN High pass filter
MRA_file='BG0010_01.nii.gz';
onefile=load_untouch_nii(MRA_file);
img = onefile.img;

MRI_image = img;
F = fftn(MRI_image);
F_shifted = fftshift(F);

temp = -size(MRI_image,1)/2:size(MRI_image,1)/2-1
[x, y, z] = ndgrid(-size(MRI_image,1)/2:size(MRI_image,1)/2-1, ...
                   -size(MRI_image,2)/2:size(MRI_image,2)/2-1, ...
                   -size(MRI_image,3)/2:size(MRI_image,3)/2-1);
               
radius = 5;
filter = sqrt(x.^2 + y.^2 + z.^2) > radius;

F_filtered = F_shifted .* filter;
F_inv_shift = ifftshift(F_filtered);
filtered_MRI_image = ifftn(F_inv_shift);
filtered_MRI_image = real(filtered_MRI_image);
onefile.img = filtered_MRI_image;
save_untouch_nii(onefile, "HighPassFilteredImg");
