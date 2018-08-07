import os

for s in nuke.selectedNodes("Read"):
    s["colorspace"].setValue("AlexaV3LogC")

    newFile = s["file"].getValue()

    # PANEL
    p = nuke.Panel("WriteFromRead")
    p.addSingleLineInput('Replace:', '')
    p.addSingleLineInput('With:', '')
    p.addSingleLineInput('Replace2:', '')
    p.addSingleLineInput('With2:', '')
    p.show()

    rp1 = p.value("Replace:")
    rw1 = p.value("With:")
    rp2 = p.value("Replace2:")
    rw2 = p.value("With2:")

    newFile = newFile.replace(rp1,rw1)
    newFile = newFile.replace(rp2,rw2)


    n = nuke.createNode("Write")
    n.setInput(0,s)
    n["file"].setValue(newFile)
    #n["name"].setValue(os.path.basename(newFile))
    n["colorspace"].setValue("AlexaV3LogC")
    n["first"].setValue(s["first"].getValue())
    n["last"].setValue(s["last"].getValue())
    n["use_limit"].setValue(1)