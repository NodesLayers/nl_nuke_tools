## Execute's the file with the os default application

def openFile():

    import nuke
    import os
    
    for s in nuke.selectedNodes():
        try:
                
            curFrame = nuke.frame()
            fp = s["file"].getValue()
            fp = fp.replace("%04d", str(curFrame))
            fp = fp.replace("/", os.sep)
            print fp
            
            ## Launch File
            os.startfile(fp)
        except:
            pass

openFile()