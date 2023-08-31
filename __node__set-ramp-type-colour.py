import hou

for n in hou.selectedNodes():
    cur = n.name()
    ui_ramp_name = hou.ui.readInput('Ramp name of %s'%(cur))[-1]
    ramp = n.globParms(ui_ramp_name)[0]
    
    name = ramp.name()
    
    g = n.parmTemplateGroup()
    parm = g.find(name)
    parm.setParmType(hou.rampParmType.Color)
    g.remove(name)
    g.append(parm)
    n.setParmTemplateGroup(g)