## Open source of file knob

import nuke
import os

def openFolder():
    
    n = nuke.selectedNode()
    
    ## create correct filepath
    fp = n["file"].getValue()
#    fbn = os.path.split(fp)[1]
    fp = os.path.split(fp)[0]
    fp = fp.replace("/", os.sep)
    cf = str(nuke.frame())
#    fp = fp.replace("%05d", cf)
    print fp



    ## Open explorer with path
    
    import subprocess
    subprocess.Popen('explorer '+fp)



openFolder()