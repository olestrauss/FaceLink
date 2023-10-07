import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # Check if running as a PyInstaller executable
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Directories():
    directory = resource_path('Image Database')
    inp_path = resource_path('Input Set')
    out_path = resource_path('Output')

    
