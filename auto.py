import os
import shutil
import smtplib

source_dir = '/path/to/source'
dest_dir = '/path/to/destination'

for file in os.listdir(source_dir):
  src_file = os.path.join(source_dir, file)
  dest_file = os.path.join(dest_dir, file)
  shutil.move(src_file, dest_file)
