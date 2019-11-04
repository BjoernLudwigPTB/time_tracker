import PySimpleGUIQt as sg
import pandas
import os
import sys
import datetime
import subprocess

# log file location
log_file = os.path.join("log.csv")
if not os.path.exists(log_file):
    f = open(log_file, 'a')
    f.write('date,action\n')
    f.close()

# load labels from file
config_file = os.path.join("config_labels.csv")
df = pandas.read_csv(config_file)

# put labels into layout
options = [row['label_text'] for i, row in df.iterrows()]
menu_def = ['Menu', [*options, '---', 'Done', '---', 'Show report', '---', 'Exit']]

default_icon = os.path.join('icons','23F1.png')

tray = sg.SystemTray(menu=menu_def, filename=default_icon)

while True:
    menu_item = tray.Read(timeout=5000)  # timeout of 5 seconds

    print(menu_item)

    # end program, if selected
    if menu_item == 'Exit':
        break

    if menu_item == "Show report":
        p = subprocess.Popen([sys.executable, 'report_generator.py'], cwd=os.getcwd())
        continue

    # otherwise: log entry and change icon
    if menu_item not in [None, '__TIMEOUT__', '__ACTIVATED__']:

        # log
        report_string = str(datetime.datetime.utcnow()) + ',' + menu_item + '\n'
        f = open(log_file, 'a')
        f.write(report_string)
        f.close()

        # change icon according to selected item
        if menu_item == "Done":
            icon_path = default_icon
        else:
            icon_path = df[df['label_text'] == menu_item]['label_icon'].values[0]
        tray.Update(filename = icon_path)

tray.close()
