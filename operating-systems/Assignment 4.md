# Assignment 4
### By: Ian Edington
### Student ID: 3236986
### Date: July 31th, 2017

## Part 1: Concepts

#### 1. Why is it important to distinguish between mechanisms of protection and policies of protection?

A protection policy defines the actors and the actions of a system and defines which actors can take what actions.
In short it defines what should be done.
Because policies deal with actors and actions they change over time as actors move into different rolls and actions are added and removed from a system.
A set of actors and actions are also different from system to system.

A protection mechanism is the process or enforcing which actor can make what action.
Essentially, how should it be done.
A well designed mechanism can often be used to implement many different security policies.

It is important to distinguish policies and mechanisms because by separating the what from the how it is possible to design more general mechanisms that can implement a broader spectrum of policies.
A secure system requires, among other things, both secure policies and secure mechanisms.

#### 2. What is an access matrix, and how can it be implemented?

Access matrix defines a set of domains, objects and privileges on objects.
It can be visualized as a domain by object matrix which defines the access any given domain has to an object.
Domains can also be objects allowing one domain to switch to, or modify another domain.
The access matrix should also be an object, allowing a domain to add an change objects and domains.
The matrix defines who can change what in the access table.

Many implementations of access matrices exist including a global table, access lists for objects, capability lists from domains, object locks and domain keys, and a hybrid access list with capability cache.

Global tables are simple to implement but are usually too large for main memory and result in poor performance due to their size. They also make it difficult to group objects since modifications need to be made to every object.
- Access lists for objects are easy for an object owner to use, make it possible to quickly determine if a user has access to a object they request, and revocation is immediate. However, they make it very difficult for a user to know all the objects it has available to it.
- Capability List for domain are the useful for processes since a process knows exactly what is available to it. However, it makes it hard to revoke a capability because it needs to be done on every capability list it exists.
- A lock and key - Domains have a list of keys, objects have a list of locks and if a key fits the lock it give access. This model is effective and flexible, but is also very complicated to implement.
- The Hybrid capability cache with access list storage builds list of capabilities as the process is executing. This has many of the benefits of the access list and the capabilities list, however, revocation time is longer because of the cache.

#### 3. How does a virus differ from a worm?

Worms are standalone programs that use the spawn (or fork) function in order to clone themselves.
Target systems are often identified based on some property of the current system the worm is on.
In order to infect a new system a worm will exploit a weakness in the system and install a grappling hook.
This hook then loads the worm.
Also noteworthy, since a worms uses a fork method to spawn an instance on a new computer it does not require installation on the host system and might not even leave any trace on disk.

Viruses are small executables that are attached to a host executable and direct the startup flow of control from the executable to the virus and then back to the executable.
In this way, every time the effected executable runs the virus is executed.
Viruses spread by copying themselves into the execution sequence of other existing program on a system, as well as programs or files leaving the system.
Viruses differ from worms in their execution method, they also differ in how they are transmitted. Viruses require human interaction in order to infect a system, so they often travel by email attachment, USB stick, and programs downloaded from the internet.
Because they rely on modifying executables most UNIX systems aren't susceptible to viruses, compared to worms that thrive in the constant execution environment of UNIX systems.

#### 4. What is the difference between symmetric encryption and asymmetric encryption?

Encryption is the process of protecting data that is sent from one location to another, when it might be intercepted and deciphered by another entity.
The earliest known cryptographic cypher dates back to 1900 BCE.
Almost all methods have used symmetric encryption.
It was only recently that asymmetric encryption was discovered.

Symmetric encryption uses a key in order to encrypt a block of stream of data.
This data can then be sent, in public, to another location and decrypted using the same key.
These encryption methods tend to be fast compared to asymmetric encryption.
The limitation to this process is that the key must be transported securely from one location to the other location.

Asymmetric encryption encrypts a message using the public key of a targeted system.
The public key can be made known publicly because once a message is encrypted only the private key is able to decrypt it.
This method makes it possible for messages to be sent back and forth with the need for securely transporting an encryption key.
However, asymmetric encryption is more computationally intense than symmetric encryption.
For this reason, asymmetric encryption is often used to start a connection during which a symmetric key is shared. The rest of the connection can be encrypted using the shared symmetric key for that session.

#### 5. What are the two main varieties of authentication algorithms?

Authentication algorithms compliment encryption by providing a way of knowing that a specific message came from a specific source.
Instead of encrypting the message the message a signature derived from the message using a key in order to prove the authenticity of the source.
The two main types of authentication algorithms are symmetric and asymmetric authentication.

A Message-authentication code (MAC) uses a checksum to authenticate a long message. The checksum is derived from a hashing function that takes a key as a parameter. By sharing they key, another entity can verify the checksum of the message. However, like with symmetric encryption, this relies on securely sharing a key.

A digital-signature algorithm uses a similar hash function but instead of using a symmetric key, it uses an asymmetric key. The resulting checksum is called a digital signature and can be verified using the public certificate provided by the source. The private certificate is the asymmetric key used in the signing.
