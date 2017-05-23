# Data Structures and Algorithms

## Learning Outcomes
After completing each section you should be able to:

### Unit 1: Introduction
- [ ] explain the concept of data structures
- [ ] explain the concept of algorithms
- [ ] explain the need for efficiency in data structures and algorithms
- [ ] distinguish the difference between an interface and an implementation
- [ ] use mathematical concepts required to understand data structures and algorithms
- [ ] apply a model of computation
- [ ] apply correctness, time complexity, and space complexity to data structures and algorithms

### Unit 2: Array-Based Lists
- [ ] implement List interfaces
- [ ] implement Queue interfaces

### Unit 3: Linked Lists
- [ ] implement singly-linked lists
- [ ] implement doubly-linked lists
- [ ] implement space-efficient linked lists

### Unit 4: Skiplists
- [ ] implement skiplists

### Unit 5: Hash Tables
- [ ] explain hash functions (division, multiplication, folding, radix transformation, digit rearrangement, length-dependent, mid-square)
- [ ] estimate the effectiveness of hash functions (division, multiplication, folding, radix transformation, digit rearrangement, length-dependent, mid-square)
- [ ] differentiate between various hash functions (division, multiplication, folding, radix transformation, digit rearrangement, length-dependent, mid-square)
- [ ] recognize various collision resolution algorithms—open addressing (linear probing, quadratic probing, double hashing), separate chaining (normal, with list heads, with other data structures), coalesced hashing, robin hood hashing, cuckoo hashing, hopscotch hashing, dynamic resizing (resizing the whole, incremental resizing)
    - linear probing: if you don't find it add more
- [ ] implement hash tables
- [ ] implement collision detection in hash tables
- [ ] analyze collision detection in hash tables
- [ ] develop hash codes

### Unit 6: Recursion
- [x] define recursion
    - a method that calls itself
- [x] inspect recursive programs
- [x] create different types of recursive programs
- [x] differentiate recursive solutions from iterative solutions
- [ ] estimate the time complexity of recursive programs

### Unit 7: Binary Trees
- [x] define binary tree
- [x] define binary search tree
- [x] examine a binary tree and binary search tree
- [x] implement a binary tree and binary search tree
- [x] define AVL tree

### Unit 8: Scapegoat Trees
- [x] define scapegoat tree
    * tree that preforms partial rebuilding
    * when it becomes unbalanced it finds a "scape-goat" and tells it to rebalance itself
- [x] examine a scapegoat tree
- [x] implement a scapegoat tree

### Unit 9: Red–Black Trees
- [x] define red–black tree
- [x] examine a red–black tree
- [x] implement a red–black tree

### Unit 10: Heaps
- [ ] define heap
- [ ] examine a binary heap tree
- [ ] implement a binary heap tree
- [ ] define meldable heap
- [ ] examine a randomized meldable heap

### Unit 11: Sorting Algorithms
- [ ] describe sorting algorithms (merge, quick, heap, counting, radix)
- [ ] estimate the complexity of sorting algorithms
- [ ] compare sorting algorithms

### Unit 12: Graphs
- [ ] represent a graph by a matrix
- [ ] represent a graph in adjacency lists
- [ ] understand the execution process of the depth-first-search and bread-first-search algorithms for traversing a graph
- [ ] analyze the performance of the depth-first-search and bread-first-search algorithms for traversing a graph
- [ ] implement those search algorithms for traversing a graph in pseudo-code or other programming languages, such as Java, C, or C++, etc

### Unit 13: Binary Trie
- [ ] define trie
- [ ] examine a binary trie
- [ ] explain binary trie

## Abstract Data Type (ADT)
Abstract data types is the interface. List, dictionary, stacks, queues, objects, all have their own way of thinking about data but none of them tell us how the data is stored or what algorithms are used to process the data.

### Queue Interface
Item's added and removed from a data structure in order.

#### FIFO aka Queue (First in, First out)
interface: `add queue addFirst | remove dequeue removeLast`

#### LIFO aka Stack (Last in, First out)
interface: `push addFirst | pop removeFirst`

#### Deque (Double Ended Queue)
super set of FIFO and LIFO
interface: `addFirst | addLast | removeFirst | removeLast`  

#### Priority Queue
This queue has some kind of prioritization that occurs during the add method.  
interface: `insert_with_priority | pop_next_priority_element deleteMin`

### List or Sequence Interface
![list deque and queue](img/list-deque-queue.png "list deque and queue")

Superset of Deque plus:

x_1,x_2,...,x_(n-1)
 - `size()`: returns length of list
 - `get(i)`: returns x_i
 - `set(i, x)`: sets x_i to x
 - `insert(i, x)`: add x at position i, moving x_i,...,x_(n−1) => x_(i+1),...,x_(n−1+1)
 - `remove(i)`: remove and return the value x_i, moving x_(i+1),...,x_(n−1) => x_i,...,x_(n−1-1)

### Set

#### Unordered Set (Uset or Mathematical Set)
This is the basis of dictionaries or named arrays in PHP.
Each item can be stored as a pair of items.

- `size()`: return the number of elements in the set
- `insert(x)`: add the element x to the set if not already present. Return true if x was added to the set and false otherwise.
- `search(x)`: find x in the set if it exists. Return x or null if no such element exists.
- `delete(x)`: remove x from the set. Return x or null if no such element exists.


#### Ordered Set (SSet)
Only add and find are different.
- `insert(x)`: add element in sorted order
- `search(x)`: Find smallest element y, such that y ≥ x. Return y or null if no such element exists.

### Graph

## Implementation data structures

### Arrays

### Linked Objects
- trees
- lists

## Mathematical Background

### Exponentials

### Logarithms

### Factorials

Stirling's Approximation

### Binomial Coefficients

### Sets and Set Membership

* \(x \in A\): x is an element of A
* \(B \subset A\): B is a subset of A

### Asymptotic Notation
Upper and lower bounds of running time.
Only takes into consideration the most powerful component.
Any constant can be used to make the function larger or smaller to fit the bounds.

Θ(g(n)) = {f(n): there exist positive constants \(c_1\) , \(c_1\), and \(n_0\) such that  
\(c_2∙g(n) \geq f(n) \geq c_1∙g(n) \geq 0 for all n \geq n_0\)}
- \(n_0\): minimum possible value
- \(c_1\): constant that defines lower bound
- \(c_2\): constant that defines upper bound

Big O: Upper bound  
Big \(\Omega\): Lower bound  
Big \(\Theta\): Upper and lower bound  

There are a few assumptions about the functions.

- Asymptotically non-negative: only works in the positive quadrant

Example of how to calculate constants & lower value: Intro to Alg(pg 46)

$$
c_{1}n^2 \leq \frac{1}{2}n^2 - 3n \leq c_{2}n^2
$$

For all \(n \geq n_0\). Dividing by n^2 yields

$$
c_{1} \leq \frac{1}{2} - \frac{3}{n} \leq c_{2}
$$

## Algorithm Analysis

### Properties used to analyse algorithms
Algorithms are generally analysed based on Correctness, Time Complexity, and Space Complexity.

#### Correctness
Accuracy of the algorithm's result.  
This is generally the highest concern of an algorithm since dependably calculating results is usually the most valuable feature of an algorithm. However, a less accurate algorithm may be useful for complicated problems where a accurate solution is too time consuming.

#### Time Complexity
The running time of an algorithm.  
Next to accuracy, time complexity is the next most optimized property. Algorithms are most often compared based on this property since space is generally inexpensive, and correctness is usually assumed.

- Worst-case running times
: The slowest possible time an algorithm can take. ie. Bubble sorting a list that is in reverse sorted order.

- Amortized running times
: Worst case running time of a sequence of n actions.
O(m) represents that if m operations are completed the total running time will not exceed O(m) even though a specific operation may be a larger order function.
A good example of this is the resize operation within a deque, or list operation. Even though the resize operation is expensive it is performed in proportion to the number of other operations in the sequence.

- Expected running times
: A type of probabilistic analysis where a random dataset is used to determine an average running time based on randomized dataset.

#### Space Complexity
The amount of memory needed for an algorithm.  
Except in specific cases space is not a large factor in the usefulness of an algorithm, since memory is relatively inexpensive compared to computing power and correctness.

### How to analyse an algorithm
Count up all the steps it takes for different inputs.

#### The RAM (Random Access Machine) Model of Computation
RAM model (W-bit machine)

Still don't understand how memory works in this model (w-bit word)

How do we calculate algorithm costs?
We use a model.
The model is based on memory, operators, and pointers.

1 processor: instructions are executed one after another  
cells(RAM): holds a w-bit word  
operations: arithmetic (add, subtract, multiply, divide, remainder, floor, ceiling)  
- data movement (load, store, copy)
- control (conditional and unconditional branch, subroutine call and return)

Some of these assumptions are not true about computers, however, they are close enough to be useful without being overly complicated.
The RAM model does not account for the memory hierarchy (cache, ram, drive)

### Recursion
TODO: Hakan Haberdar, “How to Compute Time Complexity of Recursive Algorithms”, Computer Science Tutorials [online\], (Accessed 10-18-2016) Available from: <http://www.haberdar.org/time-complexity-recursive-algorithms-tutorial.htm>

- [Recursive Factorial](http://www.cs.usfca.edu/~galles/visualization/RecFact.html)
- [Recursive Reverse](http://www.cs.usfca.edu/~galles/visualization/RecReverse.html)
- [Recursive N-Queens](http://www.cs.usfca.edu/~galles/visualization/RecQueens.html)

### Amortization

### Divide-and-conquer

### Prune-and-search (aka decrease-and-conquer)

### Brute force

### The greedy method

### Dynamic programming

## Array-Based: List
TODO: Implement

Fast Stack Operations Using an Array
FILO stack that is implemented using an array.

Add in the middle of an array:
    1. check if array is long enough
        1. resize if not big enough
    1. move items over (for loop)
    1. assign element

Remove for middle of array:
    1. move items left starting at item right of the item to be removed (for loop)
    1. check if array is too long
        1. resize

2.2 FastArrayStack: An Optimized ArrayStack: 
There are functions that are more efficient than for loops for copying and moving elements in an array.  
C: `memcpy(d, s, n)` and `memmove(d, s, n)`  
C++: `std :: copy(a0, a1, b)`  
Java: `System.arraycopy(s,i,d,j,n)`  

An Array-Based Queue
FIFO queue implemented with an "unlimited" array.
This array only ever has to be n elements long, where n is the number of items in the queue.
This is accomplished by wrapping around the end point.
This is accomplished using an integer to represent the first and last position of the queue.
These positions are incremented and decremented as if they were part of an unlimitedly long queue.
To find the index of first or last element a modulo over the size of the array is performed.
Checking if the array is to large is accomplished by taking the delta of the first and last number and comparing it to the size of the array.
The array is empty if the first and last positions are equal.
Growing or shrinking the array is accomplished using by copying to a new array and resetting the index.

Fast Deque Operations Using an Array
By treating the Deque as an "unlimited length" array we can use the same wrapping technique to optimize the shifting by only every making the shortest shift.
This is done by shifting on the left when the item to be shifted is on the left side and shifting on the right when the item is on the right side of centre.
This optimizes for the smallest number of elements to be shifted.

## Rootish Array Stack: A Space-Efficient Stack

The benefit of this structure is reduced size.

An array of array's n deep. Each sub-array has b elements where b is the block number.

  | 123456
--|-------
0 | x
1 | xx
2 | xxx

Because of the complicated structure finding any given item is more complicated since each index needs to be translated into a block and item index.

The block and the item both require equations to find.

## Linked Lists: List

### Singly-Linked List

### Doubly-Linked List

### Space-Efficient Linked List
TODO: Implement

## Skip list: List
Time Complexity: O(log(n)) With High Probability (WHP).
Space Complexity: O(log(n))?

## Hash Table: Unordered Set
TODO: Implement

### Hash function
TODO: finish notes

- Division Hashing (k mod m, ect)

        53 – 2^5 to 2^6
        97 – 2^6 to 2^7
        193 – 2^7 to 2^8
        389 – 2^8 to 2^9
        769 – 2^9 to 2^10

- multiplication
- folding
- radix transformation
- digit rearrangement
- length-dependent
- mid-square

### Collision Detection and Resolution Algorithms
TODO: finish notes

- probing: Linear, Quadratic, double hashing
- open addressing (linear probing, quadratic probing, double hashing)
- separate chaining (normal, with list heads, with other data structures)
- coalesced hashing, robin hood hashing, cuckoo hashing, hopscotch hashing
- dynamic resizing (resizing the whole, incremental resizing)

## Binary Trees: Ordered Set

### Binary Search Tree
- define *binary tree*.
- define *binary search tree*.
- examine a binary tree and binary search tree.
- implement a binary tree and binary search tree.

### AVL Tree
TODO: Implement

self-balancing binary search tree
height-balanced: at any node in the tree the height of it's two child subtrees differ by at most 1
rebalances using rotations on insertion and deletion
requires an additional piece of information keep in each node (height)

Lookup, insertion, and deletion all take O(log n) time in both the average and worst cases


<http://en.wikipedia.org/wiki/AVL_tree>

<http://www.cs.ucf.edu/~dmarino/ucf/cop3502/lec_biswas/trees5.pdf>

- [Binary Search Tree](http://www.cs.usfca.edu/~galles/visualization/BST.html)
- [AVL Tree (balanced binary search trees)](http://www.cs.usfca.edu/~galles/visualization/AVLtree.html)

- Check the desired learning outcomes at the beginning of this unit. Go through the exercises at the end of Chapter 6; use the Unit 7 outcomes as a focus for your activities. Post to the Unit 7 discussion forum if you have questions. Check the Unit 7 discussion forum to see if you can answer a question someone else has posted or share a link to an online resource you have found useful. Look at Assignment 2—how much can you do at this point? Plan to revise your attempts before your final submission.

### Scapegoat Tree
TODO: Implement

- define
- examine
- implement

### 2, 4 Tree
TODO: Implement

### Red–Black Tree
TODO: Implement

- define
- examine
- implement

- [Red–Black Tree](http://www.cs.usfca.edu/~galles/visualization/RedBlack.html)

### Comparison
It is important to understand and demonstrate the differences between AVL trees, red–black trees, and (2,4) trees in terms of the key properties of these trees; the process of adding or removing nodes in the trees while maintaining these key properties with appropriate operations; and running time or cost to maintain the properties.

AVL trees are often compared to red–black trees because they support the same set of operations and because red−black trees also take O(log n) time for the basic operations. AVL trees perform better than red–black trees for lookup-intensive applications. AVL trees, red–black trees, and (2,4) trees share a number of good properties, but AVL trees and (2,4) trees require extra operation to deal with restructuring (rotations), fusing, or splitting. However, red–black trees do not have these drawbacks.

## Binary Heaps (Array)
TODO: Implement
- define, examine and implement a binary heap tree

- [Min Heap](http://www.cs.usfca.edu/~galles/visualization/Heap.html)
- [Binomial Queue](http://www.cs.usfca.edu/~galles/visualization/BinomialQueue.html)
- [Fibonacci Heap](http://www.cs.usfca.edu/~galles/visualization/FibonacciHeap.html)
- [Leftist Heap](http://www.cs.usfca.edu/~galles/visualization/LeftistHeap.html)
- [Skew Heap](http://www.cs.usfca.edu/~galles/visualization/SkewHeap.html)

## Meldable Heaps
TODO: Implement

- define and examine a randomized meldable heap.

## Matrix Graphs
TODO: Implement

- represent a graph by a matrix
- understand, implement, and analyze the depth-first-search

## Adjacency Graphs
TODO: Implement

- represent a graph in adjacency lists
- understand, implement, and analyze the bread-first-search

- [Breadth-First Search](http://www.cs.usfca.edu/~galles/visualization/BFS.html)
- [Depth-First Search](http://www.cs.usfca.edu/~galles/visualization/DFS.html)
- [Connected Components](http://www.cs.usfca.edu/~galles/visualization/ConnectedComponent.html)
- [Dijkstra Shortest Path](http://www.cs.usfca.edu/~galles/visualization/Dijkstra.html)
- [Prim Minimum Cost Spanning Treeh](http://www.cs.usfca.edu/~galles/visualization/Prim.html)
- [Topological Sort (Indegree)](http://www.cs.usfca.edu/~galles/visualization/TopoSortIndegree.html)
- [Topological Sort (DFS)](http://www.cs.usfca.edu/~galles/visualization/TopoSortDFS.html)
- [Floyd-Warshall All-Pairs Shortest Path](http://www.cs.usfca.edu/~galles/visualization/Floyd.html)
- [Kruskal Minimum Cost Spanning Treeh](http://www.cs.usfca.edu/~galles/visualization/Kruskal.html)

### Breadth-First Search
TODO: Implement

### Depth-First Search
TODO: Implement

## Binary Trie

- define trie.
- examine a binary trie.
- explain binary trie.

- [B Trees](http://www.cs.usfca.edu/~galles/visualization/BTree.html)
- [B+ Trees](http://www.cs.usfca.edu/~galles/visualization/BPlusTree.html)

## Algorithms
### Recursion

- define *recursion*.
- inspect recursive programs.
- create different types of recursive programs.
- differentiate recursive solutions from iterative solutions.
- estimate the time complexity of recursive programs.

Recursion is a wonderful programming tool. It provides a simple,
powerful way of approaching a variety of problems. It is often hard,
however, to see how a problem can be approached recursively; it can be
hard to “think recursively.” It is also easy to write a recursive
program that either takes too long to run or doesn’t properly terminate
at all. In this unit we’ll go over the basics of recursion and hopefully
help you develop, or refine, a very important programming skill.

Study Appendix C in the reference text (Barnett and Tongo’s *[Data
Structures and Algorithms: Annotated Reference with
Examples](http://dotnetslackers.com/Community/files/folders/data-structures-and-algorithms/entry30283.aspx)*)
that introduces you to the concept of recursion.

Let us look at some simple recursive code.

#### Decimal to Binary Representation

Here we keep on dividing the number by 2 recursively until it reduces to
zero, then print the remainders in reverse order.

*Example:* convert decimal number 5 to its binary representation

> 5/2 = 2, remainder is 1
> 2/ 2 = 1, remainder is 0
> 1/2 = 0, remainder is 1

We stop here because the number has been reduced to zero. Now collect
the remainders in reverse order. The binary representation is 101.

*Example:* convert decimal number 11 to its binary representation

> 11/2 = 5, remainder is 1
> 5/2 = 2, remainder is 1
> 2/ 2 = 1, remainder is 0
> 1/2 = 0, remainder is 1

We stop here because the number has been reduced to zero and collect the
remainders in reverse order. The binary representation is 1011.

*Example:* convert decimal number 14 to its binary representation

> 14/ 2 = 7, remainder is 0
> 7/2 = 3, remainder is 1
> 3/2 = 1, remainder is 1
> 1/2 = 0, remainder is 1

We stop here because the number has been reduced to zero and collect the
remainders in reverse order. The binary representation is 1110.

Here is a recursive function (in C++) that prints the binary equivalent
of any given decimal number:

```
void decibinary (int num) {
    if (num < 2)
    {
        printf(“%d”,  num);
    }
    else
    {
        decibinary(num/2);
        printf(“%d”,  num%2);
    }
}
```

#### Printing a String in Reverse Order

Let ss store a string of length n. To print this string in reverse
order, print the last character of the string, and call the function
recursively with size one less than the previous length. The function
can be terminated when there is just a single character to be printed.
Here is the function in C++:

```
void  print_reverse(char ss[], int n) {
    //  Only one character to print, so print it!
    if  (n == 1)
    {
        printf("%c",  ss[0]);
    }
    // Solve the problem recursively: print the last character, then reverse the  substring without that last character.
    else
    {
        printf("%c",  ss[n-1]);
        print_reverse(ss,  n-1);
    }
}
```

#### Checking for Palindromes

Palindrome: a word, phrase, verse, or sentence that reads the same
backward or forward. Here are few palindromes:

> borrow or rob
>
> gateman sees name garageman sees name tag
>
> murder for a jar of red rum
>
> a nut for a jar of tuna

How do you mathematically define a palindrome? Here is a recursive
definition: It is a ‘string’ whose first and last characters match AND
the remaining substring is also a palindrome. According to this
definition, the examples above would be termed palindromes if you
ignored the spaces between the words:

> anutforajaroftuna

The recursive definition can be easily coded into a computer code
segment. It needs the length of the string to be supplied along with the
input string itself. Every time the function is called, it makes sure
that the first and last characters match and then calls itself
recursively after dropping the first and last characters from the
substring.

> nutforajaroftun
>
> utforajaroftu
>
> tforajaroft

Here is the function in C++:

```
int  checkPalindrome (char string[]){
    if ( check (string, strlen (string) ))
    {
        printf("nyes, it is a palindrome\n");
    }
    else
    {
        printf("nNo, it is not a palindrome");
    }
}
```

Function check returns 1 if the remaining characters in the array str
form a palindrome.

```
       int  check ( char str[], int len){
          if ( len <= 1)
          }
             return 1 ;
          }
         else
         {
             // if first and last characters match
             // and the remaining string is a palindrome
             if ( (str[0] == str[len − 1]) &&  check(str + 1, len − 2))
               {
                  return 1;
               }
             else
             {
                return 0;
              }
          }
       }
```

Note that array arithmetic is being used here. Since the first character
of the string is located at memory location [str], the new
substring begins at memory location [str] + 1, and the length of
the new substring is 2 less than that of the current string.

#### The Greatest Common Divisor (GCD)

The GCD of two non-negative integers is the largest integer that divides
evenly into both.

For example, the numbers 2, 3, 4, 6, and 12 divide evenly into the
numbers 24 and 36. So the GCD of 24 and 36 is 12, the largest integer.
The GCD can be obtained by factorizing the numbers and picking up all
the common elements. However, for very large numbers it would involve a
large number of operations. Consider, for example, obtaining the GCD of
129618 and 576234 by factorizing.

In the 3rd century B.C.E., the great mathematician Euclid proposed an
algorithm to find GCD. It was based on the facts that GCD(p, q) = GCD(q,
p), and GCD( p, 0) = p

Euclid’s algorithm:

1.  Make p the larger of two numbers p and q.
2.  Divide p by q. Let r be the remainder. If r is zero, then q is the GCD.
3.  Else, GCD of p and q equals GCD of q and r.

Using this algorithm we can find the GCD of 1296 and 576 as follows:

> GCD(1296,576)
>
> = GCD ( 576, 1296 % 576)
>
> = GCD (576, 144)
>
> = 144 as 144 divides 576 without leaving a remainder.

Here is a full implementation of GCD in recursion using Java:

<http://www.cs.princeton.edu/introcs/23recursion/Euclid.java.html>[::]

```
/*************************************************************************  
 *  Compilation: javac Euclid.java  
 *  Execution: java Euclid p q  
 *   
 * Reads two  command-line arguments p and q and computes the greatest  
 * common  divisor of p and q using Euclid's algorithm.  
 *  
 * Remarks  
 *  -----------  
 * - may  return the negative of the gcd if p is negative  
 *  
 *************************************************************************/
public class Euclid {  
    // recursive implementation  
public static int gcd(int p, int q) {
if (q == 0)
{
return p;
} 
else
{
return gcd(q, p % q);  
}
}  

     // non-recursive  implementation  
public static int gcd2(int p, int q) {  
while (q != 0)
{  
int temp = q;  
q = p % q;  
p = temp;  
}  
return p;  
}  

public static void main(String[] args)  {  
int p = Integer.parseInt(args[0]);  
int q = Integer.parseInt(args[1]);  
int d = gcd(p, q);  
int d2 = gcd2(p, q);  
System.out.println("gcd(" + p + ", " + q + ") = " + d);  
System.out.println("gcd(" + p + ", " + q + ") = " + d2);  
}
}
```

#### More on Recursive Formulations

A recursive program may not terminate if the stopping case is not
correct or is incomplete (stack overflow: run-time error)

Make sure that each recursive step leads to a situation that is closer
to a stopping case.

You can visit the following web page to see examples of recursion with
extensive explanations:

<http://www.topcoder.com/tc?module=Static&d1=tutorials&d2=recursionPt1>

Visit this web page next to see advanced examples of recursion:

<http://www.topcoder.com/tc?module=Static&d1=tutorials&d2=recursionPt2>

### Sorting Algorithms

- describe, analyze, and compare sorting algorithms
- [Comparison Sorting Algorithms](http://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html)
- [Bucket Sort](http://www.cs.usfca.edu/~galles/visualization/BucketSort.html)
- [Counting Sort](http://www.cs.usfca.edu/~galles/visualization/CountingSort.html)
- [Radix Sort](http://www.cs.usfca.edu/~galles/visualization/RadixSort.html)
- [Heap Sort](http://www.cs.usfca.edu/~galles/visualization/HeapSort.html)

#### Bucket Sort

#### Bubble Sort

#### Selection Sort

#### Insertion Sort

#### shell sort

#### merge
TODO: Implement

#### quick
TODO: Implement

#### heap
TODO: Implement

#### counting
TODO: Implement

#### radix
TODO: Implement

### Fisher-Yates shuffle
https://blog.codinghorror.com/the-danger-of-naivete/

```java
int[] cards = {1-n}; // cards from 1 to n

for (int i = cards.Length - 1; i > 0; i--) {
    int n = rand.Next(i + 1);
    Swap(ref cards[i], ref cards[n]);
}
```

Randomly swaps the last card with itself or any card smaller.
Randomly swaps the second last card with itself or any card smaller.
Continues until the second smallest card.
