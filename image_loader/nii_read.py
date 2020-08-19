import numpy, shutil, os, nibabel
import sys, getopt, cv2
import scipy.misc
import imageio
import matplotlib.pyplot as plt
import numpy as np


def main(argv):
   file_path = '/media/j/SAMSUNG/data/lung_mask' + '/'
   save_path = '/media/j/DATA/dataset/lung/lung_segmentation/zenodo_lung_seg/lung_mask' + '/'
   nii_list = [i for i in os.listdir(file_path) if 'nii.gz' in i]

   for i in nii_list:
       inputfile = file_path + i
       outputfile = save_path + i

       try:
           opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
       except getopt.GetoptError:
           print('nii2png.py -i <inputfile> -o <outputfile>')
           sys.exit(2)
       for opt, arg in opts:
           if opt == '-h':
               print('nii2png.py -i <inputfile> -o <outputfile>')
               sys.exit()
           elif opt in ("-i", "--input"):
               inputfile = arg
           elif opt in ("-o", "--output"):
               outputfile = arg

       print('Input file is ', inputfile)
       print('Output folder is ', outputfile)

       # set fn as your 4d nifti file
       image_array = nibabel.load(inputfile).get_data()
       print(len(image_array.shape))

       # ask if rotate
       # ask_rotate = input('Would you like to rotate the orientation? (y/n) ')
       ask_rotate = 'y'

       if ask_rotate.lower() == 'y':
           # ask_rotate_num = int(input('OK. By 90° 180° or 270°? '))
           ask_rotate_num = 90
           if ask_rotate_num == 90 or ask_rotate_num == 180 or ask_rotate_num == 270:
               print('Got it. Your images will be rotated by {} degrees.'.format(ask_rotate_num))
           else:
               print('You must enter a value that is either 90, 180, or 270. Quitting...')
               sys.exit()
       elif ask_rotate.lower() == 'n':
           print('OK, Your images will be converted it as it is.')
       else:
           print('You must choose either y or n. Quitting...')
           sys.exit()

       # set 4d array dimension values
       nx, ny, nz = image_array.shape

       # set destination folder
       if not os.path.exists(outputfile):
           os.makedirs(outputfile)
           print("Created ouput directory: " + outputfile)

       print('Reading NIfTI file...')

       total_slices = image_array.shape[2]

       slice_counter = 0
       # iterate through slices
       for current_slice in range(0, total_slices):
           # alternate slices
           if (slice_counter % 1) == 0:
               # rotate or no rotate
               if ask_rotate.lower() == 'y':
                   if ask_rotate_num == 90 or ask_rotate_num == 180 or ask_rotate_num == 270:
                       if ask_rotate_num == 90:
                           data = numpy.rot90(image_array[:, :, current_slice])
                       elif ask_rotate_num == 180:
                           data = numpy.rot90(numpy.rot90(image_array[:, :, current_slice]))
                       elif ask_rotate_num == 270:
                           data = numpy.rot90(numpy.rot90(numpy.rot90(image_array[:, :, current_slice])))
               elif ask_rotate.lower() == 'n':
                   data = image_array[:, :, current_slice]

               # alternate slices and save as png
               if (slice_counter % 1) == 0:
                   # if slice_counter == 28 and 'study_0015' in outputfile:
                   #     plt.imshow(data)
                   #     plt.show()
                   # if slice_counter == 29 and 'study_0015' in outputfile:
                   #     plt.imshow(data)
                   #     plt.show()
                   print('Saving image...')
                   image_name = inputfile[:-4] + "_z" + "{:0>3}".format(str(current_slice + 1)) + ".png"
                   _, data = cv2.threshold(data,0,1,cv2.THRESH_BINARY)
                   scipy.misc.imsave(image_name, data)
                   # imageio.imwrite(image_name,data)
                   print('Saved.')

                   # move images to folder
                   print('Moving image...')
                   src = image_name
                   shutil.move(src, outputfile)
                   slice_counter += 1
                   print('Moved.')

       print('Finished converting images')


# call the function to start the program
if __name__ == "__main__":
   main(sys.argv[1:])

