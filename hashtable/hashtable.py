class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity = MIN_CAPACITY):
        self.capacity = capacity
        self.table = [None] * self.capacity
        self.load = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.capacity)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.load/self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        size = 2**64
        prime = 0x100000001b3
        FNV1_64_INIT = 0xcbf29ce484222325
        value = FNV1_64_INIT
        for byte in key:
            value = (value * prime) % size
            value = value^ord(byte)
        return value


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity
        
    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        new_entry = HashTableEntry(key,value)
        
        index = self.hash_index(key)
        if self.table[index] is not None:
            if self.table[index].key == key:
                
                self.table[index].value = value
            else:
                cur_node = self.table[index]
                while cur_node.next is not None:
                    if cur_node.key == key:
                        cur_node.value = value
                    cur_node = cur_node.next
                if cur_node.key == key:
                    cur_node.value = value
                else:
                    cur_node.next = new_entry
            
        else:
            self.table[index] = new_entry
            
        self.load += 1
        if self.get_load_factor() >= .7:
            self.resize((self.capacity*2))
       
        
    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        if self.table[index] is None:
        
            return None
        elif self.table[index].key == key:
            self.load -= 1
            if self.table[index].next is not None:
                self.table[index] = self.table[index].next
            else:
                self.table[index] = None

        
        else:
            prev_node = self.table[index]
            cur_node = self.table[index].next
            while cur_node is not None:
                
                if cur_node.key == key:
                    prev_node.next = cur_node.next
                    self.load -= 1
                    return "deleted"
                else:
                    prev_node = cur_node
                    cur_node = cur_node.next
            
            return "No value found at key"
        


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        if self.table[index] is None:
            return None
        elif self.table[index].key == key:
            return self.table[index].value
        elif self.table[index] is not None:
            cur_node = self.table[index]
            while cur_node.next is not None:
                next_node = cur_node.next
                if next_node.key == key:
                    return next_node.value
                else:
                    cur_node = next_node
            return None
        

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        old_table = self.table
        self.capacity = new_capacity
        self.table = [None] * self.capacity
        for node in old_table:
            if node is not None:
                self.put(node.key, node.value)



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
