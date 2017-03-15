# Course Handbook
Student ID: 3236986
## OOP Theory
An object has state, behavior and identity.
- Everything is an object
- Every object has a type.
- Every object of a specific type can receive the same messages.
- Objects can (have their own memory of | know about) other objects.
- A program is a bunch of objects (telling eachother what to do | interacting with eachother).

### Languages in General
All languages are abstraction
    LISP: all problems can be broken down to lists
    APL: all problems are ultimately algorythmic
    OOP: all problems can be broken down to objects and actions
    Functional: same as APL
Downside is that each abstractions is bias.

### Objects have an interface:
A way for other Objects to interact with them. Accessible methods and members.
There is also an implementation.

### Object implementation:
For every object interface there is an internal way that the object provides the answer.

### Hiding of object implementation:
The object should hide as much of the internal workings of the object as is reasonable.
This reduces other programmers ability to abuse your classes and create dependencies on parts that will change in the future.
What are two reasons for controlling access to members of objects and how does Java implement control? (See TIJ page 31.)
- restricts possibility of external objects dependency on an objects implementation
    - Keeps client programmers hands of parts they shouldn't touch
    - Allows object designer to change internal working of object without affecting users of object
- implementation: class and member modifiers

### Object as service provider:
- You program provides services to a user
- it does this by consuming services from other objects

### Object oriented design:
To solve the problem this way ask, "what objects, if they exist, would solve my problem right now".

### Object Composition:
Putting many objects together to form a whole. An icicle game is made up of many icicles, a player, a scoreboard, ect.
Best expressed with a "has-a" relationship. A car has an engine.

### Object Reuse:
Once an object is well designed it is possible to reuse it in other scenarios. A stick man in a falling icicles game could be reused in a running man game, IF it is well designed.
This is much more difficult in practice than in theory.

### Object Inheritance:
One class inherits from another type. Best expressed as an "is-a" or "is-like-a" relationship: a circle is a shape.
The base class (shape) defines an interface and implementation. The derived class (circle) inherits the interface and implementation. It can change the implementation, and add to the interface (is-like-a), but can't remove from the interface.

### Object Polymorphism:
An object can be treated as any of it's base types. A circle can be treated like a shape.
This makes is easier to write programs because if you write a method that consumes a shape, instead of a circle, you can then extend the shape to be a square and the same method will work.
**late binding:** This is accomplished using late binding. At the time of compiling the compiler doesn't know which methods and functions are going to be called. In C and other early languages compilers used to hard code the function that was going to be called (early binding). Late binding is in every language I've used.
Late binding (aka dynamic binding). Instead of calling the method directly late binding calls a method-call mechanism which finds the function to call, based on the object.
Polymorphism extensively uses up-casting.

1.  How does late binding enable upcasting and polymorphism? (See TIJ pages 38 to 43.)
Late binding enables a language to delay specifying the exact function to be called until runtime. This is done using a function that determines based on runtime information which function to call based on the function signature. Since this is done at runtime, and the object who's function is being called is part of the signature, the function-caller function can call different functions based on which object is passed. If a circle object is passed to a shape Type, the circle object's function will be called instead of the base shape function because the function-caller is passed the circle object along with the rest of the signature.

### Object Singly rooted hierarchy:
Every Java object extends `java.lang.Object`
C++ does not have this. This is technically more flexible but creates more complexity. They can have many base objects, which creates a need for multiple inheritance.
It means every object has a base interface in common.
    ie. Much easier to implement Garbage collection.

### Containers (aka collection):
An object that holds other objects. (map, list, set, trees)

Why so many containers?
- Different interfaces: Not all containers implement the same interfaces. Sometimes it's worth changing containers for a different interface.
- Different Performance: containers have different underlying data structures which preform tasks at different speeds.

1.  What is a container? What is an advantage of using a container? (See TIJ page 44.)
    - a container is a object that holds other objects. A container is useful because it helps programmers organize many of the same type of object. You often don't know how many objects you'll need and how long they will be needed. Containers provide a way to hold an arbitrary quantity of objects for an arbitrary amount of time.

### Generics
1.  What is 'parameterized types/generics'? Explain how it eliminates the need for downcasting.

Before SE5 containers help the Object object, which lead to a lot of down-casting.
Down-casting is dangerous because it often leads to runtime errors when the wrong kind of object is stored in the container or the wrong kind cast is applied. These won't be caught by the compiler.

The solution is called a "parameterized type" mechanism, aka generic.
Instead of up-casting to Object, down-casting to Type, and tracking it all, you declare the container with a specific type.
That Type is the only type a container can hold. It essentially gives a new base type for the container.

### Exception handling
Often not built into languages
This is a core feature in Java.
1.  What is function of exception handling and how does Java reinforce consistent use of handling exceptions? (See TIJ page 49.)
    - seperate execution path
    - enforced by language, if you don't use their system your exceptions won't work.
    - can't be ignored
    - able to recover from an error
    - single acceptable way to report errors

### Concurrent Programing
Breaking problems into multiple pieces works well in Java. However, there is still the issue of resource locking.
2.  What are the functions of threads in single-processor and multi-processor environments? (See TIJ page 50.)
    - In single-processor architectures, tasks or threads serve to break up the program into chunks that can be scheduled on a processor.
    - In multi-processor architectures, these tasks can be scheduled to different processors and run concurrently. However, special care needs to be made when multiple threads need access to the same resource.

### Client/Server
Client side: applet and Java Web Start
- mostly useful in Intranet/Enterprise situations. Mostly replaced by JS.
Server site: JSP's and Servlets
- in wide use today.

1.  What is the primary idea of a client/server system? (See TIJ page 51.)
    - The state of a program resides on a central computer(server), and the user interface runs on computer local to the user(client). The logic of the program often resides mostly on the server side, however, many applications have a mix of both sever and client side logic.
2.  How did Web serving lead to client-side programming? (See TIJ pages 52 to 53.)
    - For a long time much of the web served static documents, however, as more and more people and companies started using it there was a demand for interactivity. HTML had some interactivity built in. However, the limited bandwidth, cost of servers, and the powerful clients, made the server workhorse paradigm less appealing. By off loading some of the tasks to 
3.  What is CGI programming and what is its major shortcoming? (See TIJ pages 53 to 54.)
    - Common Gateway Interface is a standard for command line programs to interact with a server in order to create html. Was the original way to generate html, often standalone programs written in perl, python, or other languages.
4.  Why is client-side programming efficient for the Web? (See TIJ page 54.)
    - reduces the load on servers, allows faster user experiences.
5.  What is a plugin? (See TIJ page 54.)
    - an add on program to a browser that lets arbitrary code run on your machine from a server.
6.  What is a scripting language? (See TIJ page 55.)
    - a language where it's possible to make very specific actions happen within a larger program. ECMAscript is the best example of this. Simple instructions can be inserted into a document to make very specific changes.
7.  Compare scripting languages to Java for Web page needs. (See TIJ pages 56 to 57.)
    - Java however, is a full OOP language and generally holds the entire program in one body of code.
8.  What are the issues of Intranet versus Internet programming? (See TIJ page 58.)
    - Intranet you generally have more control over what clients are in use. Because of this control it's possible to implement client server apps that would have large barriers to entry for general use.

TODO: What is the role of Java in server-side programming? (See TIJ pages 59 to 60.)

## The Java platform
Completely abstracted hardware.
The JVM is built for each environment but once it's built everything else runs on top of it.

### Memory allocation
What are the roles of registers, the stack, the heap, constant storage, and non-RAM storage in Java programming? (See TIJ pages 63 to 64.)
    - registers: memory inside the CPU. Very fast and very limited. Java manages this for you.
    - the stack: maintained in RAM, maintains the execution pointer primitives, and object references. Java needs to know at the time of running the program the exact size and lifetime of items in the stack.
    - the heap: maintained in RAM. Holds objects. Much more flexible in the size and lifetime of items, however, this comes at the price of speed. This is slower than stack memory.
    - constant storage: Sometimes put in ROM for embedded systems but usually kept in RAM.
    - non-RAM storage: anything that will maintain state outside the object. Streamed objects and persistent storage are two examples.
Memory allocation and garbage collection is done using a multi-generational approach.
Objects are allocated quickly by bumping a pointer by the fixed amount and returning the location.
This is done in a "young" generation heap also called the nursery.
Once the nursery is full objects that are still in use are moved to a second generation heap and the nursery pointer is returned to the start of the nursery.
Since most objects are extremely short lived this strategy allows for quickly allocating and overwriting objects without much movement of objects.

#### Garbage Collection
Many Garbage collection methods exist, each with +ves, and -ves.

##### Mark and Sweep
1. Go through storage, marking items that are in use.
2. Stop program
3. compact only items at the top of memory

Good when objects are stable (don't have to move large, stable objects)

##### Stop and Copy
cons:
- 2x heaps needed (one for origin other for copy too)
- Needs to copy entire block even if it's mostly stable objects

Not good when objects are relatively stable

##### Adaptive generational stop-and-copy mark-and-sweep
Best of both worlds, maintains information about how a M&S or S&C is working and switches between them for more efficiency.

3.  Where in memory does Java create objects? (See TIJ pages 47 to 48.)

### Tools of the JDK
javac - compiles code
java - runs code
javas- reveals source code
jar archiver

### JIT (Just in time compiler)
Partially or fully converts to machine code so the JVM doesn't need to interpret the code.

Lazy Evaluation
- only compile parts when they are needed
HotSpot Technology
- compile a piece of code a little better every time it runs

## Language Basics

### Reserved names
Reserved names:
    special values
        true
        false
        null
    primitives
        boolean
        char
        byte
        short
        int
        long
        float
        double
        void
    control structures
        if
        else
        for
        do
        while
        case
        default
        break
        continue
    method
        return
    classes
        class
        new
        extends - defines class as a sub-class another class
        this
        super - like this but refers to super-class constructor
        instanceof - checks if an object is an instance of a class or any of it's sub-classes
        interface - Defines an object API
        implements - defines a class or interface as implementing a specific or multiple interfaces.
    class modifiers
        public
        protected
        private
        static
        abstract
        final
    exceptions
        throw
        throws
        try
        catch
    packages
        import
        package

assert
const
goto
enum
finally
native
strictfp
switch
synchronized
transient
volatile

### Variable Declaration
All variables must be declared before they are used.
There are two main types of variables; primitives and objects.
Objects are actually pointers(references) to a data structure, whereas a primitives is the data.

### Assignment

```
    = //straight assignment
    op= //assignment while performing operation (op)
        //x op= 2 is equivalent to x = x op 2
```

For primitives the data is copied to another memory location.
For objects only the pointer is copied.

For Objects this means making a replica of the **pointer**.<a name="object-assignment"></a>

### Casting
Two types. Explicit and Implicit.
Implicit casting happens when operations produce a larger object and that larger object is expected

```
int i = 42;
double d = i; // implicit casting from int to double
i = d; // implicit cast results in loss of precision; compile error is thrown
```

Explicit casting can be done anywhere there is implicit casting however it is necessary where a casting would result in loss of precision. `(type) exp` is the general form.

```
i = (int)d; // forces the casting and loss of precision;
```

Strings break this rule. Explicit casting to a string is not allowed.

```
String s = 22; // this is wrong!
String s = Integer.toString(22); // this is good
String t = (String) 4.5; // this is wrong!
String t = "" + 4.5; // correct, but poor style
String u = "Value = " + (String) 13; // this is wrong!
String u = "Value = " + 13; // this is good
```

#### Casting types, object and interfaces
Moving to a more generic datatype does not need an Explicit type cast. (widening conversion)
    - correctness can be checked by compiler
Moving to a more specific datatype needs an Explicit type cast. (narrowing conversion)
    - must be tested by java run time environment
    - throws ClassCastException if not the correct type

```
// example of widening conversion
CreditCard card = new PredatoryCreditCard(...);
// example of narrowing conversion with explicit cast
PredatoryCreditCard pcard = (PredatoryCreditCard) card;
```

A narrowing conversion happens when a type T is converted into type S given:
- S is a subclass of T
- S is a subinterface of T
- S is a class that implements the interface T

**instanceof is a useful operator when working with object casting**

#### RTTI Runtime type identification
Downcasting sometimes causes errors. There is type checking during runtime on downcasts. If the wrong type of object occurs an error with be thrown.

### Comments
Three types of comments

`//` start inline comment: ignore everything after these characters

Comment block: starts at `/*` ends at `*/`

```
/*
 * This is a block comment and is not read by automatic documenting tools.
 */
```

Javadoc Comment block: starts at `/**` ends at `*/`

```java
/**
 * This is a block comment that is parsed by the javadoc and other automatic documentation tools.
 *
 * @author text: Identifies each author (one per line) for a class.
 */
public class SomeClass {
    /**
     * This is a method comment that will be attached to the method below
     * @throws exceptionName description: Identifies an error condition that is signaled by this method.
     * @param parameterName description: Identifies a parameter accepted by this method.
     * @return description: Describes the return type and its range of values for a method.
     */
    public someMethod(){
        // something here
    }
}
```

### Primitive types (Base Types)
bool, char and 6 number types:

- `boolean`: a boolean value (`true` or `false`)
- `char`: a 16-bit unicode character value
    - denoted with single quotes: `i`
- `byte`: 8-bit signed two's compliment integer
- `short`: 16-bit signed two's compliment integer
- `int`: 32-bit signed two's compliment integer
- `long`: 64-bit signed two's compliment integer
- `float`: 32-bit floating point number
- `double`: 64-bit floating point number
- `void`: nothing (used in methods)

For larger floats or integers checkout BigInteger and BigDecimal. Same as int or float but arbitrarily accurate.

Initial values:
When a primitive is declared in a method, Java does not guarantee primitives values. A compile time error will occur if a primitive is used without being initialized.
When a primitive is declared as a member of a class. The variable is initialized with an initial variable.

Wrapper Types:
Each primitive has a corresponding wrapper object type. This is because many datastructures and algorythems in Java are specifically designed for objects, not primitives.

Autoboxing(SE5): Automatic boxing and unboxing is the process of converting from primitive to wrapper and back.
The result is that you can use the primitive and wrapper class interchangeably.

|Primitive|Wrapper Type|Class Initial Value|
|--|--|--|
|boolean|Boolean|false|
|char|Character|‘\u0000’ (null)|
|byte|Byte|(byte)0|
|short|Short|(short)0|
|int|Integer|0|
|long|Long|0L|
|float|Float|0.0f|
|double|Double|0.0d|

### Scope
Scope is determined by the placement of curly braces.
Variables defined in an outer scope cannot be redefined in an inner scope.
Since primitives are created on the stack they are destroyed when the scope ends. Objects however, can exist past the end of the scope by passing a reference back to the receiving function.
```java
{
    int x = 12;
    // Only x available
    {
        int q = 96;
        // Both x & q available
        int x = 96; // Illegal
    }
    // Only x available
    // q is "out of scope"
}
```

### Expression Literals
Constants in the expression

- **null**: only object literal, allowed to be any object type.
- Boolean: **true** and **false**.
- Integer: whole number, `1`, `23984`
- Long: number with trailing L, `1L`, `1l`
    - lowercase l looks like 1, use uppercase L by convention
- Floating point: number with trailing f, `23f`, `23.00239F`
- Double: number with dot, or trailing d, `23.23`, `23d`
- Octal: leading zero, `01771`
- Hexadecimal: leading 0x, `0x23af`
- Exponential: `1.39e-43` defaults to double, add `f` for float

- Character: surrounded by single quotes
    - '\t' (tab)
    - '\b' (backspace)
    - '\f' (form feed)
    - '\n' (newline)
    - '\r' (return)
    - '\'' (single quote)
    - '\"' (double quote)
    - '\\' (backslash)
- Strings: surrounded by double quotes

### Operators

#### Arithmetic (mathematical)

```
    - unary minus: reverses sign of number (* -1)
    ∗ multiplication
    / division (int division truncates rather than rounds)
    + addition
    − subtraction
    % the modulo operator
```

#### Increment and decrement

```
    ++i : add 1 to i then preform expression i is involved in
    i++ : preform expression i is involved in then increment i
    --i :
    i-- :

    // given
    i = 1;
    j = 5;

    j = i++; // is equivalent to
    j = i;
    i += 1;

    j = ++i; // is equivalent to
    i += 1;
    j = i;
```

TODO: what happens when there's multiple ++ operators in a single line? Follows the operator order.
ie:

```
    a[5] = 10;
    j = 5;
    a[j++] = a[j++] + 2;
```

#### String Concatenation

```
    + string concatenation
```

#### Relational
```
    < less than
    <= less than or equal to == equal to
    != not equal to
    >= greater than or equal to
    > greater than
    == equal, for objects this compares references only.
```

#### Logical
Can ONLY take boolean values, unlike python, JS and others.

- ! not (prefix)
- && conditional and
- || conditional or
- boolean-exp ? exp-0 : exp-1;
    - see Ternary Operator

#### Bitwise (for boolean and integer variables)

```
    ∼ bitwise complement (prefix unary operator)
    & bitwise and : 1 if (1,1) else 0
    | bitwise or : 0 if (0,0) else 1
    ˆ bitwise exclusive-or: 1 if (1,0) or (0,1) else 0
    << shift bits left, filling in with zeros
    >> shift bits right, filling in with sign bit
    >>> shift bits right, filling in with zeros
```

### Operator precedence

Operators on the same line are evaluated in left-to-right order.
Except for assignment which is done in right-to-left order.

Operation Precedence Reference table:

|Operator Precedence|
|-|-|-|
| | Type | Symbols |
|1| array index method call dot operator | [] () . |
|2| postfix ops <br/> prefix ops <br/> cast | exp++ exp−− <br/> ++exp −−exp +exp −exp  ̃exp !exp <br/>(type) exp
|3| mult./div. | ∗ / % |
|4| add./subt. | + - |
|5| shift | << >> >>> |
|6| comparison | < <= > >= instanceof |
|7| equality | == != |
|8| bitwise-and | & |
|9| bitwise-xor | ^ |
|10| bitwise-or | \| |
|11| and | && |
|12| or | \|\| |
|13| conditional | booleanExpression ? valueIfTrue : valueIfFalse |
|14| assignment | = += −= ∗= /= %= <<= >>= >>>= &= ^= \|= |

### Logical Control Flow

#### Ternary Operator

    boolean-exp ? exp-0 : exp-1;

Returns exp-0 if true, exp-1 if false.

This is both a control structure and an operator:
- Control Structure: Allows different execution paths based on logic expression (Does not evaluate the other expression).
- Operator: Returns the value of the evaluated expression.

    Type var = boolean-exp ? exp-0 : exp-1;

Both expressions must return the same type.

#### If
Single statement bodies don't need curly braces

```java
if (firstBooleanExpression)
    firstBody
else if (secondBooleanExpression) {
    secondBody
    withTwoLines
} else
    thirdBody
```

#### Switch
Evaluates expression which must result in an integer, string, or Enum.
Jumps to case that matches that result, or the default expression.
Brake statement must be used to exit the switch once the code is finished.

- especially useful with Enum types
- no curly braces are needed

```
switch (expression) {
    case result1:
    case result2:
        System.out.println("This is tough.");
        break;
    case result3:
        System.out.println("This is getting better.");
        break;
    default:
        System.out.println("Day off!");
}
```

### Loop Control Flow

#### While Loop

```
while (booleanExpression)
    loopBody
```

This example advances through an array data until it finds the value target or reaches the end of the array and exits.
```java
int[] data = {1,2,3,4,5};
int target = 3;
int j = 0;
while ((j < data.length) && (data[j] != target))
    j++;
```

#### Do While
Same as While but executes body once before evaluating.
Most useful where the condition is dependent on the body code.

```
do
    loopBody
while (booleanExpression)
```

#### For
```
for (initialization; booleanCondition; increment)
    loopBody

for (int i = 0, j = 5; i < length; i++, j += 2) {
    loopBody
}
```
- variables define in initialization step are only available in loop scope
- booleanCondition is checked at beginning of loop
- increment is executed after the loopBody and can be any valid statement including empty.
- Multiple variables of the same type can be initiated and iterated over using the comma operator

#### For each (JE5)

```
for (elementType containerElement : container)
    loopBody
```

- container must either be an array of `elementType` or a collection that implements the Iterable interface.
- containerElement is assigned next element in the container and is scoped to the loop
    - regular assignment rules apply as per [object-assignment](#object-assignment)

### Breaking Control flow (continue, break, and label)
`continue` moves flow of control to the end of the loopBody
TODO: does `continue` execute the condition at the end of a do-while loop?
`break` moves flow of control out of a switch, for, while, or do-while
If you need to break out of multiple loops you can use a label.

```
label1:
outer-iteration {
    inner-iteration {
        break; // only breaks out of inner-iteration
        continue; // continues the inner-iteration
        continue label1; // continues the labeled iteration
        break label1; // breaks out of the labeled iteration
    }
}
```

### References
Basically a hirerachie of what can be garbage collected. This allows limited interaction with the garbage collector.
1.  What are the three types of **References** and what are their differences?
    Strong - default reference type. Cannot be garbage collected.
    Soft - can be garbage collected IF there is no more room on the heap.
        Soft references are for implementing memory-sensitive caches
    Weak - Still accessible but doesn't prevent the object from being reclaimed.
        weak references are for implementing canonicalizing mappings that do not prevent their keys (or values) from being reclaimed
    Phamtom - underlying object is unreachable. It is only useful for knowing if an object has been finalized. Doesn't stop it from being garbage collected.
        phantom references are for scheduling pre-mortem cleanup actions in a more flexible way than is possible with the Java finalization mechanism.

## Object Lifetime

### Class Loader
Searches for the \*.class file. Other Class Loaders exist that might search in areas other than the default database. Chain of class loaders.
The default class loader searches for a \*.class file in the \$CLASSPATH
Loads "trusted" classes.

### Initialization
Unlike other languages java files are not loaded until they are needed. They are needed when the first static member is called that can't be a compile time constant.

Compile time constants are final static primitives that don't depend on initialization for their value.

Static Initialization, First time Class is used:

Initialization of the Class object:
The first time a static class member is referenced the class loader searches for it's \*.class file.
The \*.class bytecode is checked for correctness.
1. Loading, performed by the classloader. Finds the bytecodes and creates a Class object from those bytecodes. All methods are stored.
1. recursive: If extending a class the base class gets initialized here. Linking.The link phase verifies the byte codes, allocates storage for static fields, and if necessary, resolves all references to other classes made by this class.
3. Initialization. If there’s a superclass, initialize that. Execute static initializers and static initialization blocks.

Initialization of the instance object:
1. Object field memory is allocated on the heap and wiped to zero's
1. recursive: If extending a class the base object gets initialized.
1. fields declarations and initializations are executed in sequential order
1. constructor is called see \<init\> methods

TODO: make proof class for this initialization sequence

All objects are created on the heap, specifically they are created in the nursery to begin with.

### Cleanup
When using external resources sometimes objects need to be cleaned up. Since there is no destructor in Java this needs to be done manually with a method. Similar to managing memory in C/C++, but without a destructor. `dispose()` seems to be a loose convention.

If you override `dispose()` you should call the base-class dispose using `super.dispose();`

Objects should be disposed of in reverse order of creation, for dependency management.

### Garbage Collection
See finalize()

## Object Basics

### Class, Method, and Field Modifiers
Best practice: default to `private`, then `protected`, then `package-protected`, then `public`.

#### Access control modifiers:

##### private
Methods, fields are ONLY accessible within the immediate class
    - Also JVM with with concurrency
    - Doesn't make sense to have a private Class.

##### package-private
Class, Method or Field is accessible to other classes within the same package.
    - Default without any modifier

##### protected
Class, Method or Field is accessible to:
    - classes within the same package
    - sub-classes through inheritance

##### public
Class, Method or Field can be accessed from anywhere by any class or method

#### static
Declare constants using `final static` modifiers by default.

This field, method, or class is not tied to any particular instance of the enclosing class. Created and associated with class instead of instance.
This means there is only one version for every instance to share.
When methods are static they are usually called using the ClassName instead of the instanceName.

#### abstract
Define only the Method Signature.
This allows for public classes to be completely abstracted from the user.

#### final
Final version of that element (this can not be changed):
Primitives
    - non-static: creates an unmodifiable instance field
    - static: creates a constant for the class
Objects / Arrays
    - Makes a reference final but the object is still mutable
Method Arguments
    - Within a method you can make an argument final

        void methodName(final int i) {
            i = 5; // this will fail
        }

Methods
    - explicitly prevents overriding method in sub-classes
Classes
    - explicitly prevents inheritance from this class.

Finals can be unique for the instance.
Finals can be initialized in the constructor. (blank final fields)

- final variable is similar to a constant, and usually has static (uses less space)
Final method or class: Only relevant for inheritance
- a final method cannot be overriden by a subclass
    - TODO: is this specific to the name of the method or to the method signature?
- a final class cannot be have a subclass

Be careful with final. Use with extreme caution.

### Initialization

#### Field initialization
Methods can be called in the initialization phase.
Fields can be initialized based on parameters in the constructor or based on literals in the initialization statement

#### Object field initialization
Since some objects are quite large, special consideration should be given to when they should be initialized.
1. when defined
2. in the instance initialization
3. in the constructor
4. right before they are needed, (lazy initialization)

#### Initialization Block
An entire execution area of the method can be called wrapped in braces to execute with initialization.
Initialization blocks can either be static or non-static

```
class Teaset() {
    static Cup cup;
    static Cup cup2;
    static {
        cup = new Cup();
        cup2 = methodCup();
    }
    Cup cup3;
    Cup cup4;
    {
        cup3 = new Cup(3);
        cup4 = methodCup();
    }
    methodCup() {
        return new Cup();
    }
}
```

### Methods
Method Signature: Method name with the number and types of its parameters
An object can have multiple methods with the same name so long as they return the same type(because type isn't part of the "Method Signature").
Type isn't part of the Method Signature because of calling a method for it's side effect. If you call a method an ignore it's return value the compiler has no way of knowing which method to call.
When multiple methods are present, the JVM uses the first method that matches the number and type of parameters being called.

Method Overloading: multiple methods can have the same name in Java. They just need to have unique Method Signatures.

#### Arguments
Arguments are a list of Type Arg-name pairs.

    (Type name, Type2 name2, Type3, name3)

VarArgs: It is also possible to use a variable length array as an argument:

    (Type... argName)

varargs complicates overloading methods since it can create many ambiguous situations.

#### Declaring methods
Declaring a class (static) or instance (without static) variable

    [modifiers] type identifier_1[=initialValue1], identifier_2[=initialValue2];

Declaring a Method signature and method body

    [modifiers] returnType methodName(type_1 param_1, ..., type_n param_n) {
        // method body ...
    }

`returnType`: Must return a valid Type either a primitive or defined type.
If multiple items must be returned:
- return a compound object
- modify the internal state of an existing object

Parameters: Primitives are passed as copies of the original value using assignment, objects are passed as references to the original object. see [object-assignment](#object-assignment)

#### The main Method
Every java program starts with a main method:

```java
public static void main(String[ ] args) {
    // main method body...
}
```

#### return
A method that is declared as returning a type must return that type!
If you need to return from a void method you can `return;`.

#### Constructor Method
Define a constructor method by naming it after the class.  
Default constructor: `public NameOfClass()`.
If there is no constructor Java will creat a blank default constructor.

1. cannot be static, abstract, or final
1. cannot specify a `returnType`

Constructing a `new` object with variables initiated.  
1. new object is allocated in memory on the heap (dynamically)
1. instance variables are initialized
1. the constructor method is called
1. returns a (reference | memory address | pointer) to the newly created object

Call constructor from inside a constructor
    super();
    this();

#### finalize() Garbage Collection
This method will be called instead of being garbage collected the first time. On the following garbage collection the object will be collected.

Your object might never be garbage collected.
The object does not get destroyed, it get released.

Use Cases:
    - Cleaning storage allocated by native methods
        - better to use a C or C++ destroy paradigm
    - Error handling

### this
Static pointer to the class instance from within an instance method (nonstatic).
- instance variables can be accessed from within a method, however, `this` allows differentiation between instance variables and local variables
- allows calling other instance methods from within an instance method `this.method()`
- allows calling one constructor from within another constructor `this()`

Method scope is inherited from class so `this` is not required to reference instance variables.

### Object equality
TODO: how is equality determined in Java?

object.equals(); // for object equivalence.
Default is to compare references (==).

### Package management
In order to manage the global name space every library is contained in it's own package. This completely eliminates the namespace issues of C and C++.

Group files containing Enums and Classes into packages by:
- all located in directory _packagename_
- first line of every file must be `package packagename;`

By convention:
- packages are lowercase
- classes are upper camel case
You immediately know if referring to a package or a class within a package.

Reverse URL package names are recommended to avoid name collision.
ie. com.ianedington.comp308.tpa1

#### Compilation Unit
Each \*.java file is a "compilation unit"
Each \*.java file can have a public class with the same name as the file.
This is the only public class allowed in a compilation unit

#### Class Path
The entire JAR path must be added to the Class Path.

The JVM searches for the package by converting the package name into a path and searching each element in the $CLASSPATH for the \*.class at that file location.
ie. If the import statement is `import com.ianedington.comp308.HelloWorld;` and the class path is `/java:/usr/local/java/:/home/ie.jar:.`. the JVM will look to see if a `HelloWorld.class` file exists at the following locations:

    /java/com/ianedington/comp308/HelloWorld.class
    /usr/local/java/com/ianedington/comp308/HelloWorld.class
    /home/ie.jar/com/ianedington/comp308/HelloWorld.class
    ./com/ianedington/comp308/HelloWorld.class

#### Importing Packages
It is possible to refer to a class or enum within a package directly:

```
fully.qualified.package.ClassName object = new fully.qualified.package.Class();
```

but this gets long and so we use `import`

import a specific Class or Enum from a package:
- name collision will throw error

```
import fully.qualified.package.ClassName;
```

import an entire package:
- name collision will force you to use the qualified package name `package.ClassName`
TODO: with a name collision using `import package.*` do you need to use the fully qualified or partially qualified package name?

```
import fully.qualified.package.*;
```

Every file imports all the classes from `java.lang` equivalent to bellow
https://docs.oracle.com/javase/7/docs/api/java/lang/package-summary.html

    import java.lang.*;

**static import** imports static members of a class

#### Collision

If you \* import multiple packages you might import two classes with the same name.
In this case if you use the explicit class name it will work.

## Object Reuse

### Composition
Using one or more objects inside another object.
"has-a" relationship.
This is accomplished by creating an object and assigning it to a field in the composed object.

Useful when you want the features of one or more existing class inside your class but not it's interface.

### Inheritance
Using everything from the initial class with the option of overriding members. This allows you to use another class as a template for a new class.
"is-a" or "is-like-a" relationship
 "is-a": only has the same methods as the super-class
 "is-like-a": extends the super-class with other methods

Very useful when you want a specialized version of an existing class, want to maintain the interface of the base-class.

Uses the key word `extends`.
The resulting MyClass is a "sub-class" of YourClass.

    class MyClass extends YourClass {};

`super` is like `this` but refers to the super-class.

In Java, each class can extend exactly one other class. Because of this property, Java is said to allow only single inheritance among classes.

Interfaces can be nested within classes. This leads to interesting results.

#### Initialization
Constructor methods are never inherited in java.

You can think of an extended class as a wrapper around each a base class. The base class exists underneath.
This means that when an extended object is initialized on object for every class in the inheritance hierarchy is initialized.
Java starts with the basest of the base classes and works it's way down the inheritance.

By default the constructor of the extended class will call the constructor of it's base before executing the rest of it's body.
However, it's often useful to call it explicitly.
`super()` is used to call a method from within the sub-class constructor.
If it exists, `super(*args)` needs to be the first line of the constructor.
If `super(*args)` is not found an implicit call to `super()` is made before a sub-classes constructor.

If calling an over ridden method in a constructor there might be weird bugs that happen. It will call the method but objects might not be initialized. Of course this can happen in a base class, but with inheritance being about to call base class fields at runtime makes this more complicated.
Methods in the super-class constructor might call a method from the sub-class, which isn't initialized yet.

**Good guildline is to do as little as possible in the constructor and try not to call methods.**

#### Overriding base Methods
It it possible to both override and overload methods from a base-class. This distinction is dangerous since it is easy to do one when you meant to do the other.
For this reason there is a @override annotation that throws a compile time error if the method does not override a base method.

Covariant return types: In a sub-class it's possible for a method to return a type that is a sub-type of the overridden method.
A method can return a downstream type of it's overridden method's return type.

Overridden methods can only throw the exceptions that were specified in the base method.

### Polymorphism
Variables in java are **polymorphic**: A variable declared as a super-class can hold a sub-class but are limited to the interface of the super-class.
```java
// If PredatoryCreditCard is a subclass of CreditCard this assignment with work.
CreditCard card;
card = new PredatoryCreditCard();
```

"dynamic dispatch" is how java calls the sub-class methods instead of the super-class methods for a given instance.

`instanceof` tests at runtime if a variable is an instance of a specific class or any of it's sub-classes.
```java
CreditCard card1 = new CreditCard();
CreditCard card2 = new PredatoryCreditCard();

print(card1 instanceof CreditCard); // will return true
print(card2 instanceof CreditCard); // will return true
print(card1 instanceof PredatoryCreditCard); // will return false
print(card2 instanceof PredatoryCreditCard); // will return true
```

Polymorphism makes it possible to write less code since the code can be generalized to a general type of object and will run on any object that has the general type as an ancestor.

Extensible because you are able to extend a class without reworking all the code. This is a powerful separation of things that change from things that stay the same when creating new classes of objects.

Not everything is Polymorphic. No fields are, which means they are all set at compile time.
**If a sub-class and super-class have a field with the same name, and a sub-class object is cast into it's super-type, a request for the field will go to the super-class.**
**Static Methods don't behave polymorphically either.**

### Abstract Class
A class that is partially defined in that you can mix methods with method signatures.
`abstact` modifier must be used for abstract classes or methods within an abstact class.
- can extend another class
- can implement an interface
- can not produce object `new AbstractClass();` will fail.
- Sub-classes that do not implement all abstract methods are themselves abstract

Useful in many design patterns.

```
public abstract class AbstractProgression {
    /** Constuctors can be created and called using super() */
    public AbstractProgression() { this(0); }
    public AbstractProgression(long start) { current = start; }

    /** Concreat methods can be created */
    public long nextValue() { /* code goes here */ }

    /** so to can abstract methods */
    protected abstract void advance();
}
```

### Interface

`interface` defines an interface. Same modifiers as class but without method body.
`implements` keyword is used to declare a class as implementing an interface.
- a class can implement multiple interfaces
- an interface can extend multiple other interfaces

A useful interface is a set of methods that stand alone and complete a useful amount of work together, but are not to big to exclude other classes.

Interfaces are always public.
It is possible to extend an interface, the result is another interface.
Collision can occur when inheriting from multiple interfaces if they both define a method.
It's possible to nest interfaces within classes, classes within interfaces, ect.

```java
public interface Sellable {
    public String description();
    public int listPrice();
    public int lowestPrice();
}

/∗∗ Class extending an interface ∗/
public class Photograph implements Sellable {
    // MUST implement all interface methods!
}

public interface Transportable {
    public int weight();
    public boolean isHazardous();
}

/∗∗ Class extending multiple interfaces ∗/
public class BoxedItem implements Sellable, Transportable {
    // MUST implement all interfaces methods!
}

/∗∗ interface extending multiple interfaces ∗/
public interface Insurable extends Sellable, Transportable {
    public int insuredValue();
}

/** class extending Insurable interface */
public class BoxedItem2 implements Insurable {
    // MUST implement all interfaces methods!
}
```

## Special Object Structures

### Runtime Type Information (RTTI)
Ability to know about type information at runtime.

Polymorphism is good and all but sometimes it's practical to know what type you're dealing with. This is where you can 

### Class object
When classes are loaded they are created as objects on the heap.
Once a class object is in memory it is used to create all objects of that type.
All class objects belong to the Class class.
Classes are the same as any other object and can be passed around the same way.


`Class.forName("String")` : return reference to a class object of the class String.
newInstance() : creates a new instance of a class without knowing what type it is.
ClassType.class(Class Literal) : literal of the class object.
ClassType.getSuperclass() : returns the super class of an object

#### with Generics
The Class class of objects is a bit different than regular objects.
An ordinary Class reference can be assigned any other Class object.
However, a bounded Class reference can only hold the class object of that class.

    Class nonBoundedClass = int.class;
    Class<Integer> boundedClasss = int.class;
    nonBoundedClass = double.class; // This might not be the disired result.
    //genericIntClass = double.class; // Type checking at compile time will flag this.

This problem is so common that there is a convention in place to show that you really want an unbounded Class reference, `Class<?>`.

#### Inheritance with Class Objects
Inheritance gets tricky because although a class can be a sub-class of another class, it's class object is not a sub-class object of the original object... wrap your head around that :P.

This is solved using the extends key word.

    Class<? extends Number> bounded = int.class;
    bounded = double.class;
    //bounded = char.class; // Type error

    Class<? super Integer> superOfInt = int.class;
    superOfInt = Number.class;
    superOfInt = int.class.getSuperclass();

#### Casting generically
Really only useful in generics where you don't know the types of objects you're working with.

classObject.cast() : takes a subclass or superclass object and casts it to this type.
classObject.asSubclass() : cast object to a more specific type.

#### Checking your cast
object instanceof Class : checks if an instance is of a certain Type (Type is fixed at compile time)
classObject.isInstance(object) : dynamically check if it is an instance (Type can be dynamic at runtime)

instanceof and isInstance() are true if the object being checked is a sub-class of the Type. `x instanceof Object` is always true.
This is not true for comparison of the Classes. `classObject.equals(objectObject)` returns false.

#### Reflection
RTTI is great and all but it falls apart when you start using classes that aren't available at runtime. This is where reflection comes in.
Reflection is a system to define classes at runtime. It uses Class to hold generic information, Field, Method, and Constructor to hold the class members since they can't be compiled at runtime. This is amazing since it means you can use objects you don't even know about when you're programing the code. TODO: I'm assuming this incurs a performance penalty.
Useful for:
- latent typing write a method that works with any object but calls object specific methods.

Downside:
- Moves all type checking to runtime.

This is how you can create an object of a type at runtime.

TODO: I don't know if this actually works but this is my understanding of how it would work.

    KnownClass known = null;
    Object unknown = null;
    Class<?> c = Class.forName(userInputString);
    if (c.class extends KnownClass) {
        known = (KnownClass)c.newInstance();
    } else {
        unknown = c.newInstance();
    }

Example proxy: especially useful for splitting up a large object.

    import java.lang.reflect.InvocationHandler;
    import java.lang.reflect.Method;
    import java.lang.reflect.Proxy;

    class DynamicProxyHandler implements InvocationHandler {
        private Object proxied;
        public DynamicProxyHandler(Object proxied) {
            this.proxied = proxied;
        }
        public Object
        invoke(Object proxy, Method method, Object[] args) throws Throwable {
            System.out.println("**** proxy: " + proxy.getClass() +
                    ", method: " + method + ", args: " + args);
            if(args != null)
                for(Object arg : args)
                    System.out.println("  " + arg);
            return method.invoke(proxied, args);
        }
    }

    class SimpleDynamicProxy {
        public static void consumer(Interface iface) {
            iface.doSomething();
            iface.somethingElse("bonobo");
        }
        public static void main(String[] args) {
            RealObject real = new RealObject();
            consumer(real);
            // Insert a proxy and call again:
            Interface proxy = (Interface)Proxy.newProxyInstance(
                    Interface.class.getClassLoader(),
                    new Class[]{ Interface.class },
                    new DynamicProxyHandler(real)
                );
            consumer(proxy);
        }
    }

Reflection also makes it possible to call any method, field or constructor no matter what permissions it was given. Basically, If you are not the one running your code nothing is safe in java.

### Enum types
Enums are static classes with some default behaviour.
Constructors, initializes and everything about a static class is also available to an enum.

Automatically provided with the ENUM
    ordinal(): returns 0-index order of enum
    toString(): returns name of enum
    static values(): an array of values (iterable)

Useful for representing groups of constants like the days of the week.

modifier enum name { valueName0 , valueName1 , . . . , valueNamen−1 };

Modifiers: public, protected, private
valueName_n: can be any legal identifier but convention is to use all caps

```
// Declare enum type of Day
public enum Day { MON, TUE, WED, THU, FRI, SAT, SUN };

// Declare variable will Day enum type
Day today;

// assign value of TUE to variable (1)
today = Day.TUE;
```

#### ENUMs as classes
enum types are full static classes so they have access to all the methods and static variables you would expect a class to have.

```java
public enum Planet {
    // Instances of the ENUM
    MERCURY (3.303e+23, 2.4397e6),
    VENUS   (4.869e+24, 6.0518e6),
    EARTH   (5.976e+24, 6.37814e6),
    MARS    (6.421e+23, 3.3972e6),
    JUPITER (1.9e+27,   7.1492e7),
    SATURN  (5.688e+26, 6.0268e7),
    URANUS  (8.686e+25, 2.5559e7),
    NEPTUNE (1.024e+26, 2.4746e7);

    private final double mass;   // in kilograms
    private final double radius; // in meters
    Planet(double mass, double radius) {
        this.mass = mass;
        this.radius = radius;
    }
    private double mass() { return mass; }
    private double radius() { return radius; }

    // universal gravitational constant  (m3 kg-1 s-2)
    public static final double G = 6.67300E-11;

    double surfaceGravity() {
        return G * mass / (radius * radius);
    }
    double surfaceWeight(double otherMass) {
        return otherMass * surfaceGravity();
    }
    public static void main(String[] args) {
        if (args.length != 1) {
            System.err.println("Usage: java Planet <earth_weight>");
            System.exit(-1);
        }
        double earthWeight = Double.parseDouble(args[0]);
        double mass = earthWeight/EARTH.surfaceGravity();
        for (Planet p : Planet.values())
           System.out.printf("Your weight on %s is %f%n",
                             p, p.surfaceWeight(mass));
    }
}
```

#### Enums Constant-specific methods
Each enum instance can have it's own specific instance methods, weird.

    public enum Day {
        MON {
            String whatToDo() {
                return "Work.";
            }
        },
        TUE {
            String whatToDo() {
                return "Party!";
            }
        },
        WED, THU, FRI, SAT, SUN;

        String whatToDo() {
            return this.toString();
        };
    };

#### ENUMs with switches
enum Signal { GREEN, YELLOW, RED, }

public class TrafficLight {
    Signal color = Signal.RED;
    switch(color) {
        case RED:
            color = Signal.GREEN;
            break;
        case GREEN:
            color = Signal.YELLOW;
            break;
        case YELLOW:
            color = Signal.RED;
            break;
    }
}

#### ENUM Generator

    public class Enums {
        private static Random rand = new Random(47);
        public static <T extends Enum<T>> T random(Class<T> ec) {
            T[] values = random(ec.getEnumConstants());
            return values[rand.nextInt(values.length)];
        }
    }

    enum Activity { SITTING, LYING, STANDING, HOPPING,
        RUNNING, DODGING, JUMPING, FALLING, FLYING }

    public class RandomTest {
        public static void main(String[] args) {
            for(int i = 0; i < 20; i++)
                System.out.print(Enums.random(Activity.class) + " ");
        }
    }

#### SubTypes of ENUMs using interfaces and enums of enums
Inheritance isn't possible with enums. The only way to implement types of enums is to use interfaces.
The outer enum holds 

    public enum Meal {
        MAINCOURSE(Food.MainCourse.class),
        DESSERT(Food.Dessert.class);
        private Food[] values;
        private Meal(Class<? extends Food> kind) {
            values = kind.getEnumConstants();
        }
        public interface Food {
            enum MainCourse implements Food { LASAGNE, BURRITO, PAD_THAI; }
            enum Dessert implements Food { FRUIT, CREME_CARAMEL; }
        }
        public Food randomSelection() {
            return Enums.random(values);
        }
        public static void main(String[] args) {
            Food food = Dessert.FRUIT;
            food = MainCourse.LASAGNE;
            food = Dessert.CREME_CARAMEL;

            for(int i = 0; i < 5; i++) {
                for(Meal meal : Meal.values()) {
                    Food food = meal.randomSelection();
                    System.out.println(food);
                }
                System.out.println("---");
            }
        }
    }

#### EnumSet (Collection)
Very useful for flags (on off) (replaces BitSet).
Very fast!

#### EnumMap (Collection)


### Inner and Nested Classes

Why Inner classes?
Each inner-class can inherit/implement multiple interfaces/base-classes, while maintaining access to the outer-class instance.
This allows for:
- sudo-multi-inheritance
- Closures

1. The inner class can have multiple instances, each with its own state information that is independent of the information in the outer-class object.
2. In a single outer class you can have several inner classes, each of which implements the same interface or inherits from the same class in a different way.
3. The point of creation of the inner-class object is not tied to the creation of the outer-class object.
4. There is no potentially confusing "is-a" relationship with the inner class; it’s a separate entity.

Inner class relies on an outer object. Nested class (static) does not, but is inside another class.

Inner-classes cannot:
- have static Fields
- have Nested (static) Inner-classes
Nested (static) Inner-classes can!

Useful for keeping closely related classes together.

OuterClass.this: like this but refers to outer class instance.
outerInstance.new: creates a new inner-class linked to that instance of the outerclass
These work multiple levels deep.

```
public class OuterName {
    // declaring a nested class
    public static class NestedName { /∗ class details omitted ∗/ }
    private class NestedName2 {
        public NestedName2(){
            OuterName.this; // refers to outer class instance
        }
    }
}

public class Other {
    public void main(String[] args) {
        // Accessing nested class from outside outer class
        OuterName.NestedName nested = new OuterName.NestedName();
    }
}
```

Inner-classes are very powerful for information hiding when they implement a base-class or interface. It's possible to create an object with a type and pass it back as an interface or base-type without ever knowing the full underlying type.

fully qualified name is OuterName.NestedName
private nested class can be used by the outer class, but by no other classes

A nonstatic nested class (inner class) can only be created from within a nonstatic method of the outer class. The inner instance becomes associated with the outer instance that creates it.
The outer instance can be referenced from within the inner class using `OuterName.this`
Inner instance has private access to all members of its associated outer instance, and can rely on the formal type parameters of the outer class, if generic.

upcasting

anonymous class

TODO: lots more about inner-classes. Do more reading about use cases.
Use case for:
- annonymous inner-classes.
    - Factory method?
- inner-classes within arbitrary scope

Inheriting from an inner-class:
You need to do a few special things to makes sure you have an outer class initialized.

    InheritInnerConstructor(OuterClass oC) {
        oC.super();
    }

5.  How do inner classes create a situation that looks like multiple inheritance? (See TIJ pages 378 to 382.)
    Two inner classes can extend different classes, but still have access to the members of the outer class.

1.  What is a local inner class and what are its features? (See TIJ 385.)
2.  How are inner classes identified? (See TIJ page 387.)
    using $ between outer and inner class name.

### Generics
Why Generics?
- Type safe containers (usually not a huge benefit).
- Generic code that can be reused for any object.

Introduced in Java 5. Which means there are issues with backwards compatibility.

Type generic code with types specified at use rather than with initial code. All types are still declared before compile time.

This is code that can be used with many different object without specifying the Type. When the code is implement specify the object. This give you type checking going in and out of the code but lets you write code that can be used on many different object types.
Less powerful than other generics language implementations.
Most useful for containers.

Used to create type independent methods.
```java
public class Pair<A,B> {
    A first;
    B second;

    // constructor
    public Pair(A a, B b) {
        first = a;
        second = b;
    }

    // getters for a and b
    public A getFirst() { return first; }
    public B getSecond() { return second;}
}
```

By default every type within this declaration is the completely generic Object type. However there are many ways to narrow these types which makes this framework more useful.
Use `<E>` when refering to class. Use `E` when refering to element within class.

#### Tuples
Also returning multiple items as Tuples.

Tuples are unique objects grouped together to be returned. With Generics, tuples allow you to return type information with the tuple.

    public class TwoTuple<A,B> {
        public final A first;
        public final B second;
        public TwoTuble(A a, B b) {
            first = a;
            second = b;
        }
        public String toString() {
            return "(" + first + ", " + second + ")";
        }
    }

#### Arrays and Generics
Don't make array's of generics, do make generics containing arrays.

#### Generic Methods
If static it knows what Type based on whats passed in.
the <T> in the static method defines a new Type. This is seperate from any Type defined in the Class.

Super useful for infinitely overloading methods.
By accepting a generic object as a parameter you essentially give the method the ability to accept any object type. Thus unlimitedly overloading the method.

Also works with variable argument lists (T... t).

    public <T,J> void doSomething(T t, J... j) { execute; }

```
class ClassParameter<T> {
    public T[] f(T[] arg) { return arg; }
}
class MethodParameter {
    public static <T> T[] f(T[] arg) { return arg; }
}
public class ParameterizedArrayType {
    public static void main(String[] args) {
        Integer[] ints = { 1, 2, 3, 4, 5 };
        Integer[] ints2;
        ints2 = new ClassParameter<Integer>().f(ints);
        ints2 = MethodParameter.f(ints);
    }
}
```

#### Complex models
Very useful for creating simple but complex data models.

#### Erasure
All type information is erased withing a generic. This is because of limitations in the Java language spec and the need to remain backwards compatible with older libraries.

- You can't use `instanceof` within generics!
- You can't get any type information within a generic.

Class type is based on the generic not on the generic's implementation. A generic is defined in a class file so the underlying class object is the same no matter what the generic is holding.

This is a fundamental difference between Java and other implementations of generics. The generics have NO idea what they are dealing with once they are created. This means that code must written assuming everything is an object.

There are ways around this with template and factory methods.

#### Bounding Generic types
This is where you start to be able to create complex code within your generics. By making sure it is of a type. The following returns an exact type instead of a generic Number. If used properly this makes more complex code more simple, but can make simple code more complex.

    <T extends Class & Interface & Interface2> T map (T digit) { return digit; }

`Generic<T2 extends T1> boundedRef;` A reference can contain a generic that holds a specific Type T2 or greater. Since we don't know what type it is holding we can't use assignment statements or any method that uses T as an argument. You can call methods that return T so long as the reference they are assigned to is T2 or a super-class of T2.
`Class Generic<T2 extends T1> {}` a generic where T2 can be any subclass of T1. The methods associated with T1 are available within the generic.

##### Wildcards
<?> This tells the compiler it can be any type, but that it's a specific type. This makes it hard for the compiler to make any specific determinations about the class being represented. It usually means that you can't assign an object to it because you don't know what type it is and you can't call any methods because you don't know what type it is.

##### Bounding and Wildcards
Allow for an upcasting relationship.
These are more restrictive than strait bounds because once you say it's a wild card, we don't know what that means.

    List<? extends Apple>

Basically you can't use any methods that will add, or change the array using a parameter, but you can call methods that will perform actions on the generic.

Super type is the opposite. You know that this object is at least an apple. It might even be less than an apple but we don't know that. This will let us pass apple types in but not less than an apple.

    List<? super Apple>

##### Self Bounding
It's possible to bound a generic with itself. I'm not sure why this is useful.

#### Exceptions
Catch clauses cannot catch an exception of a generic type, because the exact type of the exception must be known at compile time.
This means that the error checking is very limited within generics.
You can however, write a generic that takes an exception. This allows you to write code that varies based on the exception thrown.

#### Legacy Code
Pre java 5 syntax didn't have support for generics. Because of that extra care needs to be used when mixing code with generics with pre java 5 code. One way to do that is to use checkedCollections.
checkedCollection( ), checkedList( ), checkedMap( ), checkedSet( ), checkedSortedMap( ), checkedSortedSet( )
If you didn't use these methods you wouldn't get an error until you take out the object and it throws a bad assignment error. With these methods you find out when you try to assign them to the collection.

### Exceptions
An exceptional condition is a condition you don't have enough information to solve in the current scope. All you can do is jump to a wider scope and let them try to solve the condition.

Error handling has fallen out in favour of tests.

#### Resumption vs Termination Error Handling Theory
Resumption: Should the invoker continue after throwing an exception, assuming the error has been handled?
Termination: The invoker stops what it's doing and returns control to the Error Handler.

Java supports termination. If you want to do resumption call a method that fixes the problem (growing an array).

#### Throwing Exceptions
`throw`: from within a method, throws an exception
acts like return but instead of following the execution stack it returns up the exception 'stack'.

A new exception object is created on the heap.
The current exception is halted.
The exception-handling mechanism then traces back up the stack to the exception handler and passes it the exception.
If the exception handler fails to deal with the exception the program will halt.

#### Catching Exceptions
```java
try {
    guardedBody
} catch (exceptionType1 variable1) {
    remedyBody1
} catch (exceptionType2 | exceptionType3 variable2) {
    remedyBody2
} catch ... {
    remedy...
} finally {
    executes no mater what.
}
```

exceptionType: valid exception type extending the Exception class
|: separates multiple exceptions
variable: valid java variable name holding the execption object

Try block:
`try` followed by scope with code that might throw exceptions

Catch block:
`catch` if an exception is thrown in the try block the first catch block with that exception will be executed.

finally:
`finally` useful when you need to return something to its original state. Release external resources, close a file or network connection, remove something from the screen, or flip a switch in the outside world.
- can cause exceptions to be lost
    - throw exception in finally block
    - return in the finally block

#### Add Exceptions to a method
```java
// method definition with throws and throw
modifiers returnType methodName(parameters) throws exceptionType1, exceptionType2 {
    throw new exceptionType1(parameters);
    throw new exceptionType2(parameters);
}
```

`throws`: defines a method as possibly throwing an exception.
- all checked exceptions that might propagate upward from a method must be explicitly declared in its signature.
- Can be thrown in the method itself or in one of the methods it calls.
- Multiple exceptionTypes can be separated by commas.
- Can designate a super-class of the exception thrown instead.
- does not negate the need for @throws javadoc

#### Creating new Exception types
An exception is a special class extenpeaked from the Exception class.
Create a new exception type by extending the Exception class or any of it's subclasses.

This can be as simple as:

    class SimpleException extends Exception {}

    class MessageException extends Exception {
        public MessageException() {}
        public MessageException(String msg) {
            super(msg);
        }
    }

#### Checked vs Un-Checked exceptions
TODO: understand and take notes on Checked vs Un-Checked exceptions
`RuntimeException` is the base class of UnChecked exceptions
Everything else is a Checked exception.

#### Chaining exceptions
An exception might be caused by another exception and so you pass the first exception into the second exception.
You do this using initCause() method.

#### Edge cases
Exceptions in constructors: might not clean up resources
When you override a method you can only throw exceptions from the base class.
    This gets messy fast. Try to create exceptions that can't fail or don't allocate resources.
    TODO: There are some rules about inheriting exceptions but they are unclear to me
You can pass a checked exception to a runtime exception so you don't have to worry about it. You can still catch the exception later.

    try {
        // do something
    } catch(IdontKnowException e) {
        throw new RuntimeException(e);
    }

#### Exception guidelines
1. Handle problems at the appropriate level. (Avoid catching exceptions unless you know what to do with them.)
2. Fix the problem and call the method that caused the exception again.
3. Patch things up and continue without retrying the method.
4. Calculate some alternative result instead of what the method was supposed to produce.
5. Do whatever you can in the current context and rethrow the same exception to a higher context.
6. Do whatever you can in the current context and throw a different exception to a higher context.
7. Terminate the program.
8. Simplify. (If your exception scheme makes things more complicated, then it is painful
and annoying to use.)
9. Make your library and program safer. (This is a short-term investment for debugging, and a long-term investment for application robustness.)



#### Exception Matching
A sub-class exception can be caught by a super-class catch block.
If a sub-class catch block is bellow a super-class catch block the compiler will give an error since it know the sub-class catch block will never be reached.

## Java Standard Library Types

### Strings
Java has a built in string class denoted by double quotes.

String class
- immutable
- All string methods return new string objects

String immutability comes at a performance cost. Usually this is acceptable but sometimes it's better to go with a string builder.

```
String title = "Data Structures & Algorithms in Java";
char[ ] msg = original.toCharArray();
```

indexing by character
the String class is immutable
For a mutable string use the StringBuilder class.

#### formater
`java.io.Console`, `java.io.PrintStream` `String` format/printf
C like string formating.

#### Scanner
Takes almost any object and can read them line by line or search for the next of any itme type.
Default splits input tokens along whitespace but you can specify your own delimiter.
You can also scan using regex patterns.

#### String Tokenizer (replaced by Scanner)
Takes a string and splits it into a list of strings.
Tokens the strings.
These strings are seen as independent so operations (regex) on one doesn't have others as part of their context.

### Regex
Be careful of escape sequences
very close to perl

`java.util.regex` Pattern and Matcher

Pattern: compiles the regex pattern (thread safe)
Matcher: matching engine that uses pattern to search a string. (not thread safe)
group(): returns a group specified by ()

Can be used with I/O: 

### Arrays
Arrays are first class object with greatly reduced functionality.

Why? Efficiency when using primitives. Containers are better in every other way.

- hold primitives directly
- hold objects as references.
- fixed size
- has final property `length`: returns int of array size.
- Arrays in Java are zero indexed.
    - `length - 1` is the last element in the array
- guaranteed to be initialized:
    - objects to null
    - primitives to their zero type
- impossible to access an array outside its range.
- arrays can hold references to another array
    - Nested array
    - Ragged arrays are nested arrays that have different lengths
- additional array functionality is implemented using `java.util.Array` static class.
    - Except System.arraycopy which is a faster copy method.


Don't make array's of generics, they usually break.
You can use array's within generics `T[]`

```java
ElementType[ ] variableName; //assign an array

// create new array
variableName = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};
variableName = new ElementType[5]; // empty array of length
variableName = new ElementType[]{2, 3, 4};

// assign reference to same array
ElementType[] a2 = variableName;

// [] -> assignment and retrival
variableName[2] = 8;
print(variableName[2]); // output: 8

// only other info for the array:
System.out.println(measurements.length);
```

### Containers
Type-safe containers (new in 1.6 because of generics): A container that can be made to hold a specific type of object. Instead of a container holding an Object object it's able to hold object of varying types and returns that type. This is compared to non-type safe containers that contain base level object types so there is no compile time checking of objects as they go into the container.

#### Collections
- sequence of elements
- with special rules
    - list: must hold elements in order inserted
    - set: cannot have duplicate elements
    - Queue: returns elements according to it's queuing discipline

All collections implement iterators

`java.util.Collections` - collections of static methods that help with Collections.

##### List
ArrayList:
    - Random access & set
    - bad: insertion, removal, growing
LinkedList:
    - insertion, removal, growing, sequential access.
    - bad: random access

##### Set
All Elements in a set are unique.
This uniqueness is established using the equals() method.
Therefore all elements should implement an appropriate equals() method.
###### TreeSet
Keeps items in sorted order based on the comparator used.
Implemented using a red-black tree.
Elements must implement Comparable interface.
###### HashSet
unsorted (order is unspecified).
Very fast lookup time.
hashCode() is used to set the hash buckets.
It is advisable to override this method.
###### LinkedHashSet
Same as HashSet but maintains doubly-linked list through it's nodes, in order to keep insertion order.
Lookups are fast, insertion is slightly slower because of linked-list.

##### Queue
- FIFO
- LIFO
- PriorityQueue
- DeQue
    - implements both FIFO & LIFO queue's
###### Priority Queue
Uses Comparator function to determine return order.
Sort on insert or Sort on retrieval based on performance.
- Sort on insert is usually more efficient.
- Sort on retrieval is useful when item order can change while in the Queue.

#### Maps
Maps, aka associative arrays or dictionaries, are group of key-value object pairs. Most useful type of container.
Similar implementations to sets. The keys can be thought of as a set.

##### HashMap
##### LinkedHashMap
Provides order guarantee for keys. See LinkedHashSet for implementation.
Also allows for a least recently used (LRU) order.
##### TreeMap
Keeps keys in sorted order based on the comparator used (natural is default).
Only Map allowing for returning a subMap.
##### WeakHashMap
If no references to a particular key are held outside the map, that key may be garbage collected.
##### ConcurrentHashMap
no synchronization locking, thread safe Map.
##### IdentityHashMap
uses == instead of equals() for identity. Not used often.

#### HashTables and Hashing
How a hashtable works:
Array of fixed length is created.
(key.hashCode() % bucket.length) gives which bucket to store/retrieve object.
LinkedList of Tuple<key, value> is put in the bucket if one doesn't exist.
key is compared with other key's in LinkedList using equals().
If it already exists the object is returned/replaced.
If not a new Tuple<key, value> is added to the LinkedList.

Speed is based on:
- Capacity: The number of buckets in the table. Initial capacity can be set in HashMap and HashSet.
- Size: The number of entries currently in the table.
- Load factor: Size/capacity defaults to 0.75. This can be set in HashMap and HashSet.

If you make more buckets it will decrease the collisions, increasing access and put speed, but decreasing traversal speed. This is usually set in the Constructor.

##### hashCode()
Two things contribute to a good hashCode, uniqueness and generation speed.
These should be balanced but favouring generation speed.
A non unique hash will result in more keys in the same bucket, where a slow generation speed will decrease performance for every operation.

1. Store some constant nonzero value, say, 17, in an int variable called result.
2. For each significant field f in your object (each field taken into account by the equals method, that is), do the following:
    a. Compute an int hash code c for the field:
        i. If the field is a boolean, compute (f ? 1 : 0).
            c = f ? 1 : 0;
        ii. If the field is a byte, char, short, or int, compute (int) f.
            c = (int) f;
        iii. Ifthefieldisalong, compute (int)(f^(f>>>32)).
            c = (int)(f^(f>>>32));
        iv. If the field is a float, compute Float.floatToIntBits(f).
            c = Float.floatToIntBits(f);
        v. If the field is a double, compute Double.doubleToLongBits(f), and then hash the resulting long as in step 2.a.iii.
            long l = Double.doubleToLongBits(f);
        vi. If the field is an object reference and this class’s equals method compares the field by recursively invoking equals, recursively invoke hashCode on the field.
            c = f.hashCode();
            If a more complex comparison is required, compute a “canonical representation” for this field and invoke hashCode on the canonical representation.
            If the value of the field is null, return 0 (or some other constant, but 0 is traditional).
        vii. If the field is an array, treat it as if each element were a separate field.
            That is, compute a hash code for each significant element by applying these rules recursively, and combine these values per step 2.b.
            If every element in an array field is significant, you can use one of the Arrays.hashCode methods added in release 1.5.
    b. Combine the hash code c computed in step 2.a into result as follows: result = 31 * result + c;
3. Return result.
4. When you are finished writing the hashCode method, ask yourself whether equal instances have equal hash codes. Write unit tests to verify your intuition! If equal instances have unequal hash codes, figure out why and fix the problem.

The most common error for hashing results when creating a new object type.
When two objects of the same time should be equal but aren't.
Even though they logically should be equal, they both return false because the default hashCode and equals methods are based on the objects address in memory.

    gh1 = new Groundhog("Willy", "Wiarton");
    gh2 = new Groundhog("Willy", "Wiarton");
    out.println("these should be equal: " + (gh1.equals(gh2)));
    out.println("these should have the same hashCode: " + (gh1.hashCode().equals(gh2.hashCode())));

#### Optional Methods
Both Collections and maps use optional methods. These methods are possible because of Java's runtime errors. The methods make the container interfaces more flexible, but in certain cases push type checking to runtime.
This is a departure from conventional static typing.


### Iterators
Why? Collections are a lot more work to get foreach functionality.

An iterator is a standardized way of moving through a collection.
An iterator has no current element it is always between two elements. The element before and the element after.

 E0 E1 E2 E3
^  ^  ^  ^  ^

When next() is called for the first time E0 is returned and the cursor is advanced to just before E1. If previous() is called E0 is called and the cursor is moved back to just before E0. If next, next, next, remove is called E2 is removed and the cursor maintains it's current position between E1 and E3. At this possition next would return E3 and previous would return E1.

#### Iterable (foreach)
Interface that returns an iterator. Used by foreach loop.

#### Iterator interface
Only moves one direction and optionally can remove elements.
- hasNext, next
- optional: remove

#### ListIterator Interface
Everything in Iterator, moves two directions, know it's location in the list, and can optionally add elements.
- hasPrevious, previous
- nextIndex, previousIndex
- optional: set, add

### Comparable & Comparator
`java.lang.Comparable`
`java.lang.Comparator`

Generalized comparison for use in sorting algorithms.
Comparable is an interface that objects implement to compare themselves with other objects.

    object1.compareTo(object2);

Comparator is a function Class that compares two objects.

    ComparatorClass.compare(object1, object2);

### Random
Psudo random number generator

### Clonable Interface
Seems to be a concessus that clonable is broken. 
http://www.artima.com/intv/bloch13.html

Cloning is a secondary object creation path that does not use the object constructors and instead relies on class creators to implement a clone method.
This method starts by calling the `supper.clone()` method on the object in order to get a hierarchically cloned object. This intoduces room for errors since there are now two object creation paths to maintain.

```java
public class clonableClass implements Cloneable {
    public clonableClass clone() throws CloneNotSupportedException {
        // Call all previous clonning steps in order to clone any private elements from super classes.
        clonableClass other = (clonableClass) super.clone();
        // preform cloning process for the current class.
        return other;
    }
}
```

## Design Patters

### Delegation
Delegation is when one object delegates members to another object.

A space ship control panel is a delegation mechanism. Anything you do to the control panel is actually delegated to the spaceship to perform.

In java you would:

### Template method
ie. application framework

A general template that pretty much works the way it should but needs to be customized.
Instead of creating new objects you simply extend the existing objects with the customization and leave the heavy lifting to the template/framework.

The template stays the same and the methods are what change.

#### Control framework
Event driven framework.
Inner-classes are all the different types of events.

### Composition

### Adapter

### Position

### Iterator
A nested that iterates through the elements of a class.

The class needs to implement `java.util.Iterable`.
Iterable has a method `iterable()` which returns an `java.util.Iterator`.
`Iterator` is a class, usually a nested class that implements `java.util.Iterator`.

This is a complicated way to reliably get an object on which you can call:
```
Obj<E> obj = new Obj;
Iterator<E> objIter = obj.iterator();

boolean nextExists = objIter.hasNext();
E nextElement = obj.next();
```

### Factory Method
Can be implemented using Interfaces

### Generators
Generates data based on a _strategy_, Factory method?

### Comparator

### Locator

### Flyweight
Abstracts away object attributes that don't need to be part of the object. Useful when many objects are needed and they are very similar (Charachters in a word editor, potions in a alchamy shop).

### Null Object
There is a pattern where instead of constantly checking for null you instantiate an Object that is nullish.

### Mock Objects and Studs
Objects that create

Stubs
Large almost real objects that act like the real object but aren't actually them.

### Mixins
Mixins are difficult to accomplish in Java because it doesn't allow for multiple inheritance.
Interface - gives certain characteristics of mixins (multiple types have the same interface)
    - breaks down because each class has to implement their own code for this.
Decorator - allows code to be reused and multiple classes to share functionality
    - breaks down because it only allows the last 'decoration' to be used.
Dynamic Proxy & interfaces - Hold the underlying classes.
    - Doesn't provide a common interface for everything however, it does allow casing to different types.
    - Each object is still kept separate like with the composition pattern.
    see TIJ - Mixins with dynamic proxies

### Latent Typing
Reflection - able to write a method that will call methods on any objects.
    - this is the best way to get a trully dynamic language like python.
    - however, delays all typechecking till runtime
Reflection + interface - adds some type checking
adapter pattern - Using an adapter interface and a generic adapter, it is possible to create a common interface for objects that don't have a common interface but do have common methods.
    - Still requires a lot of structural code but gives you type checking.
    see TIJ - Simulating latent typing with adapters

## JavaDocs
Tags:
@see "See Also" with link to another class

    @see classname
    @see fully-qualified-classname
    @see fully-qualified-classname#method-name

{@link package.class#member label}

@since
@param
@return
@throws fully-qualified-class-name description

## Compilation
Class files will run cross platform. No need to compile on each system individually.
Provides API for system functions - meaning it completely abstracts away the underlying hardware.

Each file can only have one public class defined. That class must have the same name as the file.
Main program file must have a "main" method. The main method is always the first thing to run.

```flow
f1=>start: *.java
o1=>operation: javac|past
f2=>start: *.class
o2=>operation: java|past
p=>end: End

f1(right)->o1(right)->f2(right)->o2(right)->p(right)
```

### ClassPath
Calling `java program.class` the runtime environment locates the packages and class according to a special operating system environment variable named “CLASSPATH”.
This variable defines an order of directories in which to search for the package or class.

```
export CLASSPATH=.:/usr/local/java/lib:/usr/netscape/classes
```

## Testing

- zero, null, '', "", or empty value

### Stub classes / packages
Maintain a wrapper class in a sub-package. Use `import package.*;` for the deployment version, and use `import package.debug.*;` when debugging.

### debug wrapper methods
It is possible to write wrapper methods that pass calls to the real method and add functionality.

## Java for Programmers COMP308

### Tutor Questions:
1. What are the turn around times for assignment marking?
4. Is there information about what will be tested for on the final exam?

Topics I'm having a hard time understanding:
2. Anonymous inner-classes. What are they useful for?

### Tutor Answers:
#### Questions about assignment 1
1. I have Java 8 installed on my machine. Can I submit assignments that work in this version?
>> Yes
2. Is there a marking rubric for the assignments? I have found the submission guide, however, it does not talk about what you are looking for when you mark the assignments. For example:
- Will the assignments be marked based on most efficient implementation or based on readability and maintainability.
>> No, design is more important
- Will there be marks given for documentation or simply for functionality?
>> Documentation will take up 10% of the marks, functionality 50%, coding/design 20%, testing 15%, the rest 5% is for the answers to the objective questions.
- How in depth do the tests need to be?
>> It is more on the coverage. Of course we need to cover all requirements, but we also need to test for abnormal cases.
3. Can I submit the objective questions as a plain text file or markdown file?
>> Text file is fine. 
4. Programs 1, 3, and 4 do not ask for tests to be written. Does this mean they do not need tests?
>> We need to test all programs. Program 3 and 4 doesn't have user input, so a listing of the output will be fine. There are several methods required for Program 1 (Circle), some needs more than 1 tests (e.g., isInside). 

### All assignments must:
Java 6 was the current version of Java when this course was created.
However, all assignments must compile and run with Java 5.
If you want to use a feature of Java 6 (plus) you need to inform your tutor.

Guidelines Submitting all TME's
- You must submit all the files for the TME in either windows zip or unix/linux gzip format. Please zip all files and submit as one zip file. The zip file must unzip into a directory structure that can be used to compile and run the programs without further file management. Please use a relative directory structure and include only those directory levels needed. 
- Solutions to the TME exercises must be contained in one single directory, and must compile from that directory with the standard Sun Java SDK for the course using the command "javac *.java". Failure to follow this guideline will result in your TME being returned to you for correction. If you re-submit code that does not compile with the Java SDK using the simple command outlined above, you will receive a mark of 0 on that exercise.
- Programs must compile correctly, run with the specified JDK for the course,and be fully test prior to submission. 
- Applets will be tested using the appletviewer in JDK. Please include the appropriate .html file. 
- A test plan must be submitted indicating the tests done, their purpose, and the test results. You must submit all the files necessary for testing the program along with the necessary directions. Where necessary, a program should also include a test driver. Please see testplan.html for a sample test plan. 
- Test for both valid and error conditions - error conditions need reporting the program user in an appropriate way. 
- All program source files must be text files. Class files need not be submitted. 
- Design and testing documentation should be submitted as separate text or as MSWord files. 
- Program documentation should be inline. This should include:
    - Problem description and detailed requirements - this can be adapted from the TME problem description
    - Documentation header block identifying the program, your name, student ID date written , statement of the overall program purpose.
    - Compiling and running instructions
    - Documentation of purpose of individual methods you have written.
    - Documentation of algorithms of complex logic, when not obvious from reading the code
    - Purpose of main names used for variables, methods
- Where a TME suggests developing a program in stages, document and submit the final deliverable only, not the intermediate stages. 
- Please include examples, code fragments, etc to illustrate your points in your answers to the unit questions. 

## Quiz 1: (3 / 3 percent)
## Tutor Marked Exercise 1 (5 / 5 percent)
## Tutor Marked Exercise 2 (9.2 / 10 percent)
## Unit 7: Java IO and Networking

### Unit Purpose
Discuss and use Java IO and Java Networking features.

### Conferencing
Post any questions or comments to the CMC system (conferencing is optional, but is recommended)

### Digital Reading Room
-   [On cloning and object immutability](http://library.athabascau.ca/drr/redirect.php?id=8129) [On cloning and object immutability](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27638)
-   [Networking Basics](http://library.athabascau.ca/drr/redirect.php?id=25146) [Networking Basics](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27639)
-   [Working with URLs&gt;](http://library.athabascau.ca/drr/redirect.php?id=25147) [Working with URLs](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27640)
-   [Working with Sockets](http://library.athabascau.ca/drr/redirect.php?id=25148) [Working with Sockets](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27641)

### Section 1: Java IO
**Section Goal**: Describe and use the I/O facilities of Java.

#### Learning Objective 1
-   Use the **File** class.

##### Readings
**Required**: Pages 901 to 914 of TIJ

##### Exercises
**Questions**
1.  What are two ways of using the **File** object to get a directory listing? (See TIJ page 902.)
2.  What are four other uses of the **File** class? (See TIJ page 912.)

##### Programs
Compile, run, and analyze programs:

[DirList.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/io/DirList.java)
[DirList2.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/io/DirList2.java)
[DirList3.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/io/DirList3.java)
[Directory.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/net/mindview/util/Directory.java)
[DirectoryDemo.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/io/DirectoryDemo.java)
[ProcessFiles.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/net/mindview/util/ProcessFiles.java)
[MakeDirectories.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/io/MakeDirectories.java)

#### Learning Objective 2
-   Describe I/O streams in Java.

##### Readings
**Required**: Pages 914 to 922 of TIJ

##### Exercises
**Questions**
1.  What are the six types of **InputStream**? (See TIJ pages 915 to 917.)
2.  What are the four types of **OutputStream**? (See TIJ pages 917 to 918.)
3.  What is a Decorator? (See TIJ pages 918 to 919.)
4.  What are the four types of **FilterInputStream**? (See TIJ page 919 to 920.)
5.  What are the three types of **FilterOutputStream**? (See TIJ page 921 to 922.)

#### Learning Objective 3
-   Use I/O streams.

##### Readings
**Required**: Pages 922 to 973 of TIJ

##### Exercises
**Note**: You should be able to recognize these types and use them
appropriately, but you are not expected to generate them verbatim for
examination purposes.

**Questions**
1.  What are the additional features provided by Java 1.1 **Reader** and **Writer** classes? (See TIJ pages 922 to 923.)
2.  How is **RandomAccessFile** used? (See TIJ pages 926 to 927.)
3.  What is the use of buffered input? (See TIJ pages 927 to 928.)
4.  What is one way of reading input from memory? (See TIJ pages 928 to 929.)
5.  What is the difference between a **PrintWriter** and a **DataOutputStream**? (See TIJ page 932.)
6.  How do you redirect I/O in Java? (See TIJ pages 942 to 943.)
7.  What is the goal of the Java *new* I/O library? (See TIJ page 946.)
8.  What are the four indexes of a **Buffer**? (See TIJ page 962.)
9.  How to lock and release a file? (See TIJ pages 970 to 971.)

##### Programs
Compile, run, and analyze programs:

[BufferedInputFile.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/io/BufferedInputFile.java)
[MemoryInput.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/io/MemoryInput.java)
[FormattedMemoryInput.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/io/FormattedMemoryInput.java)
[TestEOF.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/io/TestEOF.java)
[BasicFileOutput.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/io/BasicFileOutput.java)
[FileOutputShortcut.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/io/FileOutputShortcut.java)
[StoringAndRecoveringData.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/io/StoringAndRecoveringData.java)
[UsingRandomAccessFile.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/io/UsingRandomAccessFile.java)
[TextFile.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/net/mindview/util/TextFile.java)
[BinaryFile.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/net/mindview/util/BinaryFile.java)
[Echo.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/io/Echo.java)
[ChangeSystemOut.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/io/ChangeSystemOut.java)
[Redirecting.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/io/Redirecting.java)
[OSExecuteDemo.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/io/OSExecuteDemo.java)
[GetChannel.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/io/GetChannel.java)
[ChannelCopy.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/io/ChannelCopy.java)
[TransferTo.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/io/TransferTo.java)
[BufferToText.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/io/BufferToText.java)
[AvailableCharSets.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/io/AvailableCharSets.java)
[GetData.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/io/GetData.java)
[IntBufferDemo.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/io/IntBufferDemo.java)
[ViewBuffers.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/io/ViewBuffers.java)
[Endians.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/io/Endians.java)
[UsingBuffers.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/io/UsingBuffers.java)
[LargeMappedFiles.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/io/LargeMappedFiles.java)
[MappedIO.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/io/MappedIO.java)
[FileLocking.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/io/FileLocking.java)
[LockingMappedFiles.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/io/LockingMappedFiles.java)

#### Learning Objective 4
-   Use the Java compression facilities.

##### Readings
**Required**: Pages 973 to 980

##### Exercises
**Questions**
1.  What is the primary function of GZIP? (See TIJ pages 974 to 975.)
2.  When would you use Zip? (See TIJ page 975.)
3.  What is the JAR format? (See TIJ page 978.)

##### Programs
Compile, run, and analyze programs:

[GZIPcompress.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/io/GZIPcompress.java)
[ZipCompress.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/io/ZipCompress.java)

#### Learning Objective 5
-   Describe and use object serialization facilities in Java.

##### Readings
**Required**: Pages 980 to 1003 of TIJ

##### Exercises
**Questions**
1.  What is *lightweight persistence*? (See TIJ pages 980 to 981.)
2.  What are two functions of *serialization*? (See TIJ page 981.)
3.  What is a rule for serializing to save the state of a system? (See TIJ pages 986 to 990.)
4.  What is the function of the **transient** keyword? (See TIJ pages 990 to 991.)
5.  How do **writeObject** and **readObject** function? (See TIJ pages 992 to 995.)

##### Programs
Compile, run, and analyze programs:

[Worm.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/io/Worm.java)
[FreezeAlien.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/io/FreezeAlien.java)
[ThawAlien.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/io/xfiles/ThawAlien.java)
[Blips.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/io/Blips.java)
[Blip3.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/io/Blip3.java)
[Logon.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/io/Logon.java)
[SerialCtl.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/io/SerialCtl.java)
[MyWorld.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/io/MyWorld.java)
[StoreCADState.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/io/StoreCADState.java)
[RecoverCADState.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/io/RecoverCADState.java)

#### Learning Objective 6
-   Use XML and Preferences.

##### Readings
**Required**: Pages 1003 to 1008 of TIJ

##### Exercises
**Questions**
1.  What is the limitation of object serialization and what is the advantage of converting data to XML format? (See TIJ page 1003.)
2.  What is the advantage and what is limitation of the **Preferences API**? (See TIJ page 1006.)

##### Programs
Compile, run, and analyze programs:

[Person.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/xml/Person.java)
[People.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/xml/People.java)
[PreferencesDemo.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/io/PreferencesDemo.java)

#### Learning Objective 7
-   Summarize the materials in this section and complete the exercises.

##### Readings
**Required**: pages 1008 to 1009 of TIJ

##### Exercises
**Exercises** 7 to 9 on page 928, exercise 12 on page 932, exercise 27
on page 984 of TIJ

##### Answers To Exercises
-   [Answer 7](http://scis.athabascau.ca/html/course/COMP308/Unit_7/Section_1/Ch19ex7.java)
-   [Answer 8](http://scis.athabascau.ca/html/course/COMP308/Unit_7/Section_1/Ch19ex8.java)
-   [Answer 9](http://scis.athabascau.ca/html/course/COMP308/Unit_7/Section_1/Ch19ex9.java)
-   [Answer 12](http://scis.athabascau.ca/html/course/COMP308/Unit_7/Section_1/Ch19ex12.java)
-   [Answer 27](http://scis.athabascau.ca/html/course/COMP308/Unit_7/Section_1/Ch19ex27.java)

### Section 2: Passing and Returning Objects
**Section Goal**: This section introduces Java networking features.

**Note**: Java support of networking is very straight forward that once
a connection is made, the reading and writing through the network is
very much the same as a local I/O. Notice that the sample codes in the
links use **BufferedReader** and **PrintWriter** to read and write data
from/to the network, which is the same as reading and writing to local
files.

#### Learning Objective 1
-   Introduce networking basics.

##### Readings
**Required**: [Networking Basics](http://library.athabascau.ca/drr/redirect.php?id=25146)

##### Exercises
**Questions**
1.  Explains the difference between TCP and UDP.

#### Learning Objective 2
-   Work with URLs.

##### Readings
**Required**: [Working with URLs](http://library.athabascau.ca/drr/redirect.php?id=25147)

##### Exercises
**Questions**
1.  Give an example of a URL and identify the protocol, host, filename, and port number.
2.  What is the default port number if it is not included in a URL?
3.  Study URLConnectionReader.java listed under the last section of the external website. Modify it so that it will access
    http://www.athabascau.ca and write the content to the console.

#### Learning Objective 3
-   Describe the use of Sockets.

##### Readings
**Required**: [Working with Sockets](http://library.athabascau.ca/drr/redirect.php?id=25148)

##### Exercises
**Questions**
1.  Define a Socket.

### Digital Reading Room
Unit 7 Section 2 Links:
-   [On cloning and object immutability](http://library.athabascau.ca/drr/redirect.php?id=8129)

## Tutor Marked Exercise 3 ( / 12 percent)

## Unit 8: GUI Development

### Unit Purpose
Design, develop, and implement GUIs and
simple graphical effects.

### Conferencing
Post any questions or comments to the CMC system (conferencing is optional, but is recommended)

### Digital Reading Room
-   [Book, Doug Lea, Concurrent Programming in    Java](http://library.athabascau.ca/drr/redirect.php?id=8131) [Book, Doug Lea, Concurrent Programming in Java](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27644)
-   [Apache ANT](http://library.athabascau.ca/drr/redirect.php?id=8133) [Apache ANT](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27646)
-   [Introduction to ANT using JUnit](http://library.athabascau.ca/drr/redirect.php?id=8134) [Introduction to ANT using JUnit](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27647)
-   [Technical tips on using    Logger](http://library.athabascau.ca/drr/redirect.php?id=8135) [Technical tips on using Logger](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27648)
-   [A collection of questions of OO design](http://library.athabascau.ca/drr/redirect.php?id=8136) [A collection of questions of OO design](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27649)
-   [A brief overview of applets](http://library.athabascau.ca/drr/redirect.php?id=25149) [A brief overview of applets](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27650)
-   [jguru: awt](http://library.athabascau.ca/drr/redirect.php?id=25151) [jguru: awt](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27651)
-   [AWT Short Course: Introduction](http://library.athabascau.ca/drr/redirect.php?id=25152) [AWT Short Course: Introduction](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27652)
-   [javabeans](http://library.athabascau.ca/drr/redirect.php?id=25153) [javabeans](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27653)
-   [Download AWT 1.0 Tutorial](http://library.athabascau.ca/drr/redirect.php?id=25154) [Download AWT 1.0 Tutorial](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27654)
-   [Swing: Part I](http://library.athabascau.ca/drr/redirect.php?id=25155) [Swing: Part I](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27655)
-   [The Swing Connection](http://library.athabascau.ca/drr/redirect.php?id=25156) [The Swing Connection](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27656)

### Section 1: Swing Essentials
**Section Goal**: Introduce Java Swing

#### Learning Objective 1
-   Briefly describe the Java graphical user interface(GUI) history and the emergence of the Swing model.

##### Readings
**Required**: Pages 1303 to 1307 of TIJ

##### Exercises
**Questions**
1.  What are the characteristics and advantages of Swing? (See TIJ page 1304 to 1305.)
2.  According to the textbook author, what is the reason applets failed to be the next stage in the evolution in Internet use? (See TIJ page 1306.)

#### Learning Objective 2
-   Create a basic GUI using Swing.

##### Readings
**Required**: Pages 1307 to 1316 of TIJ

##### Exercises
**Questions**
1.  How do you submit a task to the Swing *event dispatch thread*? (See TIJ page 1308.)
2.  How do you capture events with Swing? (See TIJ pages 1312 to 1314.)
3.  How is a **JTextArea** different from a **JTextField**? (See TIJ page 1315.)

##### Programs
Compile, run, and analyze programs:

[HelloSwing.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/gui/HelloSwing.java)
[Hellolabel.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/gui/HelloLabel.java)
[SubmitLabelManipulationTask.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/gui/SubmitLabelManipulationTask.java)
[SubmitSwingProgram.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/gui/SubmitSwingProgram.java)
[Button1.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/gui/Button1.java)
[Button2.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/gui/Button2.java)
[Button2b.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/gui/Button2b.java)
[TextArea.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/gui/TextArea.java)

#### Learning Objective 3
-   Describe how Java Swing controls GUI layout.

##### Readings
**Required**: Pages 1317 to 1321 of TIJ

##### Exercises
**Questions**
1.  What are the predefined layouts in Swing? (See TIJ pages 1317 to 1320.)

##### Programs
Compile, run, and analyze programs:

[BorderLayout1.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/gui/BorderLayout1.java)
[FlowLayout1.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/gui/FlowLayout1.java)
[GridLayout1.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/gui/GridLayout1.java)

#### Learning Objective 4
-   Use the Java Swing event model to react to various GUI events.

##### Readings
**Required**: Pages 1321 to 1332 of TIJ

##### Exercises
**Questions**
1.  Describe the Swing event model. (See TIJ page 1321.)
2.  What Events and Listeners are available in Swing? (See TIJ pages 1322 to 1323.)
3.  How do listener adaptors simplify the coding of a program? (See TIJ page 1328.)

##### Programs
Compile, run, and analyze programs:

[ShowAddListeners.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/gui/ShowAddListeners.java)
[TrackEvent.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/gui/TrackEvent.java)

#### Learning Objective 5
-   Summarize the materials in the section and finish the exercises.

##### Exercises
Exercise 2 on page 1310, exercise 5 on page 1315, and exercise 10 on
page 1332 of TIJ

##### Answers To Exercises
-   [Answer 2](http://scis.athabascau.ca/html/course/COMP308/Unit_8/Section_1/Ch23ex2.java)
-   [Answer 5](http://scis.athabascau.ca/html/course/COMP308/Unit_8/Section_1/Ch23ex5.java)
-   [Answer 10](http://scis.athabascau.ca/html/course/COMP308/Unit_8/Section_1/Ch23ex10.java)

### Section 2: Java Swing Components
**Section Goal**: Describe and use common Swing components.

#### Learning Objective 1
-   Use Swing Components for GUI development - part 1.

##### Readings
**Required**: Pages 1332 to 1344 of TIJ

##### Exercises
**Questions**
1.  When is it necessary to use a button group? (See TIJ page 1334.)
2.  How do you add a tool tip to a component? (See TIJ page 1337.)

##### Programs
Compile, run, and analyze programs:

[Buttons.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/gui/Buttons.java)
[ButtonGroups.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/gui/ButtonGroups.java)
[Faces.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/gui/Faces.java)
[TextFields.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/gui/TextFields.java)
[Borders.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/gui/Borders.java)
[TextPane.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/gui/TextPane.java)
[CheckBoxes.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/gui/CheckBoxes.java)
[RadioButtons.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/gui/RadioButtons.java)

#### Learning Objective 2
-   Use Swing Components for GUI development - part 2.

##### Readings
**Required**: Pages 1345 to 1364 of TIJ

##### Exercises
**Questions**
1.  What is the difference between **JComboBox** and **JList**? (See TIJ pages 1345 to 1347.)
2.  What are the three types of menu items inherited from **JMenuItem**? (See TIJ page 1353.)
3.  What is the purpose of **paintComponent()**? (See TIJ pages 1360 to 1361.)

##### Programs
Compile, run, and analyze programs:

[ComboBoxes.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/gui/ComboBoxes.java)
[List.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/gui/List.java)
[TabbedPane1.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/gui/TabbedPane1.java)
[MessageBoxes.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/gui/MessageBoxes.java)
[SimpleMenus.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/gui/SimpleMenus.java)
[Menus.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/gui/Menus.java)
[Popup.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/gui/Popup.java)
[SineWave.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/gui/SineWave.java)

#### Learning Objective 3
-   Use Swing Components for GUI development - part 3.

##### Readings
**Required**: Pages 1364 to 1376 of TIJ

##### Exercises
**Questions**
1.  What is the purpose of a dialog box? (See TIJ pages 1364 to 1365.)
2.  How do you use UIManager to select a look & feel? (See TIJ pages 1373 to 1374.)

##### Programs
Compile, run, and analyze programs:

[Dialogs.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/gui/Dialogs.java)
[TicTacToe.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/gui/TicTacToe.java)
[FileChooserTest.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/gui/FileChooserTest.java)
[HTMLButton.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/gui/HTMLButton.java)
[Progress.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/gui/Progress.java)
[LookAndFeel.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/gui/LookAndFeel.java)

#### Learning Objective 4
-   Explain the issues of concurrency and Swing.

##### Readings
**Required**: Pages 1382 to 1393 of TIJ

##### Exercises
**Questions**
1.  What is one fundamental mistake sometime made when programming an application with a GUI interface? (See TIJ page 1382.)

##### Programs
Compile, run, and analyze programs:

[LongRunningTask.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/gui/LongRunningTask.java)
[InterruptableLongRunningTask.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/gui/InterruptableLongRunningTask.java)
[InterruptableLongRunningCallable.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/gui/InterruptableLongRunningCallable.java)
[MonitoredLongRunningCallable.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/gui/MonitoredLongRunningCallable.java)
[ColorBoxes.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/gui/ColorBoxes.java)

#### Learning Objective 5
-   Summarize the materials in this section and finish the exercises.

### Digital Reading Room
Unit 8 Section 2 Links
-   [Apache ANT](http://library.athabascau.ca/drr/redirect.php?id=8133)
-   [Introduction to ANT using JUnit](http://library.athabascau.ca/drr/redirect.php?id=8134)
-   [Technical tips on using Logger](http://library.athabascau.ca/drr/redirect.php?id=8135)
-   [A collection of questions of OO design](http://library.athabascau.ca/drr/redirect.php?id=8136)

##### Programs
**Note**: The objectives **Programs** examples are intended to clarify
any problems you have understanding these programs in the text. You do
not have to compile and run every program if you are sure you understand
the function of the programs.

### Section 3: Java Beans
**Section Goal**: Discuss and use JavaBeans.

#### Learning Objective 1
-   Create a basic Bean.

##### Readings
**Required:** Pages 1393 to 1403 of TIJ

##### Exercises
**Questions**
1.  What is critical about the use of visual components? (See TIJ pages 1393 to 1395.)
2.  What is a JavaBean? (See TIJ pages 1395 to 1396.)

##### Programs
Compile, run, and analyze programs:

[Frog.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/frogbean/Frog.java)
[BeanDumper.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/gui/BeanDumper.java)

#### Learning Objective 2
-   Create a sophisticated Bean.

##### Readings
**Required:** Pages 1403 to 1412 of TIJ.

##### Exercises
**Questions**
1.  What is the role of serialization in creating Beans? (See TIJ pages 1405 to 1406.)
2.  Why is it important that the public methods of a Bean be synchronized? (See TIJ pages 1407 to 1408.)

##### Programs
Compile, run, and analyze programs:

[BangBean.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/bangbean/BangBean.java)
[BangBeanTest.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/bangbean/BangBeanTest.java)
[BangBean2.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/gui/BangBean2.java)

#### Learning Objective 3
-   Package Java Beans into JAR files

##### Readings
**Required**: Pages 1412 to 1415 of TIJ

##### Exercises
**Questions**
1.  How do you package all Bean classes into a JAR file? (See TIJ page 1412.)

#### Learning Objective 4
-   Summarize the materials in this section and complete the exercises.

### Section 4: Java Client
**Section Goal**: Discuss various strategies of developing and launching
clients over the Internet.

#### Learning Objective 1
-   Briefly describe Java applets.

##### Readings
**Required**: Page 1306 of TIJ.

**External link**: [A brief introduction to applets](http://library.athabascau.ca/drr/redirect.php?id=25149)

##### Exercises
**Questions**
1.  According to the textbook author, what are the reasons that the applet revolution did not happen? (See TIJ pages 1306.)

#### Learning Objective 2
-   Explain JNLP and Java Web Start.

##### Readings
**Required:** Pages 1376 to 1382 of TIJ.

##### Programs
Compile, run, and analyze programs:

[JnlpFileChooser.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/gui/jnlp/JnlpFileChooser.java)

#### Learning Objective 3
-   Briefly describe *Flex* as an alternative to Swing.

##### Readings
**Required**: Pages 1415 to 1430 of TIJ

##### Programs
Compile, run, and analyze programs:

[SongService.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/gui/flex/SongService.java)

#### Learning Objective 4
-   Briefly discuss SWT as and alternative to Swing.

##### Readings
**Required**: Pages 1430 to 1447 of TIJ

##### Programs
Compile, run, and analyze programs:

[HelloSWT.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/swt/HelloSWT.java)
[Menus.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/swt/Menus.java)
[TabbedPane.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/swt/TabbedPane.java)
[SineWave.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/swt/SineWave.java)
[ColorBoxes.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/swt/ColorBoxes.java)

## Unit 9: Concurrency

### Unit Purpose
Explain and use Java support of concurrency.

### Conferencing
Post any questions or comments to the CMC system (conferencing is optional, but is recommended)

### Digital Reading Room

-   [Overview of Java XML APIs](http://library.athabascau.ca/drr/redirect.php?id=11518)
-   [Introduction to SAX (Simple API for XML)](http://library.athabascau.ca/drr/redirect.php?id=11519)
-   [Create an XML file for SAX parsing](http://library.athabascau.ca/drr/redirect.php?id=11520)
-   [Parse an XML file using SAX parser](http://library.athabascau.ca/drr/redirect.php?id=11521)
-   [xerces parser](http://library.athabascau.ca/drr/redirect.php?id=12349)
-   [Xalan xslt processor](http://library.athabascau.ca/drr/redirect.php?id=12350)
-   [MSDN Download](http://library.athabascau.ca/drr/redirect.php?id=12351)
-   [Javadoc utility](http://library.athabascau.ca/drr/redirect.php?id=25165)

  [Overview of Java XML APIs](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27659)
  [Validator](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27660)
  [On-line Validator](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27661) Validate Your XML Document Using IBM's XML4J Parser
  [Introduction to SAX (Simple API for XML)](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27662)
  [Browser Information](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27663)
  [Create an XML file for SAX parsing](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27664)
  [XML DTD - An Introduction to XML Document Type Definitions](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27665)
  [Parse an XML file using SAX parser](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27666)
  [Altova XMLSpy®](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27667) the industry standard XML development environment for modeling, editing, debugging, and transforming all XML technologies
  [xerces parser](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27668)
  [Cover pages: Validate/Check XML](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27669)
  [Xalan xslt processor](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27670)
  [XML :: XQL :: Tutorial](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27671)
  [MSDN Download](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27672)
  [WDVL:XLink and XPointer: XML Linking/Pointer Languages](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27673)
  [Brett McLaughlin, Java & XML: SOAP](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27674) O'REILLY on-line catalog
  [Javadoc utility](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27675)

### Section 1: Basic Threads
**Section Goal**: Explain and use basic threads features of Java.

#### Learning Objective 1
-   Explain the idea of concurrency programming.

##### Readings
**Required**: Pages 1109 to 1116 of TIJ

##### Exercises
**Questions**

1.  What is meant by *preemptive* threading? (See TIJ page 1115.)

#### Learning Objective 2
-   Explain and use basic Java threading features.

##### Readings
**Required**: Pages 1116 to 1150 of TIJ

##### Exercises
**Questions**

1.  How do youdefine a task in Java? (See TIJ page 1116 to 1117.)
2.  How do you write a program as a **Thread**? What will happen when making a call to **start()**? (See TIJ pages 1118 to 1119.)
3.  In what way does an **Executor** simplify the management of asynchronous tasks? Give an example. (See TIJ pages 1120 to 1121.)
4.  What is the difference between a **Runnable** interface and a **Callable** interface? (See TIJ pages 1124 to 1125.)
5.  What is the effect of calling **yield()**? (See TIJ pages 1129 to 1130.)
6.  What is a daemon thread? (See TIJ page 1130.)

##### Programs
Compile, run and analyse programs:

[LiftOff.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/LiftOff.java)
[MainThread.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/MainThread.java)
[BasicThreads.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/BasicThreads.java)
[MoreBasicThreads.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/MoreBasicThreads.java)
[CachedThreadPool.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/CachedThreadPool.java)
[FixedThreadPool.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/FixedThreadPool.java)
[SingleThreadExecutor.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/SingleThreadExecutor.java)
[CallableDemo.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/CallableDemo.java)
[SleepingTask.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/SleepingTask.java)
[SimplePriorities.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/SimplePriorities.java)
[SimpleDaemons.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/SimpleDaemons.java)
[DaemonFromFactory.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/DaemonFromFactory.java)
[Daemons.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/Daemons.java)
[DaemonsDontRunFinally.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/DaemonsDontRunFinally.java)
[SimpleThread.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/SimpleThread.java)
[SelfManaged.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/SelfManaged.java)
[ThreadVariations.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/ThreadVariations.java)
[Joining.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/Joining.java)
[ResponsiveUI.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/ResponsiveUI.java)
[ExceptionThread.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/ExceptionThread.java)
[CaptureUncaughtException.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/CaptureUncaughtException.java)
[SettingDefaultHandler.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/SettingDefaultHandler.java)

#### Learning Objective 3
-   Discuss the issues of sharing resources among threads.

##### Readings
**Required** : Pages 1150 to 1179 of TIJ.

##### Exercises
**Questions**
1.  What is the purpose of the **synchronized** keyword in Java? (See TIJ pages 1154 to 1155.)
2.  Explain how to use a **Lock** object. (See TIJ pages 1157 to 1158.)
3.  What is an *atomic operation* and how do you get atomicity in Java? (See TIJ page 1160.)
4.  According to the textbook author, what is the general principle of using **Atomic** classes? (See TIJ page 1169.)
5.  What is a *critical section* and how do you create it? (See TIJ page 1169.)
6.  What are the ways to prevent tasks from colliding over shared resources? (See TIJ pages 1175 to 1177.)

##### Programs
Compile, run, and analyze programs:

[EvenChecker.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/EvenChecker.java)
[EvenGenerator.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/EvenGenerator.java)
[SynchronizedEvenGenerator.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/SynchronizedEvenGenerator.java)
[MutexEvenGenerator.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/MutexEvenGenerator.java)
[AttemptLocking.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/AttemptLocking.java)
[AtomicityTest.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/AtomicityTest.java)
[SerialNumberGenerator.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/SerialNumberGenerator.java)
[SerialNumberChecker.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/SerialNumberChecker.java)
[AtomicIntegerTest.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/AtomicIntegerTest.java)
[AtomicEvenGenerator.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/AtomicEvenGenerator.java)
[CriticalSection.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/CriticalSection.java)
[ExplicitCriticalSection.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/ExplicitCriticalSection.java)
[SyncObject.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/SyncObject.java)
[ThreadLocalVariableHolder.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/ThreadLocalVariableHolder.java)

#### Learning Objective 4
Explain the issues of terminating tasks.

##### Readings
**Required**: Pages 1179 to 1197 of TIJ

##### Exercises
**Questions**
1.  What are the four states a Java Thread can be in? (See TIJ pages 1183 to 1184.)
2.  What are the four ways a Java Thread can become blocked? (See TIJ page 1184.)
3.  What will happen when the **interrupt()** method is being called? (See TIJ page 1185.)

##### Task
Compile, run, and analyze programs:

[OrnamentalGarden.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/OrnamentalGarden.java)
[Interrupting.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/Interrupting.java)
[CloseResource.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/CloseResource.java)
[NIOInterruption.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/NIOInterruption.java)
[MultiLock.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/MultiLock.java)
[Interrupting2.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/Interrupting2.java)
[InterruptingIdiom.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/InterruptingIdiom.java)

#### Learning Objective 5
-   Discuss the issues of task cooperation.

##### Readings
**Required**: Pages 1197 to 1223 of TIJ

##### Exercises
**Questions**
1.  Why does busy waiting generally considered undesirable? What is the consequences of calling **wait()** in comparison to **sleep()** or
    **yield()**? (See TIJ pages 1199.)
2.  What is the difference between **notify()** and **notifyAll()**? (See TIJ pages 1204 to 1205.)

##### Task
Compile, run, and analyze programs:

[WaxOMatic.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/waxomatic/WaxOMatic.java)
[NotifyVsNotifyAll.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/NotifyVsNotifyAll.java)
[Restaurant.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/Restaurant.java)
[WaxOMatic2.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/waxomatic2/WaxOMatic2.java)
[TestBlockingQueues.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/TestBlockingQueues.java)
[ToastOMatic.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/ToastOMatic.java)
[PipedIO.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/PipedIO.java)

#### Learning Objective 6
-   Explain the issue of deadlock.

##### Readings
**Required**: Pages 1223 to 1229 of TIJ

##### Exercises
**Questions**
1.  What is a *deadlock*? What are the conditions that a deadlock can occur? (See TIJ pages 1223 and 1227 to 1228.)

##### Programs
Compile, run, and analyze programs:

[Chopstick.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/Chopstick.java)
[Philosopher.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/Philosopher.java)
[DeadlockingDiningPhilosophers.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/DeadlockingDiningPhilosophers.java)
[FixedDiningPhilosophers.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/FixedDiningPhilosophers.java)

#### Learning Objective 7
-   Explain and use Java 5 support on concurrency.

##### Readings
**Required**: Pages 1223 to 1253 of TIJ

##### Exercises
**Questions**

1.  What is the purpose of a **CountDownLatch** object? Give an example. (See TIJ pages 1230 to 1232.)
2.  What is the purpose of a **CyclicBarrier** object? Give an example. (See TIJ pages 1232 to 1235.)
3.  What is a **counting semaphore**? (See TIJ page 1246.)

##### Programs
Compile, run, and analyze programs:

[CountDownLatchDemo.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/CountDownLatchDemo.java)
[HorseRace.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/HorseRace.java)
[DelayQueueDemo.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/DelayQueueDemo.java)
[PriorityBlockingQueueDemo.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/PriorityBlockingQueueDemo.java)
[GreenhouseScheduler.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/GreenhouseScheduler.java)
[Pool.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/Pool.java)
[Fat.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/Fat.java)
[ExchangerDemo.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/ExchangerDemo.java)

#### Learning Objective 8
-   Summarize the materials in this section and complete the exercises.

##### Exercises
Exercise 1 on page 1120, exercise 3 on page 1124, exercise 15 on page
1177, and exercise 24 on page 1212 of TIJ.

##### Answers To Exercises
-   [Answer 1](http://scis.athabascau.ca/html/course/COMP308/Unit_9/Section_1/Ch22ex1.java)
-   [Answer 3](http://scis.athabascau.ca/html/course/COMP308/Unit_9/Section_1/Ch22ex3.java)
-   [Answer 15a](http://scis.athabascau.ca/html/course/COMP308/Unit_9/Section_1/Ch22ex15a.java)
-   [Answer 15b](http://scis.athabascau.ca/html/course/COMP308/Unit_9/Section_1/Ch22ex15b.java)
-   [Answer 24](http://scis.athabascau.ca/html/course/COMP308/Unit_9/Section_1/Ch22ex24.java)

### Section 2: Issues of Concurrency
**Section Goal**: This section introduces the advanced features of
concurrency in Java 5.

#### Learning Objective 1
-   Discuss various examples of applying Java concurrency support on simulation.

##### Readings
**Required**: Pages 1253 to 1270 of TIJ

##### Exercises
**Questions**

1.  Examine the example on pages 1264 to 1269. Do you think we should synchronize all methods in class Car? (open question)

##### Programs
Compile, run, and analyze programs:

[BankTellerSimulation.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/BankTellerSimulation.java)
[RestaurantWithQueues.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/restaurant2/RestaurantWithQueues.java)
[CarBuilder.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/CarBuilder.java)

#### Learning Objective 2
-   Discuss performance issues of Java concurrency support.

##### Readings
**Required**: Pages 1270 to 1295 of TIJ

##### Exercises
**Questions**

1.  According to the textbook author, what are the factors affecting the use of the **synchronized keyword**? (See TIJ pages 1280 to 1281.)
2.  What is the general strategy behind lock-free containers? (See TIJ page 1281.)
3.  What is optimistic locking? (See TIJ page 1290.)
4.  Under what circumstance cn a **ReadWriteLock** can help to optimize locking? (See TIJ 1292.)

##### Programs
Compile, run, and analyze programs:

[SimpleMicroBenchmark.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/SimpleMicroBenchmark.java)
[SynchronizationComparisons.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/SynchronizationComparisons.java)
[Tester.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/Tester.java)
[ListComparisons.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/ListComparisons.java)
[MapComparisons.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/MapComparisons.java)
[FastSimulation.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/FastSimulation.java)
[ReaderWriterList.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/ReaderWriterList.java)

#### Learning Objective 3
-   Discuss the idea of active objects as alternative to threading control.

##### Readings
**Required**: Pages 1295 to 1299 of TIJ

##### Exercises
**Questions**

1.  What are the characteristics of an active object? (See TIJ pages 1298 to 1299.)

##### Programs
Compile, run, and analyze programs:

[ActiveObjectDemo.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/concurrency/ActiveObjectDemo.java)

#### Learning Objective 4
-   Summarize the materials in this section.

##### Readings
**Required**: Pages 1300 to 1302 of TIJ

-   [Ask AU Library](http://library.athabascau.ca/AskAULibrary.html "Ask AU Library")
-   [Library](http://library.athabascau.ca/ "myAU Student Portal")
-   [myAU](http://my.athabascau.ca/ "myAU Student Portal")
-   [Index of Digital Reading Room](http://drr2.lib.athabascau.ca/)

1.  [<span class="glyphicon glyphicon-home" aria-hidden="true"></span>](http://drr2.lib.athabascau.ca/index.php)
2.  [COMP](http://drr2.lib.athabascau.ca/index.php?c=index&m=listcourses&sid=44)
3.  COMP 308: Java for Programmers

## Unit 10: Annotations and Java Documentation

### Unit Purpose
This unit introduces annotation and metadata, Java documentation, and deployment issues of Java applications.

### Section 1: Annotations
**Section goal**: This section explains a formalized way to add information to your Java codes so that you can use easily use the data later.

#### Learning Objective 1
-   Discussthe basic idea and syntax of annotation.

##### Readings
**Required**: Pages 1059 to 1063 of TIJ

##### Exercises
**Questions**
1.  What is the syntax of annotations? (See TIJ pages 1060 to 1061.)
2.  What are the three standard annotations and the four meta-annotations defined in Java? (See TIJ pages 1059 to 1060, 1063)

##### Programs
Compile, run, and analyze programs:

[Testable.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/annotations/Testable.java)
[UseCase.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/annotations/UseCase.java)
[PasswordUtils.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/annotations/PasswordUtils.java)

#### Learning Objective 2
-   Explain how to write annotation processors.

##### Readings
**Required**: Pages 1064 to 1074 of TIJ

##### Exercises
**Questions**

1.  What are the allowed types for annotation elements? (See TIJ page 1065.)
2.  Explain the circumstance in which annotations are useful. (See TIJ pages 1066 to 1069.)

##### Programs
Compile, run, and analyze programs:
[UseCaseTracker.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/annotations/UseCaseTracker.java)
[Constraints.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/annotations/database/Constraints.java)
[Member.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/annotations/database/Member.java)
[TableCreator.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/annotations/database/TableCreator.java)

#### Learning Objective 3
-   Explain how to use the **apt** annotation processing tool.

##### Readings
**Required**: Pages 1074 to 1083 of TIJ

##### Programs
Compile, run, and analyze programs:
[Multiplier.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/annotations/Multiplier.java)
[InterfaceExtractorProcessor.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/annotations/InterfaceExtractorProcessor.java)
[InterfaceExtractorProcessorFactory.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/annotations/InterfaceExtractorProcessorFactory.java)
[TableCreationProcessorFactory.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/annotations/database/TableCreationProcessorFactory.java)

#### Learning Objective 4
-   Explain annotation-based unit testing

##### Readings
**Required**: Pages 1083 to 1106 of TIJ

##### Programs
Compile, run, and analyze programs:

[AtUnitExample1.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/annotations/AtUnitExample1.java)
[AtUnitExternalTest.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/annotations/AtUnitExternalTest.java)
[AtUnitComposition.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/annotations/AtUnitComposition.java)
[AtUnitExample2.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/annotations/AtUnitExample2.java)
[HashSetTest.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/annotations/HashSetTest.java)
[AtUnitExample3.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/annotations/AtUnitExample3.java)
[AtUnitExample4.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/annotations/AtUnitExample4.java)
[AtUnitExample5.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/annotations/AtUnitExample5.java)
[StackLStringTest.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/annotations/StackLStringTest.java)
[AtUnit.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/net/mindview/atunit/AtUnit.java)
[ClassNameFinder.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/net/mindview/atunit/ClassNameFinder.java)
[AtUnitRemover.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/net/mindview/atunit/AtUnitRemover.java)

#### Learning Objective 5
-   Summarize the materials in this section.

##### Readings
**Required**: Pages 1106 to 1107 of TIJ

### Section 2: Java Documentation
**Section goal**: This section explains the use of Javadoc utility.

#### Learning Objective 1
-   Use javadoc.

##### Readings
**Required**: [Using Javadoc](http://library.athabascau.ca/drr/redirect.php?id=25165)

## Tutor Marked Exercise 4 ( / 20 percent)

## Final Exam ( / 50 percent)
The exam will be a closed-book online examination three hours in length.
- Nine percent of the mark will be for analyzing a program and describing its output.
- Thirty percent of the mark will be for 10 short-answer questions (100 words or less) from the questions in the Study Guide.
- Twenty-seven percent of the mark will be for three questions relating to the tutor-marked exercises (TMEs).
- Twenty-four percent of the mark will be for programming questions. You will not be expected to have the syntax totally correct nor memorize all the class libraries you have used in the course. However, you should be able to make it clear what classes and methods you are using, and you should be familiar with any classes you used in the tutor marked exercises (TMEs). The question will give details on the classes you must use and on some you may wish to use.
- Five percent of the mark will be for your assessment, in 500 words or less, of Java as a programming language from both a technical and a market viewpoint and your view of the future of Java.
- Five percent of the mark will be for your assessment, in 500 words or less, of Java generics.
