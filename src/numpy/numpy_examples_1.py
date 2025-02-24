import numpy

if __name__ == '__main__':
    array1: numpy.ndarray = numpy.arange(15).reshape(3, 5)  # returns a numpy array from 0 to 14. Then converts it to a matrix of 3 rows and 5 columns
    print(array1)
    print(type(array1))
    print(array1.shape)  # 3 rows and 5 columns
    print(array1.ndim)  # number of dimensions
    print(array1.dtype)  # data type of the items inside our ndarray
    print(array1.itemsize)  # The size in bytes of each element of the array
    print(f"Size of the array1 in memory is : {array1.nbytes}")

    # Now we convert the items inside our array to something of a smaller size
    array2: numpy.ndarray = array1.astype(numpy.int8)
    print(array2)
    print(type(array2))
    print(array2.dtype)
    print(f"size of the array2 in memory is : {array2.nbytes}")

    array3 = numpy.random.rand(1_000_000).reshape(1_000_000, 1)  # a numpy nd array of 1 million random numbers, those numbers are between 0 (inclusive) and 1 (exclusive)
    print(array3)
    print(type(array3))
    print(array3.shape)
    result = numpy.sum(array3 ** 2)  # Sum of the squares of all the elements in array3 will be assigned to result
    print(result)

    list1 = [3, 4, 7, 8, 5, 3, 4, 9, 8, 5]
    print(list1)
    print(type(list1))
    array4 = numpy.array(list1)  # Converting a bare python list into a numpy array
    print(array4)
    print(type(array4))
    print(array4.shape)

    array5 = numpy.array([(6, 9, 3, 6), (0, 2, 7, 9)])  # Converting an array of tuples into numpy array
    print(array5)
    print(array5.shape)

    array6 = numpy.array([(8, 6, 2), (1, 5, 9)])
    print(array6)
    print(array6.shape)
    for element in array6.flatten():  # The easiest way for iterating through all the elements of a numpy array
        print(element)

    # This defines 10_000 random numbers following a normal distribution with a mean of 27_000 and a standard deviation of 15_000
    array7 = numpy.random.normal(27_000, 15_000, 10_000)
    mean: numpy.floating = numpy.mean(array7)
    print(mean)
    print(array7)
    print(type(mean))
