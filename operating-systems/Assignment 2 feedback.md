# Mark Sheet: Tutor Marked Assignment 2

Ian Edington

2017.07.24

Your answer for each question should include about 150 of your own words.

1. Define short-term and long-term scheduler and explain the main differences between them.
6/6

2. Explain the concept of a context switch.
5/6

    > So what is the “state” that is stored in the PCB?

3. Explain the terms at most once and exactly once, and indicate how these terms relate to remote procedure calls.
5/6

    > How is "at most once" implemented? (you did describe “exactly once”)

4. Identify and briefly explain each of the four major categories of benefits of multithreaded programming.
6/6

5. Briefly describe the benefits and challenges for multithreaded programming that are presented by multicore systems.
8/8

6. Define coarse-grained multithreading and fine-grained multithreading, and explain their differences.
5/6

    > Somewhat brief, as explained in previous feedback. Here, you could discuss relative efficiency, etc.

7. Explain process starvation and how aging can be used to prevent it.
6/6

8. How does the dispatcher determine the order of thread execution in Windows?
5/6

    > Again, a brief. Add details like the queue for each scheduling priority, queue traversal, etc.

9. Define critical section, and explain two general approaches for handling critical sections in operating systems.
6/8

    > Critical sections in operating systems are dealt with by preemptive or nonpreemptive kernels. Discuss these, although you “sort of” discussed the mechanics behind it.

10. Describe the dining-philosophers problem, and explain how it relates to operating systems.
6/6

11. Define the two-phase locking protocol.
5/6

    > Brief. Consider discussing “serializability” and / or some typical application.

12. Describe how an adaptive mutex functions.
6/6

13. Describe a scenario in which the use of a reader-writer lock is more appropriate than using another synchronization tool, such as a semaphore.
6/6

14. What is the difference between deadlock prevention and deadlock avoidance?
5/6

    > What sort of “restrictions”?

15. Describe a wait-for graph, and explain how it detects deadlock.
5/6

    > Yes, you can find 2 components strongly connected in linear time, but to check for any cycle in the graph requires n^2 operations. We should run this algorithm periodically.


16. Describe how a safe state ensures that deadlock will be avoided.
5/6

    > Brief.

> Excellent!

Total: 90/100
