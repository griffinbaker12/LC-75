class SimpleHashTable:
    def __init__(self, size=8) -> None:
        self.size = size
        self.count = 0
        self.buckets = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def set(self, key, value):
        index = self._hash(key)
        v = self.buckets[index]
        if v is None:
            self.buckets[index] = [[key, value]]
        else:
            for item in v:
                if item[0] == key:
                    item[1] = value
                    return
            self.buckets[index].append([key, value])
        self.count += 1

    def get(self, key):
        index = self._hash(key)
        buckets = self.buckets[index]
        if buckets is None:
            return -1
        else:
            for [k, v] in buckets:
                if k == key:
                    return v

    def remove(self, key):
        index = self._hash(key)
        buckets = self.buckets[index]
        if buckets is None:
            return
        self.buckets[index] = [[k, v] for k, v in buckets if k != key]


ht = SimpleHashTable()
ht.set("name", "joe")
print(ht.get("name"))
ht.set("name", "greg")
print(ht.get("name"))
ht.remove("name")
print(ht.get("name"))
