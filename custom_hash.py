def print_separator():
    print("\n" + "=" * 50 + "\n")


class MutableKey:
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        print(f"calculating hash for {self.value}")
        return hash(self.value)

    def __eq__(self, other):
        print(f"comparing {self.value} and {other.value}")
        return isinstance(other, MutableKey) and self.value == other.value

    def __repr__(self):
        return f"MutableKey({self.value})"


original_key = MutableKey(5)
my_dict = {original_key: "some_value"}

print("init state:")
print(f"dict: {my_dict}")
print(f"value for original_key: {my_dict[original_key]}")

print_separator()

print("modifying the key:")
original_key.value = 10
print(f"changed original_key.value to {original_key.value}")
print(f"dict (note the key change): {my_dict}")

print_separator()

print("trying to access with the modified original key:")
try:
    print(my_dict[original_key])
except KeyError:
    print("KeyError: unable to find key")

print_separator()

print("trying to access with a new key of the original value:")
old_key = MutableKey(5)
try:
    print(my_dict[old_key])
except KeyError:
    print("KeyError: unable to find key")

print_separator()

print("actual contents of the dict:")
for k, v in my_dict.items():
    print(f"{k}: {v}")

print_separator()

print("the key-value pair still exists in the dict but is effectively unreachable...")
print("don't use mutable values as keys in dicts")
