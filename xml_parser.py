#!/usr/bin/env python

from xml.dom import minidom
import urllib

class IpCam:
	def __init__(self, name = None, loc_addr = None, rem_addr = None):
		self.name = name
		self.loc_addr = loc_addr
		self.rem_addr = rem_addr
	def update_name(self, name):
		self.name = name
		return self.name
	def update_loc_addr(self, addr):
		self.loc_addr = addr
		return self.loc_addr
	def update_rem_addr(self, addr):
		self.rem_addr = addr
		return self.rem_addr
	def get_name(self):
		return self.name
	def get_loc_addr(self):
		return self.loc_addr
	def get_rem_addr(self):
		return self.rem_addr


class XmlParser:
        def __init__(self, source):                
                print "parsing stream list..."
		self.url = source
		usock = urllib.urlopen(source)
                self.xmldoc = minidom.parse(usock)
		usock.close()
		print self.xmldoc.toxml()
                print "parsed ok"
        def build_cam_list(self):
		self.list = []
                print "building list"
		#get camera nodes loop and build IpCam objects list
		for cam in self.xmldoc.getElementsByTagName('cam'):
			node_name = cam.getElementsByTagName('name')
			name = self.get_tag_value(node_name[0])
			node_loc_addr = cam.getElementsByTagName('loc_addr')
			loc_addr = node_loc_addr[0].attributes['href']		
			node_rem_addr = cam.getElementsByTagName('rem_addr')
			rem_addr = node_rem_addr[0].attributes['href']
			ipcam = IpCam(name=name, loc_addr = loc_addr.value, rem_addr = rem_addr.value)		
			print "Adding Cam: %s" % ipcam.get_rem_addr()
			self.list.append(ipcam)
		return self.list
	def get_tag_value(self, node):
    		xml_str = node.toxml() # flattens the element to string
 
    		# cut off the base tag to get clean content:
    		start = xml_str.find('>')
    		if start == -1:
        		return ''
    		end = xml_str.rfind('<')
    		if end < start:
        		return ''
 
    		return xml_str[start + 1:end]	
def main():
	cameras = 'stream_list.xml'
	p = XmlParser(cameras)
	list = p.build_cam_list()
	print "here is the ful list"
	for item in list:
		print item.get_name()
if __name__ == '__main__':
    main()
