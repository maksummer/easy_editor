from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from ui import Ui_MainWindow
import os
from imageprocesor import ImageProccesor

app = QApplication([])
win = QMainWindow()

ui = Ui_MainWindow()
ui.setupUi(win)
#-----------------------------
workdir = ""
img_proc = ImageProccesor(ui)

def chooseWorkDir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
    print(workdir)


def filter(files, extensions):
    graphical_files = []

    for file in files:
        for ext in extensions:
            if file.endswith(ext):
               graphical_files.append(file)

    return graphical_files

def showFilenamesList():
    chooseWorkDir()
    extensions = [".png", ".jpg", ".jpeg", ".bmp", ".gif"]
    
    filenames = os.listdir(workdir)
    filenames = filter(filenames, extensions)
    print(filenames)
    ui.files_list.clear()
    ui.files_list.addItems(filenames)
ui.dir_btn.clicked.connect(showFilenamesList)

def showChossenImage():
    if ui.files_list.currentItem():
        filename = ui.files_list.currentItem().text()
        img_proc.open(workdir, filename)
        img_proc.show()


ui.files_list.currentItemChanged.connect(showChossenImage)
#-------------------------------
win.show()
app.exec()
