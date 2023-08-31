import hou
print('\n')
n = hou.selectedNodes()
node_target = hou.ui.selectNode(initial_node=n[0])
target = hou.node(node_target)

for i in n:
	rel_path = hou.node(node_target).relativePathTo(i)
	node_src = i.path()
	print('Referencing Ramps from %s in %s'%(node_src, node_target))
	ramp_list = []
	for p in i.parms():
		type = p.parmTemplate().type().name()
		if type == 'Ramp':
			ramp_name = p.name()
			ramp_list.append(ramp_name)
			path_src = p.path()
			path_target = path_src.replace(node_src, node_target)
			#print(hou.parm(path_target))
			#hou.parm(path_target).setFromParm(p)
			
			p_name = p.name()
			relref = 'ch("%s/%s")'%(rel_path, p_name)
			ramp = target.parm(p_name)
			ramp.setFromParm(p)
			#i.parm(p_name).setExpression(relref)
			#FUTURE DEV:
			#the following could work by looping over all the parameters, if
				#parameter.name()==ramp.name()*pos || parameter.name()==ramp.name()*value || parameter.name()==ramp.name()*interp:
					#hou.node(node_target).parm(parameter.name().setExpression(relref)
		else:
			pass

	for l in ramp_list:
		c = 0
		r_len = i.parm(l).evalAsRamp().basis()
		for m in r_len:
			c += 1
			pos = '%s%spos'%(l, c)
			value = '%s%svalue'%(l, c)
			interp = '%s%sinterp'%(l, c)
			
			relref_pos = 'ch("%s/%s")'%(rel_path, pos)
			relref_value = 'ch("%s/%s")'%(rel_path, value)
			relref_interp = 'ch("%s/%s")'%(rel_path, interp)
			
			target.parm(pos).setExpression(relref_pos)
			target.parm(value).setExpression(relref_value)
			target.parm(interp).setExpression(relref_interp)