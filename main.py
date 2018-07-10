import numpy as np
import os.path as path

filename = path.join(path.abspath(path.dirname(__file__)), 'Data Files/TestData.bin')

print(filename)

fp = np.memmap(filename, dtype = 'int16', mode='r', shape=(1,100))

print(fp)