import nuke

def changeSelectedVectorBlurs():
    try:
        p = nuke.Panel("Change all selected VectorBlur's")
        p.addSingleLineInput("Width", "0")
        p.addSingleLineInput("Height", "0")
        p.show()

        x = p.value("Width")
        y = p.value("Height")

        new_scale = []
        new_scale.append(x)
        new_scale.append(y)


        for s in nuke.selectedNodes("VectorBlur2"):
            s["scale"].setValue(new_scale)
    except:
        pass

changeSelectedVectorBlurs()
