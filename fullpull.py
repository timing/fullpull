from glob import glob
from subprocess import call
from shlex import split
from sys import exit

rcs = {
	'.git': 'git pull',
	'.svn': 'svn up',
	'.bzr': 'bzr pull'
}

hiddenFiles = glob('.*')

found = False

for hiddenFile in hiddenFiles:
	if hiddenFile in rcs:
		found = True
		print 'Found ' + hiddenFile[1:] + ' repository! Running ' + rcs[hiddenFile]
		call(split(rcs[hiddenFile]))
		exit()

if found == False:
	print "No (known) revision control system found in this directory"
