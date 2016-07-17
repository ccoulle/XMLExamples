#!/usr/bin/python

import sys
import xml.sax
import Tkinter as tk
import tkFileDialog
import include.model

GEOMETRY = '590x570+200+10'
WIDTH=66
HEIGHT=30

class View(object):
  def __init__(self, controller):
    root = tk.Tk()
    root.bind('<Escape>', lambda event: sys.exit())
    root.title("XML File Reader")
    root.geometry(GEOMETRY)
    self.docList = []
    self.controller = controller

    # define options for opening or saving a file
    self.file_opt = options = {}
    options['defaultextension'] = '' # couldn't figure out how this works
    options['filetypes'] = [('xml files', '.xml')]
    options['initialfile'] = 'xmlData/movies.xml'
    options['parent'] = root
    options['title'] = 'Get file to read:'

    frame1 = tk.Frame(root)
    frame1.config(padx=5, pady=5, bd=5, relief=tk.RAISED, bg='#00ff00')
    frame1.pack(side=tk.TOP)
    scrollbar = tk.Scrollbar(frame1)
    scrollbar.pack( side = tk.RIGHT, fill=tk.Y )

    self.mylist = tk.Listbox(frame1, yscrollcommand = scrollbar.set)
    self.mylist.pack( side = tk.LEFT, fill = tk.BOTH )
    self.mylist.config( bg='white', bd=5 )
    self.mylist.config(width=WIDTH, height=HEIGHT)
    self.mylist.bind('<Double-1>', self.displayItem)

    frame2 = tk.Frame(root)
    frame2.config(padx=5, pady=5, bd=5, relief=tk.RAISED, bg='#5f9ea0')
    frame2.pack(side=tk.BOTTOM, fill=tk.BOTH)
    clear = tk.Button(frame2, text="Clear", command=self.clearText)
    clear.pack(side=tk.LEFT, anchor=tk.W)
    clear.config(padx=5, pady=5, bd=5, relief=tk.RAISED, bg='#00ff00')
    load = tk.Button(frame2, text="Load", command=self.loadFile)
    load.pack(side=tk.LEFT, anchor=tk.W)
    load.config(padx=5, pady=5, bd=5, relief=tk.RAISED, bg='#00ff00')

    quit = tk.Button(frame2, text="Quit", command=sys.exit)
    quit.pack(side=tk.RIGHT, anchor=tk.E)
    quit.config(padx=5, pady=5, bd=5, relief=tk.RAISED, bg='#ff0000')

    scrollbar.config( command = self.mylist.yview )

  def displayItem(self, event):
    index = self.mylist.curselection()
    label = self.mylist.get(index)
    print "You selected:", label

  def clearText(self):
    self.controller.clearDocument()
    self.mylist.delete(0, tk.END)

  def loadFile(self):
    self.clearText()
    fileName = tkFileDialog.askopenfilename(**self.file_opt)
    if not fileName:
      return
    self.docList = self.controller.loadFile(fileName)
    for x in self.docList:
      self.mylist.insert(tk.END, x)

if __name__ == "__main__":
  view = View()
  tk.mainloop()
