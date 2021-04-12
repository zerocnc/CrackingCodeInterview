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

**Quadratic Probing** Resolving a hash collision by using the rehashing formula 
```c++
(HashValue + I*I) % arraySize
```
, where I is the number of times that the rehash function has been applied.

**Random Probing** - Resolving a hash collision by generating pseudo-random hash values in successive applications of the rehash function.

## Buckets and Chaining
### Another alternative for handling collisions is to allow multiple element keys to hash to the same location.

**Bucket** - A collection of elements associated with a particular hash location.

**Chain** - A linked list of elements that share the sasme hash location.

### **_Chosing a good Hash Function_**
* One way to minimize collisions is to use a data structure that has more space than is actually needed for the number of elements, in order to increase the range of the hash.
* Selecting the table size invovles a space vs. time-trade off.
* To avoid collisions, you need to know something about the **_statistical distribution_** of the keys.

#### **_Division method_**
* Very Simple
* The general function 
```c++
key % tableSize
```
* Best if the table size is a prime number.

**Folding** - A hash method that breaks the key into several pieces and concatenates or exclusive -OR's some of them to form the hash value.