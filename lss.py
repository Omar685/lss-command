from os import mkdir, name as _name, path, system
from lib import pystyle
from time import sleep
import sys


def _start(color: str) -> str:
   return f"\033[38;2;{color}m"

def _makergbcol(var1: list, var2: list) -> list:
   col = list(var1[:12])
   for _col in var2[:12]:
      col.append(_col)
   for _col in reversed(col):
      col.append(_col)
   return col

ERROR_RED = _start('255;0;0')
RED_TO_PURPLE = pystyle.Colors.red_to_purple
PURPLE_TO_BLUE = pystyle.Colors.purple_to_blue
RED_TO_BLUE = _makergbcol(RED_TO_PURPLE, PURPLE_TO_BLUE)


class Errors:
   class DashError:
      def __init__(self, proj_name) -> None:
            print()
            text = f"DashError: name '{proj_name}' none dash.\n"
            pystyle.Write.Print(text, interval=0.0, color=ERROR_RED, end='\n')
            print()
            system("pause")
            sys.exit()
   class FileExistsError: 
      def __init__(self, filename) -> None:
            print()
            text = f"FileExistsError: name '{filename}' is not defined"
            pystyle.Write.Print(text, interval=0.0, color=ERROR_RED, end='\n')
            print()
            system("pause")
            sys.exit()
   class ColorError: 
      def __init__(self, colorname) -> None:
            print()
            text = f"ColorError: name '{colorname}' is not color"
            pystyle.Write.Print(text, interval=0.0, color=ERROR_RED, end='\n')
            print()
            system("pause")
            sys.exit()
   class CreateFileError: 
      def __init__(self, filename) -> None:
            print()
            text = f"CreateFileError: fail create '{filename}' file."
            pystyle.Write.Print(text, interval=0.0, color=ERROR_RED, end='\n')
            print()
            system("pause")
            sys.exit()
   class IsExistsError: 
      def __init__(self) -> None:
            text = f"A subdirectory or file black already exists."
            pystyle.Write.Print(text, interval=0.0, color=ERROR_RED, end='\n')
            system("pause")
            sys.exit()

system("cls" if _name == "nt" else "clear")
project_name = pystyle.Write.Input("Enter a project name for create: ", color=RED_TO_BLUE, end='\n')
if path.exists(project_name):
   Errors.IsExistsError()
else:
   for dash in project_name:
      if dash == "-":
         Errors.DashError(project_name)
      else: pass
   
   try:
      mkdir(project_name)
      pystyle.Write.Print("Loading...", interval=0.0, color=RED_TO_BLUE, end='\n')
   except: 
      pystyle.Write.Print("NameNone: please enter name for project.", interval=0.0, color=ERROR_RED, end='\n\n')
      sys.exit()
   sleep(2)
      
pystyle.Write.Print("Loading...", interval=0.0, color=RED_TO_BLUE, end='\n')
sleep(2)
mkdir(f"./{project_name}/API")
pystyle.Write.Print("Done create API", interval=0.0, color=RED_TO_BLUE, end='\n')
sleep(2)
mkdir(f"./{project_name}/Style")
pystyle.Write.Print("Done create Style", interval=0.0, color=RED_TO_BLUE, end='\n')
sleep(2)
mkdir(f"./{project_name}/resources")
pystyle.Write.Print("Done create resources", interval=0.0, color=RED_TO_BLUE, end='\n')
sleep(2)
path.exists("resources")
mkdir(f"./{project_name}/resources/fonts")
sleep(2)
pystyle.Write.Print("Done create fonts", interval=0.0, color=RED_TO_BLUE, end='\n')
mkdir(f"./{project_name}/resources/icons")
sleep(2)
pystyle.Write.Print("Done create icons", interval=0.0, color=RED_TO_BLUE, end='\n')
mkdir(f"./{project_name}/resources/logo_app")
sleep(2)
pystyle.Write.Print("Done create logos_app", interval=0.0, color=RED_TO_BLUE, end='\n')

with open(f"./{project_name}/API/interface.ui", 'w') as file_interface_ui: 
   file_interface_ui.write(f'''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>{project_name}</class>
 <widget class="QMainWindow" name="{project_name}">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>{project_name}</string>
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
   file_init_.write(f"""# ####### {project_name.upper()}-PROJECT #########
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
   file_fun.write("""# FUNCTION FILE
""")
with open(f"./{project_name}/API/MainWindow.py", 'w') as file_main_window: 
   file_main_window.write(f'''from API.Ui_interface import Ui_{project_name}
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from API.function import *
import json


class MainWindow(QMainWindow):
   def __init__(self) -> None:
      super().__init__()
      self.ui = Ui_{project_name}()
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
   file_style_CSS.write("/* This file for style application */")

with open(f"./{project_name}/{project_name}.py", 'w') as file_start: 
   file_start.write("""# This file for start a application.

from API import main

if __name__ == "__main__":
   main()
""")
system(f"pyuic5 -x ./{project_name}/API/interface.ui -o ./{project_name}/API/Ui_interface.py")

database = pystyle.Write.Input("Are you database (y/n): ", interval=0.0, color=RED_TO_BLUE, end='\n').lower()
if database == "y":
   mkdir(f"./{project_name}/Database")
   pystyle.Write.Print("Loading...", interval=0.0, color=RED_TO_BLUE, end='\n') 
   sleep(2)
   with open(f"./{project_name}/API/Database.py", 'w') as file_database: 
      file_database.write("# THIS FILE FOR CREATE DATABASE\nimport sqlite3")
else: pass
mkdir(f"./{project_name}/Json")
pystyle.Write.Print("Loading...", interval=0.0, color=RED_TO_BLUE, end='\n') 
sleep(2)
pystyle.Write.Print("Done Json Folder", interval=0.0, color=RED_TO_BLUE, end='\n') 
with open(f"./{project_name}/Json/style.json", 'w') as json: 
   json.write("{\n"
f'    "TitleApplication": "{project_name}"'
"\n}\n"
)
   
system("pause")
