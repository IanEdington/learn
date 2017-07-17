# Assignment 2
## By Ian Edington
### July 17th, 2017

This assignment should be submitted after you have completed Unit 2. It is worth 10% of your final grade for this course.

Instructions: Please answer the following questions in complete sentences. Your answer for each question should be about 150 words. (100 marks total)

## 1. Define short-term scheduler and long-term scheduler, and explain the main differences between them. (6 marks)
    - short-term decides which of the ready processes to execute.
    - long-term decides which job to start next.
    From internet:
    - Short-term (CPU scheduler)-selects from jobs in memory those jobs that are ready to execute and allocates the CPU to them.
    - Medium-term- used especially with time-sharing systems as an intermediate scheduling level. A swapping scheme is implemented to remove partially run programs from memory and reinstate them later to continue where they left off.
    - Long-term (job scheduler)-verifies which jobs are brought into memory for processing.

## 2. Explain the concept of a context switch. (6 marks)
    When switching from one process to another a processor needs to save the state of the currently running process in order to be able to pick up where it left off the next time it runs the process. The context switch expresses a process where one process is halted, all state associated with it is saved in it's Process Control Block, the new process to be run has it's state loaded from it's PCB, and the new process starts executing in the CPU. All the times spent in context switching is overhead since the CPU does no useful work while switching.

## 3. Explain the terms at most once and exactly once, and indicate how these terms relate to remote procedure calls. (6 marks)
    When and RPC happens "at most once" it means that it is guaranteed that the procedure does not happen more than once, however, it does not guarantee that the procedure will happen less than once.
    "Once and exactly once" guarantees that the process will happen once, and only once. This is usually accomplished by having the client process attach an identifier to the call and the server keep track of the RPC's it's performed. This way if the client doesn't receive the ACK, it can send the call again and the server will return the ACK without performing the procedure.
    - 3.6: Consider the "exactly once" semantic with respect to the RPC mechanism. Does the algorithm for implementing this semantic execute correctly even if the ACK message sent back to the client is lost due to a network problem? Describe the sequence of messages, and discuss whether “exactly once” is still preserved.
        > yes.
        > - On the client machine the call is sent and the process waits.
        > - On the server the cache is checked to see if this call has been processed, the call is processed, the ACK is returned, and the call and return are cached.
        > - the ACK is lost
        > - after a given amount of time the client sends the call again, the server looks in the cache and find the call and returns the return.
    - 3.7 Assume that a distributed system is susceptible to server failure. What mechanisms would be required to guarantee the “exactly once” semantic for execution of RPCs?
        > Keep a redundant copy of the RPC cache (either on disk or a NAS.

## 4. Identify and briefly explain each of the four major categories of benefits of multithreaded programming. (6 marks)
    - Responsiveness: When a process is waiting for IO or a long calculation, it is not possible to interact with that process. By breaking a single process into multiple section, one to wait for IO, one to do a big calculation, and a third one to manage them and listen to input the entire system can be more responsive.
    - Resource sharing: a process can only share information with other processes through shared memory and message passing. Since threads are all part of the same process, the code, data and files are shared between all the threads in the process automatically.
    - Economy (efficiency): Because of the shared code, data and files, both making a new thread and context switching between threads is much more efficient than the equivalent with processes.
    - Scalability: by having a single process with multiple threads, that process can run across as many core as a computer has, vs a process with a single thread can only run on a single core.

## 5. Briefly describe the benefits and challenges for multithreaded programming that are presented by multicore systems. (8 marks)
    Benefits: 
    - speedup processing time
    Challenges:
    - cache coherency

## 6. Define coarse-grained multithreading and fine-grained multithreading, and explain their differences. (6 marks)
    from wikipedia: 
    - Coarse-grained multithreading. The simplest type of multithreading occurs when one thread runs until it is blocked by an event that normally would create a long-latency stall. Such a stall might be a cache miss that has to access off-chip memory, which might take hundreds of CPU cycles for the data to return.
    - Interleaved multithreading: Interleaved issue of multiple instructions from different threads, also referred to as temporal multithreading. It can be further divided into fine-grained multithreading or coarse-grained multithreading depending on the frequency of interleaved issues. Fine-grained multithreading—such as in a barrel processor—issues instructions for different threads after every cycle, while coarse-grained multithreading only switches to issue instructions from another thread when the current executing thread causes some long latency events (like page fault etc.). Coarse-grain multithreading is more common for less context switch between threads. For example, Intel's Montecito processor uses coarse-grained multithreading, while Sun's UltraSPARC T1 uses fine-grained multithreading. For those processors that have only one pipeline per core, interleaved multithreading is the only possible way, because it can issue at most one instruction per cycle.

## 7. Explain process starvation and how aging can be used to prevent it. (6 marks)
    Process starvation is when a process doesn't receive the resources it requires to make progress. If it continues to starve it might never execute. This can occur with any type of priority scheduling algorithms. Aging is a process where processes that have spent a certain amount of time waiting get bumped up a priority level. Any type of aging eliminates starvation since processes will eventually become a high priority task.
## 8. How does the dispatcher determine the order of thread execution in Windows? (6 marks)
## 9. Define critical section, and explain two general approaches for handling critical sections in operating systems. (8 marks)
    A critical section is a area of code where an executing process/thread modifies a shared data structure. Critical sections only exist in systems that run concurrently since only in concurrent systems can two processes be modifying a data structure at the same time. There are two main ways of dealing with critical section, either move the processor into a single threaded mode and disable interrupts so the section is guaranteed not to be messed with, or set a lock in order to force only one thread to use the area at a time. 
## 10. Describe the dining-philosophers problem, and explain how it relates to operating systems. (6 marks)
## 11. Define the two-phase locking protocol. (6 marks)
## 12. Describe how an adaptive mutex functions. (6 marks)
## 13. Describe a scenario in which the use of a reader-writer lock is more appropriate than using another synchronization tool, such as a semaphore. (6 marks)
    - a database is read very often and written not so often. This is a perfect candidate.
## 14. What is the difference between deadlock prevention and deadlock avoidance? (6 marks)
## 15. Describe a wait-for graph, and explain how it detects deadlock. (6 marks)
## 16. Describe how a safe state ensures that deadlock will be avoided. (6 marks)
