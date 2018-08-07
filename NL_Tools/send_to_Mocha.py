import os
import nuke
import nukescripts
import subprocess

mocha_path = "//ldn-fs1/projects/__pipeline/software/windows/mocha/bin/mocha Pro V5/bin/mochapro.exe"


try:
    n = nuke.selectedNode()
    first_frame = n["first"].getValue()
    path = n["file"].getValue()
    path = nukescripts.replaceHashes( path ) % n.firstFrame()
    
    print path
    
    cmd = "<Q>"+mocha_path+"<Q> <Q>"+path+"<Q>"
    cmd = cmd.replace("<Q>",'"')
    print cmd
    subprocess.Popen([mocha_path, path])
except:
    nuke.message("Something went wrong :( ")
    pass