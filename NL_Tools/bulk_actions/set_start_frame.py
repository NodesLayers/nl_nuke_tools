## Multi Set Start Frame

import nuke

def setStartFrame():
    p = nuke.Panel('Multi - Set Start Frame')
    p.addSingleLineInput('New start frame:', 1001)
    p.show()
    
    newStartFrame = p.value("New start frame:")
    #print newStartFrame
    
    for s in nuke.selectedNodes():
        try:
            s["frame_mode"].setValue("start at")
            s["frame"].setValue(newStartFrame)
        except:
            pass

setStartFrame()