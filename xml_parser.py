#!/usr/bin/env python

from xml.dom import minidom
import urllib

class XmlParser:
        def __init__(self, source):                
                print "parsing stream list..."
		self.url = source
		usock = urllib.urlopen(source)
                self.xmldoc = minidom.parse(usock)
		usock.close()
		print self.xmldoc.toxml()
                print "parsed ok"
        def build_url_list(self):
		self.list = []
                print "building list"
		cams =self.xmldoc.getElementsByTagName('rem_addr')
                for cam in cams:
			addr = cam.attributes['href']
			print "Adding Cam: %s" % addr.value
			self.list.append(addr.value)
		return self.list
	def getText(self, nodelist):
    		rc = []
    		for node in nodelist:
        		if node.nodeType == node.TEXT_NODE:
            			rc.append(node.data)
    		return ''.join(rc)	
def main():
	cameras = 'stream_list.xml'
	p = XmlParser(cameras)
	list = p.build_url_list()
	print "here is the ful list"
	for item in list:
		print item
if __name__ == '__main__':
    main()
