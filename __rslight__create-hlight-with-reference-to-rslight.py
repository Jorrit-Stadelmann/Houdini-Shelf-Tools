import hou
s = hou.selectedNodes()

for n in s:
    if (n.type().name() == 'rslight'):
        path = n.parent()
        name = '%s_hlight'%(n.name())
        light = path.createNode('hlight::2.0', node_name=name)
        light.setPosition(n.position())
        light.move((2,0))
        light.parm('tx').setExpression('ch("%s/tx")'%(light.relativePathTo(n)))
        light.parm('ty').setExpression('ch("%s/ty")'%(light.relativePathTo(n)))
        light.parm('tz').setExpression('ch("%s/tz")'%(light.relativePathTo(n)))
        light.parm('rx').setExpression('ch("%s/rx")'%(light.relativePathTo(n)))
        light.parm('ry').setExpression('ch("%s/ry")'%(light.relativePathTo(n)))
        light.parm('rz').setExpression('ch("%s/rz")'%(light.relativePathTo(n)))
        light.parm('light_intensity').setExpression('ch("%s/RSL_intensityMultiplier")'%(light.relativePathTo(n)))
        light.parm('light_exposure').setExpression('ch("%s/Light1_exposure")'%(light.relativePathTo(n)))
        light.parm('light_colorr').setExpression('ch("%s/light_colorr")'%(light.relativePathTo(n)))
        light.parm('light_colorg').setExpression('ch("%s/light_colorg")'%(light.relativePathTo(n)))
        light.parm('light_colorb').setExpression('ch("%s/light_colorb")'%(light.relativePathTo(n)))
        lightType = n.parm('light_type').evalAsString()
        if lightType == 'spot':
            light.parm('light_type').set(0)
            light.parm('coneenable').set(1)
        elif lightType == 'distant':
            light.parm('light_type').set(7)
        elif lightType == 'point':
            light.parm('light_type').set(0)
        elif lightType == 'area':
            light.parm('light_type').set(2)
            light.parm('singlesided').set(1)
            light.parm('areasize1').setExpression('ch("%s/areasize1")'%(light.relativePathTo(n)))
            light.parm('areasize2').setExpression('ch("%s/areasize2")'%(light.relativePathTo(n)))