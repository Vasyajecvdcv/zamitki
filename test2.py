from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,QInputDialog,QMessageBox
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow

notes=[]
note=[]
class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.list_notes.itemClicked.connect(self.show_note)
        self.ui.btn_create_note.clicked.connect(self.add_note)
        self.ui.btn_save_note.clicked.connect(self.save_note)

    def show_note(self):
        key=self.ui.list_notes.selectedItems()[0].text()
        for note in notes:
            if key in note:

                self.ui.text.setText(note[1])
                self.ui.list_tags.clear()
                self.ui.list_tags.addItem(note[2])

    def add_note(self):
        name,ok=QInputDialog.getText(self,"Додати замітку","Назва замітки")
        if ok and name !="":
            note=list()
            note=[name,"",[]]
            notes.append(note)
            self.ui.list_notes.addItem(note[0])
            filename=str(len(notes)-1)+".txt"
            with open(filename,"w",encoding="utf-8")as file:
                file.write(note[0]+"\n")


    def save_note(self):
        if self.ui.list_notes.selectedItems():
            key=self.ui.list_notes.selectedItems()[0].text()
            index=0
            for note in notes:
                if key in note:

                    note[1]=self.ui.text.toPlainText()
                    with open(str(index)+".txt","w",encoding="utf-8")as file:
                        file.write(notes[0]+"\n")
                        file.write(note[1]+"\n")
                        for tag in note[2]:
                            file.write(tag+" ")
                        file.write(note[2])
                index+=1
        else:
            win=QMessageBox()
            win.setText("Замітка для збереження  не вибрана!")
            win.exec()

app=QApplication([])
ex=Widget()
ex.show()
name=0
while True:
    filename=str(name)+".txt"
    try:
        with open(filename,"r",encoding="utf-8")as file:
            for line in file:
                line=line.replace("\n","")
                note.append(line)
        note[2]=note[2].split(" ")
        notes.append(note)
        note=[]
    except:
        break
for note in notes:
    ex.ui.list_notes.addItem(note[0])


app.exec_()
