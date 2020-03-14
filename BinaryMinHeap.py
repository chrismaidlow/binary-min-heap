class BinaryMinHeap:
    # DO NOT MODIFY THIS CLASS #
    def __init__(self):
        """
        Creates an empty hash table with a fixed capacity
        """
        self.table = []

    def __eq__(self, other):
        """
        Equality comparison for heaps
        :param other: Heap being compared to
        :return: True if equal, False if not equal
        """
        if len(self.table) != len(other.table):
            return False
        for i in range(len(self.table)):
            if self.table[i] != other.table[i]:
                return False

        return True

    ###### COMPLETE THE FUNCTIONS BELOW ######

    def __str__(self):
        pass

    def get_size(self):
        """
        returns size of table
        :return: length of list
        """
        return len(self.table)

    def parent(self, position):
        """
        returns parent of value at given index
        :param position: index of value
        :return: parent of given index
        """
        return (position - 1) // 2

    def left_child(self, position):
        """
        returns left child of value at given index
        :param position: index of value
        :return: left child of given index
        """
        return 2 * position + 1

    def right_child(self, position):
        """
        returns right child of value at given index
        :param position: index of value
        :return: right child of given index
        """
        return 2 * position + 2

    def has_left(self, position):
        """
        returns whether a value is present at index
        :param position: index to check
        :return: True or False
        """
        index = 2 * position + 1
        if index >= len(self.table):
            return False
        else:
            return True

    def has_right(self, position):
        """
        returns whether a value is present at index (right)
        :param position: index to check
        :return: True or False
        """
        index = 2 * position + 2
        if index >= len(self.table):
            return False
        else:
            return True

    def find(self, value):
        """
        Iterates through list searching for value
        :param value: value to search for
        :return: Index or false
        """
        counter = 0
        for item in self.table:
            if item == value:
                return counter
            else:
                counter += 1
        return None 
    
    def heap_push(self, value):
        """
        Pushes on to heap and then percolates
        :param value: value to push
        :return: no return
        """
        if value in self.table:
            return 
        # add the new value to the end of the array.
        self.table.append(value)
        # percolate up from the last index to restore heap property
        self.percolate_up(len(self.table) - 1)

    def heap_pop(self, value):
        """
        Pops value from heap and the percolates
        :param value: value to pop
        :return: no return
        """
        index = self.find(value)
        # move the last item in the array into index of value.
        if index == None:
            return
        last_child = self.table.pop()
        if len(self.table) > index:
            self.table[index] = last_child
            # percolate down to restore min heap property.
            self.percolate_down(index)

    def pop_min(self):
        """
        Pops value minimum value from heap and the percolates
        :return: minimum value
        """
        if self.get_size() == 0:
            return None
        if self.get_size() == 1:
            return_val = self.table.pop()
            return return_val
        # save the max value from the root of the heap.
        min_value = self.table[0]
        # move the last item in the array into index 0.
        replace_value = self.table.pop()
        if len(self.table) > 0:
            self.table[0] = replace_value
            # percolate down to restore min heap property.
            self.percolate_down(0)
        # return the max value
        return min_value

    def swap(self, p1, p2):
        """
        swaps values at given indeces
        :param p1: index of first value
        :param p2: index of second value
        :return: no return
        """
        val1 = self.table[p1]
        val2 = self.table[p2]
        self.table[p1] = val2
        self.table[p2] = val1

    def percolate_up(self, position):
        """
        percolate value upwards
        :param position: index of percolate position
        :return: no return
        """
        while position > 0:
            # compute the parent node's index
            parent_index = (position - 1) // 2
            # check for a violation of the max heap property
            if self.table[position] >= self.table[parent_index]:
                # no violation, so percolate up is done.
                return
            else:
                # swap heap_array[node_index] and heap_array[parent_index]
                temp = self.table[position]
                self.table[position] = self.table[parent_index]
                self.table[parent_index] = temp
                # continue the loop from the parent node
                position = parent_index

    def percolate_down(self, position):
        """
        percolate value downwards
        :param position: index of percolate position
        :return: no return
        """
        child_index = 2 * position + 1
        value = self.table[position]
        while child_index < len(self.table):
            # Find the min among the node and the node's children
            min_value = value
            min_index = -1
            i = 0
            while i < 2 and i + child_index < len(self.table):
                if self.table[i + child_index] < min_value:
                    min_value = self.table[i + child_index]
                    min_index = i + child_index
                i = i + 1
            # check for a violation of the max heap property
            if min_value == value:
                return
            else:
                # swap heap_array[node_index] and heap_array[max_index]
                temp = self.table[position]
                self.table[position] = self.table[min_index]
                self.table[min_index] = temp
                # continue loop from the larger child node
                position = min_index
                child_index = 2 * position + 1


def heap_sort(unsorted):
    """
    sort a list in ascending order
    :param unsorted: list to be sorted
    :return: sorted list
    """
    heap = BinaryMinHeap()
    final_heap = BinaryMinHeap()
    for item in unsorted:
        heap.heap_push(item)
    i = 0
    sizer = heap.get_size()
    final_heap.table = [None] * heap.get_size()
    while i < sizer:
        minim = heap.pop_min()
        final_heap.table[i] = minim
        i += 1
    return final_heap.table
    