#!/usr/bin/env python

from time import sleep
import subprocess
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
  #input section
  cec_proc = subprocess.Popen('cec-client',stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = False)
  # wrap p.stdout with a NonBlockingStreamReader object:
  nbsr = NBSR(cec_proc.stdout)
  while True:
    output = nbsr.readline()
    # 0.1 secs to let the shell output the result
    if output:
      if(output.startswith('waiting')):
	print "Ready for input"
      if(output.startswith('TRAFFIC:')):
	sub = output.split('>>')
	if (len(sub) > 1):
	  if(sub[1].startswith(' 01:44:2')):
	    code = sub[1].split(':2')
	    print code[1]
	    char = int(code[1])
  #while True:
	#char = raw_input("choose camera [1 - %s ]: " % len(cam_list))
	    if char == 0:
		    subprocess.Popen(['killall', 'omxplayer.bin'])
		    break
	    if (int(char) <= len(cam_list)):
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
    

