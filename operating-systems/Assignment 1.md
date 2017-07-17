# Assignment 1
## By Ian Edington
### July 17th, 2017

This assignment should be submitted after you have finished Unit 1. It is worth 10% of your final grade.

## Part 1: Concepts and Principles
(60 marks; 5 marks each)

Instructions: Please answer the following questions in complete sentences. Your answer for each question should be about 150 words.

## 1. Define the concepts interrupt and trap, and explain the purpose of an interrupt vector.  
    An interrupt is a signal sent to the CPU when an context switch is required.
    When an interrupt is fired it first halts and saves a pointer to the next instruction in a know place.
    Using the interrupt vector the correct interrupt handler is found and executed.
    Once the interrupt handler completes the processor continues executing the next instruction (it might have been changed by the interrupt handler).
    The purpose of interrupt vector is to store an indexed list of interrupt handlers in order to find the instructions needed to process each type of interrupt.
    A trap is a special type of software interrupt that is caused by an execution error in the CPU such as a divide by zero error.
## 2. How does a computer system with von Neumann architecture execute an instruction?
    Load the instruction from memory.
    decode the instruction
    execute the instruction
## 3. What role do device controllers and device drivers play in a computer system?
    They provide a layer of abstraction for the OS. The OS implements a common way to request information from a driver and the driver has intimate knowledge of the device so is able to translate the request from the OS to the IO device hardware. This makes it possible for an OS to use many special case devices with a much more simple interface and allows device manufacturer to add support for their device without requiring permission from the maker of the OS.
## 4. Why do clustered systems provide what is considered high-availability service?
    Clustered systems provide HA service in order to continue to serve users despite faults.
    A high-availability service is one that continues to be available for use despite multiple failures. In a clustered system this is accomplished by redundancy in order to eliminate single points of failure. For the most robust HA systems advanced algorithms are used in order to synchronize data and services across many regionally separated clustered in order to provide redundancy in case of extreme outages.
## 5. Describe an operating system’s two modes of operation.
    A bit, set in the CPU, determines if the CPU is running as the kernel or as a user.
    Whenever the CPU receives an interrupt, the mode bit is set to kernel mode.
    User mode: Only allows a limited instruction set to be run.
    Kernel mode: allows privileged instructions to be executed.
    Separating these instructions is the basis of much of the security in modern CPU's since it forces programs in user mode to request access to the underlying hardware from the Operating System. This gives the OS a chance to mitigate problematic or malicious code.
## 6. Define cache, and explain cache coherency.
    Cache is the process of moving data from a larger slower form of memory into a smaller faster form of memory in order to increase the efficiency of accessing that piece of memory. Cache coherency is the processes of making sure that modifications to data that has been cached is available for other processes or systems using that data. This is accomplished by writing the data back to a commonly shared cache, sending changes to a parallel cache, or back to the origin of the data.
## 7. Describe why direct memory access (DMA) is considered an efficient mechanism for performing I/O.
    In a regular I/O process the CPU manages the process of transfering data from the device.
    Using DMA the IO device has a separate path to main memory. This enables the CPU to instruct the IO device on where and how much data to move to main memory. Once the IO device has copied the data into memory it sends an interrupt to the CPU informing it that it was successful. This greatly reduces the load on the CPU when large chunks of data need to be copied.
## 8. Describe why multicore processing is more efficient than placing each processor on its own chip.
    Basically communication between the processors on a single chip is faster than for processors on separate chips.
    Inter-processor communication has less distance to travel.
    In multi-core processors a single shared cache decreases writing to main memory while maintaining cache coherency.
## 9. Describe the relationship between an API, the system-call interface, and the operating system.
    In modern CPU's only the OS has permission to execute certain instructions in order to maintain control of the system. System-calls are an operating systems way of safely exposing these instructions to a user-space program.
    The API is a tool used in a programming language to interface with an OS's system-calls. It isn't necessarily maintained by the OS and is more likely maintained by the language compiler or interpreter. It creates a common interface for many different systems often based on a standard, such as POSIX.
## 10. Describe some requirements and goals to consider when designing an operating system.
    - Systems:
        - batch
        - time sharing
        - single user
        - multiuser
        - distributed
        - real time
        - general purpose
    - Goals:
        - user goals
            - convenient to use, easy to learn and to use, reliable, safe, and fast
            - easy to design, implement, and maintain; and it should be flexible, reliable, error free, and efficient
        - system goals
    - Requirements:
        - maximum run time (real-time systems)
        - best possible single-user experience
## 11. Explain why a modular kernel may be the best of the current operating system design techniques.
    The modular kernel strikes a balance between kernel efficiency, extensibility, and programmers cognitive load. By dividing a system into 
    This results in a system that has a huge amount of flexible pieces but only loads them when they are needed.
    The core kernel isn't as big because lots of pieces are off loaded to kernel moduals
    You don't need to recompile the entire system in order to update one module
    Moduals are kernel space programs so they don't suffer from as much of the added runtime paths of layers and micro-kernels. This increase in security checking and pathways through the kernel do still exist compared to a monolithic kernel, just not to the same extent.
    Moduals are distinct programs with their own area of control so they don't suffer from they massive complexity of monolithic kernels.
## 12. Distinguish between virtualization and simulation.
    Simulation: the hardware instructions and architecture are simulated by a software runtime environment.
    Virtualization: the instructions are run directly on the hardware, however, without knowing it the virtualized system is running inside another system.

## Part 2: Design Considerations
(40 marks)

Instructions: Please answer the following questions in about 1-2 pages each.

## 1. Draw a typical computer organization figure that includes the main components of Von Neumann architecture. Identify each component, and explain its function and interaction relative to other components. (15 marks)
    CPU: Retrieve instructions from memory and execute them
        Control Unit: ensures other elements are executing correctly and at the correct time.
        Arithmetic/Logical Unit: performs operations provided by Control Unit on registers.
    BUS: Connect the main memory and IO device to the CPU
    Main memory: hold program instructions, the stack and application data
    IO device controller: access external devices and return data to the CPU, as requested
## 2. Define system call, and list the main types of system calls. Elaborate on how a system call interacts with a standard C library and hardware under a dual-mode operating system environment. (10 marks)
    What are the advantages and disadvantages of using the same system-call interface for manipulating both files and devices?
        advantage: simple to think about them the same way. easy to implement new driver. disadvantage: special functions of devices may not be available through system calls.
    2. define system calls and types of system calls, and explain how system calls work in an operating system.
    - operating-system functions that ensure the efficient operation of the system itself
        - resource allocation
            - So many resources to manage (CPU, memory, cache, IO)
        - accounting
            - keeping records of who uses what
        - protection and security
            - keep things from touching when there not supposed to (memory, processes)
            - only as strong as the weakest link.
    - system calls
        - a way for a user program to ask the OS to do a protected thing on it's behalf
        - System calls are a way for the OS to expose privileged instructions to a user program.
    - system-call interface
        - usually in OS's there is an array table containing system calls and the index of that table calls that syscall.
    - types of system calls
        - Process control
          control of running program (start, wait, end, end with error (+level?))
            - end, abort
            - load, execute
            - create process, terminate process
            - get process attributes, set process attributes
            - wait for time
            - wait event, signal event
            - allocate and free memory
        - File management:
          often mixed with device manipulation (linux unix) or faked (microsoft).
            - create file, delete file
            - open, close
            - read, write, reposition
            - get file attributes, set file attributes
        - Device management:
            - request device, release device
            - read, write, reposition
            - get device attributes, set device attributes
            - logically attach or detach devices
        - Information maintenance:
            pass info between kernel and user program. Useful for debugging, error reporting, system profiling, ect
            - get time or date, set time or date
            - get system data, set system data
            - get process, file, or device attributes
            - set process, file, or device attributes
        - Communications:
            between processes and between systems
            - create, delete communication connection
            - send, receive messages
            - transfer status information
            - attach or detach remote devices
        - Protection:
            Control which users have access to what resources.
            - set permission
            - get permission
            - allow user
            - deny user
        - locking: provides a way for processes to control certain resources for a specified amount of time (memory, devices, files)
    3. What are *system calls*, and how does a system call work in a dual-mode context?
        > system calls for an interface from a user program to the kernel. system calls generally execute a CPU's protected instruction on behalf of a user program while making sure that program isn't abusing it's power.
    4. How do you see the relationship between Linux system calls and a standard C Library?
        > the standard C library is an API to the system calls. Any calls to the standard C library are generally translated to that OS's system calls.
    - 2.16: What are the advantages and disadvantages of using the same system-call interface for manipulating both files and devices?
        > advantage: simple to think about them the same way. easy to implement new driver. disadvantage: special functions of devices may not be available through system calls.
    - 2.1: What is the purpose of system calls?
        > interface between OS and user space.
    - [CPU switching between processes due to system calls or interrupts](http://cs.uttyler.edu/Faculty/Rainwater/COSC3355/Animations/switch.htm)
## 3. Describe the overall structure of virtual machines, and compare VMware and JVM. (15 marks)
    No idea. Will wait to learn about this in section 5.
