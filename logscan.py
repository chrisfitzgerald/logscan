import PySimpleGUI as sg
import os.path
from scan import logscan

# Add theme
sg.theme('Reddit')	

# Objects in the window.
layout = [  [sg.Text('Select Log File:')],
            [sg.In(key='_file_'), sg.FileBrowse()],
            [sg.Button('Scan'), sg.Button('Cancel')],
            [sg.Output(size=(100, 20))] ]

# Create the Window
window = sg.Window('LogScan', layout, icon='logscan.ico')

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    input_text = str(values['_file_'])
    is_file = os.path.isfile(input_text)
    if event == sg.WIN_CLOSED or event == 'Cancel':	# if user closes window or clicks cancel
        break
    if event == 'Scan':
        if input_text == 'about':
            print('\nThis is Logscan Version <<YOURVERSION>>.\n \nVisit: <<YOURLINK>> for more information.\n\n')
        elif is_file is False:
            print('\nThis is not a valid file. Please check the file path.')
        elif values['_file_']:
            logscan(values['_file_'])
window.close()
