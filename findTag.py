#!/usr/bin/python
# Demonstrating SAX-based parsing of XML

import sys
from xml.sax import parse, SAXParseException, ContentHandler

class TagInfoHandler( ContentHandler ):
  """Custom xml.sax.ContentHandler"""

  def __init__(self, tagName ):
    ContentHandler.__init__(self)
    self.tagName = tagName

  def startElement( self, name, attributes ):
    if name == self.tagName:
      print "Element name:", name

  def endElement( self, name ) : pass
  def characters( self, content ) : pass

def main():
  print "Beginning XML parsing..."
  if len(sys.argv) != 2:
    print "usaage:", sys.argv[0], "<xml file>"
    sys.exit()
  file = sys.argv[1]
  tagname = raw_input( "Enter a tag to search for: " )
  try:
    parse ( file, TagInfoHandler( tagname ) )
  except IOError, message:
    print "Error reading file: ", message
  except SAXParseException, message:
    print "Error parsing file: ", message

if __name__ == "__main__":
  main()
