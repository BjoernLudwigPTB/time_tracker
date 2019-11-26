# time tracker

Big system tray utility to allow you to monitor your time usage
. *time_tracker* is written to be used in the
[KDE Plasma desktop environment](https://kde.org/plasma-desktop) and is
prepared to use some of its basic components like

*   [konsole](https://konsole.kde.org/),
*   [kate](https://kde.org/applications/utilities/org.kde.kate),
*   [kdialog](https://kde.org/applications/utilities/org.kde.kdialog),
*   and a few common linux components
    *   [bash](https://www.gnu.org/software/bash/bash.html),
    *   [nohup](https://www.gnu.org/software/coreutils/manual/coreutils.html#nohup-invocation).

Icons are taken from [openmoji.org/](https://openmoji.org).

A small visualization script is provided by clicking the *Show report* link
 in the GUI.

# Getting started

1.  [Clone the repo](
        https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository
    )
1.  Navigate to repo.
    ```bash
    $ cd /your/path/to/repo
    ```
1.  [Create virtual environment](
        https://docs.python.org/3/library/venv.html#creating-virtual-environments
    ).
    ```bash
    $ python3 -m venv /path/to/new/virtual/environment
    ```
1.  [Install dependencies into new virtual environment from *requirements.txt*](
        https://pip.pypa.io/en/stable/user_guide/#requirements-files
    ).
    ```bash
    $ /path/to/new/virtual/environment/bin/pip install -r requirements.txt
    ```
1.  Adapt the [launch_tray_app.sh](launch_tray_app.sh). Comments should be
    sufficiently explaining.
1.  Adapt the [config.json](config.json), which is hopefully sufficiently
    self explaining.
1.  Run the app from the commandline,
    ```bash
    $ ./launch_tray_app.sh
    ```
    [create a .desktop file](
        https://wiki.archlinux.org/index.php/Desktop_entries#File_example
    ) or [put it in autostart](
        https://wiki.archlinux.org/index.php/Autostart_applications
    ).
