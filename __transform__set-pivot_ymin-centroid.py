import hou

for n in hou.selectedNodes():
    n.setParmExpressions({'p': ('$CEX', '$YMIN', '$CEZ')})
    print(n.name())
    print('Pivot Transform set to ($CEX, $YMIN, $CEZ)')