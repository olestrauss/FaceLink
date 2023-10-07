# FaceLink - Facial Recognition Image Matching System

FaceLink is a Python-based facial recognition image matching system that allows you to match faces in an input set of images against a pre-defined database of known faces. This tool is useful for tasks like organizing and categorizing images based on individuals' faces.

## Features

- Create facial encodings for a database of known faces.
- Match faces in an input set of images to the known faces in the database.
- Allocate matched images to corresponding folders for easy organization.
- User-friendly graphical user interface (GUI) built with PySimpleGUI.
- Cross-platform compatibility.
- 
### Prerequisites

- Python 3.x installed on your system.
- Required Python packages can be installed using `pip` by running:

### Getting Started

- Download the setup file and follow instructions.
- If using setup file, you must run the programm as administrator.

### Running Locally

- Clone repository.
- Install necessary requirements using `pip install -r requirements.txt`.
- Run **gui.py** to access the main graphical user interface.


## Usage
1. **IMPORTANT:** If using the .exe file through the setup installer, you must run the file as admin.

1. **Setting Up Configuration**: Start by specifying the input set, database, and output folders using the GUI.

2. **Matching Faces**: Click start and FaceLink will match the faces in those images to the known faces in the database.

3. **Allocation**: Matched images will be allocated to corresponding folders in the output directory for easy organization.

4. **Completion Screen**: After the process is complete, you can exit or open the output folder from the completion screen.

## Configuration

FaceLink uses a configuration file (`config.json`) to store folder paths for future use. You can manually edit this file if needed.
The file is created after saving, therefore save the configuration after creating. After that, it will automatically load for the next use.
## Contributing

Contributions to FaceLink are welcome!.

## Acknowledgments

- [face_recognition](https://github.com/ageitgey/face_recognition): A face recognition library for Python.
- [PySimpleGUI](https://pysimplegui.readthedocs.io/): A Python GUI framework.
- [termcolor](https://pypi.org/project/termcolor/): A simple library for ANSI color formatting.
- [Pillow](https://pillow.readthedocs.io/en/stable/): A Python Imaging Library.
