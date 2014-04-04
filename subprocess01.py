#!/usr/bin/env python

from time import sleep
import subprocess

url1 = str("rtsp://admin:admin@192.168.0.16:554/live1")
url2 = str("rtsp://admin:admin@9002a9acc3e3.dahuaddns.com:554/cam/realmonitor?channel=1&subtype=0")
url3 = str("rtsp://admin:admin@9002a9acc3e3.dahuaddns.com:554/cam/realmonitor?channel=2&subtype=0")

url_list = [url1, url2, url3]
def main():
  current_proc = subprocess.Popen(['omxplayer', url1] , stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
  while True:
	char = raw_input("choose camera [1, 2, 3]: ")
	if char == 'q':
		subprocess.Popen(['killall', 'omxplayer.bin'])
		break
	if char.isdigit() and (int(char) <= len(url_list)):
		index = int(char)-1
		url = url_list[index]
		print url
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
    

