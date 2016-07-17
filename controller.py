import sys
import xml.sax
import Tkinter as tk
import tkFileDialog
import view
import model

class Controller(object):
  def __init__(self):
    self.view = view.View(self)
    self.model = model.Model()

  def clearDocument(self):
    self.model.clearDocument()

  def loadFile(self, fileName):
    self.model.loadFile(fileName)
    docList = self.model.getDocumentList()
    return docList




if __name__ == "__main__":
  box = Controller()
  tk.mainloop()
