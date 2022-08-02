import binascii
from genericpath import exists
import shutil
import sys
import tempfile

from PyQt5 import QtCore, QtGui, QtWidgets

from bnd.bnd import BND
from data import *
from interface import main_window
from interface.tree_bundle_item import QTreeWidgetBundleItem


# -qr "test/DATA_CMN.BND.out" "test/source_file.txt" "actor/reload/tips/tips121.bnd/actorparam.dat"
def quick_replace(bnd_file_path, source_file_path, destination):
    print(
        "Replacing file", destination, "inside", bnd_file_path, "with", source_file_path
    )

    # Check if replacement file exists
    if not exists(source_file_path):
        print("Source file", source_file_path, "doesn't exist")
        return

    # Check if BND file exists
    if not exists(bnd_file_path):
        print("BND file", bnd_file_path, "doesn't exist")
        return

    # Check if destination file is valid
    if destination.endswith("/"):
        print("Destination cannot be a folder")
        return

    # Do stuff
    with open(bnd_file_path, "r+b") as f:
        data = f.read()
        bnd_file = BND(data)
        destination_array = destination.split("/")
        destination_file = bnd_file.get_bundle_from_filename_array(destination_array)

        # Return if destination file not found
        if destination_file == None:
            print("Couldn't find destination file")
            return

        # Replace
