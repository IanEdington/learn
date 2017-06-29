# Computer Science 314: Operating Systems (Revision 5)

## Course Learning Outcomes
- computer-system structures
- operating-system structures
- process management:
    - defining a process
    - CPU scheduling
    - process synchronization
    - deadlocks
    - interprocess communication
- storage management:
    - memory management
    - virtual memory
    - file-system management
    - disk management
    - I/O (input/output) systems;
- protection and security issues:
    - access matrix and its implementations
    - authentication
    - viruses and other intruders
    - encryption
- distributed and special-purpose operating systems:
    - distributed operating systems
    - real-time systems
    - embedded systems
    - multimedia systems

- describe the overall structure and components of operating systems
- explain the key concepts and mechanisms of:
    - process management
    - memory management
    - storage management
    - security and protection
- apply the appropriate principles and methods to practical tasks:
    - analysis, diagnosis, and development of functions and components that are associated with modern operating systems.
-   describe the goals and tasks of an operating system and the techniques used to handle these tasks.
-   explain key terms and principles of process management
    - kernel
    - process
    - thread
    - scheduling
    - synchronization
    - deadlock handling
    - recovery
-   explain how an operating system manages processes and threads (system queues, scheduling algorithms).
-   outline the different strategies (such as virtual memory) used by operating systems to manage memory.
-   explain the benefits, limitations, resource overhead (such as fragmentation and data structures), and hardware requirements of each memory-management technique.
-   list and describe several strategies used by systems software to manage disks and other devices.
-   explain the nature of protection for and security problems of operating systems.
-   identify and explain the protection features built into operating systems and their supporting hardware to enhance security.
-   describe the concepts, structures, and functions of real-time, embedded, mobile, multimedia, or distributed operating systems.
-   discuss, briefly, how various aspects of the theory of operating systems are implemented in practice in systems such as DOS, Windows, UNIX, Solaris 2, and Mach.
-   apply the concepts and principles of operating systems in investigating, exploring, and implementing system components or the interfaces of modern operating systems such as Linux, Windows, and Solaris.

## Goals of Operating Systems

As you work through this course it is important to keep in mind the following goals of operating systems:

-   enable efficient use of computer hardware.
-   provide a reliable environment in which to run programs.
-   handle errors reasonably and with sufficient feedback.
-   provide services (tools, languages) for users.
-   hide the details of hardware and resource management from users.
-   protect users from one another, and protect the operating system
    from users.

At times, these goals may conflict with one another; for example, it is quite common for a designer to trade efficiency for improved security or reduced cost.

## Course Materials
OSC9ed - Operating system concepts (9th ed.)

OS6ed - Operating systems: Internals and design principles (6th ed.)

- Bovet, D. P., & Cesati, M. (2006). *Understanding the Linux kernel* (3rd ed.). Sebastopol, CA: O’Reilly Media.
- Mauerer, W. (2008). *Professional Linux kernel architecture*. Indianapolis, IA: Wiley Publishing.

The following journals from ACM and IEEE may be most relevant for this course.

-   Conference Proceedings of the ACM Symposium on Operating Systems Principles
-   Journals and Magazines
    -   Operating Systems Review
    -   ACM Transactions on Computer Systems
    -   IEEE Transactions on Computers
    -   ACM Computing Surveys
    -   Communications of the ACM
    -   IEEE Computers
    -   Linux Journal

## Activities

1.  Access [the AU Library online](http://library.athabascau.ca/) and locate the databases (Databases) and the journal index (E-Journals).
2.  Locate the following databases:
    -   ACM Digital Library
    -   IEEE/IEE Electronic Library
    -   Science Direct
6.  Browse relevant online resources for this course:
    -   Textbook website
    -   Textbook Student Companion Site
    -   Textbook Solutions to Practice Exercises
    -   [Supplementary textbook website](http://williamstallings.com/OS/OS6e.html)
    -   [MIT OpenCourseWare’s 6.828 Operating System Engineering course](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-828-operating-system-engineering-fall-2006/index.htm)

## Unit 1: Overview of Computer Organization and Operating Systems
### Learning Objectives
- describe the overall structures and major components in computer organization and computer architecture
- list some of the advances in hardware and software that have enabled contemporary operating systems technology
- identify and describe the goals and tasks of operating systems
- identify and describe the techniques used to handle the tasks of operating systems

### 1.1 Computer Hardware: Organization, Architecture, and Operating Systems
#### Learning Outcomes

1.  describe the overall structure of computer-system organization.
    - CPU and its main components:
        - arithmetic-logic unit
        - control unit
        - data registers
        - addresses and control information
        - clock
        - control bus
        - and data bus
    -   interrupt and system call
    -   instruction-execution cycle
    -   instruction register
    -   multiprocessor
    -   cache
2.  identify major computer hardware components.
3.  explain how instructions are executed in a computer.
4.  explain how the I/O devices are managed.

#### Reading Assignment

-   Silberschatz, A., Galvin, P. B., & Gagne, G. *Operating system concepts* (9th ed.): Chapter 1: Introduction: 1.1 to 1.3.

#### 1.1
What is an operating system?
    The one program that is always running. Also called the kernel.
    The next layer up is system programs that aren't necesarily the kernal but are clossly related.
    The third layer is user programs.
    OS often has middle wear and other tools bundled with it.
What is it's role:
    The OS 

- central processing unit (CPU)
    - a large set of transistors that perform the instruction-execution cycle
- memory and RAM (and DRAM)
    - DRAM: dynamic RAM because it is volitile
    - SRAM: static RAM because it's not volitile
        - used for cache
- firmware and ROM (or EEPROM)
    - ROM: read only memory
    - EEPROM: Electronically Erasable Programable ROM
    - used to hold bootstrap program
- input/output (I/O) devices
    - extendable data transfer and storage space
    - cpu sends I/O request
    - data is sent or received
    - interupt is returned
- instruction-execution cycle
    - the next instruction is retrieved from memory
    - the instruction is decoded
    - the instruction is executed
- instruction register
    - the register that holds the instruction to be executed
- storage device hierarchy
    - fast and expensive - slow and cheep
    - Anything that doesn't reside along this line ends up dying like core memory and paper tapes
- small computer-systems interface (SCSI)
    - IO controller
- simple IO:
    - OS start/requests driver, driver sets registers in controller, returns cpu flow.
    - controller performs action based on registers, stores data in buffer, sends interupt.
    - CPU gets data from buffer
- direct memory access (DMA)
    - OS alocates memory & start/requests driver, driver sets registers in controller, returns cpu flow.
    - controller performs action based on registers, transfers large amount of data to memory, then sends interupt.
    - CPU accesses data in main memory
- device driver
    - provides OS with a uniform interface for the IO device
- multiprocessor system (parallel systems)
    - 
- symmetric multi-processing (SMP)
    - all processors are eqaul
- uniform memory access (UMA)
    - Every processesor can access any memory in constant time
- non-uniform memory access (NUMA)
    - Performance penalty for a certain processors accessing specific memory
    - Possible to access more memory
    - mitigating these penalties is possible with well designed algorithms that don't encourage memory crossover.
- multiple computing cores
    - a single chip with multiple cores is often what happens with current architecture.
TODO: what's the diff between Blade Servers and Clustered Systems?
    - loosely coupled vs tightly coupled?
- blade server
    - multiple OS's working in unison together.
    - usually hot swappable
- clustered system
    - a cluster is a set of systems that interact together
    - share memory, tightly networked over LAN with 1gig or greater connection
    - Asymetric vs Symetric like with processors
        - Standby server vs parallelism
        - breaking things into separate systems
    - Generally a SAN will connect the individual parts
- Beowulf clusters
    - clusters using opensource products and cheap computers
- storage-area networks (SANs)
    - Storage on a network that manages access for multiple systems.
    - generally solving problems to do with concurrent reads and writes

#### Study Questions

1. Why are operating systems important for computer systems?
    - Provide optimizations in software that are not possible in hardware.
    - Orchestration of Hardware
    - Platform for software
    - Optimization of software for a particular architecture
    - user management and control
    - security
2. How can you run a program on a computer system that has no operating system (e.g., a microcontroller system)?
    - hard code an instruction set that runs without orchestration.
    - write a program that is compiled to the native chip set instruction set.
    - have the bootstrap program load it instead of the OS
2. How is an instruction executed on a computer system with a von Neumann architecture?
    - Instruction fetched from memory
    - decode instruction
    - execute action
        - fetch data
        - fetch oporator
        - write data to cache or memory
        - ect.
3. How does interrupt-driven I/O work through the relevant device controller and device driver?
    - in CPU
        - program needs a piece of data
        - OS asks driver for that data
        - driver (knowing the device) sets the appropriate registers in the IO device and makes the request of the IO device
        - the CPU continues in a different part of the program while waiting for the IO
    - in the IO device
        - using the information provided by the driver the IO interface the interface fetches the data and either stores it locally in it's buffer or saves it into a chunk of memory using DMA (direct memory access).
        - Once the IO is finished the IO interface sends an interrupt to the CPU.
    - Back in the CPU
        - When the CPU gets the interrupt it stops what it saves it's current instruction

From OSC9ed
1.17 Consider a computing cluster consisting of two nodes running a database. Describe two ways in which the cluster software can manage access to the data on the disk. Discuss the benefits and disadvantages of each.
    - each node can access it concurrently
    - do they mean sharding?
    - do they mean caching?
    - do they mean synchronized using a lock?
1.18 How are network computers different from traditional personal computers? Describe some usage scenarios in which it is advantageous to use network computers.
    - security
1.22 Many SMP (Symmetric Multi-Processor) systems have different levels of caches; one level is local to each processing core, and another level is shared among all processing cores. Why are caching systems designed this way?
    - trade off between speed and cost. A small local cache for partial calculations with shared cache for synchronized data
1.23 Consider an SMP system similar to the one shown in Figure 1.6. Illustrate with an example how data residing in memory could in fact have a different value in each of the local caches.
    - 
1.26 Which network configuration (LAN or WAN) would best suit the following environments?
    a. A campus student union: LAN
    b. Several campus locations across a statewide university system: WAN
    c. A neighborhood: WAN

### 1.2 Computer Hardware: Organization, Architecture, and Operating Systems
OSC9ed: 1.4 to 1.13.

#### Learning Outcomes

5. describe the overall structure and operations of operating systems.
6. explain the importance of understanding how an operating system works.
7. define *multiprogramming*, *time-sharing*, *dual-mode operation*, *privileged instructions*, *timer*, and *caching*.
8. describe (briefly) the activities in process management, memory management, and storage management.
9. discuss (briefly) protection, security, computing environments, distributed operating systems, special-purpose operating systems, and open-source operating systems.

#### Key Concepts and Topics

- multiprogramming
    - running multiple programs at the same time to optimize use of resources
- job pool
    - on disk memory of all the jobs needing to be done
    - a subset is kept in main memory
- job scheduling
    - the process of deciding which job to execute next (and for how long in time-sharing systems) when the process controller get back control of the CPU.
- time sharing or multitasking
    - time-sharing is multiprogramming that splits the CPU between all the programs so it appears to be running multiple programs concurently
    - the switches happen so often that users can interact with the system as if many programs are running in parallel
- interactive (hands-on) computer system
    - computer that interacts with a human
- response time
    - amount of time it takes for a computer to respond to input
- process
    - a set of instructions executed by the CPU
- virtual memory
    - a program is on disk but parts are in memory.
    - This treats main memory as a cache on top of the disk allowing faster response times for programs
- swapping
    - This is a section on disk that is used as main memory.
    - programs are swap into and out of disk
    - This is different than Virtual Memory because whole chunks of the program are transfered leading to lower response times.
- interrupt driven
    - interrupts are used for management of the CPU as a resource.
    - they trigger process changes, IO, and system calls
- trap or exception
    - a special interrupt for when there is an error
- dual-mode
    - keeps the user code from having access to certain instructions in the CPU by setting a flag.
    - the flag is switched off when an interrupt function is called and turned on when the kernel passes control back to a user process.
- user mode
    - a restricted set of CPU instructions
- kernel mode
    - the full set of CPU instructions
- privileged instructions
    - instructions that can only be accessed from kernel mode
- timer
    - sends an interrupt after a certain period
- process management
    - scheduling
    - creating user system and kernel processes
    - pausing and resuming processes (multi-tasking)
    - how processes interact
        - data synchronization between processes
        - communication between processes
- program counter
    - points to the next instruction in a process
    - multitasking requires multiple program counters to keep track of the next instruction in each of the processes that are running concurrently
- memory management
    - the process of allocating and de-allocating main memory
    - knowing what processes are using what memory
    - deciding which processes to move from virtual memory to main memory
- instruction-fetch cycle
    - get, decode, execute
    - the process of executing an instruction has 3 steps
- data-fetch cycle
    - when the CPU reads and writes data to the main memory
- file
    - an abstraction of the bytes stored on a disk into logical chunks.
    - everything on the computer is stored as a file
    - programs, data, ect
- mass-storage
    - a device that holds a large amount of data (hard disk, NAS, ect)
- caching
    - there are multiple layers of memory each with a smaller size and faster access time
    - caching optimizes it's usage by bringing information into the higher layers when it will be used by the CPU, and pushing it back down once it has been used.
    - This is an extremely complex system.
- cache management
    - the process of deciding what piece of cache to change out and when to push it down
- I/O subsystem
    - the particular interface of the IO device
    - they are all different and only the device drive knows how to request what it needs
- protection
    - stray electrons flipping bits
    - infinite loops
    - from different users
    - from peripherals & subsystems
    - from unauthorized use
- security
    - protect system from attacks
    - worms, viruses, dos
    - privilege escalation
- network operating system
    - systems that share a LAN and work together
- real-time operating systems
    - functions with certain real-time constraints
- handheld system - mobile devices
    - require programs optimized for low memory, processing power, and energy consuption
- multimedia system
    - vertex processing to run the same function on a lot of data at the same time
- client-server
    - data and program stored on one computer and interface on another computer ie. the web
- peer-to-peer
    - all systems in the network are equal
- open-source operating system
    - programs that are open to use
- Linux
- BSD UNIX
- Solaris

#### Study Questions

1. What do you think are the major aspects of operating systems?
    - allow users to easily run their programs
    - keep users and programs from affecting eachother
    - optimize resource usage

    - Process Scheduling
    - Memory Management
    - IO
    - Security (protection)
2. Why do kernel mode and user mode need to be separated, and what mechanisms are used for the separation?
    - So users can't mess with data that isn't theirs to mess with
    - the mode flag
3. What are *interrupt* and *trap* (or *exception*), and how are they used to support multi-programming and multi-tasking?
    - a special signal to the CPU to pause what it's going and do something else
    - they allow the CPU to be managed by task
4. Compare open-source operating systems such as Linux with closed-source systems such as Windows. Which one do you prefer under what conditions (or circumstances)?
    - Linux always unless there are historical reasons to use something else

### 1.3 Operating System Structures
OSC9ed: 2.1 to 2.5

Now that you are equipped with the necessary knowledge of computer hardware and systems, you will cover more details about operating system structures in this section. You will view an operating system from several vantage points: of a user, a programmer, and a designer of operating systems. You will examine the services and interface that the system provides, and also the components and their interconnections in the system.

This section still addresses the overall structure of operating systems, but from a higher level of abstraction. Seeing the operating system as a whole will help you to understand each of its components.

This section looks at the following key concepts of operating systems:

- system call
- system and application programs

#### Learning Outcomes

1. identify the services and interfaces that an operating system provides to users, to processes, and to other systems.
2. define system calls and types of system calls, and explain how system calls work in an operating system.
3. list the main system programs that an operating system usually provides.
4. describe several main structures of operating systems, and compare their structure and performance.
5. describe the design, implementation, debugging, and generation of operating systems.
6. explain the system boot function of operating systems.

#### Key Concepts and Topics

- operating system services helpful to users
    - graphical user interface (GUI)
    - batch interface: commands are placed in files and the files are executed
    - command interpreter: Command line
    - program execution
    - I/O operations: methods to get info from IO devices
    - file-system manipulation: the files and metadata on IO devices
        - programs need access, users need access, protecting & ownership
    - communications: allow processes to send messages on the same system or over the network
        - share memory, or message passing
    - error detection: able to see when an error has occurred and know what to do about it
        - pass error code to process, destroy process, or shutdown system, ect.
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

- application programming interface (API)
    - a higher level way to interact with the system call
    - rather than using the system calls directly a user program uses the api and the api interacts with the system calls.
    - this is an abstraction strategy similar to the example of drivers. When you move to a new system you simply re-compile your code using that systems version of the API and everything else stays the same... in theory :P
- systems programs: programs that are provided by the OS and may or may not be run in kernel mode.
    - file manager programs and text editors
    - logging, registry, system information viewer
    - compilers, interpreters, assemblers, and debuggers
    - communication programs such as Web browser

#### Study Questions

1. What are the three different vantage points for considering operating systems?
    > user, programmer, system designer wrong!
    > services provided by system, User and Programmer Interface, components and how they work together
2. What services are designed for performance, and what services are designed for usability?
    > user systems are generally designed for usability over performance, and systems where direct human interaction isn't common are usually designed for performance.
3. What are *system calls*, and how does a system call work in a dual-mode context?
    > system calls for an interface from a user program to the kernel. system calls generally execute a CPU's protected instruction on behalf of a user program while making sure that program isn't abusing it's power.
4. How do you see the relationship between Linux system calls and a standard C Library?
    > the standard C library is an API to the system calls. Any calls to the standard C library are generally translated to that OS's system calls.

#### Learning Activities

- [x] Take a look at Assignment 4: Part 2: Research Project: Option 2: Programming Project and evaluate whether adding a system call to the Linux Kernel may be something you may wish to try for this assignment.
- [x] Take a look at system calls in Linux to get a sense about their coverage. Consider consulting the supplemental Linux books listed in Unit 0.
- [x] Complete Exercises of *OSC9ed*.
    - 2.12: The services and functions provided by an operating system can be divided into two main categories. Briefly describe the two categories, and discuss how they differ.
        > System and Kernel programs: System programs have less privilege and interact through system calls to the kernel. The kernel is the interface between the hardware and the programs.
    - 2.13: Describe three general methods for passing parameters to the operating system.
        > registers, memory, function parameters
        > registers, on the stack, or in memory (pointers to the memory location)
    - 2.16: What are the advantages and disadvantages of using the same system-call interface for manipulating both files and devices?
        > advantage: simple to think about them the same way. easy to implement new driver. disadvantage: special functions of devices may not be available through system calls.
    - 2.18: What are the two models of interprocess communication? What are the strengths and weaknesses of the two approaches?
        > shared memory or message passing. Shared memory is faster but much more prone to error, message passing is slower but results in fewer errors.

### 1.4 Operating System Structures
OSC9ed: 2.7 and 2.8.

#### Learning Outcomes

- describe several main structures of operating systems
    - compare their structure and performance
- describe the * of operating systems.
    - design
    - implementation
    - debugging
    - generation
- system boot
- micro kernel
- performance tuning
- operating system generation

#### Key Concepts and Topics

- operating system structure
- layered approach
- kernel
- micro kernel approach
- mach
- modular kernels
- virtual machine and virtualization
- para-virtualization
- zones or containers
- simulation
- VMware architecture
- Java virtual machine
- just-in-time (JIT) compiler

#### Study Questions

1. What do you think about operating systems based on microkernel structure compared with their layered and modular kernel counterparts?
2. Why is it important to separate kernel from user space?
3. How are user mode and kernel mode issues dealt with under a virtual machine environment?

#### Learning Activities

- [ ] Complete Exercises of *OSC9ed*:
    - 2.20
    - 2.21
    - 2.22
    - 2.24
    - 2.25

### 1.5 Operating System Structures
OSC9ed: 2.6, 2.9, 2.10, 2.11

#### Learning Outcomes

- explain the system boot function of operating systems.
- system boot
- micro kernel
- performance tuning
- operating system generation

#### Key Concepts and Topics

- operating-system design:
    - goals
    - mechanisms
    - policies
- operating-system implementation: language issue
- operating-system debugging
- debugger
- core dump
- crash dump
- operating-system performance tuning
- profiling
- operating-system generation
- system boot
- boot block
- GRUB

#### Study Questions

1. What is the reason (besides a few core codes programmed by assembly) for using high level language in OS design?
2. Why is operating-system generation and booting needed in most operating systems? What is the two-step process for system boot?

#### Learning Activities

- Complete Practice Exercises of *OSC9ed*.
    - 2.1:
    - 2.11:
    - 2.19:
    - 2.23:

### Supplementary Unit Activities

- Explore surveys and technical documents about the structures and components of modern computer organization, architecture, and operating systems. Based on this exploration, try to identify an existing problem of your interest and a possible solution to it (you may continue this work in the following units, until you find a suitable topic for Assignment 4 of this course). Share your findings and opinions with your classmates and tutor on the course discussion forum.
- If you need to know more about computer organization and architecture, please access materials on the following Suggested References through the AU Library.

AU Library: Electronic Resources
- Patterson, D. A., & Hennessy, J. L. (2009). *Computer organization and design: The hardware/software interface* (4th ed.). Burlington, MA: Morgan Kaufmann/Elsevier.
- Mostafa, A-E-B, & Hesham, E-R. (2005). *Fundamentals of computer organization and architecture.* Hoboken, NJ: Wiley.
- Dandamudi, S. P. (2003). *Fundamentals of computer organization and design.* New York: Springer.

AU Library: Print Resources
- Stallings, W. (1996). *Fundamentals of computer organization and design* (4th ed.). Englewood Cliffs, NJ: Prentice-Hall.
- Baron, R. J. (1992). *Computer architecture: Case studies.* Reading, MA: Addison-Wesley.
- Hwang, K. (1993). *Advanced computer architecture: Parallelism, scalability, programmability.* New York: McGraw-Hill.
- Mano, M. M. (1993). *Computer system architecture* (3rd ed.). Englewood Cliffs, NJ: Prentice-Hall.

## Assignment 1

This assignment should be submitted after you have finished Unit 1. It is worth 10% of your final grade.

Part 1: Concepts and Principles (60 marks; 5 marks each)

Instructions: Please answer the following questions in complete sentences. Your answer for each question should be about 150 words.

1. Define the concepts interrupt and trap, and explain the purpose of an interrupt vector.
1. How does a computer system with von Neumann architecture execute an instruction?
1. What role do device controllers and device drivers play in a computer system?
1. Why do clustered systems provide what is considered high-availability service?
1. Describe an operating system’s two modes of operation.
1. Define cache, and explain cache coherency.
1. Describe why direct memory access (DMA) is considered an efficient mechanism for performing I/O.
1. Describe why multicore processing is more efficient than placing each processor on its own chip.
1. Describe the relationship between an API, the system-call interface, and the operating system.
1. Describe some requirements and goals to consider when designing an operating system.
1. Explain why a modular kernel may be the best of the current operating system design techniques.
1. Distinguish between virtualization and simulation.

Part 2: Design Considerations (40 marks)

Instructions: Please answer the following questions in about 1-2 pages each.

1. Draw a typical computer organization figure that includes the main components of von Neumann architecture. Identify each component, and explain its function and interaction relative to other components. (15 marks)
1. Define system call, and list the main types of system calls. Elaborate on how a system call interacts with a standard C library and hardware under a dual-mode operating system environment. (10 marks)
1. Describe the overall structure of virtual machines, and compare VMware and JVM. (15 marks)

## Unit 2: Process Management
Unit 2 will define *process* and address processes, threads, CPU scheduling, process synchronization, deadlocks, and interprocess communication.

This unit elaborates on process management, which is at the core of modern operating systems. An operating system must ensure that all processes, and their threads as applicable, are assigned proper resources (CPU time, memory, files, I/O devices, etc.) to accomplish their tasks in a time sharing, multi-processor, and multi-core computer system. Process management covers processes, threads, CPU scheduling, process synchronization, and deadlock handling.

Learning Objectives:

After you complete Unit 2, you should be able to describe the behaviour and characteristics of processes in computing systems, and discuss the relationship of processes to resources. With this understanding, you should be able to explain how an operating system manages processes and threads (addressing system queues and the scheduling of algorithms). You should also be able to explain key terms and principles of process management, such as *kernel*, *process*, *thread*, *scheduling*, *synchronization*, *deadlock handling*, and *recovery*; and discuss how various aspects of the process management are implemented in practice in systems such as Linux, Windows, and Solaris.

### 2.1 Processes

This section introduces the key concepts of processes, process states, process control block (PCB), and threads. From this basis, it moves on to the basic principle of process scheduling—the main task of process management.

It also elaborates on interprocess communication (IPC) and introduces client-server communication, both of which are important for interaction among programs and processes.

The concepts of data structures and principles are key to understanding the remaining sections of Unit 2. Take special note of the following issues:

- the notion of process
- the meaning of process states
- the queuing diagram of process scheduling
- process creation and termination
- interprocess communication through shared memory and message passing
- sockets, pipes, and RPC (remote process calling)

### 2.1.1 Processes
OSC9ed: 3.1 to 3.3.

#### Learning Outcomes

1. define *process*, *process states*, and *process scheduling*.
2. outline the differences between processes and programs.
3. describe how the states of processes change during their execution.
4. explain how process control block (PCB) is used during central processing unit (CPU) switches from process to process.
5. describe the queuing diagram representation of process scheduling.
6. explain how processes are created and terminated, and how to apply them in multi-process programming in Linux or Windows operating systems.

#### Key Concepts and Topics

- process
- process states
    - new
    - running
    - waiting
    - ready
    - terminated
- process control block
- process scheduling
- process scheduler
    - job scheduler, or long-term scheduler
    - CPU scheduler, or short-term scheduler
    - medium-term scheduler
- swapping
- context switch
- scheduling queues
    - job queue
    - ready queue
    - device queue
- degree of multiprogramming
- process creation
- fork ()
- process termination

#### Study Questions

1. What are the main features of processes?
2. What information is included in PCB?
3. What data structures are involved in process scheduling?
4. What is the rationale for each kind of scheduler: long-term, short-term, and medium-term schedulers?
5. How do you use fork() to create a process?

#### Learning Activities

- Run the following online animations:
    - [the dynamic state of a process](http://cs.uttyler.edu/Faculty/Rainwater/COSC3355/Animations/dynamicprocess.htm)
    - [CPU switching between processes due to system calls or interrupts](http://cs.uttyler.edu/Faculty/Rainwater/COSC3355/Animations/switch.htm)
    - [example of a process life cycle](http://williamstallings.com/OS/Animation/Queensland/PROCESS.SWF)
- Try Exercises of *OSC9ed*.
    - 3.6
    - 3.10
    - 3.13

### 2.1.2 Processes
OSC9ed: 3.4 to 3.6.

7. define *interprocess communication* (IPC).
8. explain the foundational functions behind the two models of interprocess communication (IPC): shared-memory and message passing.
9. explain how shared-memory and message passing functions are realized in real systems such as POSIX and Windows.
10. explain the mechanisms of communication in client-server systems, including sockets, remote procedure calls (RPC), pipes, and named pipes.
11. apply IPC and client-server communication API in system programming.

#### Key Concepts and Topics

- process cooperation
- interprocess communication (IPC)
    - shared-memory
    - message passing
- producer-consumer problem
- bounded and unbounded buffer
- direct and indirect communication
- naming
- mailbox or port
- synchronization
- buffering
    - zero, bounded, and unbounded capacity
- POSIX shared memory
- message passing in Mach
- local procedure calls in Windows
- communication in client-server systems
- sockets
- remote procedure calls (RPCs)
    - port
    - stub
    - matchmaker
    - ACK message
- pipe
- named pipe

#### Study Questions

1. Why is process cooperation supported in modern operating systems?  What are the benefits?
2. What is the difference between IPC and RPC?
3. How are shared memory, message passing, RPC, sockets, and pipes implemented practically in systems such as POSIX, Mach, and Windows?

#### Learning Activities

- Try Exercises of *OSC9ed*.
    - 3.11
    - 3.12
    - 3.14
- Test and run the sample c or [Java source code of IPC and client-server communication](http://people.westminstercollege.edu/faculty/ggagne/osc/osc8e-src.zip) provided on the textbook’s website.
- Download and review the [PowerPoint slides](http://bcs.wiley.com/he-bcs/Books?action=resource&bcsId=7887&itemId=1118063333&resourceId=33777) or pdf for Chapter 3 of *OSC9ed*.
- Read “3.23 POSIX Message Passing” in the Programming Projects section near the end of Chapter 3 of *OSC9ed*., and consider whether a similar programming project might interest you for Assignment 4.
- Complete Practice Exercises 3.1 to 3.5 of *OSC9ed*. You may check the answers to these questions at Operating System Concepts (9th ed.): [Solutions to Practice Exercises](http://bcs.wiley.com/he-bcs/Books?action=resource&bcsId=7887&itemId=1118063333&resourceId=33732).

### 2.2 Threads
OSC9ed: 4.1 to 4.7.

This section addresses threads and discusses multithreading models and thread libraries. Basically, a *thread* is a basic unit of a CPU, and a multithreaded process can bring significant benefits, such as improved responsiveness, scalability, and resource sharing. Most modern operating systems support multithreading mechanisms, and many system programs use multithreading to improve their performance. It is necessary to understand multithreading mechanisms to do system or service-related implementation and programming.

#### Learning Outcomes

1. define *thread* and *multithreaded process*.
2. describe the motivation for and benefits of multithreaded programming.
3. briefly describe multicore programming, and explain its connection with multithreaded programming.
4. identify multithreading models (e.g., many-to-one, one-to-one, and many-to-many modes), and explain how they map user threads to kernel threads.
5. describe thread libraries such as Pthreads, Windows threads, and Java threads.
6. discuss issues that must be considered with multithreaded programs, such as thread cancellation, thread pool, lightweight process (LWP), etc.
7. describe how threads are implemented in Linux and Windows.

#### Key Concepts and Topics

- thread
- multithreaded programming
- multithreaded process and single-threaded process
- multicore programming
- multithreading models
    - many-to-one model
    - one-to-one model
    - many-to-many model
    - two-level model
- user threads
- kernel threads
- thread libraries
    - Pthreads
    - Java threads
    - Windows threads
- thread cancellation
- signal handling in multithreaded programs
- thread pool
- lightweight process (LWP)
- thread-specific data
- scheduler activations
- fork(), exec(), and clone()
- threads implementation in operating systems
    - Linux threads
    - Windows threads

#### Study Questions

1. What is the motivation for using multiple threads in a process?
2. What are the benefits of using multithreaded programming?
3. What are the differences between user-level threads and kernel-level threads?
4. How do POSIX, Java, and Windows implement their thread libraries?
5. How can thread libraries be used for multithreaded programming?

#### Learning Activities

- Try Exercises of *OSC9ed*.
    - 4.1
    - 4.6
    - 4.9
    - 4.10
    - 4.15
- Test and run the [sample c or Java source code of multithreaded programs](http://people.westminstercollege.edu/faculty/ggagne/osc/osc8e-src.zip) provided on the textbook’s website.
- Download the [PowerPoint slides](http://bcs.wiley.com/he-bcs/Books?action=resource&bcsId=7887&itemId=1118063333&resourceId=33777) or pdf for Chapter 4 of *OSC9ed*.
- Read “Project 1: Naming Service Project” and “Project 2: Matrix Multiplication Project” in the Projects section of Chapter 4 of *OSC9ed* to see whether such a programming project might interest you for Assignment 4.

### 2.3 CPU Scheduling
OSC9ed: 6.1 to 6.9.

CPU scheduling is the basis of modern operating systems that can execute multiple processes and threads simultaneously. This section covers the concepts, criteria, algorithms, and examples of CPU scheduling, and introduces scheduling issues related to *thread* (thread scheduling), *multiple-processors* (multiple-processor and multicore processor scheduling), and *virtualization*.

#### Learning Outcomes

1. define *CPU scheduling*, and explain the rationale for using it in modern operating systems.
2. explain the concepts and criteria associated with various CPU scheduling algorithms.
3. explain the implementation of CPU scheduling in current operating systems such as Linux, Solaris, and Windows.
4. describe and evaluate methods for CPU scheduling algorithms for a particular system.

#### Key Concepts and Topics

- CPU scheduling
    - process scheduling
    - thread scheduling
- CPU burst and I/O burst
- CPU scheduler or short-term scheduler
- pre-emptive scheduling
- non-pre-emptive or cooperative scheduling
- dispatcher
- dispatcher latency
- scheduling criteria
    - CPU utilization
    - throughput
    - turnaround time
    - waiting time
    - response time
- Gantt chart
- scheduling algorithms
    - first-come, first-served (FAFS)
    - shortest-job-first (SJF)
    - shortest-next-CPU-burst
    - shortest-remaining-time-first
    - priority scheduling
    - aging
    - starvation of indefinite blocking
    - round-robin (RR) scheduling
    - multilevel queue scheduling
    - multilevel feedback queue scheduling
- thread scheduling
    - process-contention scope (PCS)
    - system-contention scope (SCS)
    - Pthread scheduling
- multiple-processor scheduling
- asymmetric multiprocessing
- symmetric multiprocessing (SMP)
- processor affinity
    - soft affinity
    - hard affinity
    - load balancing
- multicore processor scheduling
- scheduling in virtual machines
- Linux scheduling
- Windows scheduling
- Solaris scheduling
- scheduling algorithm evaluation
    - deterministic modeling
    - queueing model
    - Little’s formula
    - queueing-network analysis
    - simulation
    - implementation

#### Study Questions

1. Why is CPU scheduling very important in modern operating systems?
2. What are the differences between pre-emptive and cooperative scheduling? How are pre-emptive scheduling and cooperative scheduling used in operating system design?
3. What are the main CPU scheduling algorithms, and how do they work?
4. What are the issues unique to multiple processor scheduling compared to single CPU scheduling?
5. In practice, how do operating systems perform CPU scheduling?

#### Learning Activities

- Try Exercises of *OSC9ed*.
    - 6.1 - 6.9
    - 6.16 - 6.20
    - 5.1
    - 5.8 
- Test the [sample c source code of Pthread scheduling](http://people.westminstercollege.edu/faculty/ggagne/osc/osc8e-src.zip) provided on the website of *OS6ed*.

### 2.4 Process Synchronization
OSC9ed: 5.1 to 5.11.

This section introduces process synchronization, which aims to provide mutually exclusive access to data and resources that are shared by a collection of cooperating sequential processes, to ensure that the data consistency is maintained. This section discusses various process synchronization mechanisms such as critical-section, locking, semaphores, monitors, and synchronization implementation in Linux, Solaris, and Windows.

This section also provides an overview of concepts and techniques of concurrent atomic transactions, such as log-based recovery, locking protocol, and timestamp-based protocols.

Key concepts and problems in this section:

- critical-section problem
- semaphores
- monitors
- classic problems of synchronization

#### Learning Outcomes

1. define *critical-section problem*.
2. explain hardware and software solutions for the critical-section problem.
3. describe semaphores and monitors, and explain how they are implemented.
4. explain how to use semaphores and monitors to handle classic problems of synchronization such as bounded-buffer problems, readers-writers problems, and dining-philosophers problems.
5. describe synchronization mechanisms in Linux, Solaris, and Windows.
6. discuss the concept of atomic transactions and the mechanisms by which to ensure atomicity.

#### Key Concepts and Topics

- synchronization
- race condition
- critical-section and critical-section problem
    - mutual exclusion
    - progress
    - bounded waiting
- Peterson’s solution
- hardware instructions executed atomically
    - swap()
    - testandset()
- semaphores
    - wait(S)
    - signal(S)
- mutex locks or binary semaphore
- counting semaphore
- spinlock
- busy waiting
- block() and wakeup(P)
- deadlocks
- starvation or indefinite blocking
- priority inversion
- classic problems of synchronization
    - bounded-buffer problem
    - readers-writers problem
    - dining-philosophers problem
- monitors
    - monitor type
    - conditions
- synchronization
    - in Solaris
    - in Windows
    - in Linux
- atomic transaction
- commit, abort, and roll back
- write-ahead logging
- log-based recovery
- checkpoints
- concurrent atomic transactions
- serializability
- serial schedule
- nonserial schedule
- conflicting operations
- conflict serializable
- locking protocol
- two-phase locking protocol (2PL)
- timestamp-based protocol

#### Study Questions

1. What is the purpose of process synchronization?
2. What requirements should be satisfied to solve the critical-section problem?
3. What are the differences between hardware instruction and semaphore-based solutions?
4. What are the differences between semaphore and monitor? How are they used for solving the classic problems of synchronization?
5. How do Windows and Linux support process synchronization?
6. What is conflict serializability, and how can locking protocols be used to ensure it?

#### Learning Activities

- Try Exercises 5.7 of *OSC9ed*.
    - 5.8
    - 5.11
    - 5.17
    - 5.34
- Read “Producer-Consumer Problem” in the Programming Projects section of Chapter 5 of *OSC9ed*, to see whether a similar programming project might interest you for Assignment 4.
- Try to run the following [animations provided on the website of *OS6ed*](http://williamstallings.com/OS/Animation/Animations.html):
    - [Process Synchronization: Producer/Consumer Problem](http://cs.uttyler.edu/Faculty/Rainwater/COSC3355/Animations/processsync.htm)
    - [The Critical Section Problem: Algorithm 3](http://cs.uttyler.edu/Faculty/Rainwater/COSC3355/Animations/criticalsection.htm)
    - [Mutual Exclusion Achieved through Semaphores](http://cs.uttyler.edu/Faculty/Rainwater/COSC3355/Animations/semaphore.htm)
    - [Producer/Consumer Workbench Semaphore Solution](http://cs.gmu.edu/cne/workbenches/pcsem/pcsem.html)
    - [Producer/Consumer Workbench Monitor Based Solution](http://cs.gmu.edu/cne/workbenches/pcmon/pcmon.html)
    - [Simple Solution to the Bounded Buffer Problem](http://williamstallings.com/OS/Animation/Queensland/BB.SWF)
    - [Implementation of the Bounded Buffer Problem Using a Counter Variable](http://williamstallings.com/OS/Animation/Queensland/BB_COUNT.SWF)
    - [Mutex: A Binary Semaphore](http://williamstallings.com/OS/Animation/Queensland/SEMA.SWF)
    - [Process Synchronization with Semaphores](http://williamstallings.com/OS/Animation/Queensland/SYNC.SWF)
- Download the [PowerPoint slides](http://bcs.wiley.com/he-bcs/Books?action=resource&bcsId=7887&itemId=1118063333&resourceId=33777) or pdf for Chapter 6 of *OSC9ed*.

### 2.5 Deadlocks
OSC9ed: 7.4 to 7.7.

The final section in this unit discusses deadlocks, which may occur when several processes compete for a finite number of resources. Topics in this section include techniques to detect, prevent, and avoid deadlocks. As operating systems typically do not provide deadlock-prevention facilities, programmers are responsible for ensuring that the programs they design are deadlock free. The information in this section will help well-trained programmers to analyze and address deadlock-related issues in their programs.

#### Learning Outcomes

1. define *deadlock*, and discuss the conditions under which a deadlock may arise.
2. summarize the different ways of and methods for handling deadlock.
3. describe how to realize deadlock prevention, deadlock avoidance, deadlock detection, and deadlock recovery.
4. explain the resource-allocation-graph algorithm, Banker’s algorithm, and deadlock detection algorithm.

#### Key Concepts and Topics

- deadlock
- necessary conditions for a deadlock to arise
    - mutual exclusion
    - hold and wait
    - no pre-emption
    - circular wait
- resource-allocation graph
- deadlock prevention
- deadlock avoidance
- safe state
- safe sequence
- resource-allocation-graph algorithm
- Banker’s algorithm
    - safety algorithm
    - resource-request algorithm
- deadlock detection
- wait-for graph
- detection algorithm
- recovery from deadlock

#### Study Questions

1. Why is it important to learn to handle deadlock issues?
2. What are the necessary conditions for a deadlock to happen, and how can knowledge of these conditions be used in deadlock prevention?
3. How can one determine whether a state is safe state (deadlock free)?  How can this knowledge be used to avoid deadlock?
4. What data structures are used in deadlock avoidance and deadlock detection?

#### Learning Activities

- Try Exercises *OSC9ed*.
    - 7.1
    - 7.9 
    - 7.10
    - 7.11
    - 7.20
    - 7.21
- Try to run the [Resource Allocation Graph animation](http://cs.uttyler.edu/Faculty/Rainwater/COSC3355/Animations/deadlock.htm) provided on the website of *OS6ed*.
- Download and review the [PowerPoint slides](http://bcs.wiley.com/he-bcs/Books?action=resource&bcsId=7887&itemId=1118063333&resourceId=33777) or pdf for Chapter 7 of *OSC9ed*.

### Supplementary Unit Activities

- Explore surveys and technical documents about process management such as processes, threads, CPU scheduling, process synchronization, and deadlock handling in widely used systems such as Linux, Mac, Windows, and Solaris.
- You may also explore Linux processes, threads, CPU scheduling, and process synchronization to see what features are provided.
- Compare other operating systems such as PDA, cell phone, and iPhone, and see whether their operating systems have the same issues in process management as those discussed in this unit, and explain why or why not.
- Share your findings and opinions with your classmates and tutor on the course discussion forum.

## Assignment 2

This assignment should be submitted after you have completed Unit 2. It is worth 10% of your final grade for this course.

Instructions: Please answer the following questions in complete sentences. Your answer for each question should be about 150 words. (100 marks total)

1. Define short-term scheduler and long-term scheduler, and explain the main differences between them. (6 marks)
1. Explain the concept of a context switch. (6 marks)
1. Explain the terms at most once and exactly once, and indicate how these terms relate to remote procedure calls. (6 marks)
1. Identify and briefly explain each of the four major categories of benefits of multithreaded programming. (6 marks)
1. Briefly describe the benefits and challenges for multithreaded programming that are presented by multicore systems. (8 marks)
1. Define coarse-grained multithreading and fine-grained multithreading, and explain their differences. (6 marks)
1. Explain process starvation and how aging can be used to prevent it. (6 marks)
1. How does the dispatcher determine the order of thread execution in Windows? (6 marks)
1. Define critical section, and explain two general approaches for handling critical sections in operating systems. (8 marks)
1. Describe the dining-philosophers problem, and explain how it relates to operating systems. (6 marks)
1. Define the two-phase locking protocol. (6 marks)
1. Describe how an adaptive mutex functions. (6 marks)
1. Describe a scenario in which the use of a reader-writer lock is more appropriate than using another synchronization tool, such as a semaphore. (6 marks)
1. What is the difference between deadlock prevention and deadlock avoidance? (6 marks)
1. Describe a wait-for graph, and explain how it detects deadlock. (6 marks)
1. Describe how a safe state ensures that deadlock will be avoided. (6 marks)

## Unit 3: Storage Management
This unit covers memory management, virtual memory, file system management, disk management, mass storage structures, and I/O systems.

### Unit Overview

Unit 3 discusses how memory, file systems, mass storage, and I/O
(input/output) are handled in modern computer systems.

In a multiprogramming system, a process may change its state from
“waiting” to “running” several times before completing its task. Clearly, if each process were loaded from secondary storage into the main memory in its entirety, a large fraction of machine time would be wasted on loading and unloading processes to and from the main memory during each section of process execution. To minimize the “overhead”
associated with loading and unloading, operating systems allocate memory to several processes simultaneously. This complex task requires effective memory management schemes and their hardware support (major topics in this unit).

The other major topic in this unit is secondary storage, in particular, file systems and disk management. Disks serve as extensions and backup for the main memory, and as economical online storage devices for program and data files. The operating system organizes files in the framework of a file system. Disk access is much slower than access to memory and, in general, several processes compete for disk access. For these reasons, in many computers, disk access is the main bottleneck to improved performance. As such, section 3.4 examines the software and hardware mechanisms employed to improve disk performance.

Input-output operations are among the main jobs of a computer system. As various I/O devices vary widely in their function and speed, different methods are needed to control them, and those methods form the I/O subsystem of the kernel. The final section of this unit covers the structure, principles, and performance aspects of I/O hardware and software.

Unit 3 is divided into five sections:

**3.1 Main Memory**

**3.2 Virtual Memory**

**3.3 File-System Interface and Implementation**

**3.4 Mass-Storage Structure**

**3.5 I/O Systems**

### Learning Objectives

When you complete Unit 3, you will be able to describe the different strategies that operating systems employ to manage memory, with knowledge of the benefits, limitations, resource overhead (such as fragmentation and data structures), and hardware requirements of each management technique. You will also learn how developers can write applications (program and data structures) that reduce overhead for memory in a shared environment and that use memory more efficiently. In modern application environments, in which virtual memory is becoming increasingly important, it is important that you can explain this concept and its importance, and that you can list and describe several strategies that systems software uses to manage disks and other devices. Finally, you should be able to describe the structure, principles, and performance issues of I/O hardware and software.

### 3.1 Main Memory

#### Overview

This section focuses on memory management in the main system. Memory is an important finite resource that has a significant impact on system throughput. As such, it must be managed carefully. In a multiprogramming environment, the operating system attempts to complete as much work as possible at one time by allowing processes to share memory. To do this, it is critical that the operating system manage memory in such a way that many processes may share it and that the memory space for each process is protected from other processes. This security measure requires that all memory addresses be validated. The overhead resource cost of verifying every memory access makes hardware support necessary.

#### Learning Outcomes

After you have completed Section 3.1, you should be able to

1. describe address binding at compile, load, and execution time.
2. explain the different strategies that operating systems use to
 manage the sharing and allocation of memory among several processes,
 including contiguous allocation, paging, segmentation, and
 segmentation with paging.
3. discuss how relocation, sharing, and protection are considered in
 memory management.
4. describe how an operating system may implement shared memory.

#### Reading Assignment

- *Operating system concepts* (9th ed.): Chapter 8: Main Memory: 8.1
 to 8.7.

As you do the assigned reading, focus on the Key Concepts and Topics outlined below to ensure that you can meet Learning Outcomes 1-4 above.

#### Key Concepts and Topics

- address binding
- compile time binding
- execution time binding
- load time binding
- logical address
- virtual address
- memory management unit (MMU)
- dynamic loading
- static and dynamic linking
- swapping
- contiguous allocation
- partitioning
- variable-partition scheme
- fragmentation
    - external fragmentation
    - internal fragmentation
- compaction
- paging
- page
- frame
- page table
- frame table
- page-table base register (PTBR)
- translation look-aside buffer (TLB)
- hit-ratio
- frame protection
- multilevel paging
- hash-page table
- inverted page table
- segment
- segment table
- segmentation
- segmentation with paging
- local descriptor table (LDT)
- global descriptor table (GDT)

#### Study Questions

1. What is *address binding*?
2. What are the main purposes of swapping, paging, and segmentation in
 memory management?
3. When should an operating system designer consider using hashed
 paging and inverted paging instead of hierarchical paging?
4. How does an Intel architecture support both paging and segmentation?

#### Learning Activities

- Download and review the [PowerPoint
 slides](http://bcs.wiley.com/he-bcs/Books?action=resource&bcsId=7887&itemId=1118063333&resourceId=33777)
 or pdf for Chapter 8 of *OSC9ed*.
- Try 8.1-8.5 of *OSC9ed*.
- Complete Exercises 8.11, 8.20, and 8.28 of *OSC9ed*. You may check
 the answers to these questions at Operating System Concepts (9th
 ed.): [Solutions to Practice
 Exercises](http://bcs.wiley.com/he-bcs/Books?action=resource&bcsId=7887&itemId=1118063333&resourceId=33732).
- Try to run the following animations from the website of *OS6ed*:
    - [Overlays for Primitive Memory
 Management](http://cs.uttyler.edu/Faculty/Rainwater/COSC3355/Animations/overlays.htm)
    - [Dynamic Relocation Using a Relocation
 Register](http://cs.uttyler.edu/Faculty/Rainwater/COSC3355/Animations/relocation.htm)
    - [Multiple Partition Contiguous Memory
 Allocation](http://cs.uttyler.edu/Faculty/Rainwater/COSC3355/Animations/multiplepartcma.htm)
    - [Compaction](http://cs.uttyler.edu/Faculty/Rainwater/COSC3355/Animations/compaction.htm)
    - [Paging
 Hardware](http://cs.uttyler.edu/Faculty/Rainwater/COSC3355/Animations/paginghardware.htm)
    - [Paging Model of Logical and Physical
 Memory](http://cs.uttyler.edu/Faculty/Rainwater/COSC3355/Animations/pagingmodel.htm)
    - [Paging Example for a 32-Byte Memory with 4-Byte
 Pages](http://cs.uttyler.edu/Faculty/Rainwater/COSC3355/Animations/pagingexample.htm)
    - [Segmentation
 Hardware](http://cs.uttyler.edu/Faculty/Rainwater/COSC3355/Animations/segmentation.htm)
    - [Paged
 Segmentation](http://cs.uttyler.edu/Faculty/Rainwater/COSC3355/Animations/pagedsegmentation.htm)

### 3.2 Virtual Memory

#### Overview

For users, the tangible benefit of virtual memory is that it removes the restriction that the size of the computer’s memory places on the size of an executable program. The key idea behind virtual memory is easy to state but much harder to implement: keep only those (code and data) parts of a process in the memory that are needed in the current CPU burst of the process. This section examines the software and hardware mechanisms needed to implement virtual memory.

#### Learning Outcomes

After you have completed Section 3.2, you should be able to

1. explain the concept of *virtual memory*, and discuss the benefits,
 implementation, and overhead.
2. define *demand paging* and *page replacement*.
3. describe the page replacement algorithms and strategies listed below
 in terms of algorithms, data structures, overhead, and benefits.
    - first-in first-out (FIFO)
    - optimal
    - least-recently-used (LRU) and variations
    - page buffering
4. outline the decision problems associated with frame allocation.
5. explain the phenomenon of thrashing and the strategies and
 techniques deployed to deal with this problem.
6. describe how memory mapping files and shared memory operate in the
 Win32 API.
7. discuss the following factors that affect the character and
 performance of a paging system: prepaging, page size, program
 structure, and I/O interlock.

#### Reading Assignment

- *Operating system concepts* (9th ed.): Chapter 9: Virtual Memory:
 9.1 to 9.10.

As you do the assigned reading, focus on the Key Concepts and Topics outlined below to ensure that you can meet Learning Outcomes 1-7 above.

#### Key Concepts and Topics

- virtual memory
- demand paging
- lazy swapper
- pager
- page fault
- locality of reference
- page fault rate
- copy-on-write
- page replacement
- reference string
- first-in first-out page replacement
- optimal page replacement
- Belady’s anomaly
- least-recently-used page replacement
- page-buffering algorithm
- frame allocation
    - global page replacement
    - local page replacement
- thrashing
- working-set model
- memory-mapped files and I/O
- shared memory
- prepaging
- I/O interlock

#### Study Questions

1. Why is virtual memory an important feature of modern operating
 systems?
2. What is page replacement? How should different page replacement
 algorithms be chosen?
3. How are memory-mapped files used for memory sharing?

#### Learning Activities

- Download and review [PowerPoint
 slides](http://bcs.wiley.com/he-bcs/Books?action=resource&bcsId=7887&itemId=1118063333&resourceId=33777)
 or pdf for Chapter 9 of *OSC9ed*.
- Try Exercises 9.3, 9.6, 9.8, 9.21, 9.27, and 9.32 of *OSC9ed*.

### 3.3 File-System Interface and Implementation

#### Overview

The main criterion for a good file system is that it provide the user with convenient (user friendly), effective, and secure means of organizing and accessing his or her files. This section examines the file-system concepts familiar to most users, such as file names, file types, directory structures, and file protection. Section 3.3 also discusses some of the practical problems, block-allocation schemes, performance criteria, and backup and recovery schemes that system designers must consider when they implement file systems on disk.

#### Learning Outcomes

After you have completed Section 3.3, you should be able to

1. explain the function of file systems and their interfaces.
2. describe the concepts of file, file attributes, file operations,
 file organization, and file access.
3. outline the different directory structures.
4. describe file system mounting and file sharing.
5. describe the nature of protection schemes, including the concept of
 owner, group, and universe (world) categories, and the concept of
 access lists.
6. explain the layered approach to file system organization.
7. describe the implementation of a local file system and directory.
8. explain contiguous, linked, and indexed disk allocation strategies,
 and the overhead, benefits, and problems associated with each.
9. discuss free-space management and its possible implementations.
10. discuss the importance of backup and recovery.
11. discuss efficiency and performance issues related to file systems
 and organization.

#### Reading Assignment

- *Operating system concepts* (9th ed.): Chapter 11: File-System
 Interface: 11.1 to 11.6.

As you do the assigned reading, focus on the Key Concepts and Topics outlined below to ensure that you can meet Learning Outcomes 1-5 above.

#### Key Concepts and Topics

- open file table
- file organization
- file structure
- packing
- internal fragmentation, files
- access method
- sequential access
- relative access
- logical record
- random access
- indexed
- indexed sequential access
- relative block number
- directory
- tree structured directory
- subdirectory
- device directory
- acyclic graph directory
- symbolic link
- mount point
- immutable shared files
- access control list

#### Study Questions

1. What are the different file access methods? How are they related to
 file organization?
2. How does access control support file sharing and file protection?

#### Learning Activities

- Download and review the [PowerPoint
 slides](http://bcs.wiley.com/he-bcs/Books?action=resource&bcsId=7887&itemId=1118063333&resourceId=33777)
 or pdf for Chapter 11 of *OSC9ed*.
- Complete Practice Exercises 11.1 to 1.9 of *OSC9ed*. You may check
 the answers to these questions at Operating System Concepts (9th
 ed.): [Solutions to Practice
 Exercises](http://bcs.wiley.com/he-bcs/Books?action=resource&bcsId=7887&itemId=1118063333&resourceId=33732).
- Try Exercises 11.10 to 11.13 and 11.17 of *OSC9ed*.

#### Reading Assignment

- *Operating system concepts* (9th ed.): Chapter 12: File-System
 Implementation: 12.1 to 12.9.

As you do the assigned reading, focus on the Key Concepts and Topics outlined below to ensure that you can meet Learning Outcomes 6-11 above.

#### Key Concepts and Topics

- basic file system
- logical file system
- file-control block
- mount table
- virtual file systems
- dynamic storage allocation
- external fragmentation
- file allocation table (FAT)
- index block
- linked allocation
- combined index
- backup
- recovery
- consistency checking

#### Study Questions

1. What are the drawbacks of a layered structure in a file-system
 implementation?
2. When would you consider designing a special file system instead of
 using the one distributed with an operating system?
3. What are the two most important functions of the Virtual File
 System (VFS) layer?
4. What are the problems associated with linked allocation of disk
 space routines?

#### Learning Activities

- Complete Practice Exercises 12.1 to 12.8 of *OSC9ed*. You may to
 check the answers to these questions at Operating System Concepts
 (9th ed.): [Solutions to Practice
 Exercises](http://bcs.wiley.com/he-bcs/Books?action=resource&bcsId=7887&itemId=1118063333&resourceId=33732).
- Try Exercises 12.11, 12.15, 12.16, and 12.20 of *OSC9ed*.
- Download and review the [PowerPoint
 slides](http://bcs.wiley.com/he-bcs/Books?action=resource&bcsId=7887&itemId=1118063333&resourceId=33777)
 or pdf for Chapter 12 of *OSC9ed*.
- Analyze a file system familiar to you, and list the features and
 characters introduced in this section.

### 3.4 Mass-Storage Structure

#### Overview

A file system can be viewed logically as consisting of three parts: the interface to the file system (for users and programmers), the internal data structures and algorithms for implementing the interface, and the secondary and tertiary storage structures. The first two parts were covered in Section 3.3; this section addresses the third. Secondary storage structure topics include the physical structure of disks, disk-scheduling algorithms, disk management (disk formatting, boot block, and bad blocks), and swap-space management. Section 3.4 also introduces RAID structure, stable-storage, and tertiary storage structure.

#### Learning Outcomes

After you have completed Section 3.4, you should be able to

1. describe overall disk structure.
2. explain and compare several algorithms for scheduling disk requests,
 including FCFS, SSTF, SCAN, C-SCAN, and LOOK.
3. describe issues related to disk management such as disk
 initialization, booting from disk, and bad-block recovery.
4. describe swap-space management, disk reliability, RAID structure,
 and tertiary storage structures.

#### Reading Assignment

- *Operating system concepts* (9th ed.): Chapter 10: Mass-Storage
 Structure: 10.1 to 10.9.

As you do the assigned reading, focus on the Key Concepts and Topics outlined below to ensure that you can meet Learning Outcomes 1-4 above.

#### Key Concepts and Topics

- magnetic disk and tape
- logical block
- constant linear velocity (CLV)
- constant angular velocity (CAV)
- host-attached and network-attached storage
- SCSI
- fiber channel (FC)
- storage-area network
- disk scheduling
- seek time
- rotational latency
- bandwidth
- first-come, first-served (FCFS)
- shortest-seek-time-first (SSTF)
- scan scheduling (SCAN) or elevator algorithm
- circular SCAN (C-SCAN)
- look scheduling (LOOK)
- disk formatting
- logical formatting
- physical formatting
- boot block
- master boot record (MBR)
- bad blocks
- swap-space management
- redundant arrays of independent disks (RAIDs)
- data striping
- bit-level striping
- block-level striping
- RAID levels
- stable-storage implementation
- tertiary-storage structure
- removable media

#### Study Questions

1. What is disk attachment? Name several kinds of disk attachment,
 outline their differences, and outline their differences
 in usability.
2. What are the main disk scheduling algorithms, and how do they work?
3. What are the main tasks in disk management?
4. What are RAID levels, and how does one determine which level to use
 for a specific computer system?
5. What technologies are used in new tertiary storage devices?

#### Learning Activities

- Try Practice Exercises 10.1 to 10.7 of *OSC9ed*. You may check the
 answers to these questions at Operating System Concepts (9th ed.):
 [Solutions to Practice
 Exercises](http://bcs.wiley.com/he-bcs/Books?action=resource&bcsId=7887&itemId=1118063333&resourceId=33732).
- Try Exercises 10.11, 10.13, and 10.17 of *OSC9ed*.
- Download and review the [PowerPoint
 slides](http://bcs.wiley.com/he-bcs/Books?action=resource&bcsId=7887&itemId=1118063333&resourceId=33777)
 or pdf for Chapter 12 of *OSC9ed*.

### 3.5 I/O Systems

#### Overview

Input-output (I/O) is one of the two main jobs of a computer (the other is processing/computing). This section briefly introduces I/O systems, including I/O hardware, services, and interfaces. It covers some concepts that are basic to computer systems such as bus structure, device drivers, direct memory access (DMA), kernel I/O subsystems, and I/O performance issues.

#### Learning Outcomes

After you have completed Section 3.5, you should be able to

1. describe (briefly) I/O hardware components and mechanisms such as
 bus, interrupt-driven I/O cycles, and DMA.
2. outline and describe the main functions of the kernel I/O subsystem.
3. briefly explain how I/O requests are transformed to
 hardware operations.

#### Reading Assignment

- *Operating system concepts* (9th ed.): Chapter 13: I/O Systems: 13.1
 to 13.7.

As you do the assigned reading, focus on the Key Concepts and Topics outlined below to ensure that you can meet Learning Outcomes 1-3 above.

#### Key Concepts and Topics

- device drivers
- bus structure
- memory-mapped I/O
- registers for I/O ports
- busy-waiting or polling
- interrupt-driven I/O
- programmed I/O (PIO)
- DMA
- block and character devices
- blocking and nonblocking I/O
- kernel I/O subsystem
    - I/O scheduling
    - buffering
    - caching
    - spooling

#### Study Questions

1. How are data transferred between an I/O device and memory?
2. What is DMA, and why do we need it as an alternative to standard
 memory access systems such as programmed I/O?
3. What is the purpose of device drivers in operating systems?
4. What are the main tasks of the kernel I/O subsystem?

#### Learning Activities

- Complete Practice Exercises 13.1 to 13.6 of *OSC9ed*. You may check
 the answers to these questions at Operating System Concepts (9th
 ed.): [Solutions to Practice
 Exercises](http://bcs.wiley.com/he-bcs/Books?action=resource&bcsId=7887&itemId=1118063333&resourceId=33732).
- Try Exercises 13.9, 13.10, and 13.12 of *OSC9ed*.
- Download and review the [PowerPoint
 slides](http://bcs.wiley.com/he-bcs/Books?action=resource&bcsId=7887&itemId=1118063333&resourceId=33777)
 or pdf for Chapter 13 of *OSC9ed*.

### Supplementary Unit Activities

- Explore surveys and technical documents about the memory,
 file-system, mass-storage and I/O subsystems. Try to identify an
 existing problem of interest and a possible solution to it (you may
 continue this work in the following units until you find a suitable
 topic for Assignment 4 of this course).
- You may also explore Linux kernel to see what features it provides
 for file-system interface and implementation, storage management,
 and I/O systems. Share your findings and opinions with your
 classmates and tutor on the course discussion forum.


## Assignment 3

You should submit this assignment after you have finished Unit 3. It is worth 10% of your final grade.

Instructions: Please answer the following questions in complete sentences. Your answer for each question should be about 150 words. (100 marks total)

1. What are the advantages of using dynamic loading? (6 marks)
1. Explain the basic method for implementing paging. (8 marks)
1. Briefly describe the segmentation memory management scheme. How does it differ from the paging memory management scheme in terms of the user’s view of memory? (8 marks)
1. Explain the distinction between a demand-paging system and a paging system with swapping. (8 marks)
1. How does the second-chance algorithm for page replacement differ from the FIFO page replacement algorithm? (8 marks)
1. Explain how copy-on-write operates. (8 marks)
1. If you were creating an operating system to handle files, what are the six basic file operations that you should implement? (8 marks)
1. To create a new file, an application program calls on the logical file system. Describe the steps the logical file system takes to create a file. (8 marks)
1. How is a hash table superior to a simple linear list structure? What issue must be handled by hash table implementation? (8 marks)
1. What are the factors influencing the selection of a disk-scheduling algorithm? (8 marks)
1. Explain the disadvantage(s) of the SSTF scheduling algorithm. (8 marks)
1. Explain the concepts of a bus and a daisy chain. Indicate how these concepts are related. (8 marks)
1. What are the three reasons that buffering is performed? (6 marks)

## Unit 4: Protection and Security
Protection and security issues covered in Unit 4 include access matrix and its implementations, authentication, viruses (and other intruders), and encryption.

### Unit Overview

Protection and security have become major issues influencing the advancement of computing and information systems in the last two decades, especially for network and operating systems. Protection and security have become a necessary part of modern operating systems. Unit
4 provides a brief introduction to these related issues. The learning activities in this unit consist primarily of readings.

Unit 4 is divided into two sections:

**4.1 Protection**

**4.2 Security**

### Learning Objectives

When you complete Unit 4, you will be able to explain the nature of protection and security problems of operating systems, and discuss the protection features that are built into operating systems and supporting hardware to enhance security. You will also be able to describe the main mechanisms used to ensure security, such as cryptography, encryption/decryption, and authentication.

### 4.1 Protection

#### Overview

Computer systems contain many objects that need to be protected from misuse. Protection refers to mechanisms for controlling access to objects such as programs, processes, data, and files. *Protection* can be regarded as internal security, whereas *security* (discussed in Section 4.2) is external. This section discusses the goals and principles of protection, and introduces several mechanisms such as access matrix, capability-based protection, and language-based protection.

#### Learning Outcomes

After you have completed Section 4.1, you should be able to

1. explain the nature of policies, mechanisms, and domains of
 protection, and discuss the alternatives for the representation of
 an access matrix.
2. explain revocation of access rights.
3. outline the main features, advantages, and disadvantages of
 language-based protection.
4. discuss protection implementation, using an example such as UNIX,
 Cambridge CAP, Hydra, or Java.

#### Reading Assignment

- *Operating system concepts* (9th ed.): Chapter 14: Protection: 14.1
 to 14.9.

As you do the assigned reading, focus on the Key Concepts and Topics outlined below to ensure that you can meet Learning Outcomes 1-4 above.

#### Key Concepts and Topics

- protection policies and mechanisms
- protection domain
- domain switching
- access matrix
- access list
- capability list
- lock-key scheme
- access control
- capacity-based protection
- language-based protection

#### Study Questions

1. Why is it important to distinguish between mechanisms and policies
 of protection?
2. What are the differences between capacity-based protection and
 language-based protection?
3. What is *access matrix*, and how is it implemented?

#### Learning Activities

- Try Practice Exercises 14.1 and 14.5 to 14.10 of *OSC9ed*. You may
 check the answers to these questions at Operating System Concepts
 (9th ed.): [Solutions to Practice
 Exercises](http://bcs.wiley.com/he-bcs/Books?action=resource&bcsId=7887&itemId=1118063333&resourceId=33732).
- Download and review the [PowerPoint
 slides](http://bcs.wiley.com/he-bcs/Books?action=resource&bcsId=7887&itemId=1118063333&resourceId=33777)
 or pdf for Chapter 14 of *OSC9ed*.

### 4.2 Security

#### Overview

Security is a much broader topic than protection. Security requires not only an adequate protection system but also consideration of the external environment within which the system operates. Security measures aim to safeguard computer systems against unauthorized access by intruders, against malicious destruction, and against accidental inconsistency.

#### Learning Outcomes

After you have completed Section 4.2, you should be able to

1. discuss security threats and attacks (viruses, Trojan horses, trap
 doors, worms, human intruders, etc.).
2. explain the fundamentals of cryptography, encryption/decryption, and
 authentication; and examine their uses for security purposes.
3. outline some of the physical and human security issues that are
 external to operating systems.

#### Reading Assignment

- *Operating system concepts* (9th ed.): Chapter 15: Security: 15.1
 to 15.9.

As you do the assigned reading, focus on the Key Concepts and Topics outlined below to ensure that you can meet Learning Outcomes 1-3 above.

#### Key Concepts and Topics

- denial-of-service (DOS)
- replay attack
- man-in-the-middle attack
- session hijacking
- phishing
- dumpster diving
- back-door demon
- Trojan horse
- spyware
- covert channels
- trap door
- logic bomb
- virus
- worm
- zombie system
- distributed DOS
- cryptography
- decryption
- encryption
- symmetric encryption
    - data encryption standard (DES)
    - advanced encryption standard (AES)
- asymmetric encryption
    - RSA (Rivest, Shamir, and Adleman)
    - public key
    - private key
- authentication
- message-authentication code (MAC)
- digital-signature
- digital certificate
- certificate authorities
- SSL
- session key
- user authentication
- security through obscurity
- auditing, accounting, and logging
- computer-security classification

#### Study Questions

1. What are the common program threats, and how can people protect
 computer systems from these threats?
2. How can symmetric encryption and asymmetric encryption help in
 authentication?
3. What are the user authentication methods, and how are they
 effective?

#### Learning Activities

- Try Exercises 15.2, 15.4, and 15.9 to 15.14 of *OSC9ed*.
- Download and review the [PowerPoint
 slides](http://bcs.wiley.com/he-bcs/Books?action=resource&bcsId=7887&itemId=1118063333&resourceId=33777)
 or pdf for Chapter 15 of *OSC9ed*.

### Supplementary Unit Activities

- Explore surveys and technical documents about the protection and
 security that an operating system provides. Try to identify an
 existing problem of interest and a possible solution to it. Check to
 see whether this may be a suitable topic for Assignment 4 of
 this course.
- You may also explore Linux kernel to see what protection and
 security features are provided and how they are realized. Share your
 findings and opinions with your classmates and tutor on the course
 discussion forum.

## Unit 5: Distributed, Real-Time, and Multimedia Systems
Unit 5 reviews distributed systems and special-purpose operating systems, such as real-time systems, embedded systems, mobile systems, and multimedia systems. This unit serves as an extension to the core topics of the course.

### Unit Overview

Unit 5 provides an extension to the core topics of operating systems. It introduces distributed systems and special-purpose operating systems such as real-time systems and multimedia systems. This extension introduces the ever-changing information technologies and products in which operating systems play an important role. In fact, with many operating systems, different versions are developed for different computing environments to meet the needs of different applications. For instance, both Linux and Windows have desktop, server, mobile, and embedded system versions for different devices and applications.
**Note:** The learning activities in this unit consist primarily of readings.

Unit 5 is divided into two sections:

**5.1 Distributed Systems Overview**

**5.2 Virtual Machines**

### Learning Objectives

When you complete Unit 5, you will be able to define the terms
*distributed operating system*, *distributed file system* (DFS), and
*real-time computer system*. You will move on to describe the general structure of distributed systems and the way in which real-time operating systems must be constructed to meet stringent timing requirements. Finally, you will be able to identify the characteristics of multimedia data and indicate how multimedia operating systems can meet the requirements of continuous-media data.

### 5.1 Distributed Systems Overview

#### Overview

This section briefly introduces distributed systems and discusses the general structures and interconnections in a distributed system. This section also discusses concepts directly related to distributed operation systems, such as distributed file systems (DFS).

#### Learning Outcomes

After you have completed Section 5.1, you should be able to

1. describe the overall structure of distributed systems.
2. discuss communications in a distributed system.
3. outline the particulars of a distributed file system.

#### Reading Assignment

- *Operating system concepts* (9th ed.): Chapter 17:
 Distributed System.

As you do the assigned reading, focus on the Key Concepts and Topics outlined below to ensure that you can meet Learning Outcomes 1-3 above.

#### Key Concepts and Topics

- distributed system
- network operating system
- distributed operating system
    - data migration
    - computation migration
    - process migration
    - network structure
- communication structure
    - naming
    - name resolution
    - routing
    - connection
    - contention
    - communication protocols
- distributed file system (DFS)
- naming structures
- name scheme
- remote file access
- file replication

#### Study Questions

1. What is a distributed operating system, and what are the main tasks
 that a distributed system supports?
2. What is a distributed file system, and what are the naming schemes
 of DFS?

#### Learning Activities

- Download and review the [PowerPoint
 slides](http://bcs.wiley.com/he-bcs/Books?action=resource&bcsId=7887&itemId=1118063333&resourceId=33777)
 or pdf for Chapter 17 of *OSC9ed*.

### 5.2 Virtual Machines

#### Overview

This section covers types of virtual systems, and differences in purpose and implementation. It is not that important to go into details of memory management and tables, as much as knowing general configurations and structure.

#### Learning Outcomes

After you have completed Section 5.2, you should be able to

1. describe various virtual machines technologies.
2. describe methods used to implement virtualization.
3. list the most common hardware features that support virtualization.

#### Reading Assignment

- *Operating System Concepts* (9th ed.): Chapter 16: Virtual Machines.

As you do the assigned reading, focus on the Key Concepts and Topics outlined below to ensure that you can meet Learning Outcomes 1-3 above.

#### Key Concepts and Topics

- virtual machines
- virtual machine manager (VMM)
- hypervisor
- Paravirtualization
- Emulators
- Disk partitioning
- Xen
- VMware
- Live migration
- Cloud computing
- Virtual CPU (VCPU)
- Page tables
- Virtual machine control structure
- Control partition
- Java virtual machine (JVM)
- Memory overcommitment
- Network address translation (NAT)
- Bytecode
- Garbage collection

#### Study Questions

1. What are the three types of traditional virtualization?
2. What are four benefits of virtualization?

#### Learning Activities

- Find some articles and technical documents on modern
 virtual machines. Explain the reason behind the recent success of
 virtual machines, although they have been around for a long time.
 What forms of virtualizations are expected in the future?
- Download and review the [PowerPoint
 slides](http://bcs.wiley.com/he-bcs/Books?action=resource&bcsId=7887&itemId=1118063333&resourceId=33777)
 or pdf for Chapter 16 of *OSC9ed*.

### Supplementary Unit Activities

- Explore surveys and technical documents about distributed operating
 systems, and virtual machines. Try to identify an existing problem
 of interest and a possible solution to it. You may consider this
 problem for Assignment 4 of the course.
- Share your findings and opinions with your classmates and tutor on
 the course discussion forum.

## Assignment 4

This assignment should be submitted after you have finished Unit 5. It is worth 15% of your final grade for this course.

### Part 1: Concepts (20 marks; 4 marks each)

Please answer the following questions in complete sentences. Your answer for each question should be about 150 words.

1. Why is it important to distinguish between mechanisms of protection and policies of protection?
1. What is an access matrix, and how can it be implemented?
1. How does a virus differ from a worm?
1. What is the difference between symmetric encryption and asymmetric encryption?
1. What are the two main varieties of authentication algorithms?

### Part 2: Research Project (80 marks)

In Part 2, you will investigate technical problems of operating systems, and provide a written report. Your research should focus on an in-depth topic about theories, algorithms, approaches, mechanisms, or implementation of one of the following fields of operating systems:

- process management
    - process and thread
    - CPU scheduling
    - synchronization
    - deadlock handling
- storage management
    - main memory
    - virtual memory
    - file systems
    - mass-storage and I/O
- protection and security
- distributed, real-time, and multimedia systems

Your topic could come from a sub-problem of cutting-edge research problems discussed in the literature (i.e., investigating a technical problem).

If you have trouble deciding what topic to work on, contact your tutor, who can advise you on the suitability of the topic and/or suggest modifications. Note that topic selection is part of your assignment requirements for this project, so you cannot rely on your tutor to assign a topic.

To ensure that your topic has adequate depth and coverage, you MUST write a one-page proposal that outlines your area of interest and associated references you will use. Send it to your tutor for consideration before you begin your project work, preferably allowing at least two weeks for consultation.

In your paper (expectations outlined below), make sure you highlight your work and outcomes in your own words. You must also properly cite any viewpoints, methods, algorithms, data, results, figures, tables, etc. that you borrow from other papers or contributors that you discuss or include in your paper/report. All references cited should be published, or at least be publicly available, stable, and accessible online (referenced in APA or IEEE Style). Using the work of others without proper credit in your paper/report may lead to a form of plagiarism, which is not tolerated in AU courses. Please review the Student Academic Misconduct Policy for more details.

#### Research Paper Your investigation will be based on recent publications (i.e., published in the past five years) such as journal/conference papers and technical documents, and the applicable software packages (open source preferred). You are encouraged to read some papers about new techniques in operating systems. You can access the following resources via the ACM Digital Library and IEEE/IEE Electronic Library databases in the Athabasca University Library.

SOSP: ACM Symposium on Operating Systems Principles (ACM) ACM SIGOPS Operating Systems Review (ACM) ACM Transactions on Computer Systems (ACM) IEEE Transactions on Computers (IEEE) ACM Computing Surveys (ACM) Communications of the ACM (ACM) IEEE Computer. . . (IEEE) Linux Journal (ACM)

Once you have chosen your topic, you need to identify meaningful, feasible outcomes for your research on the topic. Overall, the outcomes should interest and benefit the professional community of operating system research and development. Some possible outcomes:

- analysis, findings, and discovery of problems.
- results of your tests, surveys, and comparative analysis.
- proposals for new or improved methods, algorithms, etc.
- meaningful implementation plans.
- insight on future directions.

Present the outcomes of your research in a 10- to 15-page paper written in a journal or conference paper format. References should be cited using APA or IEEE Style. Your paper should include the following sections:

- Title
- Abstract: no more than 300 words.
- Introduction/background: motivation for research and introduction to the outcomes, including a literature review and reference citations.
- Methods: describe the problem and the methods you used to explore or address the problem.
- Results and findings: research results or exploration findings, including theoretical analysis and any experimental and implementation results you accomplished based on your methods.
- Related work: summarize related work by others; compare your methods and results with others’ work. Cite your references.
- Conclusion and future work: conclude your exploration and research, and suggest possible future work on the topic.
- References: include all references cited in your paper, using APA or IEEE Style.
- Appendix: Includes a list of your data, design/implementation, and source codes (as applicable), and software necessary for running your programs (if applicable). The Appendix isn’t part of the page count for your paper.

## Final Exam

The final examination for COMP 314 will be a closed-book invigilated online exam. You have three (3) hours to complete the examination. The questions will cover Unit 1-4 of the course, and may relate to any of your assignments.

Please consult the Online Exams (MuchLearning) section of the Procedures for Applying for and Writing Examinations in your online Student Manual, and visit http://registrar.athabascau.ca/exams/online/student/ for more information.

You are not allowed to use the textbook nor published articles in the examination. The use of a calculator is permitted, but computers such as laptops and hand-held computers are not allowed.

The examination will be in three parts (total 100%), as follows:

- Part I (30%): four (4) short-answer or calculation questions (to be answered in about 150 words each) about essential concepts, principles, and methods.
- Part II (60%): thirty (30) multiple-choice questions.
- Part III (10%): related to your research and/or programming project work for Assignment 4. Please ensure that you have submitted this assignment prior to writing the final exam.

If you are unsure about an answer, please write whatever you know about the question rather than leaving it unanswered. Include any assumptions you are making when answering the questions.
