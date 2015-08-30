#! usr/bin/env/python

import numpy as np
import sys
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

a = float(sys.argv[1])
b = float(sys.argv[2])
t = np.linspace(-np.pi, np.pi, 201)

x = np.sin(a*t+np.pi/2)
y = np.sin(b*t)
plot(x, y)
show()