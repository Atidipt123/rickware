'''
This file is used to make the exe. 
python setup.py build
'''

from cx_Freeze import setup, Executable

base = None    

executables = [Executable("main.py", base=base , icon="assets\\logo.ico")]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Rickware",
    options = options,
    version = "1.0",
    description = 'Rickware 1.0',
    executables = executables
)
