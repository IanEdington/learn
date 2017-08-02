# Mark Sheet: Tutor Marked Assignment 3

Ian Edington

2017.08.01

Your answer for each question should include about 150 of your own words.

1.  What are the advantages of using dynamic loading?
6/6

2.  Explain the basic method for implementing paging.
8/8

3.  Briefly describe the segmentation memory management scheme. How does it differ from the paging memory management scheme in terms of the user's view of memory?
8/8

    > Be careful of terminology. That should be contiguous, not continual. Terminology is very important!

4.  Explain the distinction between a demand-paging system and a paging system with swapping.
5/8

    > A paging system with swapping manipulates entire processes, whereas a demand pager is concerned with the individual pages of a process.
    > So, why would we want to swap a complete process? One reason is that there may be too many processes ready to efficiently run given the available physical memory. Thus, we might swap one or more complete processes out of memory to allow the others to run efficiently.


5.  How does the second-chance algorithm for page replacement differ from the FIFO page replacement algorithm?
8/8

6. Explain how copy-on-write operates.
8/8

7.  If you were creating an operating system to handle files, what would be the six basic file operations that you should implement?
8/8

8.  To create a new file, an application program calls on the logical file system. Describe the steps the logical file system takes to create a file.
4/8

    > The logical file system operates at a different layer of abstraction from that which you describe. To paraphrase the textbook, the logical file system allocates a new FCB. Alternatively, if the file-system implementation creates all FCBs at file-system creation time, an FCB is allocated from the set of free FCBs. The system then reads the appropriate directory into memory, updates it with the new file name and FCB, and writes it back to the disk. 

9.  How is a hash table superior to a simple linear list structure? What issue must be handled by hash table implementation?
8/8

10.  What are the factors influencing the selection of a disk-scheduling algorithm?
8/8

11.  Explain the disadvantage(s) of the SSTF scheduling algorithm.
7/8

> Additionally, SSTF often causes many reversals of head direction, each of which is slower than unidirectional movement across a disk surface.

12.  Explain the concepts of a bus and a daisy chain. Indicate how these concepts are related.
8/8

13.  What are the three reasons that buffering is performed?
6/6

Excellent!

Total:    92/100
