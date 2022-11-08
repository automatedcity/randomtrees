"""
Python script that draws a random tree and displays it using matplotlib

The random properties are:
	+ The angle of the child branches given parent branch angle: Generated between [angle-MAX_DEVIATION, angle+MAX_DEVIATION]
	with a uniform distribution 
	+ The length of the child branches given parent branch length: Generated between [MIN_BRANCH_SIZE_RATIO*parent_length, MAX_BRANCH_SIZE_RATIO*parent_length]

depth is also an input parameter of the function which is the number of branch levels in the tree

You can change these values and see the effect on the generated trees.


"""

import matplotlib.pyplot as plt
from math import tan, pi, sqrt, atan
from random import uniform
import numpy as np
from Branch import Branch
import os
import random

#Generate collection


# generate random integer values
from random import seed
from random import randint
# seed random number generator
seed(randint)
# generate some integers

valuerange = randint(0, 1000)
valueline = randint(0, 10)
value1 = randint(0, valuerange)
value2 = randint(0, valuerange)
value3 = randint(0, valuerange)
value4 = randint(0, valuerange)
value5 = randint(0, valuerange)
value6 = randint(0, valuerange)
value7 = randint(0, valuerange)
value8 = randint(0, valuerange)
value9 = randint(0, valuerange)
value10 = randint(0, valuerange)
value11 = randint(0, valuerange)
value12 = randint(0, valuerange)
value13 = randint(0, valuerange)
value14 = randint(0, valuerange)
value15 = randint(0, valuerange)
value16 = randint(0, valuerange)
value17 = randint(0, valuerange)
value18 = randint(0, valuerange)
value19 = randint(0, valuerange)
value20 = randint(0, valuerange)
value21 = randint(0, valuerange)
value22 = randint(0, valuerange)
value23 = randint(0, valuerange)
value24 = randint(0, valuerange)




color_list = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']

# pick a random color
color1 = random.choice(color_list)
color2 = random.choice(color_list)
color3 = random.choice(color_list)
color4 = random.choice(color_list)
color5 = random.choice(color_list)
color6 = random.choice(color_list)

print(color1, color2, color3, color4, color5, color6)




print(valuerange, valueline,value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12, value13, value14, value15, value16, value17, value18, value19, value20, value21, value22, value23, value24)

os_count = os.environ.get('count')

MAX_DEVIATION=pi/8
MAX_BRANCH_SIZE_RATIO = 0.8
MIN_BRANCH_SIZE_RATIO = 0.5


def tree(parent, depth, xs, ys):
	"""
	parent: is the root segment of the tree to be generated
	depth: number of branch levels of the tree

	the function adds generated branches extremities to params xs an ys
	"""
	if not xs:
		xs += [parent.x1, parent.x2]
		ys += [parent.y1, parent.y2]

	if depth <= 0: return
	a = parent.slope()
	parentLength = parent.length()
	angle = atan(a)

	newSlope1 = tan(uniform(angle - MAX_DEVIATION, angle))
	newLength1 = parentLength*uniform(MIN_BRANCH_SIZE_RATIO, MAX_BRANCH_SIZE_RATIO)
	childBranch1 = parent.initFromCharacteristics(newSlope1, newLength1)
	xs.append(childBranch1.x2)
	ys.append(childBranch1.y2)
	tree(childBranch1, depth-1, xs, ys)

	xs.append(np.nan)
	ys.append(np.nan)

	xs.append(childBranch1.x1)
	ys.append(childBranch1.y1)


	newSlope2 = tan(uniform(angle, angle + MAX_DEVIATION))
	newLength2 = parentLength*uniform(MIN_BRANCH_SIZE_RATIO, MAX_BRANCH_SIZE_RATIO)
	childBranch2 = parent.initFromCharacteristics(newSlope2, newLength2)
	xs.append(childBranch2.x2)
	ys.append(childBranch2.y2)
	tree(childBranch2, depth-1, xs, ys)

xs, ys = [], []
tree(Branch(0, 0, 0, 0.4), 14, xs, ys)

plt.plot(xs, ys)

my_path = fr"tree{os_count}.png"
plt.savefig(my_path)


import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

im = Image.open(my_path)

# Create figure and axes
fig, ax = plt.subplots()

# Display the image
ax.imshow(im)

#mcolors.CSS4_COLORS

#property_name = print(color_choice)

# Create a Rectangle patch
rect = patches.Rectangle((value1, value2), value3, value4, linewidth=valueline, color=color1)
rect1 = patches.Rectangle((value5, value6), value7, value8, linewidth=valueline, edgecolor=color2, facecolor='none')
rect2 = patches.Rectangle((value9, value10), value11, value12, linewidth=valueline, color=color3)
rect3 = patches.Rectangle((value13, value14), value15, value16, linewidth=valueline, edgecolor=color4, facecolor='none')
rect4 = patches.Rectangle((value17, value18), value19, value20, linewidth=1, color=color5)
rect5 = patches.Rectangle((value21, value22), value23, value24, linewidth=1, edgecolor=color6, facecolor='none')


# Add the patch to the Axes
ax.add_patch(rect)
ax.add_patch(rect1)
ax.add_patch(rect2)
ax.add_patch(rect3)
ax.add_patch(rect4)
ax.add_patch(rect5)

my_path1= fr"treebuildings{os_count}.png"
plt.savefig(my_path1)



