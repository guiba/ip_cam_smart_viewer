#!/usr/bin/env python

from time import sleep
import subprocess
from xml_parser import XmlParser

def main():
  #build ipcam list from config.xml
  config = 'stream_list.xml'
  parser = XmlParser(config)
  cam_list = parser.build_cam_list()
  print 'Full List'
  for item in cam_list:
		print item.get_name()
  default = 0 
  current_proc = subprocess.Popen(['omxplayer', cam_list[default].get_rem_addr()] , stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
  while True:
	char = raw_input("choose camera [1, 2, 3]: ")
	if char == 'q':
		subprocess.Popen(['killall', 'omxplayer.bin'])
		break
	if char.isdigit() and (int(char) <= len(cam_list)):
		index = int(char)-1
		url = cam_list[index].get_rem_addr()
		print url
#comment
		try:	
			next_proc = subprocess.Popen(['omxplayer', url],  stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			#current_proc.communicate('p')
			#current_proc.stdin.flush()
			#print next_proc.stdout
			current_proc.communicate('q')
			temp = current_proc
			current_proc = next_proc
			next_proc = temp
		except: 
			out, err = current_proc.communicate()
			print ("Error: " + err.rstrip())
	else: 
		print ("there are no cam corresponding to this number")
		
	sleep(0.1)	
    
    
if __name__ == '__main__':
    main()
    

