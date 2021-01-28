#taken reference from: https://stackoverflow.com/questions/41570359/how-can-i-convert-a-py-to-exe-for-python

from cx_Freeze import setup, Executable

base = None    

executables = [Executable("main.py", base=base)]

packages = ["idna","requests","random","art"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "wordchaindestroyer",
    options = options,
    version = "1.0",
    description = 'on9 word chain destroyer bot',
    executables = executables
)
