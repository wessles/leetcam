#!/usr/bin/python

import numpy as np
import urllib
import random,string,time
from math import sin
import cv2
import sys

# This will turn any MJPEG stream (IP
# camera) into an epic hacking scene.
# Just plug in the URL like so:
#	 leetcam http://192.168.1.4:4747/mjpegfeed

# Most of this code is stolen from
# http://stackoverflow.com/questions/21702477/how-to-parse-mjpeg-http-stream-from-ip-camera

url = 'http://192.168.1.4:4747/mjpegfeed'
if sys.argv[1]:
	url = sys.argv[1]
stream=urllib.urlopen(url)
bytes=''

while 1:
	# Read the bytes
	bytes += stream.read(1024)	# read bytes in
	a = bytes.find('\xff\xd8')	# All JPEG frames start with 0xd8
	b = bytes.find('\xff\xd9')	# and end with 0xd9

	if (a is not -1) and (b is not -1): # If there is a start or end
		jpg = bytes[a:b+2]	# grab start to EOF (end bit + 2)
		bytes = bytes[b+2:] # grab end EOF and onwards

		# LET THE MESSING UP BEGIN

		for i in range(int(max(0, sin(time.time())*10+10))): 						# This sine function just intensifies the permutations with time, so you get waves of chaos
			find = ''.join([random.choice(string.lowercase) for x in range(2)])		# Replace a random two-bit part
			replace = ''.join([random.choice(string.lowercase) for x in range(2)])	# With another random two-bit part
			jpg = jpg.replace(find, replace)										# Execute replacement

		i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)	# encode it
		cv2.imshow('i',i)																# show it
		if cv2.waitKey(1) is 27:														# if escape (27) is pressed
			break																			# break loop

# When everything is done, destroy the evidence
cv2.destroyAllWindows()
