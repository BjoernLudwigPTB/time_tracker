import PySimpleGUIQt as sg
import os
import sys
import datetime
import subprocess
import json
import shlex

# read config file
f = open("config.json", "r")
config = json.load(f)
f.close()

# log file location
log_file = os.path.expanduser(config["log_file"])
if not os.path.exists(log_file):
    f = open(log_file, 'a')
    f.write('date,action\n')
    f.close()

# put labels into layout
options = [entry[0] for entry in config["labels"]]
menu_def = ['Menu', [*options, '---', 'Done', '---', 'Show report', 'Edit log', '---', 'Exit']]

default_icon = os.path.join(config["default_icon"])

tray = sg.SystemTray(menu=menu_def, filename=default_icon)

while True:
    menu_item = tray.Read(timeout=5000)  # timeout of 5 seconds

    print(menu_item)

    # end program, if selected
    if menu_item == 'Exit':
        break

    elif menu_item == "Show report":
        cmd = shlex.split(config["report"].format(PY_BIN=sys.executable).replace("\\", "/"))
        p = subprocess.Popen(cmd, cwd=os.getcwd())
        continue

    elif menu_item == "Edit log":
        cmd = shlex.split(config["editor"].format(LOG_FILE=log_file).replace("\\", "/"))
        p = subprocess.Popen(cmd)
        continue

    # otherwise: log entry and change icon
    elif menu_item not in [None, '__TIMEOUT__', '__ACTIVATED__']:

        # log
        if config["use_utc"]:
            timestamp = datetime.datetime.utcnow()
        else:
            timestamp = datetime.datetime.now()
        
        report_string = str(timestamp.replace(microsecond=0)) + ',' + menu_item + '\n'
        f = open(log_file, 'a')
        f.write(report_string)
        f.close()

        # change icon according to selected item
        if menu_item == "Done":
            icon_path = default_icon
        else:
            icon_path = [icon for name, icon in config["labels"] if name == menu_item][0]
        tray.Update(filename = icon_path)

tray.close()
