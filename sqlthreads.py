#Morris Mwanga <mmwanga@kennesaw.edu>
#sqlthreads v0.1 : Licensed uner GPLv2  (http://www.gnu.org/licenses/gpl-2.0.html)
def initialize(storage,max_threads):
	import sys
	threads = {'storage': None, 'max_threads': None, 'threads': None}
	if(storage=='mysql'):
		threads['storage']='mysql'
		try:
			import MySQLdb
		except ImportError:
			sys.stderr.write("Error: Could not import the module the module 'MySQLdb'...\n")
	elif(storage=='internal'):
		threads['storage']='internal'
	else:
		sys.stderr.write("Error: initialize() accepts 2 arguments : storage=mysql|internal and max_threads=n ; where n is a non-negative integer\n")
	if(isinstance(max_threads,int)):
		threads['max_threads']=max_threads
	else:	
		sys.stderr.write("Error: initialize() accepts 2 arguments : storage=mysql|internal and max_threads=n ; where n is a non-negative integer\n")
	if(threads['storage'] != None and threads['max_threads'] != None):
		return threads
def start(task_id,threads):
	import threading
	all_threads=threading.enumerate()
	#Start thread if not in all_threads
def stop():
	#Stop
	pass
def get_thread():	
	#Get thread data(id,time,memory,state)
	pass
		

