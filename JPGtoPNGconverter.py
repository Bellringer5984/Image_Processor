import sys
import os
from PIL import Image

# using sys grab 1st and 2nd argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]
#check if new/ exist if not create it

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through /pokedex
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)
    img.save(f'{output_folder}{clean_name[0]}.png', 'png')
    print('all done!')

# convert images

# save to the new folder