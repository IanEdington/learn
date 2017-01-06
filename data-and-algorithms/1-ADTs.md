# ADT's
https://en.wikipedia.org/wiki/Abstract_data_type
http://opendatastructures.org/ods-python/1_2_Interfaces.html

## What are ADTs?

Abstract data types is the interface. List, dictionary, stacks, queues, objects, all have their own way of thinking about data but none of them tell us how the data is stored or what algorithems are used to process the data.

From the point of view of the user
Purely theoretical

## Types of ADTs

### Queue's
Item's added and removed from a data structure in order.

#### Deque (Double Ended Queue)
interface: `addFirst | addLast | removeFirst | removeLast`  
Can implement both LIFO and FIFO queues.

#### FIFO (First in, First out)
interface: `add queue addFirst | remove dequeue removeLast`

#### Stack aka LIFO (Last in, First out)
interface: `push addFirst | pop removeFirst`

#### Priority Queue
This queue has some kind of prioritization that occurs during the add method.  
interface: `insert_with_priority | pop_next_priority_element deleteMin`

#### But Lists basically do all this:

![list deque and queue](img/list-deque-queue.png "list deque and queue")

### List or sequence
x<sub>1</sub>,x<sub>2</sub>,...,x<sub>n-1</sub>
 - `size()`: returns length of list
 - `get(i)`: returns x<sub>i</sub>
 - `set(i, y)`: sets x<sub>i</sub> to y
 - `add(i, y)`: add x at position i, moving _x<sub>i</sub>,...,x<sub>n−1</sub>_ => _x<sub>i+1</sub>,...,x<sub>n−1+1</sub>_
 - `remove(i)`: remove the value x<sub>i</sub>, moving _x<sub>i+1</sub>,...,x<sub>n−1</sub>_ => _x<sub>i</sub>,...,x<sub>n−1-1</sub>_

### Sets

#### Unordered Set (Uset or Mathematical Set)
This is the basis of dictionaries or named arrays. Each item can be stored as a pair of items.

- `size()`: return the number of elements in the set
- `add(x)`: add the element x to the set if not already present. Return true if x was added to the set and false otherwise.
- `remove(x)`: remove x from the set. Return x, or null if no such element exists.
- `find(x)`: find x in the set if it exists. Return y, or null if no such element exists.


#### Ordered Set (SSet)
Only add and find are different.
- `add(x)`: add element in sorted order
- `find(x)`: Find smallest element y, such that y ≥ x. Return y or null if no such element exists.

### Containers
Pointers to another object

### Graph


