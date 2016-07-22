#!/usr/bin/python
# Demonstrating SAX-based parsing of XML
import sys
import xml.sax

class Person(object):
  def __init__(self):
    self.firstName = None
    self.lastName = None
    self.points = None
  def setFirstName(self, fn):
    self.firstName = fn
  def setLastName(self, ln):
    self.lastName = ln
  def setPoints(self, pts):
    self.points = pts
  def getPerson(self):
    return self.firstName, self.lastName, self.points
  def __repr__(self):
    t = '('+self.firstName+','+self.lastName+','+self.points+')'
    return str(t)

class XmlReader( xml.sax.ContentHandler ):
  def __init__(self):
    xml.sax.ContentHandler.__init__(self)
    self.tag = ''
    self.person = None
    self.contacts = []

  def startElement( self, name, attributes ):
    self.tag = name

  def endElement( self, name ) :
    pass

  def characters( self, content ) :
    # strip only removes spaces!
    content = content.strip()
    if content: 
      if self.tag == 'fn': 
        self.person = Person()
        self.person.setFirstName(content)
      elif self.tag == 'ln': 
        self.person.setLastName(content)
      elif self.tag == 'pts': 
        self.person.setPoints(content)
        self.contacts.append(self.person)

def writeElement(FILE, tag, data):
  FILE.write('    <'+tag+'>')
  FILE.write(data)
  FILE.write('</'+tag+'>\n')
  

def writeXML(contacts):
  FILE = open("newnames.xml", 'w')
  FILE.write('<?xml version = "1.0"?>\n')
  FILE.write('<contacts>\n')
  for x in contacts:
    FILE.write('  <contact>\n')
    writeElement(FILE, 'fn', x.firstName) 
    writeElement(FILE, 'ln', x.lastName) 
    writeElement(FILE, 'pts', x.points) 
    FILE.write('  </contact>\n')
  FILE.write('</contacts>\n')
  FILE.close()

def printPeople(contacts):
  for x in contacts:
    print x

def main():
  print "Beginning XML processor..."
  if len(sys.argv) != 2:
    print "usaage:", sys.argv[0], "<xml file>"
    sys.exit()
  file = sys.argv[1]
  try:
    reader = XmlReader()
    xml.sax.parse ( file, reader )
    contacts = reader.contacts
    printPeople(contacts)
    #person = Person()
    #person.setFirstName("Mark")
    #person.setLastName("Melancin")
    #person.setPoints("88")
    #contacts.append( person )
    #l = [person]
    writeXML(contacts)
  except IOError, message:
    print "Error reading file: ", message
  except xml.sax.SAXParseException, message:
    print "Error parsing file: ", message

if __name__ == "__main__":
  main()
