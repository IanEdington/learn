# Data Structures and Algorithms
## Preface
Problem - specification of generalized input and output
- allowed inputs
- output requirements
    - must be specific - best vs shortest in km
    - cannot have conflicting goals

Problem Instance - a particular instance of the problem (Mary, Lou, John)
Algorithm - procedure for solving problem
Heuristic - procedure that does a good job but is somewhat incorrect.

### Proof

Some problems have no efficient solutions.
Solutions are hard to prove incorrect, and become misleading.
Being able to reason about correctness is important.
The heart of any algorithm is an idea.
If your idea is not clearly revealed when you express an algorithm, then you are using too low-level a notation to describe it.

#### Prove Incorrectness

Counter-example: an instance of a problem that foils a solution

- Verifiability - able to calculate answer and show a better answer can be found
- Simplicity - make it as simple as possible, boil away all unnecessary parts

How?

- Think small - most alg fail fast, small examples are easier to reason about
- Exhaustively - try every small case
- Weakness - if an algorithm uses a certain heuristic, think about what might break it
- Go for a tie - sometimes a heuristic doesn't work well when there's a tie.
- Extremes - often will break with enough pressure

#### Induction is Recursion
Solve the base case, and if not break the problem up smaller until you reach the base case.
Induction is almost always the right way to prove CS theorems.

1. Base case
1. Assume that it works correctly for y = n − 1
1. Inductive case (n + 1)

Tips
- Create other variables if needed
- Make a stronger assumption if needed (works for y ≤ n - 1)

Typical errors
- boundary errors - what happens to edge cases?
- inconsistent extension - induction only works when the assumption is true.
    Convincing false claims can exist when extension produces inconsistent results.

#### Summations


### Techniques for developing algorithms
An important and honorable technique in algorithm design is to narrow the set of allowable instances until there is a correct and efficient algorithm.
For example, we can restrict a graph problem from general graphs down to trees, or a geometric problem from two dimensions down to one.

## Analysis of Data Structures and Algorithms
- mathematical concepts - required to understand data structures and algorithms
- What to measure:
    - correctness
    - time complexity
    - space complexity
- model of computation - how to estimate time and space complexity (ROM)
- Special Cases: recursion, amortization, divide and conquer, prune and search, brute force, greedy, dynamic

TODO:
- constraint relaxation

### Mathematical Background

Exponentials

Logarithms

Factorials
- Stirling's Approximation: https://en.wikipedia.org/wiki/Stirling%27s_approximation

Binomial Coefficients

$$
{n \choose k} = \frac{n!}{k!(n-k)!}
$$

Sets and Set Membership

* \(x \in A\): x is an element of A
* \(B \subset A\): B is a subset of A

#### Asymptotic Notation
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

Example of how to calculate constants & lower value: IntoAlg(pg 46)

$$
c_{1}n^2 \leq \frac{1}{2}n^2 - 3n \leq c_{2}n^2
$$

For all \(n \geq n_0\). Dividing by n^2 yields

$$
c_{1} \leq \frac{1}{2} - \frac{3}{n} \leq c_{2}
$$

### Algorithm Analysis

How to analyse an algorithm: Count up all the steps it takes for different inputs.

#### What to Measure
Correctness:  
Accuracy of the algorithm's result.  
This is generally the highest concern of an algorithm since dependably calculating results is usually the most valuable feature of an algorithm. However, a less accurate algorithm may be useful for complicated problems where a accurate solution is too time consuming.

Time Complexity:  
The running time of an algorithm.  
Next to accuracy, time complexity is the next most optimized property. Algorithms are most often compared based on this property since space is generally inexpensive, and correctness is usually assumed.

- Worst-case running times:
    The slowest possible time an algorithm can take, e.g. bubble sorting a list that is in reverse sorted order.

- Amortized running times:
    Worst case running time of a sequence of n actions.

O(m) represents that if m operations are completed the total running time will not exceed O(m) even though a specific operation may be a larger order function.
A good example of this is the resize operation within a dequeue, or list operation. Even though the resize operation is expensive it is performed in proportion to the number of other operations in the sequence.

- Expected running times:
    A type of probabilistic analysis where a random dataset is used to determine an average running time based on randomized dataset.

Space Complexity:  
The amount of memory needed for an algorithm.  
Except in specific cases space is not a large factor in the usefulness of an algorithm, since memory is relatively inexpensive compared to computing power and correctness.

#### How to Measure

The RAM (Random Access Machine) Model of Computation
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

#### Recursion
TODO: Hakan Haberdar, “How to Compute Time Complexity of Recursive Algorithms”, Computer Science Tutorials [online\], (Accessed 10-18-2016) Available from: <http://www.haberdar.org/time-complexity-recursive-algorithms-tutorial.htm>

- [Recursive Factorial](http://www.cs.usfca.edu/~galles/visualization/RecFact.html)
- [Recursive Reverse](http://www.cs.usfca.edu/~galles/visualization/RecReverse.html)
- [Recursive N-Queens](http://www.cs.usfca.edu/~galles/visualization/RecQueens.html)

#### Amortization

#### Divide-and-conquer

#### Prune-and-search (aka decrease-and-conquer)

#### Brute force

#### The greedy method

#### Dynamic programming

## Abstract Data Type (ADT)

Abstract data types is the interface.
List, dictionary, stacks, queues, objects, all have their own way of thinking about data but none of them tell us how the data is stored or what algorithms are used to process the data.

#### Queue Interface
Item's added and removed from a data structure in order.
- FIFO aka Queue (First in, First out)
    interface: `add queue addFirst | remove dequeue removeLast`
- LIFO aka Stack (Last in, First out)
    interface: `push addFirst | pop removeFirst`
- Dequeue (Double Ended Queue)
    super set of FIFO and LIFO
    interface: `addFirst | addLast | removeFirst | removeLast`  
- Priority Queue
    This queue has some kind of prioritization that occurs during the add method  
    interface: `insert_with_priority | pop_next_priority_element deleteMin`

#### List
- List or Sequence Interface
    ![list dequeue and queue](img/list-dequeue-queue.png "list dequeue and queue")

Superset of Dequeue plus:

x_1,x_2,...,x_(n-1)
 - `size()`: returns length of list
 - `get(i)`: returns x_i
 - `set(i, x)`: sets x_i to x
 - `insert(i, x)`: add x at position i, moving x_i,...,x_(n−1) => x_(i+1),...,x_(n−1+1)
 - `remove(i)`: remove and return the value x_i, moving x_(i+1),...,x_(n−1) => x_i,...,x_(n−1-1)

#### Set

- Unordered Set (Uset or Mathematical Set)
This is the basis of dictionaries or named arrays in PHP.
Each item can be stored as a pair of items.
    - `size()`: return the number of elements in the set
    - `insert(x)`: add the element x to the set if not already present. Return true if x was added to the set and false otherwise.
    - `search(x)`: find x in the set if it exists. Return x or null if no such element exists.
    - `delete(x)`: remove x from the set. Return x or null if no such element exists.

- Ordered Set (SSet)
    Only add and find are different.
    - `insert(x)`: add element in sorted order
    - `search(x)`: Find smallest element y, such that y ≥ x. Return y or null if no such element exists.

#### Graph

## Data Structures
Introduction
- data structures
- algorithms
- need for efficiency
- difference between interface and implementation

### Array and Link based Lists

- List interfaces
- Queue interfaces
- singly-linked lists
- doubly-linked lists
- space-efficient linked lists
- skip-lists

#### Array-Based: List
TODO: Implement

Fast Stack Operations Using an Array
FILO stack that is implemented using an array.

Add in the middle of an array:
    1. Check if array is long enough
        1. Resize if not big enough
    1. Move items over (for loop)
    1. Assign element

Remove for middle of array:
    1. Move items left starting at item right of the item to be removed (for loop)
    1. Check if array is too long
        1. Resize

2.2 Fast Array Stack: An Optimized Array Stack: 
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

Fast Dequeue Operations Using an Array
By treating the Dequeue as an "unlimited length" array we can use the same wrapping technique to optimize the shifting by only every making the shortest shift.
This is done by shifting on the left when the item to be shifted is on the left side and shifting on the right when the item is on the right side of centre.
This optimizes for the smallest number of elements to be shifted.

#### Rootish Array Stack: A Space-Efficient Stack

The benefit of this structure is reduced size.

An array of array's n deep. Each sub-array has b elements where b is the block number.

  | 123456
--|-------
0 | x
1 | xx
2 | xxx

Because of the complicated structure finding any given item is more complicated since each index needs to be translated into a block and item index.

The block and the item both require equations to find.

#### Linked Lists: List

##### Singly-Linked List

##### Doubly-Linked List

##### Space-Efficient Linked List
TODO: Implement

#### Skip list: List
Time Complexity: O(log(n)) With High Probability (WHP).
Space Complexity: O(log(n))?


### Hash Tables
ADT: Unordered Set, fast search of an ordered list

#### Hash Codes

#### Hash Functions
implement, explain, estimate the effectiveness, differentiate
- Division Hashing (k mod m where m is prime)

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

#### Collision Resolution Algorithms
implement, analyze, explain, estimate the effectiveness, differentiate
- open addressing (probing)
    - linear probing: if you don't find it add more
    - quadratic probing
    - double hashing
- separate chaining
    - normal
    - with list heads
    - with other data structures
- coalesced hashing
- robin hood hashing
- cuckoo hashing
- hopscotch hashing
- dynamic resizing
    - resizing the whole
    - incremental resizing

### Recursion
a method that calls itself
- inspect recursive programs
- create different types of recursive programs
- differentiate recursive solutions from iterative solutions
- analyse the time complexity of recursive programs

### Binary Trees
It is important to understand and demonstrate the differences between AVL trees, red–black trees, and (2,4) trees in terms of the key properties of these trees; the process of adding or removing nodes in the trees while maintaining these key properties with appropriate operations; and running time or cost to maintain the properties.

AVL trees are often compared to red–black trees because they support the same set of operations and because red−black trees also take O(log n) time for the basic operations. AVL trees perform better than red–black trees for lookup-intensive applications. AVL trees, red–black trees, and (2,4) trees share a number of good properties, but AVL trees and (2,4) trees require extra operation to deal with restructuring (rotations), fusing, or splitting. However, red–black trees do not have these drawbacks.

Binary tree

Binary search tree
- examine a binary tree and binary search tree
- implement a binary tree and binary search tree
- [Binary Search Tree](http://www.cs.usfca.edu/~galles/visualization/BST.html)

AVL Tree
- self-balancing binary search tree
- height-balanced: at any node in the tree the height of it's two child subtrees differ by at most 1
- rebalances using rotations on insertion and deletion
- requires an additional piece of information keep in each node (height)
- Lookup, insertion, and deletion all take O(log n) time in both the average and worst cases
- http://en.wikipedia.org/wiki/AVL_tree
- http://www.cs.ucf.edu/~dmarino/ucf/cop3502/lec_biswas/trees5.pdf
- [AVL Tree (balanced binary search trees)](http://www.cs.usfca.edu/~galles/visualization/AVLtree.html)

2, 4 Tree

Scapegoat Trees
- define scapegoat tree
    * tree that preforms partial rebuilding
    * when it becomes unbalanced it finds a "scape-goat" and tells it to rebalance itself
- examine a scapegoat tree
- implement a scapegoat tree

Red–Black Trees
- define red–black tree
- examine a red–black tree
- implement a red–black tree
- [Red–Black Tree](http://www.cs.usfca.edu/~galles/visualization/RedBlack.html)

### Heaps
- define heap
- examine a binary heap tree
- implement a binary heap tree
- define meldable heap
- examine a randomized meldable heap

#### Binary Heaps (Array)
- define, examine and implement a binary heap tree

- [Min Heap](http://www.cs.usfca.edu/~galles/visualization/Heap.html)
- [Binomial Queue](http://www.cs.usfca.edu/~galles/visualization/BinomialQueue.html)
- [Fibonacci Heap](http://www.cs.usfca.edu/~galles/visualization/FibonacciHeap.html)
- [Leftist Heap](http://www.cs.usfca.edu/~galles/visualization/LeftistHeap.html)
- [Skew Heap](http://www.cs.usfca.edu/~galles/visualization/SkewHeap.html)

#### Meldable Heaps
- define and examine a randomized meldable heap.

### Graphs
- represent a graph by a matrix
- represent a graph in adjacency lists
- understand the execution process of the depth-first-search and bread-first-search algorithms for traversing a graph
- analyze the performance of the depth-first-search and bread-first-search algorithms for traversing a graph
- implement those search algorithms for traversing a graph in pseudo-code or other programming languages, such as Java, C, or C++, etc.

#### Matrix Graphs
TODO: Implement

- represent a graph by a matrix
- understand, implement, and analyze the depth-first-search

#### Adjacency Graphs
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

##### Breadth-First Search
TODO: Implement

##### Depth-First Search
TODO: Implement


### Binary Trie
- define trie
- examine a binary trie
- explain binary trie

- [B Trees](http://www.cs.usfca.edu/~galles/visualization/BTree.html)
- [B+ Trees](http://www.cs.usfca.edu/~galles/visualization/BPlusTree.html)

## Algorithms

### Sorting Algorithms
- describe sorting algorithms (merge, quick, heap, counting, radix)
- estimate the complexity of sorting algorithms
- compare sorting algorithms

### Recursion

- define recursion
- inspect recursive programs
- create different types of recursive programs
- differentiate recursive solutions from iterative solutions
- estimate the time complexity of recursive programs

Recursion is a wonderful programming tool.
It provides a simple, powerful way of approaching a variety of problems.

Introduce the concept of recursion:
http://dotnetslackers.com/Community/files/folders/data-structures-and-algorithms/entry30283.aspx

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

Euclid's algorithm:

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

describe, analyze, and compare sorting algorithms

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

## Course 2

### Learning Outcomes

Most of the emphasis of the first portion of the course will be on problems that can be solved efficiently; in the latter portion we will discuss intractability and NP-hard problems.
Finally, we will discuss methods to approximate NP-hard problems and how to prove how close these approximations are to the optimal solutions.

- background
    - asymptotic analysis
    - summations
    - recurrences
    - sorting.
- divide-and-conquer approach
- designing optimization algorithms
    - dynamic programming
    - greedy algorithms.
- topic—multithreaded algorithms.
- number-theoretic algorithms

Upon successful completion of the course, you will be able to

- describe modern algorithms and design techniques
- chose suitable algorithm design technique for a given problem
- apply algorithms and design techniques to solve problems
- mathematically evaluate the quality of a solutions

### Proofs in Algorithm Design

Algorithms are mathematical objects (in contrast to the much more concrete notion of a computer program implemented in some programming language and executed on some machine).
Thus we can reason about the properties of algorithms mathematically.

When designing an algorithm there are two fundamental issues to be considered: correctness and efficiency.
It is important to justify an algorithms correctness mathematically.
For very complex algorithms, this typically requires a careful mathematical proof, which may require the proof of many lemmas and properties of the solution upon which the algorithm relies.

### Citation Practice
We recommend the APA standard for citation

### Assignment

Zip into a single file.

Doing the Assignments
Throughout out this course, when you are asked to present an algorithm, this means that you need to do three things:

1. Present a clear, simple, and unambiguous description of the algorithm (in pseudocode, for example).
The key here is keeping it simple.
Uninteresting details should be kept to a minimum, so that the key computational issues stand out.
For example, it is not necessary to declare variables whose purpose is obvious, and it is often simpler and clearer to simply say, “Add X to the end of list L” than to present code to do this or use some arcane syntax, such as `L:insertAtEnd(X)`.

2. Present a justification or proof of the algorithm's correctness.
Your justification should assume that the reader is someone of similar background to yours, say another student in this class, and should be convincing enough make a skeptic believe that your algorithm does indeed solve the problem correctly.
Avoid rambling about obvious or trivial elements.
A good proof provides an overview of what the algorithm does and then focuses on any tricky elements that may not be obvious.

3. Present a worst-case analysis of the algorithm's efficiency, typically its running time (but also its space, if space is an issue).
Sometimes this is straightforward, but if not, concentrate on the parts of the analysis that are not obvious.

### Unit 1: Foundations

This unit addresses the following topics of interest:
- overview of algorithms
- their place in modern computing systems
- examination of two different sorting algorithms (insertion sort and merge sort) to determine their running times and develop a useful notation to express them
- a definition of the notation (called asymptotic notation) that we use for bounding algorithm running times from above and/or below.

Why do we choose asymptotic notation and analysis for algorithm analysis?
This approach allows us to focus on the “big-picture” aspects of an algorithm's running time.

#### 1.1: Problems

Your goals for this section are
- to know the definition of algorithm
- the reasons for studying algorithms
- the role of algorithms relative to other technologies used in computers
- to know what kind of problems are solved by algorithms.

##### Understanding Algorithms
- give a definition of the term algorithm.
- identify practical applications of algorithms.
- explain the role of algorithms in computing science.

Chapter 1

Exercises 1.1-4 and 1.2-2
Problem 1-1 on pages 14–15
How would you go about solving this problem?

#### 1.2: Complexity and Analysis

The framework that we will use throughout the course.

#####  Using Pseudocode
specify algorithms using pseudocode conventions introduced in the textbook

Section 2.1

Exercise 2.1-3

#####  Analyzing Algorithms - analyze the running time of algorithms.

Section 2.2

Exercise 2.2-3

Start from 17:20): http://freevideolectures.com/Course/1941/Introduction-to-Algorithms/1

#####  Designing Algorithms
- explain the divide-and-conquer approach to the design of algorithms
- use it to develop a merge sort algorithm

Section 2.3

Exercise 2.3-5

#### 1.3: Asymptotic Analysis

Your goals for this section are
- to know the meaning of the asymptotic efficiency of algorithms.
- to define several types of asymptotic notation.
- to use standard methods for simplifying the asymptotic analysis of algorithms.

#####  Asymptotic Notation - define several types of asymptotic notation.

Section 3.1

Exercise 3.1-1

http://freevideolectures.com/Course/1941/Introduction-to-Algorithms/2

#####  Standard Notation and Common Functions
- review some standard mathematical functions and notations
- explore the relations among them

Section 3.2

Problem 3-1

What are the common abuses in the basic asymptotic notations? 

### Unit 2: Divide-and-Conquer Algorithms

This unit will introduce
- the divide-and-conquer method.
- Strassen's surprising method for multiplying two square matrices
- solving recurrences
- the “master method” http://freevideolectures.com/Course/1941/Introduction-to-Algorithms/3
- methods for analyzing recursive algorithms.

#### 2.1: The Maximum-subarray Problem

Describe the maximum-subarray problem.
Design and analyze its divide-and-conquer algorithm.

Section 4.1

Exercise 4.1-2

#### 2.2: Strassen's Algorithm for Matrix Multiplication

Strassen's algorithm for matrix multiplication.

#####  Strassen's Method

Describe Strassen's method for matrix multiplication.
Design and analyze its divide-and-conquer algorithm.

Section 4.2

Exercise 4.2-1

#### 2.3: Methods for Solving Recurrences

#####  The Substitution Method

Describe the substitution method for solving recurrences.

Section 4.3

Exercises 4.3-2

#####  The Recursion-tree Method

Describe the recursion-tree method for solving recurrences.

Section 4.4

Exercise 4.4-7

#####  The Master Method

Describe the master method for solving recurrences.

Section 4.5

Exercise 4.5-3

### Assignment 1

Weight: 10% of your final grade

Submit your solutions to the following exercises and problems:

Exercise 1.1-4 from the textbook (5 marks)
Exercise 1.2-2 from the textbook (5 marks)
Exercise 2.1-3 from the textbook (10 marks)
Exercise 2.2-3 from the textbook (10 marks)
Exercise 2.3-5 from the textbook (10 marks)
Exercise 3.1-1 from the textbook (5 marks)
Problem 3-1 from the textbook (10 marks)
Exercise 4.1-2 from the textbook (10 marks)
Exercise 4.2-1 from the textbook (5 marks)
Exercise 4.3-2 from the textbook (10 marks)
Exercise 4.4-7 from the textbook (10 marks)
Exercise 4.5-3 from the textbook (10 marks)

### Unit 3: Dynamic Programming and Longest Common Subsequence

Dynamic programming, like the divide-and-conquer method, solves problems by combining the solutions to sub-problems.
Why do we call it programming?
In fact, programming in this context refers to a tabular method, not to writing computer code.
The term dynamic programming was first coined by Richard Bellman in the 1950's, a time when computing programming was an esoteric activity practiced by so few people as to not even merit a name.
Back then programming meant planning, and “dynamic programming” was conceived to optimally plan multistage processes.

Why do we need dynamic programming?

Divide-and-conquer algorithms partition the problem into disjoint sub-problems, solve the sub-problems recursively, and then combine their solutions to solve the original problem.
In contrast, dynamic programming applies when the sub-problems overlap—that is, when sub-problems share sub-sub-problems.
In this context, a divide-and-conquer algorithm does more work than necessary and efficient!

The basic idea behind dynamic programming is eliminating overlapping recursive calls by using more memory to keep track of previous values.

http://freevideolectures.com/Course/1941/Introduction-to-Algorithms/15

This unit will address the following topics of interest:
- developing a dynamic-programming algorithm.
- applying dynamic programming to optimization problems.

#### 3.1: Dynamic Programming

The method of dynamic programming and how to use the dynamic programming method to solve some optimization problems.

#####  Rod Cutting

Examine the problem of cutting a rod into rods of smaller length in a way that maximizes their total value.

Section 15.1

Exercises 15.1-1 and 15.1-5

#####  Matrix-chain Multiplication

Describe another example of dynamic programming—how we can multiply a chain of matrices while performing the fewest total scalar multiplications.

Section 15.2

Exercises 15.2-1 and 15.2-2

#####  Elements of Dynamic Programming

Discuss two key characteristics that a problem must have for dynamic programming.

Section 15.3

Exercise 15.3-1
Exercise 15.3-6

#### 3.2: Longest Common Subsequence

Show how to find the longest common subsequence of two sequences via dynamic programming.

Section 15.4

Exercises 15.4-1 and 15.4-2

### Unit 4: Greedy Algorithms

Before learning this unit, you should learn dynamic programming.
Why do we study greedy algorithm?
For many optimization problems, using dynamic programming to determine the best choices is overkill.

Like dynamic-programming algorithms, greedy algorithms typically apply to optimization problems in which we make a set of choices in order to arrive at an optimal solution.

The idea of a greedy algorithm is to make each choice in a locally optimal manner.

A simple example is coin-changing: to minimize the number of Canadian coins needed to make change for a given amount e.g.
CAD$38, we can repeatedly select the largest-denomination coin that is no larger than the amount that remains.
We have 38-20=18, 18-10=8, 8-5 = 3, 3-2 =1, 1-1 =0.
So $38 is changed to $20 + $10 + $5 +$2 + $1.

A greedy algorithm approach provides an optimal solution for many such problems much more quickly than would a dynamic programming approach.
However, is this approach effective? This unit will introduce matroid theory, which provides a mathematical basis that can help us to show that a greedy algorithm yields an optimal solution.

Is the greedy method powerful?
Yes, it is quite powerful and works well for a wide range of problems.
More importantly, the greedy algorithm approach is more straightforward than the dynamic programming approach.

This unit addresses the following topics of interest:
- the basic elements of the greedy approach
- an important application of greedy techniques: designing data-compression (Huffman) codes

#### 4.1: Greedy Algorithms and their applications.

http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-introduction-to-algorithms-sma-5503-fall-2005/video-lectures/lecture-16-greedy-algorithms-minimum-spanning-trees/

#####  An Activity-selection Problem

Describe a simple but nontrivial problem for which a greedy algorithm efficiently computes an optimal solution.

Section 16.1

Exercise 16.1-2

#####  Elements of the Greedy Strategy

Discuss some of the general properties of greedy methods and tell whether a greedy algorithm will solve a particular optimization problem.

Section 16.2

Exercise 16.2-2
Exercise 16.2-3

### Assignment 2

Weight: 15% of your final grade

Submit your solutions to the following exercises and problems:

Exercise 15.1-1 from the textbook (5 marks)
Exercise 15.1-5 from the textbook (15 marks)
Exercise 15.2-1 from the textbook (5 marks)
Exercise 15.2-2 from the textbook (15 marks)
Exercise 15.3-1 from the textbook (10 marks)
Exercise 15.4-1 from the textbook (5 marks)
Exercise 15.4-2 from the textbook (15 marks)
Exercise 16.1-2 from the textbook (15 marks)
Exercise 16.2-2 from the textbook (15 marks)

### Unit 5: Multithreaded Algorithms

With the advent of multicore technology, every new laptop and desktop machine is now a shared-memory parallel computer.
However, programming a shared-memory parallel computer directly using static threads is difficult and error-prone.
This state of affairs has led to the creation of concurrency platforms, which provide a layer of software that coordinates, schedules, and manages the parallel-computing resources.

In this unit, we introduce a model for dynamic multithreading, which is a simple extension of our serial programming model.
This model allows the programmer to specify only the logic parallelism within a computation and the threads within the underlying concurrency platform schedule, which load-balance the computation themselves.
That is, it allows programmers to specify parallelisms in applications without worrying about communication protocols, load balancing, and other vagaries of static-thread programming.

And then we look at how to design multithreaded algorithms written for this model.
We will see how the underlying concurrency platform can schedule computations efficiently.
We present the metrics of work, span, and parallelism and use them to analyze multithreaded algorithms.

This unit will
- introduce the basics of the model.
- show how to quantify parallelism in terms of the measures of work and span.
- investigate a multithreaded algorithm for matrix multiplication.

#### 5.1: Dynamic Multithreading Model

Explain the dynamic multithreading model.
Use the metrics of work, span, and parallelism to analyze multithreaded algorithms.

http://freevideolectures.com/Course/1941/Introduction-to-Algorithms/20
http://youtu.be/PYvJmLKhM-Y
http://student.athabascau.ca/~oscarl/COMP372/MultithreadedAlgorithms Part 1.pptx

Section 27.1

Explain these keywords or terms relating to parallel algorithms:
- Spawn
- Sync
- Nest parallelism
- Strand
- Computation dag
- Work
- Span
- Critical path
- Parallelism
- Parallel for

Explain how a multithreaded scheduler works.

Exercises 27.1-1 and 27.1-7

What do we need parallel algorithms?
What are the key features of the model for dynamic multithreading?
What are the important advantages of dynamic multithreading?

#### 5.2: Matrices Multiplication with Multithreading

Design and analyze multithreaded algorithms based on
- the standard triply nested loop
- the divide-and-conquer algorithms

Section 27.2

Exercise 27.2-1

### Unit 6: Number-Theoretic Algorithms

#### 6.1: Concepts of Number Theory

Discuss elementary number-theoretic notions.

Section 31.1

Explain the following elementary but important concepts:
- Divisor
- Prime number
- Quotient, remainder, division theorem
- Equivalence class modulo n, the set Zn
- Common divisor, greatest common divisor
- Relatively prime, pairwise relatively prime numbers
- Unique factorization

Exercise 31.1-7

#### 6.2: Euclid's Algorithm

Explain and analyze Euclid's algorithm for computing the greatest common divisor.

Section 31.2

Exercise 31.2-3

#### 6.3: Modular Algorithms

#####  A Formal Model for Modular Arithmetic

Describe a formal model for modular arithmetic within the framework of group theory.

Section 31.3

Explain the following concepts:
- Group
- Abelian group
- Finite group

Exercise 31.3-1

#####  Modular Linear Equations

Solve modular linear equations.

Section 31.4

Exercise 31.4-1

#### 6.4: Chinese Remainder Theorem and Powers of an Element

#####  Chinese Remainder Theorem

Apply the Chinese remainder theorem.

Section 31.5

Exercise 31.5-1

#####  A Repeated-squaring Algorithm

Apply a repeated-squaring algorithm for efficiently computing ab mod n, given a, b, and n.

Section 31.6

Exercise 31.6-1

#### 6.5: RSA Public-key Cryptosystem

Explain the RSA public-key cryptosystem.

Section 31.7

View this recommended video: http://youtu.be/ejppVhOSUmA

Explain the following concepts:
- Digital signature
- RSA public key
- RSA private key

Exercises 31.7-1

### Assignment 3

Weight: 15% of your final grade

Submit your solutions to the following exercises and problems:

Exercise 27.1-1 from the textbook (10 marks)
Exercise 27.1-7 from the textbook (10 marks)
Exercise 27.2-1 from the textbook (10 marks)
Exercise 31.1-7 from the textbook (10 marks)
Exercise 31.2-3 from the textbook (10 marks)
Exercise 31.3-1 from the textbook (10 marks)
Exercise 31.4-1 from the textbook (10 marks)
Exercise 31.5-1 from the textbook (10 marks)
Exercise 31.6-1 from the textbook (10 marks)
Exercise 31.7-1 from the textbook (10 marks)

### Unit 7: NP-completeness

The Millennium Prize Problems are seven problems in mathematics presented by the Clay Mathematics Institute in 2000.
As of December 2012, six of the problems remained unsolved.
A prize of US$1,000,000 is offered by the institute for correct solutions.
The Poincaré conjecture is the only Millennium Prize Problem to be solved so far, by Grigori Perelman, who declined the award in 2010.

The seven problems are as follows:
- P versus NP problem
- Hodge conjecture
- Poincaré conjecture (solved)
- Riemann hypothesis
- Yang–Mills existence and mass gap
- Navier–Stokes existence and smoothness
- Birch and Swinnerton–Dyer conjecture

The first problem relates to our topic for Unit 8—NP-completeness.
The question is whether, for all problems for which an algorithm can verify a given solution quickly (that is, in polynomial time), an algorithm can also find that solution quickly.
The former describes the class of problems termed NP, while the latter describes P.
The question is whether or not all problems in NP are also in P.
This is generally considered one of the most important open questions in mathematics and theoretical computer science, as it has far-reaching consequences for other problems in mathematics, and in biology, philosophy, and cryptography (see P versus NP problem, proof consequences).

Most mathematicians and computer scientists expect that P ≠ NP.

#### 7.1: P ≠ NP Question

#####  Polynomial Time

- formalize the notion of problem
- define the complexity class P of polynomial-time solvable decision problems
- determine how these notions fit into the framework of formal-language theory

Pages 1048-1053 and Section 34.1
Explain the following concepts:
- abstract problem
- decision problem
- optimization problem
- encoding
- concrete problem
- polynomial-time solvable
- complexity class P
- alphabet
- language
- A language is accepted in polynomial time.
- A language is decided in polynomial time.

Exercises 34.1-1 and 34.1-4

Do you agree that the concept of a reduction is the central tool for analyzing the difficulty of a problem?
Why do we generally regard the polynomial-time solvable problems as tractable, but for philosophical, not mathematical, reasons?
Why should we use a formal-language framework to discuss solvability of decision problems?
Why do we focus on the concept of “problem” instead of “algorithm” in this unit?

##### Optimization and Decision Problems

Define the class NP of decision problems whose solutions are verifiable in polynomial time.
Formally pose the P≠ NP question.

Section 34.2
Exercises 34.2-1 and 34.2-8

#### 7.2: NP-completeness

#####  Polynomial-time Reductions and NP-completeness

Show we can relate problems via polynomial-time “reductions.”
define NP-completeness.
Sketch a proof that one problem is NPC.

Section 34.3

Explain the following concepts:
- polynomial-time reducible
- NP-complete
- NP-hard

Exercise 34.3-1

#####  NP-completeness Proofs

Show how to prove other problems to be NPC much more simply by the methodology of reductions.

Section 34.4

Exercise 34.4-1

#####  Proving Problems NP-complete

Show that a variety of problems are NP-complete.

Sections 34.5.1 and 34.5.2

Exercise 34.5-1

### Unit 8: Approximation Algorithms

This unit shows you how to find approximate solutions to NP problems efficiently by using approximation algorithms.

#### 8.1: Performance Ratios - Basic Terms

Define the basic terms relating to approximation algorithms.

Pages 1106-1107
Explain the following terms:
- approximation ratio
- ρ(n)-approximation algorithm
- approximation scheme
- polynomial-time approximation scheme
- fully polynomial-time approximation scheme

#### 8.2: The Vertex-cover Problem - An NPC Minimization Problem

Discuss the vertex-cover problem, an NP-complete minimization problem that has an approximation algorithm with an approximation ratio 2.

Section 35.1
Exercises 35.1.1 and 35.1-2

#### 8.3: The Set-covering Problem - A Greedy Heuristic

Show how to use a greedy heuristic as an effective approximation algorithm for the set-covering problem, with a logarithmic approximation ratio.

Section 35.3
Exercises 35.3.1, and 35.3-3

#### 8.4: The Subset-sum Problem - A Polynomial-time Approximation Scheme

Discuss a fully polynomial-time approximation scheme for the subset-sum problem.

Section 35.5
Exercises 35.5-2
Problem 35-1 or 35-3 or 35-7

### Assignment 4

Weight: 15% of your final grade

Submit your solutions to the following exercises and problems:

Exercise 34.1-1 from the textbook (6 marks)
Exercise 34.1-4 from the textbook (8 marks)
Exercise 34.2-1 from the textbook (6 marks)
Exercise 34.2-8 from the textbook (8 marks)
Exercise 34.3-1 from the textbook (6 marks)
Exercise 34.4-1 from the textbook (6 marks)
Exercise 34.5-1 from the textbook (8 marks)
Exercise 35.1.1 from the textbook (8 marks)
Exercise 35.1-2 from the textbook (8 marks)
Exercise 35.3.1 from the textbook (8 marks)
Exercise 35.3-3 from the textbook (8 marks)
Exercise 35.5-2 from the textbook (8 marks)
Problem 35-3 from the textbook (12 marks)

### Assignment 5

Weight: 15% of your final grade

Project:
You should submit the project before writing the final exam.
This assignment is designed to bring together what you have covered in the course into a significant working project.

#### Select and complete one of the following projects, and submit it for evaluation and feedback.

1. Implement the Vertex Cover problem; that is, given graph G and integer k, answer the question of whether or not there is a vertex cover of size k or less.
Begin by using a brute-force algorithm to check all possible sets of vertices of size k to find an acceptable vertex cover, and measure the running time on a number of input graphs.
Then try to reduce the running time using any heuristics you can think of.
Next, try to find approximate solutions to the problem in the sense of finding the smallest set of vertices that forms a vertex cover and analyzing its running time.
2. Do the Problem 35-1 from the textbook – Bin packing.
You can implement the solution in Java, C/C++, or Python although Java is preferred.
Do not use any downloaded code or any API/template.

#### What to Hand In

This applies to both problems.
Hand in one file written in English and named ‘idnumber-name-p1.zip’, where you provide your student ID number and name.

All the following files must be included:
- The commented source code and the executable file.
- Experimental report as PDF.

The report should include the following: 
1. A description of your software and hardware environment for developing the project.
1. The design of the algorithm.
1. Testing input data and the results and complexity analysis. You should include some screen shots showing the running scenarios and the running results.
1. A user manual explaining how to run your project. 
1. Discussions and reflection on knowledge gained.
1. References.

Grading Criteria
- Proving when needed, coding, and its correctness and/or efficiency 40 marks
- The design of the algorithm 20 marks
- The test data, results, and analysis 15 marks
- User manual 15 marks
- Overall impression 10 marks 

### Participation
Weight: 5% of your final grade

Post to the COMP 372 on a regular basis:
- Answer the questions from the study guide
- comment on answers
- post questions regarding the learning material
- respond to questions from other students

At the end of the course, you will submit a summary of your participation activities to the Participation link under Assessments on the course home page.
Before you write the examination, copy all discussion postings that demonstrate your participation activities into a document that you will upload here.
Include an introductory paragraph (or more) where you reflect on what you gained and what you were able to impart to others in the class through this activity.

### Final Examination

Weight: 25% of your final grade

You are allowed to use the textbook and published articles, but NOT allowed to use solution manuals, personal notes, or to consult with other people while writing this examination.

If you have kept up with the course work and taken time to review feedback from your tutor on the marked assignments, with a little review of the main points, you should be ready to write the final examination.

The final exam consists of five parts:
- Part I: True/False questions (15 questions, 30%)
- Part II: Short-answer questions (5 questions, 20%)
- Part III: Multiple-choice questions (10 questions, 30%)
- Part IV: Algorithm writing and analysis (2 questions, 10%)
- Part V: Proving (2 questions, 10%)
