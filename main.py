import os, sys
import face_recognition as f_r
import shutil as s_t
from config import Directories as dr
from termcolor import colored
from PIL import Image 
import logging

# Configure the logging module
log_file = "output.log"  # Specify the log file name
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Redirect print statements to the log
def log_print(*args): 
    logging.info(' '.join(map(str, args)))

# Replace all print statements with log_print
#print = log_print

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Recognizer():

    def __init__(self):
        self.known_face_encodings = []  # Initialize known_face_encodings here
        self.known_face_names = []  # Initialize known_face_names here
        self.image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
        self.imgs_allocated = 0

    def create_encodings(self, database):

        self.directory = database

        for filename in os.listdir(self.directory):
            print(filename)
            f = os.path.join(self.directory, filename)
            file_extension = os.path.splitext(f)[1].lower()

            if file_extension in self.image_extensions:
                # Load and process only supported image files
                img = f_r.load_image_file(f)
                self.known_face_encodings.append(f_r.face_encodings(img)[0])
                name = os.path.basename(f).split('.')[0]
                self.known_face_names.append(name)

        print(colored(f'{len(self.known_face_encodings)} face{["", "s"][len(self.known_face_encodings) > 1]} encoded. ', 'yellow'))


    def match_face(self, file, out_path, inp_path):

            f = os.path.join(inp_path, file)
            file_extension = os.path.splitext(file)[1].lower()
        
            if file_extension in self.image_extensions:
                print(file)
                # Load and process only supported image files
                img = f_r.load_image_file(f)
                current = f_r.face_encodings(img)[0]
                results = f_r.compare_faces(self.known_face_encodings, current) 

                if True in results:
                    for i, res in enumerate(results):
                        if res:
                            self.imgs_allocated += 1
                            target = os.path.join(out_path, self.known_face_names[i])
                            if not os.path.exists(target):
                                os.makedirs(target)

                            s_t.copy2(f, target)

            print(colored(f'Successfully allocated {self.imgs_allocated} images.', 'green'))
