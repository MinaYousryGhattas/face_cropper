from PIL import Image
import os
import sys

# directory = "B:\mozakra\\fourth year\\semester1\\machine learning\\project\\sawery"
directory = raw_input("What is your name? ")

for file_name in os.listdir(directory):
  print("Processing %s" % file_name)
  image = Image.open(os.path.join(directory, file_name))

  x,y = image.size
  new_dimensions = (32, 32)
  output = image.resize(new_dimensions, Image.ANTIALIAS)
  output_file_name = raw_input("What is your name? ")
  #output_file_name = os.path.join(directory, "small_" + file_name)
  output.save(output_file_name, "JPEG", quality = 95)

print("All done")