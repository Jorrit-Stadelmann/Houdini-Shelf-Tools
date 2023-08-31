import hou

for n in hou.selectedNodes():
    n.setParmExpressions({'t': ('-1* ch("px")', '-1* ch("py")', '-1* ch("pz")')})
    print(n.name())
    print('Position set to Pivot Position (-1* ch("px"), -1* ch("py"), -1* ch("pz"))')