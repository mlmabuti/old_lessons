class HashTable:
    def __init__(self, size):
        self.size = size  # enter table size
        self.data = [[]] * self.size  # create list with size allocation

    def set(self, key, value):
        address = hash(key) % self.size  # generate hash address
        if not self.data[address]:  # if hash address empty, create list
            self.data[address] = []
        self.data[address].append([key, value])  # append key and value in list
        return self.data  # return the new hash table with inserted key value

    def get(self, key):
        address = hash(key) % self.size  # find the address by generating the hash again
        curr_bucket = self.data[address]  # point to current list with corresponding hash address
        if curr_bucket:  # check if the list has something
            for i in range(0, len(curr_bucket)):  # if it does then loop through all
                if curr_bucket[i][0] == key:  # if the current list has the matching key
                    return curr_bucket[i][1]  # then return the value
        return None