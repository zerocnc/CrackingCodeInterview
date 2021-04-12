# Chapter 1 - Arrays & Strings

## Lists

### Keywords
**Lists**: are a homogenous collection of elements with a linear relationship between elements.

**Linear relationships** - Each element except the first has a unique predecessor, and each element except the last has a unique successor.

**Length** - The number of items within a list; the length can vary over time.

**Unsorted List** - A list in which data items are placed in no particular order; the only relationship between the data elements is the list predecessor and successor relationships.

**Sorted List** - A list that is sorted by the value in the key; there is a semantic relationship among the keys of the items in the list.

**Key** - A member of a record (struct or class) whose value is used to determine the logical and/or physical order of the items in a list.

**Iterators** - Iterators are used with composite types to allow the user to process an entire structure, component by component.

## Hashing

### Keywords

**Hash Function**: A function used to manipulate the key of an element in a list to identify its location in the list.

**Hashing** - The technique used for ordering and accessing elements in a list in a relatively constant amount of time by manipulating the key to identify its location in the list.

**Collision** - The condition resulting when two or more keys produce the same has location.

**Linear Probing** - Resolving a hash collision by sequentially searching a hash table beginning at the location returned by the hash function.

**Clustering** - The tendency of elements to become unevenly distributed in the has table, with many elements clustering around a single hash location.

**Rehashing** - Resolving a collision by computing a new hash location from a hash function that manipulates the original locatoin rather than the elements key.

**Quadratic Probing** Resolving a hash collision by using the rehasing formula 
'''
(HashValue + I<sup>2</sup>) % arraySize
'''
, where I is the number of times that the rehash function has been applied.

**Random Probing** - Resolving a hash collision by generating pseudo-random hash values in successive applications of the rehash function.