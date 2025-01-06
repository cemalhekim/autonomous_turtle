import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ch/Workspace/autonomous_turtle/turtlesim/install/turtlesim'
