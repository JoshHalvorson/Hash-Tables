import bcrypt
import hashlib
# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = 0

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        hash = 0
        for i in range(0, len(key)):
            hash += ord(key[i])
        #return hash(key)
        return hash


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        if self.count >= self.capacity:
            self.resize()
        index = self._hash_mod(key)
        pair = LinkedPair(key, value)
        if self.storage[index] is not None and self.storage[index].key is not key and self.storage[index].next is None:
            self.storage[index].next = pair
            return
        elif self.storage[index] is not None and self.storage[index].key is not key and self.storage[index].next is not None:
            node = self.storage[index].next
            while node is not None:
                if node.next is None:
                    node.next = pair
                    return
                node = node.next
        self.storage[index] = pair
        self.count += 1


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        print(index)
        if self.storage[index] is not None:
            if self.storage[index].next is not None and self.storage[index].key is not key:
                node = self.storage[index]
                prev = node
                while node is not None:
                    if node.key is key:
                        if node.next is not None:
                            prev.next = node.next
                        else:
                            prev.next = None
                        return
                    prev = node
                    node = node.next
            elif self.storage[index].next is not None and self.storage[index].key is key:
                self.storage[index] = self.storage[index].next
            else:
                self.storage[index] = None


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] is not None:
            if self.storage[index].key is not key and self.storage[index].next is not None:
                node = self.storage[index]
                while node is not None:
                    if node.key is key:
                        return node.value
                    node = node.next

            return self.storage[index].value
        return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        new_storage = [None] * self.capacity
        for item in self.storage:
            if item is not None:
                new_index = self._hash_mod(item.key)
                new_storage[new_index] = item
        self.storage = new_storage
        


if __name__ == "__main__":
    ht = HashTable(8)

    ht.insert("key-0", "val-0")
    ht.insert("key-1", "val-1")
    ht.insert("key-2", "val-2")
    ht.insert("key-3", "val-3")
    ht.insert("key-4", "val-4")
    ht.insert("key-5", "val-5")
    ht.insert("key-6", "val-6")
    ht.insert("key-7", "val-7")
    ht.insert("key-8", "val-8")
    ht.insert("key-9", "val-9")
    ht.insert("key-10", "val-10")
    ht.insert("key-11", "val-11")
    ht.insert("key-12", "val-12")
    ht.insert("key-13", "val-13")

    print(len(ht.storage))

    print(ht.retrieve("key-0"))
    print(ht.retrieve("key-1"))
    print(ht.retrieve("key-2"))
    print(ht.retrieve("key-3"))
    print(ht.retrieve("key-4"))
    print(ht.retrieve("key-5"))
    print(ht.retrieve("key-6"))
    print(ht.retrieve("key-7"))
    print(ht.retrieve("key-8"))
    print(ht.retrieve("key-9"))
    print(ht.retrieve("key-10"))
    print(ht.retrieve("key-11"))
    print(ht.retrieve("key-12"))
    print(ht.retrieve("key-13"))



    # ht = HashTable(8)
    # ht.insert("key-0", "val-0")
    # ht.insert("key-1", "val-1")
    # ht.insert("key-2", "val-2")
    # ht.insert("key-3", "val-3")
    # ht.insert("key-4", "val-4")
    # ht.insert("key-5", "val-5")
    # ht.insert("key-6", "val-6")
    # ht.insert("key-7", "val-7")
    # ht.insert("key-8", "val-8")
    # ht.insert("key-9", "val-9")
    # ht.insert("key-10", "val-10")
    # ht.insert("key-11", "val-11")
    # # print(ht.retrieve("key-0"))
    # # print(ht.retrieve("key-1"))
    # # print(ht.retrieve("key-2"))
    # # print(ht.retrieve("key-3"))
    # # print(ht.retrieve("key-4"))
    # # print(ht.retrieve("key-5"))
    # # print(ht.retrieve("key-6"))
    # # print(ht.retrieve("key-7"))
    # # print(ht.retrieve("key-8"))
    # # print(ht.retrieve("key-9"))
    # # print(ht.retrieve("key-10"))
    # # print(ht.retrieve("key-11"))
    
    # # for item in ht.storage:
    # #     if item is not None:
    # #         print(item.key)
    # #     else:
    # #         print(item)

    # ht.remove("key-0")
    # ht.remove("key-1")
    # ht.remove("key-2")
    # ht.remove("key-3")
    # ht.remove("key-4")
    # ht.remove("key-5")
    # ht.remove("key-6")
    # ht.remove("key-7")
    # ht.remove("key-8")
    # ht.remove("key-9")
    # ht.remove("key-10")
    # ht.remove("key-11")

    # print(ht.retrieve("key-0"))
    # print(ht.retrieve("key-1"))
    # print(ht.retrieve("key-2"))
    # print(ht.retrieve("key-3"))
    # print(ht.retrieve("key-4"))
    # print(ht.retrieve("key-5"))
    # print(ht.retrieve("key-6"))
    # print(ht.retrieve("key-7"))
    # print(ht.retrieve("key-8"))
    # print(ht.retrieve("key-9"))
    # print(ht.retrieve("key-10"))
    # print(ht.retrieve("key-11"))