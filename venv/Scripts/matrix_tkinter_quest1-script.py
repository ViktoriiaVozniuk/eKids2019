#!C:\Projects\PythonProjects\eKids2019\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'matrix-tkinter-quest1','console_scripts','matrix_tkinter_quest1'
__requires__ = 'matrix-tkinter-quest1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('matrix-tkinter-quest1', 'console_scripts', 'matrix_tkinter_quest1')()
    )
