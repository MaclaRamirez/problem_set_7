# -*- coding: utf-8 -*-
# In the following example, we start off with a list of values, and we add some
# new values to them. We now want to find the difference between the mean of
# the original list of values, and the new list of values. This should give
# 0.625 but it gives 0.0 instead. Why is this?

#This is why with lists, when we say b = a, we point b to the same location as
#a, so the list exist only once in the memory. We have to do a deepcopy.

import numpy as np
from copy import deepcopy

# Define the original set of values.
new_values = [8., 7., 9., 4., 6., 7., 8., 4.]

# Create a new list with the original values and add a few more
values = deepcopy(new_values)
new_values.append(8.)
new_values.append(9.)
new_values.append(2.)
new_values.append(1.)
new_values.append(5.)

print values
print new_values
print "Difference in the mean:", abs(np.mean(new_values) - np.mean(values))
