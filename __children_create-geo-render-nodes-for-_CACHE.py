import hou
out = hou.node('/out')
#out.layoutChildren()

print('\n')

for i in hou.selectedNodes():
	for c in i.children():
		name = c.name()
		if name.startswith('_CACHE_'):
			name = name.split('_CACHE_')
			#print(name[1])
			
			rop = out.createNode('geometry', name[1])
			rop.moveToGoodPosition()
			
			path = rop.path()
			path += '/soppath'
			hou.parm(path).set(c.path())

			print('Created \'' + rop.name() + '\' in ' + out.path() + ' linked to \'' + i.path())