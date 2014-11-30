#!/usr/bin/env python
"""pyrios@gmail.com copyright (c) 2014 all rights reserved.

Make a new directory based on an existing directory suitable for copying to
the Octatrack.

Directory structure is preserved. Within the directory structure, depending
on the file type, a link to the original file is created or the file is
converted to a wav file.

"""
import os
import sys

import pydub


def link_or_copy(out_dir, dir_path, file_names):
    """Create a link or convert file names depending on file type."""
    dest_dir = os.path.join(out_dir, dir_path)
    src_abs_dir = os.path.abspath(dir_path)
    os.makedirs(dest_dir)
    for file_name in file_names:
        src_abs_path = os.path.join(src_abs_dir, file_name)
        if file_name.endswith("wav"):
            dest_path = os.path.join(dest_dir, file_name)
            os.symlink(src_abs_path, dest_path)
        elif file_name.endswith(".mp3"):
            sample = pydub.AudioSegment.from_mp3(src_abs_path)
            (name, ext) = os.path.splitext(file_name)
            dest_path = os.path.join(dest_dir, "{0}.wav".format(name))
            sample.export(dest_path, format="wav")


def main(argv):
    input_dir = argv[1]
    input_abs_dir = os.path.abspath(input_dir)
    output_dir = "{0}_out".format(input_abs_dir)

    print "Converting from {0} to {1}".format(input_abs_dir, output_dir)
    for dir_path, dir_names, file_names  in os.walk(input_dir):
        print dir_path
        link_or_copy(output_dir, dir_path, file_names)
        

if __name__ == "__main__":
    main(sys.argv)
