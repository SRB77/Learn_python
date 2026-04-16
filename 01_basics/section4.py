print(type("python"))

#* Mutable and imutable in python 

# > Immutable data structres in python 
"""
#! All Numerical Data-Structure are Immutable 
1. int
2. float
3. complex
4. bool(1/0)

#! All Sequential Data-Structure except (List)
1. str
2. tuple
3. range
4. bytes

#! Collection and Special types 
1. frozenset (This is a collection an immutable version of set , set is mutable)
2. NoneType : The type of None Object 
3. Ellipsis : The ... object (often used in slicing or type hinting).
the above 2 are special type 
"""
"""
print("above all are python immutable built-in data-structure / types")
def someFucn():
    print(type(...)) 
    return ... #> This would return Ellipsis (it's a placeholder object)

print(someFucn())
"""

#> mutable data structres in python

"""

1. list: An ordered collection of items that can be changed, added to, or removed using methods like .append() or .pop().

2. dict (Dictionary): A mapping of unique immutable keys to mutable values. You can add new key-value pairs or update existing ones directly.

3. set: An unordered collection of unique elements. Unlike the frozenset, a standard set allows adding or removing items.

4. bytearray: A mutable sequence of integers (0-255). It is essentially a mutable version of the bytes type, allowing in-place modification of binary data.

5. memoryview: This object provides a "view" into the memory of other objects (like bytearray). If the underlying object it points to is mutable, the memoryview itself can be used to mutate that data without making a copy.

6. User-Defined Classes: Unless explicitly designed to be immutable (e.g., using @dataclass(frozen=True)), objects created from custom classes are mutable by default. 

"""