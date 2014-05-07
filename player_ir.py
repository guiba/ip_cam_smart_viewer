#!/usr/bin/env python

from time import sleep
import subprocess
import pylirc
from xml_parser import XmlParser
from nbstreamreader import NonBlockingStreamReader as NBSR

def main():
  #build ipcam list from config.xml
  config = 'config.xml'
  parser = XmlParser(config)
  cam_list = parser.build_cam_list()
  print 'Full List'
  for item in cam_list:
		print item.get_name()
  default = 0 
  current_proc = subprocess.Popen(['omxplayer', cam_list[default].get_rem_addr()] , stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
  #ir input section
  blocking  = 0;
  if(pylirc.init("pylirc", "./pylirc/conf", blocking)):

   code = {"config" : ""}
   while (code["config"] != "0"):
      # Very intuitive indeed
      if(not blocking):
         print "."
         # Delay...
         sleep(0.5)
      # Read next code
      s = pylirc.nextcode(1)
      # Loop as long as there are more on the queue
      # (dont want to wait a second if the user pressed many buttons...)
      while(s):
         
         # Print all the configs...
         for (code) in s:
            char = code["config"]	
            print "Command: %s, Repeat: %d" % (code["config"], code["repeat"])
         # Read next code?
         if(not blocking):
            s = pylirc.nextcode(1)
         else:
            s = []
	# if 0 pressed exit close player and pylirc
#	 if int(char) == 0:
#		subprocess.Popen(['killall', 'omxplayer.bin'])
#		pylirc.exit()
#		break
	 if (int(char) <= len(cam_list) and int(char) != 0):
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
  subprocess.Popen(['killall', 'omxplayer.bin'])
  pylirc.exit()
       
    
if __name__ == '__main__':
    main()
    

