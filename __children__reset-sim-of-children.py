import hou

for i in hou.selectedNodes():
    for c in i.children():
        if c.type().name() == 'dopnet':
            c.parm('resimulate').pressButton()
        if c.type().name() == 'solver':
            c.parm('resimulate').pressButton()