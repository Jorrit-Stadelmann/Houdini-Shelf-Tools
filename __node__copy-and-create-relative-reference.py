import hou
print('\nExecuted Script\n')
n = hou.selectedNodes()
destination = hou.ui.selectNode(initial_node=n[0].parent())

for i in n:
	dest_n = i.copyTo(hou.node(destination))
	dest_n.moveToGoodPosition()
	rel_path = dest_n.relativePathTo(i)
	
	for dest_p in dest_n.parms():
		p_name = dest_p.name()
		
		if dest_p.parmTemplate().type().name() == 'String':
			parmtype = 'chs'
		else:
			parmtype = 'ch'

		relref = '%s("%s/%s")'%(parmtype, rel_path, p_name)
		dest_n.parm(p_name).setExpression(relref)
		path = i.path()
		dest_n.setComment('Relative reference to %s'%(path))
		dest_n.setGenericFlag(hou.nodeFlag.DisplayComment, True)
	dest_n_path = dest_n.path()
	print('Created %s and referenced to %s'%(dest_n_path, path))