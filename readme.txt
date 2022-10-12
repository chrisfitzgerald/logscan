░█▒░░▄▀▄░▄▀▒░▄▀▀░▄▀▀▒▄▀▄░█▄░█
▒█▄▄░▀▄▀░▀▄█▒▄██░▀▄▄░█▀█░█▒▀█

![logScan.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/900e70f1-900c-4939-912f-d3a06ace1380/logScan.png)

## Installation:

1) Install Python 3.9 or higher - [https://www.python.org/downloads/](https://www.python.org/downloads/)

2) Install PySmipleGUI - [https://www.pysimplegui.org/en/latest/](https://www.pysimplegui.org/en/latest/)

```powershell
pip install pysimplegui
or
pip3 install pysimplegui
```

2) Replace if statements in scan.py:

```python
#BEFORE
for line in searchfile:
            if '<<Replace with error Text' in line:
                print (line + '\n   See: <<Replace with your documentation>> \n')

#AFTER
for line in searchfile:
            if '[0x0001]' in line:
                print (line + '\n   See: https://github.com/chrisfitzgerald/logscan \n')
```

3) Optional - Update about prompt in logscan.py:

```python
#BEFORE
if event == 'Scan':
        if input_text == 'about':
            print('\nThis is Logscan Version <<YOURVERSION>>.\n \nVisit: <<YOURLINK>> for more information.\n\n')

#AFTER
if event == 'Scan':
        if input_text == 'about':
            print('\nThis is Logscan Version 1.1.\n \nVisit: https://github.com/chrisfitzgerald/logscan for more information.\n\n')
```

4) Test by running:

```python
python logscan.py
```

5) Compile to executable:

a) Installer pyinstaller - [https://pyinstaller.org/en/stable/](https://pyinstaller.org/en/stable/)

```powershell
pip install -U pyinstaller
```

     ensure your environment variable is set - ([help](https://stackoverflow.com/questions/45951964/pyinstaller-is-not-recognized-as-internal-or-external-command))

b) Compile:

```powershell
pyinstaller --onefile -w --icon=logscan.ico logscan.py
```

6) Your shareable executable will be located in the logscan/dist/ directory