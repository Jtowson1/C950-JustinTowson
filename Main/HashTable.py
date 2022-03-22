# Hashtable class to store the package information in a table

class HashTable:
    # Constructor to build the hashtable for use
    # space-time complexity is O(n) because of the for loop

    def __init__(self, initial_capacity=40):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Insert function to take information and insert into the hashtable
    # space-time complexity is O(n) because of the for loop

    def insert(self, key, item):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True

        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Search function to search for items in the hashtable
    # space-time complexity is O(n) because of the for loop

    def search(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]
            return None

    # Remove function to delete information from the hashtable
    # space-time complexity is O(n) because of the for loop

    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove(kv[0])
