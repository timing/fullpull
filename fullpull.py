import glob
from subprocess import call
import shlex

rcs = {
	'.git': 'git pull',
	'.svn': 'svn up',
	'.bzr': 'bzr pull'
}

hiddenFiles = glob.glob('.*')

found = False

for hiddenFile in hiddenFiles:
	if hiddenFile in rcs:
		found = True
		print 'Found ' + hiddenFile[1:] + ' repository! Running ' + rcs[hiddenFile]
		call(shlex.split(rcs[hiddenFile]))

if found == False:
	print "No (known) revision control system found in this directory"
