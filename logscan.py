import PySimpleGUI as sg
from scan import logscan

sg.theme('Reddit')	# Add theme

# Objects in the window.
layout = [  [sg.Text('Select Log File:')],
            [sg.In(key='_file_'), sg.FileBrowse()],
            [sg.Button('Scan'), sg.Button('Cancel')],
            [sg.Output(size=(100, 20))] ]

# Create the Window
window = sg.Window('LogScan v1', layout, icon='logscan.ico')

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':	# if user closes window or clicks cancel
        break
    if event == 'Scan':
        if values['_file_']:
            logscan(values['_file_'])
        elif values['']:
            print('we could not find this file')

window.close()
