"""
LINK: https://github.com/Omar685/lss-command
"""

from os import mkdir, path, system, stat
from utils import sleep, get_platform
import sys

def exists(path):
    try:
        stat(path)
    except (OSError, ValueError):
        return False
    return True

class Error(Exception):
  def __new__(cls, *args, **kwargs):
    instance = super(Error, cls).__new__(cls)
    return instance
  
  def __init__(self, *args):
    self.message = ' '.join(map(str, args)) if args else None
    super().__init__(self.message)

  def __str__(self):
    return f"{self.__class__.__name__}: {self.message}" \
        if self.message \
        else f"{self.__class__.__name__}"
  
  def __repr__(self):
    return f"{self.__class__.__name__} message=({repr(self.message)})"
  
  def __or__(self, other):
    if isinstance(other, Error):
      return self.message or other.message
    raise TypeError(f"unsupperted operand type(s) for |: '{self.__class__.__name__}' and '{type(other).__name__}'")
  
class FileAlreadyExistsErrors(Error): ...
class ColorError(Error): ...
class CreateFileError(Error): ...
class IsExistsError(Error): ...
class NameNone(Error): ...

_name = get_platform()
system("cls" if _name == 'Windows' else "clear")

project_name = input("Enter a project name for create: ")
if path.exists(project_name):
  error_is_exists_error = IsExistsError("A subdirectory or file black already exists.")
  print(error_is_exists_error)
  exit()
else:
  for dash in project_name:
    if dash == '-':
      replaces_dash = project_name.replace("-", "_")
    else: pass
  
  try:
    mkdir(project_name)
    print("Loading...")
  except:
    error_name_none = NameNone("please enter name for project.")
    print(error_name_none)
    sys.exit()
  sleep(2)

project_type = int(input("Enter a project type \n1. Console \n2. GUI PyQt5 \n3. GUI tkinter \n4. Web\n>> "))
if project_type == 1: 
  with open(f"./{project_name}/main.py", "w") as console_file:
    console_file.write("print('Hello, World!')")
elif project_type == 2: 
  print("Loading...")
  sleep(1)
  mkdir(f"./{project_name}/API")
  print("Done create API")
  sleep(1)
  mkdir(f"./{project_name}/Style")
  print("Done create Style")

  mkdir(f"./{project_name}/resources")
  print("Done create resources")
  sleep(2)
  exists("resources")
  mkdir(f"./{project_name}/resources/fonts")
  sleep(2)
  print("Done create fonts")
  mkdir(f"./{project_name}/resources/icons")
  sleep(2)
  print("Done create icons")
  mkdir(f"./{project_name}/resources/logo_app")
  sleep(2)
  print("Done create logos_app")

  
  with open(f"./{project_name}/API/interface.ui", 'w') as file_interface_ui: 
    file_interface_ui.write(f'''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
<class>{replaces_dash}</class>
<widget class="QMainWindow" name="{replaces_dash}">
  <property name="geometry">
  <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
  </rect>
  </property>
  <property name="windowTitle">
  <string>{replaces_dash}</string>
  </property>
  <widget class="QWidget" name="centralwidget"/>
  <widget class="QMenuBar" name="menubar">
  <property name="geometry">
    <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>22</height>
    </rect>
  </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
</widget>
<resources/>
<connections/>
</ui>
''')
  with open(f"./{project_name}/API/__init__.py", 'w') as file_init_: 
   file_init_.write(f"""# ####### {replaces_dash.upper()}-PROJECT #########
from PyQt5.QtWidgets import QApplication
import sys
from API.MainWindow import MainWindow

def main():
   app = QApplication(sys.argv)
   window = MainWindow()
   window.show()
   sys.exit(app.exec())
""")
  with open(f"./{project_name}/API/function.py", 'w') as file_fun: 
   file_fun.write("""# FUNCTION FILE \n""")
  with open(f"./{project_name}/API/MainWindow.py", 'w') as file_main_window: 
   file_main_window.write(f'''from API.Ui_interface import Ui_{replaces_dash}
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from API.function import *
import json


class MainWindow(QMainWindow):
   def __init__(self) -> None:
      super().__init__()
      self.ui = Ui_{replaces_dash}()
      self.ui.setupUi(self)

      with open("./Style/style.css", 'r') as style:
         code = style.read()
         self.setStyleSheet(code)
      
      with open("./Json/style.json", 'r') as jsons:
         JsonCode = jsons.read()
         load_json = json.loads(JsonCode)
         name_project = load_json["TitleApplication"]


      self.setWindowTitle(str(load_json["TitleApplication"]))

if __name__ == "__main__":
   app = QApplication(argv)
   window = MainWindow()
   window.show()
   sys.exit(app.exec_())
''')
  with open(f"./{project_name}/Style/style.css", 'w') as file_style_CSS: 
   file_style_CSS.write("/* This file for style application */\n")

  with open(f"./{project_name}/{replaces_dash}.py", 'w') as file_start: 
   file_start.write("""# This file for start a application.

from API import main

if __name__ == "__main__":
   main()
""")
  system(f"pyuic5 -x ./{project_name}/API/interface.ui -o ./{project_name}/API/Ui_interface.py")


  
  database = input("Are you database (y/n): ")
  if database == "y":
    mkdir(f"./{project_name}/Database")
    print("Loading...") 
    sleep(2)
    with open(f"./{project_name}/API/Database.py", 'w') as file_database: 
        file_database.write("# THIS FILE FOR CREATE DATABASE\nimport sqlite3")
  else: pass
  mkdir(f"./{project_name}/Json")
  print("Loading...") 
  sleep(2)
  print("Done Json Folder")
  with open(f"./{project_name}/Json/style.json", 'w') as json: 
    json.write("{\n"
  f'    "TitleApplication": "{replaces_dash}"'
  "\n}\n"
  )
    
  system("pause")
  exit()

elif project_type == 3: 
  with open(f"./{project_name}/main.py", 'w') as file_init_: 
   file_init_.write(f"""# ####### {replaces_dash.upper()}-PROJECT #########
import tkinter as tk

class {replaces_dash}:
  def __init__(self, root: object) -> None:
    self.root = root
    
    self.root.title("{replaces_dash}")

    screen_width = self.root.winfo_screenwidth()
    screen_height = self.root.winfo_screenheight()
    x = (screen_width // 2) - (400 // 2)
    y = (screen_height // 2) - (300 // 2)

    geometry = "400x300+?1+?2"
    geometry = geometry.replace("?1", str(x))
    geometry = geometry.replace("?2", str(y))
    self.root.geometry(geometry)

    self.main_frame = tk.Frame(self.root)
    self.main_frame.pack(expand=True)

    self.label = tk.Label(self.main_frame, text="Hello, World!", font=("Helvetica", 24))
    self.label.pack(pady=50, padx=100)

    self.main_frame.grid_rowconfigure(0, weight=1)
    self.main_frame.grid_columnconfigure(0, weight=1)

if __name__ == "__main__":
  root = tk.Tk()
  app = {replaces_dash}(root)
  root.mainloop()
""")
   
elif project_type == 4: 
  with open(f"./{project_name}/app.py", 'w') as app_file:
    app_file.write("""from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

if __name__ == "__main__":
  app.run(port=3000, debug=True)
""")
    sleep(2)
    mkdir(f"./{project_name}/templates")
    sleep(2)
    with open(f'./{project_name}/templates/index.html', 'w') as html_file:
      html_file.write("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Document</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
  <h1>Hello, World!</h1>
</body>
</html>
""")
  mkdir(f"./{project_name}/static")
  sleep(2)
  with open(f"./{project_name}/static/style.css", 'w') as style:
    style.write("""body {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 0;
}

h1 {
  text-align: center;
}
""")