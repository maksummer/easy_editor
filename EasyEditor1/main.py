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


ui.pushButton.clicked.connect(img_proc.do_bw)
ui.left_btn.clicked.connect(img_proc.do_left)
ui.right_btn.clicked.connect(img_proc.do_right)
ui.sharp_btn.clicked.connect(img_proc.do_sharp)
ui.mirror_btn.clicked.connect(img_proc.do_mirror)


#-------------------------------
win.show()
app.exec()
