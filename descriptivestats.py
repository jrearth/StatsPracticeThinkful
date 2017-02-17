Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> binomialvar = np.random.bionomial(10, .125 , 100)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    binomialvar = np.random.bionomial(10, .125 , 100)
AttributeError: module 'numpy.random' has no attribute 'bionomial'
>>> binomialvar = np.random.binomial(10, .125 , 100)
>>> import matplotlib.pyplot as plt
>>> plt.hist(binomialvar)
(array([ 23.,   0.,  44.,   0.,   0.,  20.,   0.,   9.,   0.,   4.]), array([ 0. ,  0.4,  0.8,  1.2,  1.6,  2. ,  2.4,  2.8,  3.2,  3.6,  4. ]), <a list of 10 Patch objects>)
>>> import panda as pd
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    import panda as pd
ModuleNotFoundError: No module named 'panda'
>>> import pandas as pad
>>> 
