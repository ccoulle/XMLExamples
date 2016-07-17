#!/usr/bin/python
# Demonstrating SAX-based parsing of XML

import sys
import xml.sax
SPACES=2

class Model( xml.sax.ContentHandler ):
  """Custom xml.sax.ContentHandler"""

  def __init__(self):
    xml.sax.ContentHandler.__init__(self)
    self.rootTag = True
    self.spaces = SPACES
    self.line = ''
    self.docList = []

  def clearDocument(self):
    self.docList = []

  def getDocumentList(self):
    return self.docList

  def startElement( self, name, attributes ):
    if self.rootTag:
      self.rootTag = False
    else:
      for x in range(0, self.spaces):
        self.line += ' '
      self.line += name+': '
    for attribute in attributes.getNames():
      print attribute, attributes.getValue( attribute )
    self.spaces += SPACES

  def endElement( self, name ) :
    self.spaces -= SPACES

  def characters( self, content ) :
    # strip only removes spaces!
    content = content.strip()
    if content: 
      self.line += content
      self.line += '\n'
      self.docList.append(self.line)
      self.line = ''

  def loadFile(self, filename):
    try:
      parser = xml.sax.make_parser()
      parser.setContentHandler( self )
      parser.parse(filename)
      docList = self.docList
      self.docList = []
      for x in docList:
        self.docList.append(x.rstrip())
    except IOError, message:
      print "Error reading file: ", message
    except xml.sax.SAXParseException, message:
      print "Error parsing file: ", message

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print "usage:", sys.argv[0], "<xml file>"
    sys.exit()
  model = Model()
  model.loadFile(sys.argv[1])
  docList = model.getDocumentList()
  for x in docList:
    print x
