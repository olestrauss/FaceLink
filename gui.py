import PySimpleGUI as sg
import json
import os
import sys
import subprocess
from main import Recognizer

# Create a function to load configuration from the file
def load_config():
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
        return config
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Create a function to save configuration to the file
def save_config(config):
    with open('config.json', 'w') as f:
        json.dump(config, f)

# Load the configuration if it exists or use defaults
config = load_config()

# Define default values for folder paths
default_input_folder = ''
default_database_folder = ''
default_output_folder = ''

default_input_folder = config.get('input_folder', default_input_folder)
default_database_folder = config.get('database_folder', default_database_folder)
default_output_folder = config.get('output_folder', default_output_folder)

image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

sg.theme('LightGreen')
face_rec = Recognizer()

# Create a function to switch to the completion screen
def show_completion_screen(imgs_allocated, output_folder):
    sg.theme('DarkGrey5')  # Apply a different theme for the completion screen

    layout_completion = [
        [sg.Text('FaceLink', font=("Helvetica", 20), justification='center')],
        [sg.Text(f'{imgs_allocated} images have been allocated.', justification='center')],
        [sg.Button('Exit', size=(10, 1), pad=(10, 10)), sg.Button('Open Output Folder', size=(15, 1), pad=(10, 10))]
    ]

    window_completion = sg.Window('FaceLink - Completion', layout_completion, finalize=True)

    while True:
        event_completion, _ = window_completion.read()

        if event_completion == sg.WINDOW_CLOSED or event_completion == 'Exit':
            break
        elif event_completion == 'Open Output Folder':
            subprocess.Popen(['explorer', os.path.abspath(output_folder)])

    window_completion.close()

layout = [
    [sg.Text('FaceLink', font=("Helvetica", 20), justification='center')],
    [sg.Text('Input Set', size=(10, 1)), sg.InputText(key='-INPUT-', default_text=default_input_folder), sg.FolderBrowse(initial_folder=default_input_folder)],
    [sg.Text('Database', size=(10, 1)), sg.InputText(key='-DATABASE-', default_text=default_database_folder), sg.FolderBrowse(initial_folder=default_database_folder)],
    [sg.Text('Output', size=(10, 1)), sg.InputText(key='-OUTPUT-', default_text=default_output_folder), sg.FolderBrowse(initial_folder=default_output_folder)],
    [sg.Button('Save'), sg.Button('Start', pad=(15, 0))],
    [sg.ProgressBar(max_value=20, orientation='h', size=(20,20), expand_x=True, key='-PBAR-')]
]


window = sg.Window('FaceLink', layout, resizable=True)

event, values = window.read()

print(values)

if event == 'Start':

    input_folder = resource_path(values['-INPUT-'])
    database_folder = resource_path(values['-DATABASE-'])
    output_folder = resource_path(values['-OUTPUT-'])
    
    try:
        #create all encodings for all images in database at once
        face_rec.create_encodings(database_folder)

        total_images = len(os.listdir(input_folder))
        
        #Update the progress bar maximum value based on the number of images
        window['-PBAR-'].update(current_count=0, max=total_images)

        #iterate through input set (done one at a time to be able to update progress bar)
        for i, img in enumerate(os.listdir(input_folder)):
            face_rec.match_face(img, output_folder, input_folder)
            window['-PBAR-'].update(current_count=i+1)

        window.close()
        # Show completion screen with output folder
        show_completion_screen(face_rec.imgs_allocated, resource_path(output_folder))  

    except Exception as e:
        print(f'An error occurred: {str(e)}')

elif event == 'Save':
    # Get folder paths from input fields
    input_folder = values['-INPUT-']
    database_folder = values['-DATABASE-']
    output_folder = values['-OUTPUT-']

    # Create a dictionary to store the configuration
    config = {
        'input_folder': input_folder,
        'database_folder': database_folder,
        'output_folder': output_folder
    }

    # Save the configuration to the file
    save_config(config)




print(f'You clicked {event}')
print(f'Input Path: {values["-INPUT-"]}')
print(f'Database Path: {values["-DATABASE-"]}')
print(f'Output Path: {values["-OUTPUT-"]}')
