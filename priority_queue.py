class PriorityQueue(object):
    """A priority queue implementation using a min-heap based on Skiena's Algorithm Design Manual.

    Attributes:
        array: An array of tuples to store data. The position of a tuple
            implicitly satisfies the rolf of pointers. Array index starts at 1
            to simplify matters. The root of the tree is stored in the first
            position of the array.
    """

    def __init__(self, array=None):
        """Initializes the priority queue with array of length 1."""
        if array is None:
            self.array = [(0, '')] # TODO: change?
        else:
            self.array = array

    def delete_min(self):
        """Remove the item from the priority queue whose key is minimum."""
        if len(self.array) > 2:
            self.array[1] = self.array.pop()
            self.__bubble_down(1)
        elif len(self.array) > 1:
            self.array.pop()
        else:
            raise ValueError('Warning: empty priority queue.')
        self.__print()

    def find_min(self):
        """Return the item whose key value is smaller than any other key in the priority queue."""
        if len(self.array) > 1:
            return self.array[1]
        else:
            raise ValueError('Warning: empty priority queue.')

    def insert(self, item):
        """Given an item with a key, insert it into the priority queue.

            Args:
                item: A tuple (key, value)
        """
        self.array.append(item)
        self.__bubble_up(len(self.array) - 1)
        self.__print()

    def __bubble_down(self, new):
        child = 2*new
        min_index = new
        for i in range(2):
            if child + i <= len(self.array) - 1:
                if self.__is_greater_than(min_index, child + i):
                    min_index = child + i
        if min_index != new:
            self.__swap(new, min_index)
            self.__bubble_down(min_index)

    def __bubble_up(self, new):
        parent = self.__parent(new)
        if parent == -1:
            return
        elif self.__is_greater_than(parent, new):
            self.__swap(new, parent)
            self.__bubble_up(parent)

    def __is_greater_than(self, parent, new):
        return self.array[parent][0] > self.array[new][0]

    def __parent(self, key):
        return -1 if key == 1 else int(key/2) # implicitly take floor(key/2)

    def __print(self):
        if len(self.array) > 1:
            print 'array: {0}\nsize: {1}; minimum: {2}'.format(self.array, len(self.array) - 1, self.find_min())
        else:
            print 'array: {0}\nWarning: empty priority queue.'.format(self.array)

    def __swap(self, new, old):
        temp = self.array[old]
        self.array[old] = self.array[new]
        self.array[new] = temp
