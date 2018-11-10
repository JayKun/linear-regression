import numpy

a = numpy.array([1, 2, 3, 1, 2], ndmin=3, dtype=complex)
b = numpy.array([[1, 3], [2]])
print(b.shape)
print(a)