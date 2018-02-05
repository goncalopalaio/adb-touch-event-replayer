#!/usr/bin/env python
import os
import subprocess
import re
import time
import sys
import datetime

# use stdin if it's full
if not sys.stdin.isatty():
	input_stream = sys.stdin
else:
	try:
		input_filename = sys.argv[1]
	except IndexError:
		message = 'need filename as first argument if stdin is not full'
		raise IndexError(message)
	else:
		input_stream = open(input_filename, 'rU')

RE = re.compile(r"^(\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d\.\d+) (\S+) (\S+) (\S+)$")
#match = line_re.match(line.strip())
#    ts, etype, ecode, data = match.groups()
#    ts = datetime.datetime.strptime(ts, "%Y-%m-%d %H:%M:%S.%f")
#    etype, ecode, data = int(etype, 16), int(ecode, 16), int(data, 16)

prev_timestamp = None
for line in input_stream:
	#print("line: ", line)
	s = line.strip().split(" ")
	if len(s) != 6 or not s[2].startswith("/dev"):
		pass	
	else:
		timestamp = datetime.datetime.strptime(str(s[0]) + " " + str(s[1]), "%Y-%m-%d %H:%M:%S.%f")
		if prev_timestamp:
			diff = (timestamp - prev_timestamp).total_seconds()
			str_diff = "%.3f" % (diff)
			if diff > 0.1:
				print("sleep %s" % diff)

		bus = s[2][:-1]
		etype = int(s[3], 16)
		ecode = int(s[4], 16)
		data  = int(s[5], 16)

		print("adb shell sendevent %s %s %s %s" % (bus, etype, ecode, data))
		
		prev_timestamp = timestamp

		