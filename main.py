#!/usr/bin/env python3.9

import os
import platform
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import crypt

system = platform.system()
externalDrives = ''
driveName = 'Mantissa3x'
driveKey = ''

home = os.path.expanduser('~')
secureDirectory = os.path.join(home, "Documents", "Secure")

if system == 'Linux':
	root = os.path.expanduser('/')
	# the path to external drives on linux, observes this folder
	externalDrives = os.path.join(root, 'media', 'misha')
	driveKey = os.path.join(root, 'media', 'misha', driveName, 'security', 'pass.key')

# Detecting when Mantissa3x will be plugged in
# on deleted is when unplugged and on created is when plugged in
key = None

class Handler(FileSystemEventHandler):
	def __init__(self, key = ''):
		self.key = key

	def on_created(self, event):
		# When plugged in decrypt folder
		print('Detecting key...')
		try:
			with open(driveKey, 'rb') as filekey:
				self.key = filekey.read()
			print("FOUND KEY!")
			print("Decrypting...")
			crypt.decryptFiles(secureDirectory, self.key)
		except:
			print('Key not found :(')
	def on_deleted(self, event):
		# print(event.event_type, event.src_path)
		# print(event.is_directory)
		crypt.encryptFiles(secureDirectory, self.key)
		del self.key
		

		
event_handler = Handler()

observer = Observer()

observer.schedule(event_handler, path=externalDrives, recursive=False)
observer.start()

while True:
	try:
		pass
	except KeyboardInterrupt:
		observer.stop()
