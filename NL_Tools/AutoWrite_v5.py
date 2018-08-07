import nuke
import os

app_name = "Terrritory autoWrite"
myVersion = "v5.0 - 171108"
author = "Written by Ricardo Musch"


def autoWrite(mov_colorspace):
    
    if mov_colorspace == "":
        mov_colorspace = "Gamma2.2"
    
    
    
    print ""
    print "----------- autoWrite -----------"
    print "----------- " + myVersion + " -----------"
    print "----------- " + author + " -----------"
    print ""

    if nuke.root().name() == "Root":
        nuke.message("You need to save your script properly before continuing!")

    # Find context from scriptname
    try:
        nuke_script = os.path.basename(nuke.root().name())
        nuke_script = str.split(nuke_script, "_")

        # Set Script Variables
        sequence = str.upper(nuke_script[0])
        sequence = sequence.lower()
        shot = nuke_script[1]
        shot = shot.lower()
        print "Context: " + sequence + "_" + shot
    except:
        print "ERROR: Couldn't find Sequence, Shot"

    # Find scriptVersion
    try:
        scriptVersion = nuke.root().name()
        scriptVersion = str.split(scriptVersion, "_")
        scriptVersion = scriptVersion[-1]
        scriptVersion = str.split(scriptVersion, ".")
        scriptVersion = scriptVersion[0]
        scriptVersion = scriptVersion.lower()
        print "Scriptversion: " + scriptVersion
    except:
        print "ERROR: Could not find Nuke Script Version"

    # PANEL
    p = nuke.Panel(app_name + " " + myVersion)
    p.addEnumerationPulldown('Context:', sequence + "_" + shot)
    p.addEnumerationPulldown('Format:', 'exr-sequence jpg-sequence movie')
    p.addEnumerationPulldown('Render type:', 'comp precomp element')
    p.addBooleanCheckBox("Latest shot version:", True)
    p.addSingleLineInput('(optional) Identifier:', '')


    ret = p.show()

    # Set User Variables
    render_type = p.value("Render type:")
    format = p.value("Format:")
    strict_versioning = p.value("Latest shot version:")
    ident = p.value("(optional) Identifier:")
    ident = ident.replace(" ", "_")


# -------------- PATHING -----------------------

    # Render base path
    nuke_script_path = os.path.dirname(nuke.root().name())
    render_basepath = nuke_script_path

    try:
        if render_type == "comp":
            #render_basepath = os.path.split(render_basepath)[0]
            #render_basepath = os.path.split(render_basepath)[0]
            render_basepath = os.path.split(render_basepath)[0]
            render_basepath = os.path.join(render_basepath, "renders", render_type)
            render_basepath = os.path.normpath(render_basepath)
        else:
            render_basepath = os.path.split(render_basepath)[0]
            render_basepath = os.path.join(render_basepath, "renders", render_type)
            render_basepath = os.path.normpath(render_basepath)
        print render_basepath
    except:
        print "ERROR: Something went wrong setting the render basepath. If you pressed cancel, please ignore this error."

    # Filepath Profiles
    ## Precomp & Element
    if (render_type == "precomp") or (render_type == "element"):
        filename_base = sequence + "_" + shot + "_" + render_type + "_" + ident + "_" + scriptVersion
        if ident == "":
            filename_base = sequence + "_" + shot + "_" + render_type + "_" + scriptVersion

    # Comp
    if render_type == "comp":
        filename_base = sequence + "_" + shot + "_" + render_type + "_" + ident + "_" + scriptVersion
    if ident == "":
        filename_base = sequence + "_" + shot + "_" + render_type + "_" + scriptVersion
    print filename_base

    if format == "movie":
        name_format = "MOV"
        filename = filename_base + ".mov"
        filepath = os.path.join(render_basepath, filename)
        print filepath

    if format == "exr-sequence":
        name_format = "EXR"
        filename = filename_base + ".%04d.exr"
        filepath = os.path.join(render_basepath, filename_base, filename)
        print filepath

    if format == "jpg-sequence":
        name_format = "JPG"
        filename = filename_base + ".%04d.jpg"
        filepath = os.path.join(render_basepath, filename_base, filename)
        print filepath

    # Set writeFile
    filepath = os.path.normpath(filepath)
    filepath = filepath.replace("\\", "/")
    print ""
    print "Created Writenode with filename: " + filepath


# -------------- CREATE WRITENODE -----------------------
    try:
        seedcount = seedcount + 1
    except:
        seedcount = 1

    # Create Writenode
    n = nuke.createNode("Write")
    n["file"].setValue(filepath)
    n["create_directories"].setValue(1)
    if ident == "":
        n["name"].setValue(render_type + "_" + name_format + str(seedcount))
    n["name"].setValue(render_type + "_" + ident + "_" + name_format + str(seedcount))


# Policies for Output
    if format == "exr-sequence":
        n["autocrop"].setValue(1)
    if format == "jpg-sequence":
        n["_jpeg_quality"].setValue(.9)
    if render_type == "comp":
        n["channels"].setValue("rgb")
        n["render_order"].setValue(2)
    if render_type == "precomp":
        n["render_order"].setValue(1)
    if (format == "movie") and (render_type == "comp"):
        n["render_order"].setValue(3)
        n["colorspace"].setValue(mov_colorspace)

autoWrite("")
