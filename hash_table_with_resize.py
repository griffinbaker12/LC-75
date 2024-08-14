class HashTableWithResize:
    def __init__(self, size=8, capacity=0.75, g_factor=2) -> None:
        self.size = size
        self.capacity = capacity
        self.g_factor = g_factor
        self.count = 0
        self.buckets = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def resize(self):
        print("\n*** BUCKETS BEFORE RESIZE ***")
        print(self.buckets)
        buckets_to_remap = [
            [k, v]
            for idx_bucket in self.buckets
            if idx_bucket is not None
            for k, v in idx_bucket
        ]
        self.size *= self.g_factor
        self.buckets = [None] * self.size
        self.count = 0
        for [k, v] in buckets_to_remap:
            self.set(k, v)
        print("\n*** RESIZED ***")
        print(self.buckets)

    def set(self, key, value):
        index = self._hash(key)
        print(f"the index for {key} is {index}")
        v = self.buckets[index]
        if v is None:
            self.buckets[index] = [[key, value]]
        else:
            for item in v:
                if item[0] == key:
                    item[1] = value
                    return
            self.buckets[index].append([key, value])
            print("*** COLLISION ***")
        self.count += 1
        if self.count / self.size >= self.capacity:
            self.resize()

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


ht = HashTableWithResize()
ht.set("name", "joe")
ht.set("name", "greg")
ht.remove("name")

ht.set("name", "pixel")
ht.set("age", 99)
ht.set("style", "hip")
ht.set("pet", "cat")
ht.set("fav_drink", "coffee")
ht.set("fav_food", "meat")
ht.set("aura", "s-tier")
