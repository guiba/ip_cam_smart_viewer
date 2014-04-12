#!/usr/bin/env python

from subprocess import Popen, PIPE
from time import sleep
from nbstreamreader import NonBlockingStreamReader as NBSR

# run the shell as a subprocess:
p = Popen('cec-client',
        stdin = PIPE, stdout = PIPE, stderr = PIPE, shell = False)
# wrap p.stdout with a NonBlockingStreamReader object:
nbsr = NBSR(p.stdout)
# issue command:
#p.stdin.write('command\n')
# get the output
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
      
      
def check_line(line):
  if(line.startswith('TRAFIC:')):
       code = line.split('>>')[1]
       return code;
       
    
    