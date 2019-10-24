# move.py

import os
import sys
import glob

sourcenum = int(sys.argv[1])
targetnum = int(sys.argv[2])

os.system("rm -rf ex%d_*.html" % targetnum)
os.system("rm -rf soln%d_*.html" % targetnum)

exfiles = glob.glob("ex%d_*.html" % sourcenum)
solnfiles = glob.glob("soln%d_*.html" % sourcenum)

exfiles.sort()
solnfiles.sort()

print exfiles
print solnfiles

for n, name in enumerate(exfiles):
    data = open(name).read()
    data = data.replace("soln%d_" % sourcenum, "soln%d_" % targetnum)
    data = data.replace("ex%d_" % sourcenum, "ex%d_" % targetnum)
    data = data.replace("ex%d_" % (sourcenum+1),"ex%d_" % (targetnum+1))
    data = data.replace("%d.%d" % (sourcenum, n+1), "%d.%d" % (targetnum,n+1))
    open("ex%d_%d.html" % (targetnum,n+1),"w").write(data)

for n, name in enumerate(solnfiles):
    data = open(name).read()
    data = data.replace("soln%d_" % sourcenum, "soln%d_" % targetnum)
    data = data.replace("ex%d_" % sourcenum, "ex%d_" % targetnum)
    data = data.replace("%d.%d" % (sourcenum, n+1), "%d.%d" % (targetnum,n+1))
    open("soln%d_%d.html" % (targetnum,n+1),"w").write(data)
    


    
