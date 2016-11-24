
# coding: utf-8

# In[ ]:

def standard_error(x):
    n = len(x)
    mean = sum(x) / n
    ssq = sum((x_i-mean)**2 for x_i in x)
    stdev = (ssq/n)**0.5
    stderr = stdev/(n**0.5)
    return(stderr)

