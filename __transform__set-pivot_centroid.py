import hou

for n in hou.selectedNodes():
    n.setParmExpressions({'p': ('$CEX', '$CEY', '$CEZ')})
    print(n.name())
    print('Pivot Transform set to ($CEX, $CEY, $CEZ)')