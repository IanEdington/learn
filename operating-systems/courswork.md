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
    Many ways to structure OS like any Software. 
    - kernel
        - The software that is always running on the computer. The minimum required in order to start an OS.
    - layered approach
        each layer adds more functionality.
        Positive: one way dependency means easy to design and debug.
        Negavite: increases distance of path through kernel by forcing function calls all the way down the layers.
            limits the ability for layers to interact in a potentially useful way.
    - micro kernel approach
        very small basic kernel with almost everything pushed into userspace. Most things are accomplished using message passing. 
        positive: small footprint, simple to reason about and debug, 
        Negative: too simple and causes inefficiency because of increased function calls.
        - mach
    - modular kernels
        monolithic kernel with interchangeable parts
        positive: dynamic loading of modules allows greater hardware flexibility
            modular design allows for boundaries to be well defined and decreases cognitive load while working
        negative: higher cognitive load than Micro or layered kernel
        IMO this is the way forward. Good balance of cognitive load vs flexibility
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
    > in order to protect the system from bad code
3. How are user mode and kernel mode issues dealt with under a virtual machine environment?
    > no idea

#### Learning Activities

- [x] Complete Exercises of *OSC9ed*:
    - 2.20: It is sometimes difficult to achieve a layered approach if two components of the operating system are dependent on each other. Identify a scenario in which it is unclear how to layer two system components that require tight coupling of their functionalities.
        > CPU scheduling and Memory Management: Complex schedulers often need to use memory for optimization. Memory Management depends on CPU scheduling to be effective.
    - 2.21: What is the main advantage of the microkernel approach to system design? How do user programs and system services interact in a microkernel architecture? What are the disadvantages of using the microkernel approach?
        > small, simple, secure, most things run in user space. Can become very complex and non performant when system grows due to complex interactions.
    - 2.22: What are the advantages of using loadable kernel modules?
        > flexibility, size of core kernel is smaller than monolith. Ability to load needed drivers/section on demand rather than as part of kernel.
    - 2.24: Explain why Java programs running on Android systems do not use the standard Java API and virtual machine.
        > Android runs a Java Interpreter instead of a VM in order to decrease resource demand. the Android API is used for legal reasons but also allows it's supposed to be more performant with low resources.
    - 2.25: The experimental Synthesis operating system has an assembler incor- porated in the kernel. To optimize system-call performance, the kernel assembles routines within kernel space to minimize the path that the system call must take through the kernel. This approach is the antithesis of the layered approach, in which the path through the kernel is extended to make building the operating system easier. Discuss the pros and cons of the Synthesis approach to kernel design and system-performance optimization.
        > downside: more complex OS, upside: faster runtimes for all programs

### 1.5 Operating System Structures
OSC9ed: 2.6, 2.9, 2.10, 2.11

#### Learning Outcomes

- explain the system boot function of operating systems.
- system boot
- operating system generation

#### Key Concepts and Topics

- operating-system design:
    separating mechanism from policy makes it possible to make modular kernel where different sections can be swapped out so long as the policy's (interface) between sections is consistent. This design pattern is an example of a modular system.
    - goals: always tricky to define for a system with many optimization points. What is the right balance of priorities in order to best service a customer.
    - policies: what to do
    - mechanisms: how to do it
- operating-system implementation: language issue
    - made in many languages both interpreted and compiled
- operating-system debugging
    - dumps core to a special area on disk for later inspection
    - dstats: a program for hooking into current kernel and user programs running through interrupt calls in order to get a better view of what's happening at any moment during execution.
    - debugger
    - core dump
    - crash dump
- operating-system performance tuning
    - profiling
- operating-system generation
- system boot
    a sequence of loaders are executed everytime a computer powers on, with the purpose of finding and executing the OS. This sequence varies by machine but often involves ROM or EEPROM, a boot loader on disk, and finally the OS.
    - boot block
    - GRUB

#### Study Questions

1. What is the reason (besides a few core codes programmed by assembly) for using high level language in OS design?
    > easier to program and maintain. More cross platform.
2. Why is operating-system generation and booting needed in most operating systems? What is the two-step process for system boot?
    > different systems have different components and an OS is only useful for a single system without this 2 step process. The OS first determines which functions it will need in order to interface with the CPU devices, memory, IO, ect. Maps those functions to the sys-calls, and then starts the OS.

#### Learning Activities

- Complete Practice Exercises of *OSC9ed*.
    - 2.1: What is the purpose of system calls?
        > interface between OS and user space.
    - 2.11: How could a system be designed to allow a choice of operating systems from which to boot? What would the bootstrap program need to do?
        > a bootstrap would need to have pointers to the OS locations of multiple OS's and would have to give the option of which OS to point to.
    - 2.19: Why is the separation of mechanism and policy desirable?
        > makes it easier to change the system in the future. Same reason OOP information hiding is important.
    - 2.23: How are iOS and Android similar? How are they different?
        > both optimized for low power devices with paired down functionality and increased special use IO devices.
        > iOS is a layered system with a micro-kernel on the bottom layer.
        > linux base with runtimes and libries built on top of it.

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
    - process
    - process states
    - process scheduling
2. outline the differences between processes and programs.
    - process vs program
3. describe how the states of processes change during their execution.
4. explain how process control block (PCB) is used during central processing unit (CPU) switches from process to process.
    - what is the PCB: 
    - how is it used?: 
5. describe the queuing diagram representation of process scheduling.
6. explain how processes are created and terminated, and how to apply them in multi-process programming in Linux or Windows operating systems.
    How are processes created and terminated?
    How do you apply processes in multi-process programming?

#### Key Concepts and Topics

- process
    - a running instance of a program
- process states
    - new: is in the process of being allocated
    - ready: is ready to execute
    - running: in the process of executing
    - waiting: is in a queue waiting for IO or time
    - terminated: finished execution ready to be deallocated
- process control block
    - a section of OS memory where the process state and other info is kept.
        - Process state: The state may be new, ready, running, waiting, halted, and so on.
        - Program counter: The counter indicates the address of the next instruction to be executed for this process.
        - CPU registers: The registers vary in number and type, depending on the computer architecture. They include accumulators, index registers, stack pointers, and general-purpose registers, plus any condition-code information. Along with the program counter, this state information must be saved when an interrupt occurs, to allow the process to be continued correctly afterward (Figure 3.4).
        - CPU-scheduling information: This information includes a process priority, pointers to scheduling queues, and any other scheduling parameters. (Chapter 6 describes process scheduling.)
        - Memory-management information: This information may include such items as the value of the base and limit registers and the page tables, or the segment tables, depending on the memory system used by the operating system (Chapter 8).
        - Accounting information: This information includes the amount of CPU and real time used, time limits, account numbers, job or process numbers, and so on.
        - I/O status information: This information includes the list of I/O devices allocated to the process, a list of open files, and so on.
- process scheduling
    - the process that decides which process to run when
- process scheduler
    - job scheduler, or long-term scheduler
        - which processes to run
    - CPU scheduler, or short-term scheduler
        - which of the running process to allocate CPU time to.
    - medium-term scheduler
        - when memory gets low, what process can be put on ice for a bit (moved to disk storage)
- swapping
    - the processes of pausing a process when resources are limited
    - copying the PCB to disk
    - restoring the PCB when resources free up.
- context switch
    - changing from one executing process to another. For most systems this means copying the saved registers and program counter into the CPU and starting execution where it left off.
- scheduling queues
    - job queue: all processes in the system
    - ready queue: processes currently in main memory that are ready to execute
    - device queue: each device can only be used by one process at a time. The device queue allows additional processes to wait for an IO device.
- degree of multiprogramming
    - the number of concurrently executing processes allowed to run on a system
    - on user systems this is often a function of how much main memory exists.
    - other systems may have more advanced queueing methods such as 
- process creation
    - fork creates a new process
    - forking then forking then exiting the first fork leave the grandchild process orphaned and init becomes it's parrent
- fork ()
    - creates a child process
- process termination
    - exit(status) exits the program with the status.

#### Study Questions

1. What are the main features of processes?
2. What information is included in PCB?
    - program counter
    - registers
    - list of files
3. What data structures are involved in process scheduling?
    - queue's and DLLists
4. What is the rationale for each kind of scheduler:
    - long-term: from the job queue, decides when to admit a new processes
    - short-term: from the ready queue, decides which processes to execute
    - medium-term: when resources are low/high, decides which process to swap from the ready queue
5. How do you use fork() to create a process?
- assign the return value of fork to a PID variable. Fork copies the running program and continues execution for both programs after returning from fork. If the return value is 0 you are in the new 'child' process. If it's greater than 0 you are in the original process. If it's less than 0, fork failed to create a new process and you are in the original process.

#### Learning Activities

- Try Exercises of *OSC9ed*.
    - 3.1 Using the program shown in Figure 3.30, explain what the output will be at LINE A.
        > 5 because the operation that adds only happens in the fork, therefore not affecting the original.
    - 3.2 Including the initial parent process, how many processes are created by the program shown in Figure 3.31?
        > 8
    - 3.3 Original versions of Apple’s mobile iOS operating system provided no means of concurrent processing. Discuss three major complications that concurrent processing adds to an operating system.
        > battery drain
        > context switching
        > make sure programs can't mess with other programs memory
        > others?
    - 3.4 The Sun UltraSPARC processor has multiple register sets. Describe what happens when a context switch occurs if the new context is already loaded into one of the register sets. What happens if the new context is in memory rather than in a register set and all the register sets are in use?
        > instead of copying the PCB from memory into the registers, the process simply continues where it left off.
    - 3.5 When a process creates a new process using the fork() operation, which of the following states is shared between the parent process and the child process?
        > only shared memory segments
        a. Stack
        b. Heap
        c. Shared memory segments

### 2.1.2 Processes
OSC9ed: 3.4 to 3.6.

7. define *interprocess communication* (IPC).
8. explain the foundational functions behind the two models of interprocess communication (IPC): shared-memory and message passing.
9. explain how shared-memory and message passing functions are realized in real systems such as POSIX and Windows.
10. explain the mechanisms of communication in client-server systems, including sockets, remote procedure calls (RPC), pipes, and named pipes.
11. apply IPC and client-server communication API in system programming.

#### Key Concepts and Topics

- process cooperation
    - processes able to share data and cooperate on a task together
    - independent process is one that can not be affected by another process.
- interprocess communication (IPC)
    - shared-memory: two or more processes use system calls to establish a shared piece of memory. Once memory is shared one can write and the others can read.
    - message passing: use system calls to pass messages either directly or indirectly.
- producer-consumer problem
- bounded and unbounded buffer
- direct and indirect communication
    - passing messages directly between processes
    - passing messages to a mailbox where other processes can attach to to get messages.
- naming
    - used in direct communication methods.
    - Either the sender names the receiver, or both name eachother.
    - This is a difficult way to manage messaging because the values are hard-coded and inflexible
- mailbox or port
    - used in indirect messaging
    - processes attach to a mailbox and either receive or send messages to it.
    - This results in more flexible coding conditions.
    - mailboxes can either be owned by the OS or by a process
    - may options in terms of
        - how many processes can attach
        - which processes receive which messages
- synchronous vs asynchronous sending and receiving
    - blocking send: sending processes is blocked until message is received (by mailbox or process)
    - non-blocking send: sending process is not blocked
    - blocking receive: receiving process is blocked until message is received from process or mailbox
    - non-blocking receive: call to get message returns the message if it's available or null if it isn't
- buffering
    - zero capacity: sender blocks until receiver is ready
    - bounded capacity: sender blocks when buffer is full
    - unbounded capacity: sender never blocks
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
    - Sharing information between users: concurrent access to a file.
    - Parallel computation on single hunk of data
    - Reduce cognitive load through modularity sometimes requires multiple parts.
2. What is the difference between IPC and RPC?
    inteprocess communication: is the overarching idea of all communication between processes in systems
    remote procedure call: specific type of structured communication using ports
3. How are shared memory, message passing, RPC, sockets, and pipes implemented practically in systems such as POSIX, Mach, and Windows?
    - POSIX:
        - shared memory
        Open (process 1):
            - shm_open: open a shared memory by name set permissions
            - ftruncate: set the size
            - mmap: attaches the file to the memory space of the program
        Open (process 2):
            - shm_unlink: destroy shared memory 
        - message passing
        - RPC
        - sockets
        - pipes
    - Mach:
        - shared memory
        - message passing
            > a FIFO queue in the OS collects messages
            > systems calls are performed using the kernel queue and notifications are received from the notification queue.
        - RPC
            > same as the message passing only with special call to allow for inter system communication
        - sockets
        - pipes
    - Windows:
        - advanced local procedure call
            > RPC for local calls, and local calls are executed using this
        - shared memory
        - message passing
        - RPC
        - sockets
        - pipes

#### Learning Activities

- Try Exercises of *OSC9ed*.
    - 3.6: Consider the "exactly once" semantic with respect to the RPC mechanism. Does the algorithm for implementing this semantic execute correctly even if the ACK message sent back to the client is lost due to a network problem? Describe the sequence of messages, and discuss whether “exactly once” is still preserved.
        > yes.
        > - On the client machine the call is sent and the process waits.
        > - On the server the cache is checked to see if this call has been processed, the call is processed, the ACK is returned, and the call and return are cached.
        > - the ACK is lost
        > - after a given amount of time the client sends the call again, the server looks in the cache and find the call and returns the return.
    - 3.7 Assume that a distributed system is susceptible to server failure. What mechanisms would be required to guarantee the “exactly once” semantic for execution of RPCs?
        > Keep a redundant copy of the RPC cache (either on disk or a NAS.
    - 3.8 Describe the differences among short-term, medium-term, and long- term scheduling.
        > short term: what process to give to the CPU
        > medium-term: if your running out of memory, what process should you pause (swap to disk)
        > long-term: most useful for large batch systems, what processes you should let execute on the system.
    - 3.9 Describe the actions taken by a kernel to context-switch between processes.
        > Process 1 is stopped, Process 1 Control Block is updated, Process 2 CPU registers and cache uploaded from PCB, Process 2 starts.
        > all of this is overhead
    - 3.11 Explain the role of the init process on UNIX and Linux systems in regard to process termination.
    > when a process terminates and it's parent process hasn't called wait() yet, it stops executing and it's resources are released but it stays in the process table because it contains the process status. If the parent process never calls wait and exits. This process is 'orphaned' and becomes the child process of the init process. When that child exits it will stay in the process table until wait is called by the init process. In order for all these zombie processes to be removed the init process periodically calls wait().

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
    - one execution path in a process - each process can have more than one thread, code, data, and files are shared between all threads in a process.
- multithreaded programming
    - when one program has more than one thread of control. This allows the process to make progress even if one thread is waiting.
- multithreaded process and single-threaded process
- multicore programming
    - when a process is running on multiple cores. This allows multiple threads from the same process to run in parallel.
- multithreading models
    - many-to-one model: many user-space threads to one kernel thread. Limited to using one core.
    - one-to-one model: many user-space threads each with it's own kernel thread. Limited by number of kernel threads.
    - many-to-many model: many user-space threads run by an equal or smaller number of kernel space threads. Not limited by either of these issues, but has extra overhead in maintaining structure. User-space scheduling of threads is required.
    - two-level model: many-to-many with optional one-to-one: best of both worlds.
- user threads: managed by a thread library in user space designed to manage all aspects of the threads.
- kernel threads: uses the threads built into the kernel thread library.
- thread libraries
    - Pthreads: POSIX Threads - a standard implemented by many unix linux systems. There are even windows implementations.
    - Java threads: thread library for java
    - Windows threads:
Main issues with Threading
    - signal handling: How do you handle synchronous and asynchronous signals?
        - synchronous need to get back to the thread who initiated them, and be handled appropriately.
        - for asynchronous there is usually a default signal handler that responds to them but custom handling must be possible in order to customize how an application reacts to external input.
    - thread cancellation: what is the right strategy for canceling a thread?
        - one asynchronous input that needs to be handled by almost every program is how to cancel a thread.
        - a thread that isn't given the chance to exit properly might have resources left behind. Although the local thread resources are freed by the system, any locks, files, half written shared data, ect. is left in a broken state. For this reason most systems suggest using a method of interupting the process that gives it a chance to finish what it's doing and clean up after itself.
        - in Java this is a try finally clause, or checking an interrupt flag
        - in PThreads this is `pthread_cancel()` it sets a flag that the thread can then check using `pthread_testcancel()` at a stable point and perform cleanup.
- thread pool
- scheduler activations
    - lightweight process (LWP) a shell around a kernel thread in order for user threads to be implemented on top of
    - usually used in many-to-many and two-level models
    - uses a light weight process as a helper between the user thread and the kernel thread.
    - an LWP is needed for each blocking system call(wait or I/O) + the number of processors.
- thread-specific data: local storage for a thread. This is often used when data can be reused on a thread by thread basis but could be corrupted as a global variable. Local working storage usable across functions in a thread.
- fork(), exec(), and clone()
    - fork() does it for the entire process including threads or just the specific thread. Does it 
    - exec() always replaces the entire program including all threads.
    - clone() creates new thread (task) that contains pointers to whatever is wanted from the original task. This gives fine grain control over what is shared and what isn't shared between processes/threads.
- threads implementation in operating systems
    - Linux threads: Processes and kernel threads are the same thing in Linux. They are both just tasks. A task is a structure which contains a link to a separate structure for File-system information, memory space, Signal handlers, and open files. When creating a new task any of these elements can be shared.
        - fork creates a new task with all of these things copied
        - clone(CLONE FS, CLONE VM, CLONE SIGHAND, CLONE FILES) creates a new task with pointers for all of these to the original task.
    - Windows threads through the Windows API
        - 1 to 1 mapping
        - ETHREAD - executive thread block
            - pointer to the process to which the thread belongs
            - address of the routine in which the thread starts control
            - pointer to the KTHREAD
        - KTHREAD - kernel thread block
            - scheduling and synchronization information
            - CPU registers
            - kernel stack
            - pointer to the TEB
        - TEB - thread environment block (user space)
            - thread ID (thread identifier)
            - user stack
            - thread local storage (private storage)

#### Study Questions

1. What is the motivation for using multiple threads in a process?
- efficiency through parallelism: If a process with multiple threads can be run in parallel and the system has multiple cores, the threads can execute on separate cores speeding up the execution time of the process.
- responsiveness because of concurrency: if one part of the program is blocked either by IO or by CPU, the main thread can still respond to input.
2. What are the benefits of using multithreaded programming?
3. What are the differences between user-level threads and kernel-level threads?
    - user space vs kernel space
    - managed by thread libraries vs managed by the kernel
    - tend to have lower over head vs are a first class process for CPU contention
4. How do POSIX, Java, and Windows implement their thread libraries?
    POSIX is a standard with different implementation
        - pthreads_
5. How can thread libraries be used for multithreaded programming?
    - using thread calls with call backs to split into multiple parts.
    - divide based on task and data

#### Learning Activities

- Try Exercises of *OSC9ed*.
    - 4.1: Provide two programming examples in which multithreading provides better performance than a single-threaded solution.
        - a browser loading assets from a network, each asset has their own thread and when the finish loading they are applied to the DOM. Blocking IO will not affect other parts of the system form rendering.
        - a large(gigs) amount of data is summed, by breaking the problem into multiple threads each thread can do it's part of the sum and the be summed with the other threads. Multiple cores will execute this faster than a single core.
    - 4.2: What are two differences between user-level threads and kernel-level threads? Under what circumstances is one type better than the other?
        - kernel-level threads are better when waiting for interrupts, or when parallel processing. No blocking on page faults.
        - user-level threads implement threads on a system that doesn't support threads. Light overhead from context switching. Allow custom thread schedules.
    - 4.3: Describe the actions taken by a kernel to context-switch between kernel- level threads.
        - registers saved to kernel thread block 1, registers loaded from kernel thread block 2, start ktb2
    - 4.4: What resources are used when a thread is created? How do they differ from those used when a process is created?
        - register set, stack & thread priority. These are lower overhead.
    - 4.5: Assume that an operating system maps user-level threads to the kernel using the many-to-many model and that the mapping is done through LWPs. Furthermore, the system allows developers to create real-time threads for use in real-time systems. Is it necessary to bind a real-time thread to an LWP? Explain.
        - yes because they still use the LWP. The LWP will contain the scheduling information about this real-time thread.
    - 4.6: Provide two programming examples in which multithreading does not provide better performance than a single-threaded solution.
        - When a divide and conquer calculation is split up into multiple sections but run on a single processor. The overhead of thread switching is big and there is no benefit in terms of the calculation speedup.
        - 
    - 4.7 Under what circumstances does a multithreaded solution using multiple kernel threads provide better performance than a single-threaded solution on a single-processor system?
        - only when there is waiting involved either for CPU or IO.
        - especially during cache misses
    - 4.8 Which of the following components of program state are shared across threads in a multithreaded process?
        a. Register values: no
        b. Heap memory: yes
        c. Global variables: yes
        d. Stack memory: no
    - 4.9 Can a multithreaded solution using multiple user-level threads achieve better performance on a multiprocessor system than on a single-processor system? Explain.
        - no. There is no parallelism in this case because only one kernel-level thread is being used, and using multiple threads increase overhead.
    - 4.10 In Chapter 3, we discussed Google’s Chrome browser and its practice of opening each new website in a separate process. Would the same benefits have been achieved if instead Chrome had been designed to open each new website in a separate thread? Explain.
        - no. processes have their own memory, files, ect that are managed by the OS. Since each webpage is a unique entitly detatched from any other webpage, there is no benifite to using the threaded processing model, and you incure the overhead of managing the user-threads.
    - 4.11 Is it possible to have concurrency but not parallelism? Explain.
        - yes. concurrency means multiple processes are progressing together, whereas parallelism is when multiple processes are progressing at each clock cycle. The former can be accomplished on a single threaded CPU using context switching. The latter can only be accomplished on multi-processor systems.
    - 4.12 Using Amdahl’s Law, calculate the speedup gain of an application that has a 60 percent parallel component for (a) two processing cores and (b) four processing cores.
        - max theoretical: 1/0.4 = 2.5x
        - 2 cpu's: 1 / (0.4 + 0.6/2) = 1.43
        - 4 cpu's: 1 / (0.4 + 0.6/4) = 1.82
    - 4.13 Determine if the following problems exhibit task or data parallelism:
        - The multithreaded statistical program described in Exercise 4.21: task
        - The multithreaded Sudoku validator described in Project 1 in this chapter: task
        - The multithreaded sorting program described in Project 2 in this chapter: data
        - The multithreaded webserver described in Section 4.1: task
    - 4.14 A system with two dual-core processors has four processors available for scheduling. A CPU-intensive application is running on this system. All input is performed at program start-up, when a single file must be opened. Similarly, all output is performed just before the program terminates, when the program results must be written to a single file. Between startup and termination, the program is entirely CPU- bound. Your task is to improve the performance of this application by multithreading it. The application runs on a system that uses the one-to-one threading model (each user thread maps to a kernel thread).
        - How many threads will you create to perform the input and output? Explain.
            - one thread for read one for write
        - How many threads will you create for the CPU-intensive portion of the application? Explain.
            - 4 threads one for each CPU. Unless there are 4 cpu's with 2 threads per CPU .: 8 threads.
    - 4.15 Consider the following code segment:
        a. How many unique processes are created? 8
        b. How many unique threads are created? 10

        1 pid_t pid; /* 1 */
        2 pid = fork(); /* *2 */
        3 if (pid == 0) { /* child process */
        4 fork(); /* +1 */
        5 thread_create( . . .);
        6 }
        7 fork(); /* *2 */

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
    - a section or sections of code that if executed concurrently can cause unstable data
2. explain hardware and software solutions for the critical-section problem.
    - hardware: atomic operations
    - software: never work if their not built on-top of hardware solutions: spin-locks (mutex), semiphore (resource lock), Monitors, Condition
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
- binary semaphore
- counting semaphore
- spinlock: lock that is waiting using a loop
- busy waiting
- block() and wakeup(P)
    - blocks a process until another process calls wakeup with that process
- deadlocks
- starvation or indefinite blocking
- priority inversion
    - given three priority levels of execution it is possible for a situation to arise where the middle is executed before the top when the lowest holds a resource that the top needs.
        - bottom starts executing locks resource A
        - middle start executing, stops bottom
        - top starts executing, stops middle, queues for resource A
        - middle continues executing, until finished even though top still exists.
    - a common solution to this problem is for the bottom process/thread to temporarily receive the priority level of the waiting thread
- atomic transaction
- commit, abort, and roll back
- write-ahead logging
- log-based recovery
- checkpoints
- concurrent atomic transactions (transactional memory)
    - A section is declared atomic
    - a log of the variables are kept
    - at the end, all the writes are performed atomically
    - if they fail (no the expected start values) then the transaction is rolled back and the transaction starts over
- serializability
- serial schedule
- nonserial schedule
- conflicting operations
- conflict serializable
- locking protocol
- two-phase locking protocol (2PL)
- timestamp-based protocol

#### hardware solutions
    - stop processor from accepting interrupts during the critical area
        - only useful on single processor machines
    - atomic operations
        - test_and_set(&boolean) sets boolean to true, returns original value.
        - compare_and_swap(int *value, int expected, int new_value) if (value == expected) value = new_value

A simple hardware based locking solution.
- It spins.
- It doesn't provide the bounded-waiting requirement, so threads can stall.
~~~
// shared information
boolean lock = false;

// for each thread
    // lock or spin until lock is aquired
    while (test_and_set(lock));

    // execute critical section

    // unlock
    *lock = false;
~~~

A more complex hardware solution.
- It spins.
- It provide the bounded-waiting requirement since elements can't wait for longer than n threads.
- need to know the number of threads ahead of time
~~~
// shared info
int n; // number of threads
boolean lock = false;
boolean waiting[n] = false;

// for each thread
    int i; // thread identity number
    waiting[i] = true;
    key = true;

    // spin until either the lock is available or another thread unblocks my waiting flag
    while (key && waiting[i])
        key = test_and_set(&lock)

    // execute critical section

    // let the next waiting process run or release the lock
    int j = (i + 1) % n; // next thread in list
    while ((j != i)) && !waiting[j])
        // loop through array until you're back at the start or you've found a waiting thread.
        j = (j + 1) % n;

    if (j == i)
        // If you're back at the start no thread is waiting for this lock and it is safe to unlock.
        lock = false;
    else
        // otherwise j is waiting on the lock. Instead of unlocking, pass the lock to j.
        waiting[j] = false;
~~~

#### mutex locks (mutual exclusion locks) (spin locks)
    - spin lock because other threads spin while waiting from lock to be freed
    - doesn't work on single CPU systems because of spinning
    - doesn't require context switch so it's a good choice multi-processor system expecting short lock sections
    - built using atomic operations

~~~
// shared information
    boolean lock = false;

    function aquire() {
        // while (!available) /* spin */ ;
        // available = false;
        while (test_and_set(lock));
    }

    function release() {
        // available = true;
        lock = false;
    }

// for each critical section
    aquire();
    // critical section
    release();
~~~

#### semaphores
- usage:
    - wait(S)
    - signal(S)
- possible to force execution order using signal() in one thread and wait() in the other.
- possible for it to be implemented without spinning

naive implementation of semaphores (without atomic operations)
~~~
object lock {
    int semi;

    constructor(int startingValue) {
        semi = startingValue;
    }

    synchronized function wait() {
        while (semi <= 0) /* busy waiting */; 
        semi--;
    }

    synchronized function signal() {
        semi++;
    }
}

// shared information
Lock lock = new lock(1);

// for each critical section
    lock.wait();
    // critical section
    lock.signal();
~~~

low spinning version of the semaphores
    - still spins during the compare_and_swap but much lower than normal
    - re-enables waiting threads one at a time.
~~~
typedef struct {
    int semi;
    struct process *list;

    wait() {
        int temp;
        do {
            temp = semi;
        } while (compare_and_swap(*semi, temp, temp--));

        if (temp < 0) {
            // register process with semiphore
            list.add(Thread.this());
            block();
        }
    }

    signal() {
        int temp;
        do {
            temp = semi;
        } while (compare_and_swap(*semi, temp, temp++));

        if (temp <= 0) {
            // wakeup the next item in the list
            wakeup(list.pop());
        }
    }
}
~~~

#### classic problems of synchronization
##### bounded-buffer problem:
a piece of shared memory is being used as a buffer. One producer, and One consumer are writing to and reading from this buffer. How do you communicate across threads what pieces of data are available and what areas of memory can be written to.

~~~
int n;
int read = -1;
int write = -1;
semaphore mutex = new semaphore(1); // only one thread should be reading from or writing to the buffer at any given time
semaphore empty = new semaphore(n); // there are n spaces in the buffer so the resources available is n
semaphore full = new semaphore(0); // at the begining there is nothing in the buffer so there isn't anything available.
shared memory buffer[n];

// consumer
    full.wait();
    mutex.wait();

    // remove item from buffer
    int next;
    do {
        int temp = read;
        next = temp + 1 % n;
    } while (compare_and_swap(*read, temp, next));
    BufferedItem item = buffer[next];

    // release the lock and signal that the buffer is emptied
    mutex.signal();
    empty.signal();

    // do something with buffer content

// producer
    // get the item to be buffered
    BufferedItem item;

    empty.wait();
    mutex.wait();

    // place item in buffer
    int next;
    do {
        int temp = write;
        next = write + 1 % n;
    } while (compare_and_swap(*write, temp, next));
    buffer[next] = item;

    // release the lock and signal that the item is ready
    mutex.signal();
    full.signal();
~~~

##### readers-writers problem
Many threads can read only one thread can write.
If you are a reader and there is a writer waiting, pause until the writ

~~~
// shared
Semaphore mutex = new Semaphore(1);
Semaphore resource = new Semaphore(1);
volatile int writers = 0;
volatile int readers = 0;

// all writer processes
    mutex.wait();
    writers++;
    mutex.signal();
    resource.wait();

    // write to the resource

    mutex.wait();
    writers--;
    mutex.signal();
    resource.signal();

// all readers
    mutex.wait();
    if (writers > 0 or readers == 0) {
        mutex.signal();
        resource.wait();
        mutex.wait();
    }
    readers++;
    mutex.signal();

    // read from the resource

    mutex.wait();
    readers--;
    if (readers == 0)
        resource.signal();
    mutex.signal();
~~~

##### dining-philosophers problem
Round robin of dead-lock! The all pick up the left chopstick at the same time! No one can eat because everyone has exactly 1/2 the resources they need to continue and the other half is taken by the person to the right.

Three solutions exist:
- allow one less than the circle to try to pick up a chopstick. If there are 5 places to sit only let 4 people sit down, when the 5th tries to sit down make them wait. At least one person will be able to pick up the other chopstick.
- only allow picking up chopsticks if both are available. Place the picking up of chopsticks in it's own critical section. This means that if a philosophers right chopstick is taken it will wait for it to be available inside a critical section but it guarnatees that the person on the right will eventually be done with the chopstick since in order for the critical section to be accessible they must have already picked up both chopsticks.
- Use an asymmetric solution. Odd places pick up the left then the right, Even pick up the right then the left. Fight over the first chopstick and you are guaranteed that the second chopstick is available.

#### monitors
Monitors are objects that control their internal content. This internal content 
- monitor type
- conditions
#### OS implementations of synchronization
- in Solaris
    - adaptive mutex: has a how bunch of potential implementations that change based on the system being used.
    - condition variables and semaphores are used for longer code segments
    - turnstile: each kernel thread can only be blocked on one lock at a time so instead of having a queue for each lock, solaris uses a turnstile in each thread. The first time a thread blocks, that threads turnstile becomes the locks turnstile. When the first item gives up the lock, it gets assigned a new turnstile from the operating system bank of blank turnstiles. These turnstiles also help implement a priority sequence. A higher priority thread will always move to the front of the turnstile, and a higher priority waiting element will bump the thread being waited on up to that priority.
- in Windows
    - multithreaded
    - on single threaded systems it pauses interrupts
    - on multi-systems it uses spin locks
    - provides semaphores
    - mutex dispatcher objects
    - critical section object. Spins for a given amount of time. After-which it uses a kernel mutex. This is usually very efficient since it only creates a mutex when it's locked.
- in Linux
    - non-premptive before 2.6
    - mutex_lock() and mutex_unlock() - a second element is put into sleep and awakened when mutex_unlock() is called.
    - semaphores and spinlocks are available
        - multiprocessor version
            - acquire spin lock
            - release spin lock
        - single processor version
            - disable kernel interrupts - preempt_disable()
            - enablet kernel interrupts - preempt_enable()
    - lots of atomic support:

        atomic t counter;
        int value;

        atomic set(&counter,5); /* counter = 5 */
        atomic add(10, &counter); /* counter = counter + 10 */
        atomic sub(4, &counter); /* counter = counter - 4 */
        atomic inc(&counter); /* counter = counter + 1 */
        value = atomic read(&counter); /* value = 12 */

#### Study Questions

1. What is the purpose of process synchronization?
2. What requirements should be satisfied to solve the critical-section problem?
3. What are the differences between hardware instruction and semaphore-based solutions?
4. What are the differences between semaphore and monitor? How are they used for solving the classic problems of synchronization?
5. How do Windows and Linux support process synchronization?
6. What is conflict serializability, and how can locking protocols be used to ensure it?

#### Learning Activities

- Try Exercises of *OSC9ed*.
    - 5.7: Race conditions are possible in many computer systems. Consider a banking system that maintains an account balance with two functions: deposit(amount) and withdraw(amount). These two functions are passed the amount that is to be deposited or withdrawn from the bank account balance. Assume that a husband and wife share a bank account. Concurrently, the husband calls the withdraw() function and the wife calls deposit(). Describe how a race condition is possible and what might be done to prevent the race condition from occurring.
    - 5.8: The first known correct software solution to the critical-section problem for two processes was developed by Dekker. The two processes, P0 and P1, share the following variables: The structure of process Pi (i == 0 or 1) is shown in Figure 5.21. The other process is Pj (j == 1 or 0). Prove that the algorithm satisfies all three requirements for the critical-section problem.

        boolean flag[2]; /* initially false */
        int turn;

    - 5.11: Explain why interrupts are not appropriate for implementing synchronization primitives in multiprocessor systems.
        Interrupts are sent to each processor so the cost of stopping all interrupts is high in a multiprocessor CPU.
    - 5.17: Assume that a system has multiple processing cores. For each of the following scenarios, describe which is a better locking mechanism—a spinlock or a mutex lock where waiting processes sleep while waiting for the lock to become available:
        The lockistobeheldforashortduration.: spinlock
        Thelockistobeheldforalongduration: mutex
        A thread maybeputto sleepwhileholdingthelock: mutex
    - 5.34: Suppose we replace the wait() and signal() operations of moni- tors with a single construct await(B), where B is a general Boolean expression that causes the process executing it to wait until B becomes true.

### 2.3 CPU Scheduling
OSC9ed: 6.1 to 6.9.

CPU scheduling is the basis of modern operating systems that can execute multiple processes and threads simultaneously. This section covers the concepts, criteria, algorithms, and examples of CPU scheduling, and introduces scheduling issues related to *thread* (thread scheduling), *multiple-processors* (multiple-processor and multicore processor scheduling), and *virtualization*.

#### Key Concepts and Topics
- CPU scheduling
    - process scheduling
    - thread scheduling
- CPU burst and I/O burst
    processes either are CPU intensive or IO intensive. A burst is defined as a sequential segment without a software interrupt:
        - CPU burst: Starts with a new process or a return from a wait interrupt, has a continual calculation being preformed until the end of the process or a software interrupt is called).
        - IO burst: any-time the process is waiting for IO
    The length of CPU bursts is usually exponential, large number of short CPU bursts with very few long CPU bursts.
- scheduling in virtual machines

##### CPU Scheduling algorithms
CPU scheduler or short-term scheduler:
- The CPU scheduler is invoked when a process:
    1. moves from the running state to the waiting state (new process must be chosen)
    2. moves from running to ready (ie. interrupt) (could be given back to same process)
    3. moves from waiting to ready (ie. IO is completed) (could be given back to original process)
    4. is terminated. (new process must be chosen)
- non-pre-emptive or cooperative scheduling: lets the process continue until it yields the CPU. This is the only option on systems that don't have a timer. Scheduling only happens after situation 1 and 4 otherwise the originally executing process continues. Doesn't work in multi-core CPU's
- pre-emptive scheduling: interrupts a process after a given amount of time with a timer. This causes race conditions since different processes can be at different points in their programs. This also affects the kernel since an interrupt can cause the entire kernel to be at the mercy of race conditions. Some kernels switch to non-preemptive scheduling while in the kernel. However, this isn't a good long term solution as CPU's get more and more cores. This also makes it impossible to make any guarantees about real-time systems. Another solution is to guard against them in the kernel.
- However, there are still a special type of process that can't be interrupted. Interrupt handlers. If an interrupt handler is not allowed to fire, information could be lost or overwritten. In a kernel the Interrupt handler will turn off interrupts while it is in running (very short) and turn it back on afterwards

dispatcher:
in charge of the context switch (switch context, switch to user mode, jump to the proper point in the user code)
dispatcher latency: amount of times this takes. This is a measure of how long a context switch takes.

Scheduling criteria:
for each set of processes there exists a God algorithm that perfectly decides which process to run when. However, because of the complex nature of scheduling an optimal algorithm is different for many factors in the set of processes. There isn't one master algorithm that solves for all possible factors. For all these criteria there are algorithms that do a better or worse job at optimizing for them. We usually optimize based on the averages but sometimes the variance is a better measure, for example user systems, users are happier with a predictably slower computer than a faster on average computer (within reason).
    - CPU utilization: what percentage of the CPU is being used at any given time.
    - throughput: number of processes completed in an hour.
    - turnaround time: amount of time from process start to process completion
    - waiting time: how long a process has to wait in the ready queue.
    - response time: amount of time from starting the process to getting the first response. 

###### First-come, first-served (FCFS)
- non-preemptive scheduler
- easy to implement with a FIFO queue.
- can result in long average waiting time especially when CPU bursts vary greatly.
- When IO and long CPU bursts are involved it can also lead to flip flopping between waiting for CPU and waiting for IO
- bad for time-sharing systems (since it's non-preemptive / cooperative)

###### Priority scheduling
- shortest-job-first, shortest-next-CPU-burst, shortest-remaining-time-first are special cases of priority scheduling
- Can be prioritized based on internal or external factors.
    - Internal: time limits job or burst, memory requirements, files requered, ratio of average IO to CPU bursts.
    - External: importance as declared by humans, funds allocated for the process, or any other factor.
- subject to starvation and indefinite blocking. A processes never runs because it's of such a low priority.
    - aging: increasing the priority of a process after x amount of time. Eventually even the lowest priority item, given enough time, will be a high priority item.

###### Shortest-job-first (SJF) (shortest-next-CPU-burst)
- implement with a priority queue based on next CPU burst's length, shortest first
- hard to know how long the next CPU burst will be:
    - in a job system it's possible since people put in the estimated job length
    - in a short-term scheduler it's possible to guess using past values for that process using exponential average of previous CPU bursts (shortest-remaining-time-first)

###### Round-robin (RR) scheduling: First-come, First-served with preemption.
- the ready queue is a circular FIFO Queue. Items are added to the tail as the CPU progresses through the Queue.
- the dispatcher choses the next processes, sets a timer for 1 quantum, loads the registers, starts the process. One of two things happens, The timer goes off or the process waits, with the timer, the processes is changed from running to ready and placed at the back of the ready queue, for waiting the processes is placed in the queue it's waiting for. The dispatcher then context switches from the current process to the next process, timer is set, and the next processes starts.
- average waiting is often long but response time and average runtime are usually lower
- How well the RR performs depends on the size of the Quanta.
    - If the Quanta is large it won't be any different than the FCFS algorithm.
    - If the Quanta is small it will spend a lot of time in the dispatcher. More wasted work the CPU is doing in the form of context switching.
    - General rule of thumb is that 80% of the CPU bursts should be shorter than the time quantum

###### multilevel queue scheduling
    - number of queues
    - how is the queue of a process determined
    - scheduling algorithm per queue
- Jobs can usually be classified into different section. For example foreground, background, batch, student processes. If the ready queue is split into these different queues for each type of process then each can have their own scheduling algorithm that optimizes for whatever is most needed for that group of processes.
- items are usually given a fixed priority for their lifetime
- because it's a priority queue starvation and indefinite blocking can happen. Aging is a solution to this.

###### multilevel feedback queue scheduling
- all of multilevel queue plus
    - when to promote a process to a higher queue
    - when to demote a process to a lower queue
- The most adaptive solution (can implement any triage you want)
- The most complex to implement

##### thread scheduling
process-contention scope (PCS)
    On many to one and many to many thread libraries the lib has it's own dispatcher and scheduler that decides what user level thread to be scheduled on to the LWP. Since this adds another layer of dispatching and scheduling it makes it difficult to maintain a strong scheduling algorithm. Often a priority queue or FIFO algorithm is used, often leading to starvation of threads. They are fighting over which one is running on a process, therefore process-contention scope.

system-contention scope (SCS)
    a kernel thread is treated the same as a process in most systems meaning it contends with all the other threads in a system. Therefore system-contention scope.

Pthread scheduling
- PTHREAD SCOPE PROCESS
- PTHREAD SCOPE SYSTEM

Linux and Mac OSX only allows System-contention scope!

##### multiple-processor scheduling
Asymmetric multiprocessing
- one core runs kernel processes the others run user processes

Symmetric multiprocessing (SMP)
- All cores run the same stuff
- more difficult because right down to the bare metal the software has to implement concurrent programs
- this is the current default.

Processor affinity
When a process is running on a processor it's L1, L2, L3 caches get built up and reduce the number of memory misses. This process is said to have affinity for the processor. OS's can implement two types of affinity soft and hard.
- soft affinity: OS will try to keep the process on the same processor
- hard affinity: OS will definitely keep the process on the same processor

Load balancing
Generally an OS wants all it's CPU's to be doing an equal amount of work.
When a CPU gets too much work it is sometimes beneficial to move a process to a new CPU even though it will take the hit. This can be done in two ways either through push, where a kernel process readjusts the CPU load, or through pull, where an empty process pulls a process from another CPU when it's empty.
When to move a process is tricky because it's always a trade-off, and isn't predictable. Some systems do it right away, others wait for a certain threshold.
This is a systems engineering problem with clear trade-offs.

Multicore processor scheduling - Multi-Threaded CPU's - Threads within a CPU
On some new CPU's there are multiple thread registers available within the core. This is a strategy to increase CPU efficiency given cache misses. By having a second set of registers it's possible to work on a second thread while the first one is waiting for instructions or cache from main memory.
This opens up the need for two levels of scheduling, the normal OS process scheduling and hardware scheduling within the CPU. Two examples of this are intel and solaris. Solaris does round robin between it's 8 threads per core. Intel has a priority from 1-7 that determines which thread to go next.
- coarse-grained - Context switching like with processors but within the CPU (similar to cooperative scheduling)
- Fine-grained (interleaved) - switching between CPU threads pretty much on every instruction (similar to time-sliced)

##### Real-time Scheduling
Different requirements than regular scheduling since there are definite points where the calculation is no longer useful. Either get it by this time or it's not valid.
Two types of guarantees, Soft and Hard.
Soft gives no guarantees about time, but guarantees that it will happen before any other process.
Hard gives specific guarantees about when a process will be complete.

Latency is the enemy of real-time systems:
- preemptive systems have lower latency because a interrupt is dealt with immediately instead of waiting for the original task to complete.
- dispatch latency: preemptive kernels keep dispatch latency low.

###### Priority-Based Scheduling
There are both Hard and Soft schedulers

scheduler needs some or all of the following information
- period: how often the task arrives
- runtime of the task
- deadline: how long after it arrives is it due

Some schedulers have admission control. Determines if a thread is allowed to run on the system or not.

####### Rate-Monotonic Scheduler
- Tasks must arrive at a steady period

- implements an admission control
- if admitted provides hard guarantees on deadlines

Real-time ready queue is a priority queue based on it's period. The shorter the period the higher the priority.

If we have runtime and deadline, this becomes a problem where we have full knowledge.
We can predict if the CPU will be able to fulfil this task.
If it is possible to do the task we have a Hard guarantee of the deadline.
If it is not possible we can issue a denial of entry.

This is an optimal solution for fixed priorities. However, a dynamic priority algorithm can do better.

####### Earliest-deadline-first scheduler
- deadline is needed

Real-time ready queue is a priority queue based on the inverse of the deadline. This leads to dynamic priority values since a new process might bump down the value of existing processes.

If runtime and period are known, we have full knowledge of the problem.
- Hard guarantees
- Admission control

This has the disadvantage of changing priorities which increases dispatch time.

####### Proportional-share scheduling
The CPU time is broken into 100 shares.
Each task requests a portion of the CPU.
An admission controller denies entry when all the shares have been requested.
The scheduler then guarantees that the process will receive it's alloted number of shares.

This scheduler cannot provide hard guarantees.

####### POSIX real-time scheduling
SCHED_FIFO: first-come, first-serve | priority can be assigned | no time-slicing between threads
- The highest priority RT thread gets the entire CPU until it finishes.
SCHED_RR: Round Robin | priority can be assigned | time-slicing between threads of the same priority.
- The highest priority RT thread shares the CPU with all the other RT threads of the same priority.
SCHED_OTHER: undefined and changes based on OS

##### OS Implementations
###### Linux scheduling
pre v2.5: traditional UNIX scheduling system | non-preemptive | didn't work well on SMP systems or systems will large number of runnable processes.
v2.5: O(1) scheduler (ran in constant time regardless of number of processes) | preemptive | poor response times for interactive systems
v2.6: Completely Fair Scheduler (CFS) classes - highest priority task from highest priority class runs
- uses red-black tree for O(log n)
- aging
    - tracks virtual run time (vruntime)
    - decay factor based on priority of task (low priority tasks have big decay factors)
    - decay factor * vruntime affects priority
    - IO task that doesn't use a lot of CPU will eventually be of a higher priority than a long running CPU bound task.

- priority rage: realtime 0 to 99 | normal 100 to 139 (nice value of -20 to 19)

###### Windows scheduling

Priorities: variable class 1 to 15 | real-time class 16 to 31
Windows API provides two values that determine priority number, priority class and relative priority within the class. The just map to priority numbers

- Preemption of lower priority threads.
- Highest priority task runs with time slice.
- for Variable priority threads
    - If time quantum runs out, it's priority is lowered. This limits the CPU consumption of compute bound threads.
    - When it waits, it's priority is raised, based on what type of wait (large for keyboard, small for disk). This tends to give good response times for interactive systems and gives IO bound threads the ability to keep the IO device busy.
    - Foreground vs background: The gui in the foreground gets a temporary increase (usually 3) in order to provide better response times.

UMS is a user space threads helper built into the windows kernel. It doesn't provide everything you need but it does provide a single thread with multiple TEB's. This helps libraries provide better one-to-many and many-to-many implementations.

###### Solaris scheduling

Multi-level feedback queue. With default being time-sharing.

Priorities vs classes:
- Interrupt threads = 160 - 169
- real-time threads = 100 - 159
- System (sys) threads = 60 - 99
- Normal threads = 0 - 59
    - Fair Share Threads (FSS)
    - Fixed priority (FX) threads
    - timeshare (TS) threads
    - interactive (IA) threads

Normal threads are time-shared and include a feedback
- feedback: when time-share expires it moves down in priority, when returning from wait it moves up in priority

Other Classes have different scheduling options but the default is the time-sharing with feedback.

##### scheduling algorithm evaluation
First you need to determine what criteria you will evaluate schedulers on. ie.
- Maximize CPU utilization given a maximum response time of 1 sec
- Maximize throughput

###### deterministic modeling
- given specific processes, calculate the actual value
- doesn't generalize well, limited to being valid on those processes

###### queueing model
Based on accounting date about the processes run on a system it is possible to create distributions of CPU vs IO bursts, and the arrival time. We can get probabilities from these distributions.

Queueing-network analysis
Based on arrival rates and service rates, we can calculate utilization, average queue lenght, average wait time.
Little's Formula:
n = average queue length
W = average waiting time in the queue
λ = average arrival rate

$$ n = W * λ $$

Because these calculations are based on averages of distributions they often don't give an accurate answer.

###### simulation
Simulations based on models using the distributions generated from accounting data.

Running these models is usually very intense, however, their results are more accurate.

###### implementation
Implementing the algorithm and testing it in the real world is the most effective solution, however, it is also the most expensive.

#### Study Questions

define *CPU scheduling*, and explain the rationale for using it in modern operating systems.
explain the concepts and criteria associated with various CPU scheduling algorithms.
explain the implementation of CPU scheduling in current operating systems such as Linux, Solaris, and Windows.
describe and evaluate methods for CPU scheduling algorithms for a particular system.

1. Why is CPU scheduling very important in modern operating systems?
    - the basis of resource management (it affects both IO and CPU usage)
    - the right algorithm can either optimize for throughput or responsiveness
2. What are the differences between pre-emptive and cooperative scheduling? How are pre-emptive scheduling and cooperative scheduling used in operating system design?
    Preemptive processes stop other processes in order to run a different process. This happens with an interrupt. ie. IO interrupt, process stops, swapped for process needing the IO. or timer interrupt (time slice for the process is up), context switch to next process in the ready queue (based on scheduling algorithm).
3. What are the main CPU scheduling algorithms, and how do they work?
    - fcfs: FIFO queue of processes, without preemption
    - priority scheduling: priority queue based on some factor of the process
        - starvation: aging is a solution
        - types:
            - shortest-job-first: based on the time alloted for the job
            - shortest-next-cpu-burst: ordered based an estimate of the next CPU bust using a quadratic formula of past CPU bursts for that process.
            - shortest-remaining-time-first: ordered based on the estimate of remaining time
    - round robin: FCFS with quantum preemption
        - given an quantity of time, schedule the first task, when the time is up put that task at the end of the queue and start the next task.
    - multi-level (feedback) queue
        - How many queues?
        - What is each queues scheduler?
        - How is it decided which queue a processes is placed in?
        - When is a process bumped up? (feedback)
        - when is a process bumped down? (feedback)
4. What are the issues unique to multiple processor scheduling compared to single CPU scheduling?
    - symmetric vs asymmetric processing
    - processor affinity
    - load balancing
    - multi-threaded CPU's
5. In practice, how do operating systems perform CPU scheduling?
Most have some kind of priority queue, with a separate real-time system, and some kind of aging policy. Solaris has the most flexible with a multi-level feedback scheduler, windows has the most complex balancing policy for interactive systems, Linux is a good mix of programmer flexibility and has a decent balancing policy.

- Try Exercises of *OSC9ed*.
    - 6.1. A CPU-scheduling algorithm determines an order for the execution of its scheduled processes. Given n processes to be scheduled on one processor, how many different schedules are possible? Give a formula in terms of n.
        n!
    - 6.3. Suppose that the following processes arrive for execution at the times indicated. Each process will run for the amount of time listed. In answering the questions, use nonpreemptive scheduling, and base all decisions on the information you have at the time the decision must be made.
            Process Arrival Time Burst Time
                P1    0.0    8
                P2    0.4    4
                P3    1.0    1
        a. What is the average turnaround time for these processes with the FCFS scheduling algorithm?
                    0    8    12   13
                    | P1 | P2 | P3 |
        turnaround:   8    12   12      avg: 11
        b. What is the average turnaround time for these processes with the SJF scheduling algorithm?
                    0    1    2    6    13
                    | P1 | P3 | P2 | P3 |
        turnaround:        1    5    13  avg: 6.33
        c. The SJF algorithm is supposed to improve performance, but notice that we chose to run process P1 at time 0 because we did not know that two shorter processes would arrive soon. Compute what the average turnaround time will be if the CPU is left idle for the first 1 unit and then SJF scheduling is used. Remember that processes P1 and P2 are waiting during this idle time, so their waiting time may increase. This algorithm could be called future-knowledge scheduling.
                    0  1    2    6    14
                    |  | P3 | P2 | P3 |
        turnaround:          5    13  avg: 6.86
    - 6.4. What advantage is there in having different time-quantum sizes at different levels of a multilevel queueing system?
        - Processes that require higher responsiveness can have a lower time-quantum trading turnaround for responsiveness. Processes that aren't optimizing for responsiveness can still receive longer time-quants giving bettern turnaround time.
        - If the CPU bursts are of different sizes than it is possible to spend less time in the dispatcher, 80% rule.
    - 6.5. Many CPU-scheduling algorithms are parameterized. For example, the RR algorithm requires a parameter to indicate the time slice. Multilevel feedback queues require parameters to define the number of queues, the scheduling algorithm for each queue, the criteria used to move processes between queues, and so on. These algorithms are thus really sets of algorithms (for example, the set of RR algorithms for all time slices, and so on). One set of algorithms may include another (for example, the FCFS algorithm is the RR algorithm with an infinite time quantum). What (if any) relation holds between the following pairs of algorithm sets?
        a. Priority and SJF: Shortest-Job-First is a priority queue where the formula for determining priority is based on the length of the job.
        b. Multilevel feedback queues and FCFS: FCFS is a MLFQ with 1 queue, priority based on entry time, 0 feedback factor
        c. Priority and FCFS: FCFS is a Priority Scheduler based on entry time
        d. RR and SJF: none
    - 6.6. Suppose that a scheduling algorithm (at the level of short-term CPU scheduling) favors those processes that have used the least processor time in the recent past. Why will this algorithm favor I/O-bound programs and yet not permanently starve CPU-bound programs?
        > IO bound have short CPU-bursts. As they progress they will get a higher and higher ranking, however, they will still have a lower ranking than new CPU-bound processes. Also if they start to take a long time they will eventually be lower than a CPU-bound program starting at the same time.
    - 6.7. Distinguish between PCS and SCS scheduling.
        > Process-contention scope: All user level threads compete for CPU time on a single kernel level thread per-process
        > System-contention scope: All threads on the system compete for CPU time.
    - 6.8. Assume that an operating system maps user-level threads to the kernel using the many-to-many model and that the mapping is done through the use of LWPs. Furthermore, the system allows program developers to create real-time threads. Is it necessary to bind a real-time thread to an LWP?
        Yes.
    - 6.9. The traditional UNIX scheduler enforces an inverse relationship between priority numbers and priorities: the higher the number, the lower the priority.
        The scheduler recalculates process priorities once per second using the following function:
        Priority = (recent CPU usage / 2) + base where base = 60
        and recent CPU usage refers to a value indicating how often a process has used the CPU since priorities were last recalculated. Assume that recent CPU usage is 
        What will be the new priorities for these three processes when priorities are recalculated?
        Based on this information, does the traditional UNIX scheduler raise or lower the relative priority of a CPU-bound process?
        40 for process P1: 40/2 + 60 = 80
        18 for process P2: 18/2 + 60 = 69
        10 for process P3: 10/2 + 60 = 65
        lowers priority for CPU-bound processes
    - 6.16 Consider the following set of processes, with the length of the CPU burst given in milliseconds:

            Process Burst Priority
                P3    8    4
                P5    5    3
                P1    2    2
                P4    4    2
                P2    1    1

        | FCFS:                    |0| P1 |2| P2 |3| P3 |11| P4 |15| P5 |20|
        | SJF:                     |0| P2 |1| P1 |3| P4 |7| P5 |12| P3 |20|
        | nonpreemptive priority:
        | RR (quantum = 2):

    - 6.17 The following processes are being scheduled using a preemptive, round- robin scheduling algorithm. Each process is assigned a numerical priority, with a higher number indicating a higher relative priority. In addition to the processes listed below, the system also has an idletask (which consumes no CPU resources and is identified as Pidle). This task has priority 0 and is scheduled whenever the system has no other available processes to run. The length of a time quantum is 10 units. If a process is preempted by a higher-priority process, the preempted process is placed at the end of the queue.
    - 6.18 The nice command is used to set the nice value of a process on Linux, as well as on other UNIX systems. Explain why some systems may allow any user to assign a process a nice value >= 0 yet allow only the root user to assign nice values lt 0.
        - Kernel processes generally have a value lt 0. the lower the nice value the higher the priority. Users shouldn't have the power to be more important than the all knowing kernel!
    - 6.19 Which of the following scheduling algorithms could result in starvation?
        a. First-come, first-served: no
        b. Shortest job first: true
        c. Round robin: false unless there is priority
        d. Priority: true
    - 6.20 Consider a variant of the RR scheduling algorithm in which the entries in the ready queue are pointers to the PCBs.
        a. What would be the effect of putting two pointers to the same process in the ready queue?
            - they would get 2x the CPU time of all the other processes
        b. What would be two major advantages and two disadvantages of this scheme?
            - advantage, fast to access process, no extra data in the ready queue
            - disadvantage, slower access time because of following links, there are two pointers in each spot
        c. How would you modify the basic RR algorithm to achieve the same effect without the duplicate pointers?

### 2.5 Deadlocks
OSC9ed: 7.4 to 7.7.

The final section in this unit discusses deadlocks, which may occur when several processes compete for a finite number of resources. Topics in this section include techniques to detect, prevent, and avoid deadlocks. As operating systems typically do not provide deadlock-prevention facilities, programmers are responsible for ensuring that the programs they design are deadlock free. The information in this section will help well-trained programmers to analyze and address deadlock-related issues in their programs.

#### Key Concepts and Topics

##### What is a deadlock?
2 or more processes are blocked indefinitely because they all need something that one of the others in the group has.

necessary conditions for a deadlock to arise
- mutually exclusive resources: two or more resources in the system must be limited in the number of processes that can access them.
- non-preemptive resources: none of the resources involved can preempt the access a process has. The process must release the resource on its own.
- wait and hold: all the processes involved have to acquire one resource at a time with some kind of wait between them, aka non-atomic operations.
- circular waiting: a loop must exists between the processes that are deadlocked.

##### How can we detect if a deadlock has occurred?
resource-allocation graph
    A visual/CS representation of a deadlock
    - Two types of nodes: Processes (P) and Resources (R)
    - A directed edge from P -> R means a process has requested but not received a resource
    - A directed edge from R -> P means a resource is acquired by a process
    - multiple R -> P edges can exist since R can have multiple instances

##### How can we deal with deadlocks?
1. do nothing (Linux and Windows)
2. prevent deadlocks (deadlock prevention)
    - prevent one of the 4 deadlock events:
        - Mutual exclusion: Not possible to prevent
        - Hold and Wait: two possible ways
            - process must request all resources up front. A process is only allowed to run when it has the required resources.
            - process can only request resources when it has non.
            - resource utilization is low
            - starvation is possible if a process needs multiple resources and they are always given to other processes
        - No Preemption: Allow preemption
            - When a process is waiting for a resource, the resources it holds can be preempted in another process asks for it. The waiting process is now waiting on two resources.
            - This does not work on stateful resources like memory (semaphores, mutex locks). It does work for printers, registers, swap memory space, ect.
        - Circular wait: total ordering on resources.
            - programs can only request resources in ascending/descending order. This eliminates the possibility that a circle is formed. P_a requests R_1 then R_2, P_b requests R_2 then R_1 = deadlock, vs P_b requests R_1 then R_2.
            - developers need to follow it for it to work
            - Can lead to strange situations when resources aren't logically requested in the order they are needed.
            - Doesn't work when resources are requested dynamically
3. avoid deadlocks (deadlock avoidance)
    - requires additional information about which processes request which resources
    - track resources requested and only allow a process to get a resource when it leaves the system in a safe state.
    - a safe state is a state where no deadlock is possible.
    - Resource-Allocation-Graph Algorithm:
        - the resource allocation graph + a claim edge: any resource a process might request
        - when a process requests a resource, the graph is checked for a cycle using the acquired edges, request edges, and claim edges of processes already given resources. For every resource that is given out, the system in guaranteed not to have created a potential cycle.
        - downside: checking for a cycle takes n^2 time where n = number of processes.
        - doesn't work on resources with multiple instances
    - Bankers algorithm:
        - requires more complicated data structures
            - resources available: int array[m] holding the number of each resource type
            - max: int array[n][m] holding the max number of resources each process might need
            - Allocation: int array[n][m] the currently allocated number of resources each process has
            - Need: max - allocation
        - slower runtime
        - safety algorithm: m × n^2, where m = resource types
        - allocation algorithm: does it exceed what the process said it needed? is the resource available? If the resource is given does it remain in a safe state?
4. detect and recover after entering a deadlocked state
    - detection algorithm
        - wait-for graph: collapsed resource graph with only processes, showing which processes are waiting on which other processes.
            - only useful for resources with single instances
        - modification of bankers algorithm:
            - requires more data structures and takes longer to run
        - deadlock detection algorithms should be run according to how often deadlocks occur. This depends on the system and the programs. Might be useful to check it when CPU usage drops bellow a certain threshold since deadlocks decrease ready processes.
    - recovery algorithm
        - let the admin know
        - abort one or more of the deadlocked processes
        - preempt one or more of the resources from the deadlocked processes

#### Study Questions

1. define *deadlock*, and discuss the conditions under which a deadlock may arise.
2. summarize the different ways of and methods for handling deadlock.
3. describe how to realize deadlock prevention, deadlock avoidance, deadlock detection, and deadlock recovery.
4. explain the resource-allocation-graph algorithm, Banker’s algorithm, and deadlock detection algorithm.

1. Why is it important to learn to handle deadlock issues?
2. What are the necessary conditions for a deadlock to happen, and how can knowledge of these conditions be used in deadlock prevention?
3. How can one determine whether a state is safe state (deadlock free)?  How can this knowledge be used to avoid deadlock?
4. What data structures are used in deadlock avoidance and deadlock detection?

7.1 List three examples of deadlocks that are not related to a computer-system environment.
7.9 Suppose that you have coded the deadlock-avoidance safety algorithm and now have been asked to implement the deadlock-detection algorithm. Can you do so by simply using the safety algorithm code and redefining Maxi = Waiting_i + Allocation_i, where Waiting_i is a vector specifying the resources for which process i is waiting and Allocation_i is as defined in Section 7.5? Explain your answer.
7.10 Is it possible to have a deadlock involving only one single-threaded process? Explain your answer.
7.11 Consider the traffic deadlock depicted in Figure 7.10.
    a. Show that the four necessary conditions for deadlock hold in this example.
    b. State a simple rule for avoiding deadlocks in this system.
7.19 Consider the version of the dining-philosophers problem in which the chopsticks are placed at the center of the table and any two of them can be used by a philosopher. Assume that requests for chopsticks are made one at a time. Describe a simple rule for determining whether a particular request can be satisfied without causing deadlock given the current allocation of chopsticks to philosophers.
7.20 Consider again the setting in the preceding question. Assume now that each philosopher requires three chopsticks to eat. Resource requests are still issued one at a time. Describe some simple rules for determining whether a particular request can be satisfied without causing deadlock given the current allocation of chopsticks to philosophers.
7.21 We can obtain the banker’s algorithm for a single resource type from the general banker’s algorithm simply by reducing the dimensionality of the various arrays by 1. Show through an example that we cannot implement the multiple-resource-type banker’s scheme by applying the single-resource-type scheme to each resource type individually.

## Unit 3: Storage Management
This unit covers memory management, virtual memory, file system management, disk management, mass storage structures, and I/O systems.

### Intro

In a multiprogramming system, a process may change its state from “waiting” to “running” several times before completing its task. Clearly, if each process were loaded from secondary storage into the main memory in its entirety, a large fraction of machine time would be wasted on loading and unloading processes to and from the main memory during each section of process execution. To minimize the “overhead” associated with loading and unloading, operating systems allocate memory to several processes simultaneously. This complex task requires effective memory management schemes and their hardware support (major topics in this unit).

The other major topic in this unit is secondary storage, in particular, file systems and disk management. Disks serve as extensions and backup for the main memory, and as economical online storage devices for program and data files. The operating system organizes files in the framework of a file system. Disk access is much slower than access to memory and, in general, several processes compete for disk access. For these reasons, in many computers, disk access is the main bottleneck to improved performance. As such, section 3.4 examines the software and hardware mechanisms employed to improve disk performance.

Input-output operations are among the main jobs of a computer system. As various I/O devices vary widely in their function and speed, different methods are needed to control them, and those methods form the I/O subsystem of the kernel. The final section of this unit covers the structure, principles, and performance aspects of I/O hardware and software.

When you complete Unit 3, you will be able to describe the different strategies that operating systems employ to manage memory, with knowledge of the benefits, limitations, resource overhead (such as fragmentation and data structures), and hardware requirements of each management technique. You will also learn how developers can write applications (program and data structures) that reduce overhead for memory in a shared environment and that use memory more efficiently. In modern application environments, in which virtual memory is becoming increasingly important, it is important that you can explain this concept and its importance, and that you can list and describe several strategies that systems software uses to manage disks and other devices. Finally, you should be able to describe the structure, principles, and performance issues of I/O hardware and software.

### 3.1 Main Memory
OSC9ed: 8.1 to 8.7.

This section focuses on memory management in the main system. Memory is an important finite resource that has a significant impact on system throughput. As such, it must be managed carefully. In a multiprogramming environment, the operating system attempts to complete as much work as possible at one time by allowing processes to share memory. To do this, it is critical that the operating system manage memory in such a way that many processes may share it and that the memory space for each process is protected from other processes. This security measure requires that all memory addresses be validated. The overhead resource cost of verifying every memory access makes hardware support necessary.

#### Key Concepts and Topics

The CPU doesn't have direct access to any memory storage other than CPU registers, cache and main memory.
If the data isn't in one of these places, it needs to be moved there before it can be operated on.
From the view of the memory unit, they don't care what the CPU is doing only the stream of addresses coming over the bus.

Speed:
CPU registers - ~1 cycle
L1 CACHE hit  - ~4 cycles
L2 CACHE hit  - ~10 cycles
L3 line unshared - ~40 cycles
L3 shared line in another core - ~65 cycles
L3 modified in another core - ~75 cycles
Main memory - 100's of cycles

Protecting memory:
- An OS executing in kernel mode has unlimited access to all the system memory.
- Using a privileged instruction the OS sets the limit and base registers for a process before moving from kernel to user mode.
- These registers are used to give a limit to what a process can access.
    - Base register (or relocation register) - starting memory range for process
    - Limit register: how much memory it can access.
    - relocation register - every time a user program accesses a piece of memory the relocation register is added to the request meaning the user program only ever sees the address space from 0 to limit register.

How a user program is compiled
- source program
- through compiler
- becomes object module
- plus other object modules
- through linkage editor
- becomes load module
- plus statically linked system library
- through loader
- becomes an in-memory binary (block of physical memory)
- with dynamic linking
- can attach dynamically loaded system library

Static linking: When a program is loaded a copy of all the system library routines used by the program are copied into it's memory space. This is necessary for systems that don't use a MMU, however duplicates code in main memory and requires everything to be defined ahead of time.
Dynamic linking: When a program is loaded, it has stubs for each system library that is required. The first time the stub is called it requests a link to the code from the kernel. The code is added to the programs memory space and it then accessible. The stub is then replaced with a link to the executable code. This requires hardware and OS support. This also means the libraries can be updated without the link being updated. Libraries are versioned so you don't get a newer version that is incompatible.
Dynamic loading: similar to dynamic linking. Programs need to be in main memory for them to execute, however, most programs today are too large to fit. Dynamic loading is the process of getting instructions from disk, and attaching them to main memory. This requires Hardware support but the OS doesn't need to be part of this process.

Types of addresses:
- logical address: the address used in the CPU
- physical address: the address used by memory unit
- virtual address: the term used for the logical address when it's not the same as the physical address
Address Binding:
- Symbolic binding: User program usually stores data in symbolic addresses
- Relocatable binding: The compiler binds these symbolic address to relocatable addresses (ie. 14 bytes from the beginning of this module).
- Physical binding: The linkage editor or loader binds these relocatable addresses to physical addresses (ie. 74014).
When is an address bound? Address binding can be done at different points in the user program loading diagram
- Compile time (by compiler, logical = physical) - used by MS-DOS. When the code is compiled it determines where in main memory it will be located.
- Load time (by loader, logical = physical) - when a program is loaded into main memory it's addresses are calculated based on the relocatable address
- Execution time (by dynamic linking, logical ≠ physical) - addresses are determined dynamically at runtime. Most flexible but requires special hardware.

Memory management unit (MMU) - hardware device that translates between virtual (logical) addresses and physical addresses in memory.
- User program in CPU uses logical address (ie. 378)
- When the CPU requests that memory, it first adds the relocation register (ie. 378 + 74014 = 74392)
- The MMU takes the address from the CPU and translates it into the physical address before accessing it from memory (ie. MMU(74392) = 29379842).

#### Swapping
Moving process memory to a backing store (disk).
This makes it possible for physical memory addresses to exceed the physical memory on a machine.
- swapping takes a long time (2 sec for 100mb, 60 sec for 3gb)
- IO - a processes is swapped to disk and is waiting for IO the data from the IO might be sent directly back to memory, overwriting the process that was swapped in, and being lost to the process that was swapped out. This can be fixed by only allowing IO to Kernel buffers, but then the data needs to be copied from the kernel buffer to the program (double buffering).
- Modern OSs don't uses traditional swapping. Although variations exist:
    - swapping portions of programs instead of the entire program (used with virtual memory)
    - mobile IOS - ask applications to relinquish memory, read-only data is removed and later reloaded. Otherwise applications are terminated.
    - mobile Android - terminates and saves application state to disk (not entire memory). It starts where it left off.

#### Contiguous allocation
Old way of doing it. This is what I learned about when I first learned about disk-management.

Each processes is contained in a single continuous block of memory.
This makes protection easy. The relocation and limit registers define the size of the continuous block.
Memory is partitioned into OS and User space. OS is usually in low memory to be close to the interrupt vector.

Fixed-partition scheme (very old) - The remaining memory is divided into partitions and each partition can run one program. A program can't get more memory than is available in the partition, and the system can't run more programs than there are partitions. Lots of wasted memory.

Variable-partition scheme (old) - The OS maintains a table of all user memory blocks (started at a byte).
- As memory gets larger the table gets harder to maintain. At a certain point it makes sense to make the memory block larger. The larger the block the smaller the memory allocation table.
Hole - A group of unused memory blocks
job queue - list of processes waiting for a memory
The OS takes the each job and sees if there's a hole big enough for it.

Dynamic-allocation-storage problem: first fit and best fit are the best and change based on type of load.
- first fit: the first hole that will fit the program
- best fit: search for the smallest hole that will still fit the program
- worst fit: find the biggest hole.

Fragmentation: The big problem with all these strategies is fragmentation. Unusable holes in memory.
- External fragmentation: As a system continues to free and allocate memory, holes will appear between programs. Since none of these holes are big enough they can't be used for a program and are external fragmentation. Memory holes between programs. Statistically 1/3 of memory will be unusable.
- Internal fragmentation: If a program requests a smaller amount of memory than a block, the system will round up. This unused rounded memory is the internal fragmentation.
- Compaction: Moving the program and data from one part of memory to another in order to move the holes together. Must have hardware support (registers) and is very expensive.

#### Segmentation
If the space between processes was able to be allocated to other systems much more of the main memory could be used by processes.
Programmers don't need big chunks of data they think in methods, objects, stack, heap, module, ect.

A segment is a chunk of data assigned to a user-program. Each process has multiple segments that are defined using a segment number and an offset. The number is how the program refers to the segment and the offset determines where the data resides in memory. Program refers to address with two dimensions (segment, offset) but physical memory is still a one dimensional array.

Hardware is needed to translate the two dimensional address into one dimensional memory. There exists a table that knows all the segments on in main memory. It stores the segment limit and the segment base.
When the user-program requests a piece of memory it sends segment and the offset. The segment table looks up the limit and the base for that segment. If (offset lteq limit){return offset + base} else {throw trap}. The resulting address is fetched from memory.

Still suffers from fragmentation but at a lower level.
Requires programmer support.

#### Paging

Break all storage into fixed-sized blocks of the same size:
- for physical memory and the backing store they're called frames.
- for logical memory they are called pages.

Each process gets their own page table.
Each page table holds a set of pages allowed by the process.
The process indexes into the page table as if it were one long array.
If the index is greater than the allocated pages a trap is thrown.
The index is split into the page part and the offset part.
The page part is used to look up the frame that is mapped to that page.
The frame + offset is looked up in main memory.

Because of this separation of virtual and physical memory:
- 0 external fragmentation: any program that can fit into the remaining pages can be held in memory
- 1/2 page internal fragmentation expected per process: Since a process can request an arbitrary size of data we would expect that each program will have some internal fragmentation. If it's evenly distributed across the page size, then the average will be 1/2 a page per process.

Management by OS
- OS needs to know how many frames are available on the system, and how many are allocated.
- Frame table: one entry per frame - free or allocated - to which page of which process
- Page table: stored in kernel either as part of PCB or as one or more large tables.
    - OS maintains a copy of the page table for each process
    - for context switch
    - for mapping a logical address in a process needs to a physical address
    - for Mapping IO to the right spot in memory

Hardware:
- defines the page/frame-size
    - larger: leads to wasted memory
    - smaller:
        - more page faults
        - larger page table
- Registers:
    - If only a few pages are used per process a set of registers can be used to hold the table.
    - Entire page-table has to be sent to registers from memory on every context switch
    - only useful for up to 256 entries (at 4kb = 1mb of data .: not enough!)
- TLB Translation look-aside buffer: key-value lookup with 0 penalty
    - a cache specifically for page lookups. A key (index) is checked against all entries, and if it exists the value is returned.
    - ASIDs - address space identifiers - used to identify the process making the TLB request
        - TLB might be able to hold page lookups for multiple processes using ASIDs or might have to flush every time a context switch happens.
    - if it fails it either has to look at a L2 cache (6 cycles) or loop back to main memory.
    - often there are two sets one for instructions, one for data. Since lookups happen in each step of the pipeline.
    - (PTBR) page-table base register - address to memory where the page table resides
    - (PTLR) page-table length register - (only on some systems) the limit for the page length.
    - instead of the entire page-table being moved into registers only the PTBR needs to be moved on a context switch.
    - TLB miss - interrupt to OS or hardware - we lookup the missing address and add it to the TLB
        - LRU - round robin - locked down - 
    - Hit ratio - up to 99%

Protection (mostly implemented in hardware)
- bits in the value retrieved from the page table are used to determine if a piece of physical memory should be allowed to be used for a specific purpose. Hardware trap on invalid operation.
    - read-write
    - read bit, write bit, execute bit
    - valid-invalid bit: for page misses
- For systems with a PTLR the function `if (page lteq PTLR) {return TLB(page) + offset} else {trap illegal page }`

Does not require user-programmer support.
Does not suffer from fragmentation .: no compaction.
Can be applied to swap disks (backing stores).
Shared Pages! Since read only pages are possible an OS can have multiple processes running with their text sections overlapping.
Also makes shared memory pages easier.
Requires hardware support.

#### How are page tables implemented
Page tables
- are usually large (2^32 or 2^64 addressable space)
- grow and shrink
- are very sparse
So how do you manage the manager?

Hierarchical paging / forward-mapped page table / multilevel paging (most common)
- table of tables each one getting closer to the address
- the address is split into sections | p_1 | p_2 | ... | d
- for each section there is a table with an address that points to the next section until you reach the address d.
- This was one of the first approaches but became unmanageable as tables grew large.

Hashed page table
- hash table - key: virtual page address, value: physical page address
- linked list to next address

Clustered page tables
- hash table with a block of physical addresses
- key: shift right virtual page address, use shifted bits to index into resulting array.

Inverted page table
- uses the frame table for page lookup using the pid.
- difficult to implement shared memory since one frame can't point to two pages, but two pages can point to one frame.

#### Intel
IA-86
segmentation with paging

First the logical address is converted from a segment and offset into a 'linear address' using segmentation.
Then the 'linear address' is converted to a physical address using paging.
First bit of the page directory address denotes if it's a 4kb or 4mb block
If it's a 4mb block the offset is added to the directory address.
If not a second lookup is needed.

local descriptor table (LDT)
global descriptor table (GDT)

Intel x86-64
- still uses the same system but with 4 levels of paging hierarchy

Why segmentation plus paging? Seems like a waste.

#### Study Questions

1. describe address binding at compile, load, and execution time.
    > address binding can happen at one of three levels
    1. compile time. msdos. physical addresses are hardcoded into the code
    2. load time. unasisted software. physical addresses are fixed when the binary is linked into memory
    3. execution time. hardware assisted. physical addresses are determined when the code is running.
2. explain the different strategies that operating systems use to manage the sharing and allocation of memory among several processes, including contiguous allocation, paging, segmentation, and segmentation with paging.
    - continues allocation was back in the day. Each process had a chunk of memory.
    - segmentation, split up those chunks so one processes could have multiple chunks.
    - paging, blows it away by allowing an arbitrary number of chunks associated with each process, while giving the processe the illusion that it is only accessing one chunk.
3. discuss how relocation, sharing, and protection are considered in memory management.
    - relocation only works with execution time address binding. a chunk of memory can be moved to make the memory more efficient
    - sharing only works when there's a read write flag. Two processes can read from the same code.
    - or sharing happens when two processes agree so share a section, the physical memory is linked into both their pages.
    - protection: each memory model has a way to make sure the process isn't addressing memory outside of it's own space.
        - for continuous this means having a limit that the process is allocated. The process is allowed to access 0 to limit, and is bumped by the base.
        - for segmentation, that means having a segment limit associated with each segment.
        - for paging, that means having an page limit register that tells the CPU how many pages a process has available
4. describe how an operating system may implement shared memory.
    - an os might implement shared memory by having a page linked into two processes page tables.

2. What are the main purposes of swapping, paging, and segmentation in memory management?
    - swapping is in order to move memory off memory to save space. paging makes this very easy. Only the least used pages are moved off. Since they are small unused sections of programs can be swapped without much problem.
    - mobiles don't usually use this since rw isn't as reliable with flash.
3. When should an operating system designer consider using hashed paging and inverted paging instead of hierarchical paging?
    - when the address space is sparse
4. How does an Intel architecture support both paging and segmentation?
    - first segment, then page = stupid!

8.2 logical are in the cpu, need to be translated, physical are on disk
8.2 extra register, what if instructions can be modified? faster lookups.
8.3 so they corespond with a number of bits to be addressed by. If not there would be unaddressed bits, or unused memory
8.5 The memory would be imediately accessible by the other process. edits would be reflected in both pages.

8.11 
8.20
8.28

### 3.2 Virtual Memory
OSC9ed: 9.1 to 9.10.

For users, the tangible benefit of virtual memory is that it removes the restriction that the size of the computer’s memory places on the size of an executable program. The key idea behind virtual memory is easy to state but much harder to implement: keep only those (code and data) parts of a process in the memory that are needed in the current CPU burst of the process. This section examines the software and hardware mechanisms needed to implement virtual memory.

#### Virtual memory
In an operating system with paging it is possible for an OS to implement a virtual view of the memory space available to user programs.
This is accomplished by promising a program as much memory as it needs, and then only give it to the program when it actually uses it.
- logical address space is very large and programs can take up huge amounts of space in virtual memory
- programmers don't have to think about program size
- more programs can fit in memory, since only the parts of a program being used are in memory.
- shared pages:
    - easy to share files
    - easy to share memory
    - libraries can be linked in
    - provides efficient methods for process creating (fork, vfork)
- the space between the stack and the heap aren't actually being used unless necessary.

This technique relies heavily on the page-table and MMU.

#### Demand paging (How virtual memory is implemented in practice)
For an instruction/data to be used executed/used it must be in memory!
But most instructions/data of a program are never used.

Demand paging only brings a page into memory when it is used

Lazy swapper(pager) - only bring page into memory when it is referenced in execution

Hardware needed:
- page tables
- valid-invalid bit in the lookup value of page-table
- ability to restart any instruction
- secondary memory (swap space)

Page fault:
1. The process references a page that doesn't exist in physical memory.
1. The value of the address returned from the TLB has the invalid bit set.
1. A trap is called to the OS.
1. Context switch
1. Interrupt handler for page faults
1. The OS checks to see if the address is valid in a table usually in the PCB
1. If not the process is terminated
1. The OS finds a free frame
1. The OS makes an IO call to bring the page from storage into the frame
1. Interrupt and context switch
1. When IO completes The OS updates the page-table with the new address
1. The OS starts the process back at the instruction that caused the trap

Page fault rate
- Number of times a page fault will occur.
- effective access time = (1 - pfr) x (access time) + pfr x (page fault access time)
                        = access time + (page fault access time - access time) x pfr

Locality of reference:
- If an instruction needed addresses from multiple places it might cause multiple page faults leading to poor performance.
- This is exceedingly rare because programs tend to reference things close to them or close to other referenced things.

Zero-fill-on-demand frames: OS's usually use zero-fill-on-demand page allocation
- A new frame is filled with zero's and placed in a ready queue.
- This way when the frame is assigned to a frame the data is consistent.

Pure demand paging(extreme) - When the OS sets the process to start it doesn't load anything.
- when the PCB tries to execute the first instruction it causes a page fault
- only pages that are used are ever loaded
- in practice not efficient because of IO

Page Replacement: When a system runs out of memory it must choose a page to move to the backing store.
1. Find desired page on disk
1. Find free frame
    - if free frame exists use it
    - or use the page-replacement algorithm to select frame
        - and change victim page and frame tables
        - and write victim frame to disk (IO operation!)
1. Read page from disk into frame (IO operation!)
1. Change page and frame tables

#### Efficiency
Page faults and page replacement is VERY slow!
Any decrease has HUGE performance improvements!

Ways to speed it up:
- Frame allocation algorithm: if we can accurately decide how much and which pages to give to process it will decrease page faults.
- Page replacement algorithm: if we can efficiently decide which pages to remove from a process we will decrease page faults.
- Buffers strategies: free frames pool, free frames with link maintained, write modified frames to disk

Non-Uniform Memory Access (NUMA) - these algorithms change on boards with non-uniform memory access.
- processes running on the same chip should have their memory on the same board.
- similar processes should be scheduled together.
- duplication of read only pages might be beneficial for programs with multiple threads running across the entire system.

How to measure?
- It's possible to record or generate a list of address lookups for a system but page faults are only affected when the page being addressed changes.
- reference string: A list of address lookups stripped of offsets and with duplicate sequential entries removed.
- With a reference string, a number of frames, and an algorithm we can determine the efficiently of that algorithm

Certain apps know their memory and IO use better than an OS.
Raw memory and IO is sometimes available from an OS.

##### Frame Allocation Algorithms
Scheduling frames for processes has many overlapping strategies that perform differently for different workloads.
There are some best practices:
- Min # of frames per process
    - Minimum number of frames strategy: It usually makes sense to have a min num of frames allocated per process. This reduces the page faults at startup especially if the OS has historical data on what the program usually needs.
    - some also define a max (windows)
- Proportional allocation based on process priority & memory requirements
    - Evenly split: easiest way to split frames between processes
    - Proportional:
        - to size of memory requested: simple but easy to trick
        - adjusted for process priority

##### Page Replacement Algorithms

Replacement policy: Global
- Where do we take the paging frames from?
- Local replacement
    - set of pages in a process can only be affected by itself
    - makes thrashing local to a process
    - gives more benefit to the individual task at the expense of the system
- Global replacement
    - process can't control it's own frames
    - leads to varied performance based on external factors
    - more commonly used because it leads to better overall system performance

Belady’s anomaly
- Sometimes adding more frames to an algorithm makes it performs worse.
- This usually happens with non-optimal algorithms but might be 

**Replacement Algorithms**
FIFO: First page in is the last page out
- easy to implement without hardware support
- not very good
- Belady's anomaly

Optimal page replacement
- If we could see ahead in time we would remove the page that will next used in the most amount of time.
- NO Belady's anomaly!!!

Last Recently Used (LRU) replacement
- next best to OPR without foreknowledge
- requires special hardware to implement (else it is VERY inefficient)
    - Counter: update access time - search to find LRU (short constant, long search)
    - DLL stack: every page is moved to top of stack and replacement is taken from tail (long constant, short search)
- NO Belady's anomaly!!!

Additional-Reference-Bits Algorithm: approximation of LRU
- When a page is referenced a reference bit is set for that page
- at a specific time period the bits all switch right
- if a byte is available 8 periods are kept
- the lowest number gets replaced
- low Belady's anomaly

Second-Chance Algorithm
- FIFO with one ARB bit
- If the bit is 1 move to end of queue and reset bit
- if the bit is 0 take the frame.
- often implemented with circular array queue
- Belady's anomaly

Second-Chance + Modification
- Modify bit:
    - If the victim in memory page has been modified since the last read from storage, it can be replaced without writing.
    - removes need for one IO operation
- Replace the page in the lowest non empty class
    - (0,0) not recently used - not modified
    - (0,1) not recently used - modified
    - (1,0) recently used - not modified
    - (1,1) recently used - modified

Least-frequently used & Most-frequently used
- keep counter of number of times used
- Neither are very useful

##### Other Strategies
Frame Buffer (or pool)
- The OS keep a certain number or percentage of free frames
- When a process needs them they are available from the buffer
- usually a very low priority task in the system
- optionally zero out the frames ahead of use (doesn't work with next strategy)

Frame Pool with original reference maintained
- pages that are moved to the frame pool can be reclaimed
- Keep address on where the frames in the pool came from
- incompatible with pre-wiped frames
- very useful in conjunction with FIFO algorithm
- somewhat useful with second-chance algorithm

Modified page queue
- Pages that have been modified are written to disk
- Very low priority task

Prepaging
- Bring into memory working set
- very hard to make efficient

Page clustering
- Bring in a few pages after the page fault

#### Thrashing
When a system or process doesn't have enough memory and the paging replacement system is trying to provide it by paging.
Basically a live lock in a paging algorithm.

Locality (scope) - the pages a process is currently using
- A process works within a locality at any given time.
- A process moves from locality to locality over the course of it's life (some overlapping).
- A process can't make progress without the pages in that locality.
- If a process doesn't have enough memory for it's locality it will thrash.

Local frame allocation makes thrashing local to a process.

** Working set model **
- An attempt to define locality.
- A set of pages being used by a process over a given period.
- keeps degree of multi-programing as high as possible while preventing thrashing (If ∆ is set correctly)
- hard to calculate working set

How:
- Working set window: ∆ - an amount of time used to define the working set.
    - Accuracy of working set depends on how you define ∆
- Demand = sum of working sets for all processes
- Suspend a process when the demand is above the available memory

** Page Fault Frequency **
- Track page fault rate per process
- define upper and lower bounds
- take and remove frames from programs based on bounds
- suspend a process if a page fault rate is high and there are no free frames

#### I/O interlock
HUGE Problem!

1. Process makes IO request - waiting for IO
2. Process in CPU page faults
3. Frame from IO requests is returned to pool and allocated to process
4. IO returns and writes to frame that is linked to new process

Allow locked memory - locked memory can not be replaced
Never allow IO to user memory - double copying causes performance decrease.

Locking or pinning is often useful
- kernel
- databases
- low priority process that gets preempted by high priority processes never gets to use the frame it brought in from disk.
    - The LPP is constantly just requesting the frame (extra work for pager) and never executes... sad ;(

#### Other Efficiencies made possible by Virtual Memory

##### Copy-on-write
Pages can be marked as copy on write.
This allows new processes to be created without copying private memory block.
If either process edits the block a copy will be made before editing.
This is usually stored in a bit from the page table address.
Only modifiable blocks need this. Read only blocks can just use the original rw bit.

vfork: makes a copy of the PCB but not the virtual memory. The old process is halted and the new process uses the old processes virtual memory. This is useful for fork() exec() but can be dangerous if exec isn't called right away.

##### Memory-Mapped files

Any block on disk can be used as the backing store for a section of virtual memory.
A file mapped to virtual memory has all the same properties as the rest of virtual memory
- Efficient paging
- Efficient IO writes
    - Writes are done to memory and moved to disk as a block
- Copy on write for processes
- Shared between processes
- Read only between processes

Some systems implement MMF even over standard IO syscalls:
- mmap() maps to process memory
- read() maps to kernel memory

##### Memory-Mapped IO

Like with Memory Mapped files the IO registers can also be mapped to memory.
Memory is mapped to device registers and accessed by the device.

Control register: register in IO device that lets the CPU know the device is available

Ways for IO device and Memory-Mapped IO to work together:
- Programmed IO (PIO) - Pole the control register
- Constantly fill the memory - used by GPU's
- Interrupt driven - IO device sends interrupt when it's done

#### Kernel Memory
- Kernel needs access to physical memory block for certain operations like IO.
- Needs to manage memory the way any process would (inside a page)
- Has better knowledge of it's need so can allocate memory differently based on need.
- Kernel processes are almost always higher priority than system processes

Buddy system
- One chunk is split into two until it is the size needed for a structure
- lots of wasted space

Slab system:
- A separate cache for each type of kernel object (semaphore, PCBs, TBS, ect.)
- Each cache can span multiple slabs
- When the kernel needs an object it just asks the cache
    - caches are either empty, partial, or full
    - if one exists it is returned
    - if not a new slab is added to the cache
- No wasted space from fragmentation - The only wasted space is for not full caches
- Works best for objects that are allocated and deallocated often.
    - Instantiation is fast (return pointer). Destruction is free (mark as available)
- SLUB: Linux's optimized version of slab

SLOB (simple list of blocks)
- slob with 3 caches (small lt 256bytes, medium - lt 1024 bytes, large = lt x)
- first fit algorithm

#### Windows
Demand paging with clustering: page fault -> page and a few after it (IO efficient)
Memory management is done on a process by process basis.
- each processes is given a memory range on startup
    - working set minimum: the minimum amount of physical memory a process gets
    - working set maximum: the max pages
- local LRU: when a process is over it's max it must select a page to let go from it's own pages
- trimming: when the free memory is below the threshold processes are trimmed up to their minimum.


#### Study Questions

1. explain the concept of *virtual memory*, and discuss the benefits, implementation, and overhead.
    > Virtual memory is the idea that the logical memory understood by programs and the CPU does not need to parallel the physical memory on the system.
    > By having a translation from physical to virtual and back, sections of virtual memory can be kept on disk without the knowledge of the processes.
    > This allows the use of memory as a cache.
    > This also applies to any arbitrary file on disk
    > physical memory can be mapped into the virtual memory of multiple programs
2. define *demand paging* and *page replacement*.
    > demand paging
    >     A process is not all loaded at once into memory.
    >     When a process requests an address that is not in memory the pager fetches it from the backing store.
    >     In this way the process is loaded as it is needed
    > page replacement
    >     Because of demand paging the physical memory can be over-promised
    >     When we run out of physical memory a victim piece of memory is chosen to be replaced
3. describe the page replacement algorithms and strategies listed below in terms of algorithms, data structures, overhead, and benefits.
    - first-in first-out (FIFO)
    - optimal
    - least-recently-used (LRU) and variations
    - page buffering
4. outline the decision problems associated with frame allocation.
5. explain the phenomenon of thrashing and the strategies and techniques deployed to deal with this problem.
    > working set
    > - based on process locality
    > - a working set time is decided upon
    > - any references used during this time is known as the working set
    > - the demand is the total working set of all processes in a system
    > - When demand exceeds supply a process is chosen to be stopped.
    > frequency of page fault
6. describe how memory mapping files and shared memory operate in the Win32 API.
7. discuss the following factors that affect the character and performance of a paging system: prepaging, page size, program structure, and I/O interlock.

1. Why is virtual memory an important feature of modern operating systems?
2. What is page replacement? How should different page replacement algorithms be chosen?
3. How are memory-mapped files used for memory sharing?

- Try Exercises 9.3, 9.6, 9.8, 9.21, 9.27, and 9.32 of *OSC9ed*.

### 3.4 Mass-Storage Structure
OSC9ed: 10.1 to 10.9.

A file system can be viewed logically as consisting of three parts: the interface to the file system (for users and programmers), the internal data structures and algorithms for implementing the interface, and the secondary and tertiary storage structures. The first two parts were covered in Section 3.3; this section addresses the third. Secondary storage structure topics include the physical structure of disks, disk-scheduling algorithms, disk management (disk formatting, boot block, and bad blocks), and swap-space management. Section 3.4 also introduces RAID structure, stable-storage, and tertiary storage structure.

#### Key Concepts and Topics

- magnetic disk
    - logical block: smallest unit of transfer - usually 512 bytes
    - constant linear velocity (CLV) the head travels over the disk at the same speed no matter how far out it is.
    - constant angular velocity (CAV) the disk spins at the same speed
- host-attached
    - SCSI - small computer system interface
    - fiber channel (FC) - high-speed serial (1-128gb/sec)
- network-attached storage - over RPC - iSCSI pretends its attached
- storage-area network - NAS eats up bandwidth - SAN is a storage only network
    - storage is shared between servers
    - allows dedicated storage for servers

#### Magnetic Disk scheduling
OS is responsible for effectively using system resources including IO.
Disks are slow due to head movement and rotation.
It's possible to improve them with a good queue.

Modern disks don't usually give this kind of info to the OS.
Usually a bunch of requests are made and the device decides how to do them.
Sometimes order matters though so the OS sometimes sends one request at a time (critical write order)

Seek time: amount of time it takes to move the head over the cylinder
Rotational latency: amount of time it takes for the disk to rotate into place
Bandwidth: amount of data moved divided by the amount of time it takes to move it.

FCFS (First come first served) algorithm
- fair but not very efficient

SSTF (Shortest seek time first) algorithm
- performs well except for starvation
- Priority queue by head distance
- May cause starvation
- better than FCFS but not optimal

SCAN (elevator) algorithm
- sweeps back and forth across the disk servicing every request in its path
- when it starts to go back the area it did most recently gets done again.
C-SCAN (circular) variant
- sweeps in one direction than restarts at beginning
- performs well when heavily loaded
LOOK and C-LOOK algorithm don't actually sweep entire disk unless needed

#### Disk formatting

Low-level formatting or physical formatting:
- divide into sectors (blocks)
- header and trailer: holds Error Correcting Code
- data usually 512, can be 256, 1024

Logical formatting: creation of file system
- partitioning into groups of cylinders
- usually low-level blocks are chunked into clusters

#### swap-space management
Location
- large file in file system
    - easy to implement
    - inefficient multiple seeks due to traversing file system data structure
- raw partition
    - many different ways of implementing

Page slots - holds an Memory page
swap map - array of shorts, 0 = available, n = number of processes using this data

#### Other

Boot block: fixed location on disk where bootstrap program is stored
- computer firmware usually allows you to choose what IO devices you want to be allowed to boot from.
- usually the first sector of the hard disk
- (MBR) master boot record: the mini partition used by OSX and Windows for booting
- boot sector of a partition (first sector) - if a partition can be booted from this is where the boot loader will be.

Bad blocks: blocks sometimes go bad.
- Most of the time the hard disk will manage this.
- Sometimes OS's have to deal with it.
    - OS requests block of data
    - IO device checks the ECC and it is unrecoverable - notifies OS
    - OS flags block so that next time it reboots it tells the IO device to replace the block
- devices usually have spare blocks scattered throughout disk.
- slipping is sometimes used within a sector

Redundant arrays of independent disks (RAIDs)
    - parallel storage in order to increase access speed and redundancy
    - parity: ECC that can recalculate 4 bits for every 1 bit
    - data striping: keeping data across multiple disks increases access speed
    - bit-level striping: each disk holds one bit each, 4 disk accesses are needed for 1 block
    - block-level striping: each disk holds a sequence of blocks
        - getting 1 block accesses 1 disks
        - getting 4 blocks accesses 4 disks
    - RAID levels
        - 0 - block striping
        - 1 - mirroring
        - 0+1 - block striping then mirroring
        - 1+0 - mirroring then block striping
        - 2 - bit level striping with ECC
        - 3 - bit level striping with parity bit using knowledge of sector failures
        - 4 - block level striping with parity blocks using sector failures
        - 5 - spread parity across all disks
        - 6 - extra redundancy Reed-Solomon codes

Stable-storage implementation
- Disk write results in:
    - success
    - partial failure - in the middle of failure
    - total failure - failed before anything changed
- Recovery
    1. Write onto first block
    1. Write onto second block
    1. Declare complete
- Failure:
    1. Are they the same? nothing to do
    1. If one block contains an error than we replace with the other block
    1. If neither has error we replace first block with contents of second (rollback)

#### Study Questions

1. describe overall disk structure.
2. explain and compare several algorithms for scheduling disk requests, including FCFS, SSTF, SCAN, C-SCAN, and LOOK.
3. describe issues related to disk management such as disk initialization, booting from disk, and bad-block recovery.
4. describe swap-space management, disk reliability, RAID structure, and tertiary storage structures.

1. What is disk attachment?
1. Name several kinds of disk attachment, outline their differences, and outline their differences in usability.
2. What are the main disk scheduling algorithms, and how do they work?
3. What are the main tasks in disk management?
4. What are RAID levels, and how does one determine which level to use for a specific computer system?
5. What technologies are used in new tertiary storage devices?

- Try Practice Exercises 10.1 to 10.7 of *OSC9ed*
- Try Exercises 10.11, 10.13, and 10.17 of *OSC9ed*.

### 3.3.1 File-System Interface and Implementation
OSC9ed: 11.1 to 11.6.

The main criterion for a good file system is that it provide the user with convenient (user friendly), effective, and secure means of organizing and accessing his or her files. This section examines the file-system concepts familiar to most users, such as file names, file types, directory structures, and file protection. Section 3.3 also discusses some of the practical problems, block-allocation schemes, performance criteria, and backup and recovery schemes that system designers must consider when they implement file systems on disk.


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

1. explain the function of file systems and their interfaces.
2. describe the concepts of file, file attributes, file operations, file organization, and file access.
3. outline the different directory structures.
4. describe file system mounting and file sharing.
5. describe the nature of protection schemes, including the concept of owner, group, and universe (world) categories, and the concept of access lists.

1. What are the different file access methods? How are they related to
 file organization?
2. How does access control support file sharing and file protection?

- Complete Practice Exercises 11.1 to 1.9 of *OSC9ed*
- Try Exercises 11.10 to 11.13 and 11.17 of *OSC9ed*.

### 3.3.2 File-System Interface and Implementation
OSC9ed: 12.1 to 12.9.

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

6. explain the layered approach to file system organization.
7. describe the implementation of a local file system and directory.
8. explain contiguous, linked, and indexed disk allocation strategies, and the overhead, benefits, and problems associated with each.
9. discuss free-space management and its possible implementations.
10. discuss the importance of backup and recovery.
11. discuss efficiency and performance issues related to file systems and organization.

1. What are the drawbacks of a layered structure in a file-system
 implementation?
2. When would you consider designing a special file system instead of
 using the one distributed with an operating system?
3. What are the two most important functions of the Virtual File
 System (VFS) layer?
4. What are the problems associated with linked allocation of disk
 space routines?

- Complete Practice Exercises 12.1 to 12.8 of *OSC9ed*
- Try Exercises 12.11, 12.15, 12.16, and 12.20 of *OSC9ed*.
- Analyze a file system familiar to you, and list the features and characters introduced in this section.

### 3.5 I/O Systems
OSC9ed: 13.1 to 13.7.

Input-output (I/O) is one of the two main jobs of a computer (the other is processing/computing). This section briefly introduces I/O systems, including I/O hardware, services, and interfaces. It covers some concepts that are basic to computer systems such as bus structure, device drivers, direct memory access (DMA), kernel I/O subsystems, and I/O performance issues.

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

1. describe (briefly) I/O hardware components and mechanisms such as bus, interrupt-driven I/O cycles, and DMA.
2. outline and describe the main functions of the kernel I/O subsystem.
3. briefly explain how I/O requests are transformed to hardware operations.

1. How are data transferred between an I/O device and memory?
2. What is DMA, and why do we need it as an alternative to standard memory access systems such as programmed I/O?
3. What is the purpose of device drivers in operating systems?
4. What are the main tasks of the kernel I/O subsystem?

- Complete Practice Exercises 13.1 to 13.6 of *OSC9ed*
- Try Exercises 13.9, 13.10, and 13.12 of *OSC9ed*.

- Explore surveys and technical documents about the memory, file-system, mass-storage and I/O subsystems. Try to identify an existing problem of interest and a possible solution to it (you may continue this work in the following units until you find a suitable topic for Assignment 4 of this course).
- You may also explore Linux kernel to see what features it provides for file-system interface and implementation, storage management, and I/O systems. Share your findings and opinions with your classmates and tutor on the course discussion forum.


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

Unit 5 provides an extension to the core topics of operating systems. It introduces distributed systems and special-purpose operating systems such as real-time systems and multimedia systems. This extension introduces the ever-changing information technologies and products in which operating systems play an important role. In fact, with many operating systems, different versions are developed for different computing environments to meet the needs of different applications. For instance, both Linux and Windows have desktop, server, mobile, and embedded system versions for different devices and applications.

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
OSC9ed: 16

This section covers types of virtual systems, and differences in purpose and implementation. It is not that important to go into details of memory management and tables, as much as knowing general configurations and structure.

#### Key Concepts and Topics
Started with IBM trying to make their mainframes usable by multiple OS's.
- virtual machines: guest operating systems that 
- virtual machine manager (VMM)
    - type 0: hardware based systems like IBM LPAR and Oracle LDOM
    - type 1: purpose built OS based systems like VMware's ESX
    - also type 1: general purpose OS with VM capabilities, linux kvm, windows hyperV
- Paravirtualization: when a guest OS helps be a better guest (aka it knows)
- Emulators: 
- Disk partitioning
- Virtual machine control structure
- Control partition

##### Overall structure of VM's
VM's have been implemented by many companies using different systems.
All VMM's have certain things in common. This is what's considered the core of what it means to be a VMM.
These three tennants are that the VMM will provide an environment virtually identical to the system the original software would have run on, there is only minor efficiency losses due to virtualization, and the VMM maintains complete control of the underlying hardware.
By maintaining these three characteristics across all VMM's means that certain principles need to be maintained.
- virtualization can't rely on emulation for it's instructions and must instead provide processor parity to the guest OS.
- The virtual processor 
- virtual machines are 
The fundamentals of a 
- The Virtual Machine Manager (VMM) provides an environment that is basically identical to the system a guest would run on.
- There are only minor performance decreases compared with running on bare metal.
- The VVM maintains complete control of the underlying hardware.

Benefits:
- OS's are isolated from eachother. One bad program doesn't automatically have access to all the servers on the machine.

Disadvantage:
- Processes on different guests on the same machine can't share resources.
    - share file system volume .: files can be shared
    - virtual network of VM .: message passing (on the same machine, but through a software network)

- freeze / copy / restore (snapshots)
    - very easy in VMM's
- possible to develop the system a lot easier
    - snapshots
    - development is done on the VM.
    - multiple VM's can be running on a host at the same time, giving oportunity for faster iterations
    - Because a bad OS can cause a system crash, (and make it hard to reboot) It takes a long time to develop
    - with VM's this is easier because the VMM means that a system crash doesn't affect the host OS only the guest OS which can be easily be restored to a previous state using snapshots.
    .: decrease in System Development Time
    - multiple OS's on the same host make porting and testing programs easier across OS's because you don't have to boot up in separate modes each time you want to make a change.

- For data-centers VM's help to increase average load on the data-center by taking lots of smaller systems and putting them on a single large machine. The resulting machine is usually more cost efficient than the large number of smaller lightly used machines.
- VM templating allows for management of many more servers than is usually possible with a given number of people (100 servers with 20 VM's each = 2000 virtual servers)
    - managing the patching of all guests
    - backing up all guests
    - managing resource use
- VMM's usually provide a way for VM's to be ported form one VMM system to another without downtime.
    - This allows Systems with high workload to offload VM's to systems with lower workload.
    - This allows hardware that needs maintenance to offload VM's, get maintenence, then get VM workloads back, without interruption to service.
- With these benefits it almost becomes more beneficial for each application to run in it's own machine and for that machine to be tuned for the workload being managed. The result is that the VM revolution has changed the way apps are developed.

##### Building blocks
VCPU: the state of the CPU according to the VM.
The VCPU acts much line the PCB does but for the system as a whole.

Because of User Kernel mode, the VCPU must also be able to track a virtual user and kernel mode.
This is accomplished by catching exceptions thrown when a guest OS tries to execute a privileged instruction.
When a guest OS executes a privileged instruction it thinks it's in kernel mode, however, it is still in guest mode. The CPU throws a trap because this is an error. The trap is then handled by the host OS and the action the Guest was trying to do is emulated for them.
All non-privileged instructions run on the hardware at the same speed running on bare metal would give you, however, because of the trap and emulate, privileged instruction do not. This is where the performance decrease comes from! Plus it might be sharing the CPU between multiple VM's meaning more slowdown.
- Software solutions
    - Binary translation: Then in user-mode the CPU executes normally. When in Kernel mode the host analyses the next few instructions and swaps privileged instructions for an equivalent non-privileged instructions/ system calls.
        - Very hard
        - caching makes this better
    Another problem page tables
    - nested page tables (virtual page tables like the vCPU)
        - increase TLB misses
- Hardware solutions that help this problem.
    - extra-modes (taken away from VCPU management)
    - triaged privileges (CPU's have larger range in what the can allow)

- Virtual machine control structure (VMCS) is a hardware accelerated way to increase performance.

Intel and AMD both provide hardware solutions for:
- vCPU: host and guest mode in CPU alongside kernel/user mode
- NPT in hardware: 
- IO: hardware is aware of sections within the VM making it possible for an guest OS to use DMA.
- Interrupt remapping: sends the right interrupt to the right guest OS without VMM interference.

##### VM's implementations
Startup:
- the VMM defines the system available to the VM
- VMM makes the VM 'hardware'
    - in type 0: hardware is dedicated so if the resources don't exist the request will fail.
    - in type 1: hardware might be virtualized based on the type of resource. Often vCPU's are multiplexed onto physical CPU's. Memory is also often virtualized. IP addresses on the other hand cannot be shared.
- The VMM then starts the VM with the image provided. Instead of an installation disk, VM's are usually a ready to run OS environment that don't require the initial setup steps. This results in lightning fast startup times. Just copy the image and start execution.

Type 0 Hypervisor
- proprietary
- hardware
- limited features
- dedicated hardware

Type 1 Hypervisor
- Software
- hardware assisted
- possible to virtualize CPU's, memory, networking, IO
- also possible to have dedicated CPU, and others
- Most used
- custom proprietary (VMware, XenServer)
- general (Windows, Linux)

Type 2 Hypervisor
- Poor overall execution because it's just a process
- good for experimentation

Paravirtualization
A guest knows it's being virtualized and plays ball.
- Can help increase performance especially of IO using a shared buffer.
- requires complicated recompilation of OS instructions
Xen is no longer using this and is instead using the hardware accelerated solutions.

Virtual programming environment
- Java Virtual Machine (JVM)
- a set of instructions
- virtual environment based on a set of API's

Emulation
- 10x slower
- each non native instruction can take up to 10 instruction in a new architecture.
- easy to make mistakes in the emulator since you need to create a software implementation of a hardware device.

Application Containment
- if the main goal is Application containment and portability, sometimes other solutions are better
- applications think they are the only process running on the system.
- might have their own networking, IO, memory, CPU, system and user processes.
- many implementations (Redhat Jail, Solaris zones)


##### OS components in VM's
CPU scheduling:
- multiprocessor system
- vmm or guest threads
- overcommitment -> more vCPU than CPU's 
- timers can drift since they aren't running on a hardware CPU
- realtime systems suffer the most
- sometimes counteracts the scheduling optimizations that the guest OS does

Memory use:
- Efficient memory use is very important for an efficient machine
- VMM's often over commit memory
- guest thinks it's hitting a page-table, when it's actually hitting a nested page table (npt)
Some solutions for over-commitment of memory
- npt tell the guests pt where to look
    - when system is full, npt swaps to disk. Guest thinks memory is still in memory.
    - downside: VMM has less info about memory usage so swapping is less efficient.
- sudo-device driver or kernel module (balloon method)
    - when memory gets low on the system.
    - driver or module requests chunk of memory from guest
    - memory is pinned in the OS's page-table
    - Since VMM knows memory won't be used by guest it allocates it elsewhere
    - guest manages it's own memory knowing it has less.
- doubling up on memory
    - many functions use the same block of memory over and over again (text for the linux kernel)
    - hashes of the memory are taken and compare.
    - if a hash matches the entire block is compared
    - both guest OS's get a pointer to one read-only version of the block.

IO drivers: device drivers and devices allow a lot of flexibility in their implementation
- the host presents a simple IO device to the guest that is actually backed by a more complicated IO device
- or the host has it's own custom driver that acts as an intermediary between the guest and host for IO.

networking IO
- bridging: guest is seen by outside world
- NAT (Network Area Translation) local to the machine but allows for external connections

Booting
- type 0 hypervisor: dedicated hardware makes this possible but also less flexible
- type 1 hypervisor: stores a virtual disk, which has it's own bootloader
    - virtual disk allows easy copying and migration
- type 2 hypervisor: keeps this info within the host filesystem

Live migration
- with type 1: very little noticeable disruption
How?!
- connection between source and destination is established
- dest creates vCPU
- src sends all read-only pages
- src sends all rw pages, marking them clean
- loop over rw pages and resend modified pages
- as the loop gets tighter and tighter eventually the src will decide to move it.
- stops the vm, sends final rw pages, current vCPU state, tells dest to start running

##### Compare VMware and JVM

###### VMware workstation
- type 2 hypervisor

###### JVM
- Programming-environment virtualization
- Java virtual machine (JVM)
- Memory overcommitment
- Network address translation (NAT)
- Bytecode
- Garbage collection

Because it's a 

Implements JIT compilation

#### Study Questions

1. describe various virtual machines technologies.
2. describe methods used to implement virtualization.
3. list the most common hardware features that support virtualization.

1. What are the three types of traditional virtualization?
2. What are four benefits of virtualization?

Find some articles and technical documents on modern virtual machines.
Explain the reason behind the recent success of virtual machines, although they have been around for a long time.
What forms of virtualizations are expected in the future?

## Assignment 4

This assignment should be submitted after you have finished Unit 5. It is worth 15% of your final grade for this course.

**Part 1: Concepts (20 marks; 4 marks each)**

Please answer the following questions in complete sentences. Your answer for each question should be about 150 words.

1. Why is it important to distinguish between mechanisms of protection and policies of protection?
1. What is an access matrix, and how can it be implemented?
1. How does a virus differ from a worm?
1. What is the difference between symmetric encryption and asymmetric encryption?
1. What are the two main varieties of authentication algorithms?

**Part 2: Research Project (80 marks)**

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

**Research Paper Your investigation will be based on recent publications (i.e., published in the past five years) such as journal/conference papers and technical documents, and the applicable software packages (open source preferred). You are encouraged to read some papers about new techniques in operating systems. You can access the following resources via the ACM Digital Library and IEEE/IEE Electronic Library databases in the Athabasca University Library.**

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
