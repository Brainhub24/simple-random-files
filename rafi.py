# For testing purposes
# A small python commandline-tool that creates super fast different files with the following file extensions:
# [".jpg", ".png", ".doc", ".raw", ".txt"]

import os
import random

extensions = [".jpg", ".png", ".doc", ".raw", ".txt"]

for i in range(5):
    # Generate a random file name
    file_name = "testfile" + str(i)
    extension = random.choice(extensions)
    full_file_name = file_name + extension

    # Open a file with the generated file name and write random data to it
    with open(full_file_name, "wb") as f:
        f.write(os.urandom(1024))
