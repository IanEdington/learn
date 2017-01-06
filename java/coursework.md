# Course Handbook
## Language Constructs
### Reserved names
Reserved names:
    special values
        true
        false
        null
        void
    primitives
        boolean
        char
        byte
        short
        int
        long
        float
        double
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

### indexing
Java is a zero indexed language.
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

### Base types (primitives)
bool, char and 6 number types:

`boolean`: a boolean value (`true` or `false`)
`char`: a 16-bit unicode character value
- denoted with single quotes: `i`
`byte`: 8-bit signed two's compliment integer
`short`: 16-bit signed two's compliment integer
`int`: 32-bit signed two's compliment integer
`long`: 64-bit signed two's compliment integer
`float`: 32-bit floating point number
`double`: 64-bit floating point number

#### Wrapper Types
Each primitive has a corresponding wrapper object type. This is because many datastructures and algorythems in Java are specifically designed for objects, not primitives.

Automatic boxing and unboxing is the process of converting from primitive to wrapper and back.
The result is that you can use the primitive and wrapper class interchangeably.

### Array
TODO: what happens when you declare an array of objects? Are arrays limited to primivites?

Arrays are a special type of object with slightly different syntax.

Has final property `length` 

```java
// Declare an array variable (pointer):
int[ ] variableName;

// create array and assign to variable
variableName = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};

// create new array with size n
variableName = new elementType[n];

// declare array variable and assign it a new array
double[ ] measurements = new double[1000];

// retreive length of array
System.out.println(measurements.length);
```

### Enum types
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

### Strings
Java has a built in string class denoted by double quotes

```
String title = "Data Structures & Algorithms in Java";
char[ ] msg = original.toCharArray();
```

indexing by character
the String class is immutable
For a mutable string use the StringBuilder class.



### Expressions
#### Literals
Constants in the expression

- **null**: only object literal, allowed to be any object type.
- Boolean: **true** and **false**.
- Integer & Floating point: Literal number
- Character: surrounded by single quotes
        '\n' (newline)
        '\b' (backspace)
        '\f' (form feed)
        '\'' (single quote)
        '\t' (tab)
        '\r' (return)
        '\\' (backslash)
        '\"' (double quote)
- Strings: surrounded by double quotes

#### Operators

Arithmetic

```
    + addition
    − subtraction
    ∗ multiplication / division
    % the modulo operator
    -- unary minus: reverses sign of number (* -1)
```

Increment and decrement

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

TODO: what happens when there's multiple ++ operators in a single line?
ie:

```
    a[5] = 10;
    j = 5;
    a[j++] = a[j++] + 2;
```

String

```
    + string concatenation
```

Logic

```
    < less than
    <= less than or equal to == equal to
    != not equal to
    >= greater than or equal to
    > greater than

    ! not (prefix)
    && conditional 
    || conditional or
```

Bitwise (for boolean and integer variables)

```
    ∼ bitwise complement (prefix unary operator)
    & bitwise and | bitwise or
    ˆ bitwise exclusive-or
    << shift bits left, filling in with zeros
    >> shift bits right, filling in with sign bit
    >>> shift bits right, filling in with zeros
```

Assignment

```
    = straight assignment
    op= : assignment while performing operation (op)

    x op= 2 is equivalent to x = x op 2
```

#### Operator precedence

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
|9| bitwise-xor | ˆ |
|10| bitwise-or | &#124; |
|11| and | && |
|12| or | &#124;&#124; |
|13| conditional | booleanExpression ? valueIfTrue : valueIfFalse |
|14| assignment | = += −= ∗= /= %= <<= >>= >>>= &= ˆ= &#124;= |

#### Control Flow
- single statement bodies don't need curly braces

##### If

```java
if (firstBooleanExpression)
    firstBody
else if (secondBooleanExpression) {
    secondBody
    withTwoLines
} else
    thirdBody
```

##### Switch
Evaluates expression which must result in an integer, string, or Enum.
Jumps to case that matches that result, or the default expression.
This is the only explicit jump, therefor a brake statement must be used to exit the switch once the code is finished or it will continue evaluating the next expression.

- especially useful with Enum types
- no curly braces are needed

```
switch (expression) {
    case result1:
        System.out.println("This is tough.");
        break;
    case result2:
        System.out.println("This is getting better.");
        break;
    default:
        System.out.println("Day off!");
}
```

##### While Loop

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

##### Do While
Same as While but executes body once before evaluating.
Most useful where the condition is dependent on the body code.

```
do
    loopBody
while (booleanExpression)
```

##### For
```
for (initialization; booleanCondition; increment)
    loopBody

for (int i = 0; i < length; i++) {
    loopBody
}
```
- variables define in initialization step are only available in loop scope
- booleanCondition is checked at beginning of loop
- increment is executed after the loopBody and can be any valid statement.

##### For each
introduced in java 5

```
for (elementType containerElement : container)
    loopBody
```

- container must either be an array of `elementType` or a collection that implements the Iterable interface.
- containerElement is assigned next element in the container and is scoped to the loop
    - regular assignment rules apply as per [object-assignment](#object-assignment)

##### Explicit Control flow (continue and break)
`break` moves flow of control out of a switch, for, while, or do-while
`continue` moves flow of control to the end of the loopBody
TODO: does `continue` execute the condition at the end of a do-while loop?

#### return
A method that is declared as returning a type must return that type!
TODO: in a Java method defined as returning void can you `return void`?

### Variables, Objects and Assignment
All variables must be declaired before they are used.
There are two main types of variables; primivites and objects.
Objects are actually pointers(references) to a datastructure, whereas a primitives is the data.

When two variables are assigned the same object they are assigned the same instance of that object.
For primitives this means making a replica of the data point.
For Objects this means making a replica of the **pointer**.<a name="object-assignment"></a>

Declare constants using `final` modifier

### Objects
#### Class Modifiers
Access control modifiers:
- default without any modifier (package-private): restricts access to within the same package
- public: an element with this modifier can be accessed from anywhere by any class or method
- private: ONLY accessible to the class itself
- protected: restricts access to a class, method or variable to:
    - classes that are part of the same package
    - sub-classes through inheritance

static:
Created and associated with class instead of instance.
This means there is only one version for every instance to share.
When methods are static they are usually called using the ClassName instead of the instanceName.

abstract:
Define only the Method Signature.
This allows for public classes to be completely abstracted from the user.

final:
Final version of that element:
- final variable is similar to a constant, and usually has static (uses less space)
Final method or class: Only relevant for inheritance
- a final method cannot be overriden by a subclass
    - TODO: is this specific to the name of the method or to the method signature?
- a final class cannot be have a subclass

#### Methods
Method Signature: Method name with the number and types of its parameters
An object can have multiple methods with the same name so long as they return the same type(because type isn't part of the "Method Signature").
When multiple methods are present, the JVM uses the first method that matches the number and type of parameters being called.

#### Declaring methods and variables
Declaring a class (static) or instance (without static) variable
$$$
[modifiers] type identifier_1[=initialValue1], identifier_2[=initialValue2];
$$$

Declaring a Method signature and method body
$$$
[modifiers] returnType methodName(type_1 param_1, ..., type_n param_n) {
    // method body ...
}
$$$

Void is a valid `returnType`.
Method must return a value of type `returnType`.
If multiple items must be returned:
- return a compound object
- modify the internal state of an existing object

Parameters are passed as copies of the original value using assignment. see [object-assignment](#object-assignment)
- objects passed can be modified

#### Constructor Method
Define a constructor method by naming it after the class.  
Default: `public nameOfClass() { }`. If you override the default the default signature won't be available.

1. cannot be static, abstract, or final
1. cannot specify a `returnType`

Constructing a `new` object with variables initiated.  
1. new object is allocated in memory on the heap (dynamically)
1. instance variables are initialized
1. the constructor method is called
1. returns a (reference | memory address | pointer) to the newly created object

#### this
Static pointer to the class instance from within an instance method (nonstatic).
- instance variables can be accessed from within a method, however, `this` allows differentiation between instance variables and local variables
- allows calling other instance methods from within an instance method `this.method()`
- allows calling one constructor from within another constructor `this()`

Method scope is inherited from class so `this` is not required to reference instance variables.

#### The main Method
must be declared as follows:

```java
public static void main(String[ ] args) {
    // main method body...
}
```



#### Object equality
TODO: how is equality determined in Java?

#### Inheritence
`extend` is used to create a sub-class in java
`super` is like `this` but refers to the super-class.

In Java, each class can extend exactly one other class. Because of this property, Java is said to allow only single inheritance among classes.

The constructor methods are never inherited in java.
`super()` is used to call a method from within the sub-class constructor.
If `super(*args)` is not found an implicit call to `super()` is made before a sub-classes constructor.


#### Polymorphism
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

#### Abstract Class
A class that is partially defined in that you can mix methods with method signatures.
`abstact` modifier must be used for abstract classes or methods within an abstact class.
- can extend another class
- can implement an interface
- can not produce object
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

#### Interface

`interface` defines an interface. Same modifiers as class but without method body.
`implements` keyword is used to declare a class as implementing an interface.
- a class can implement multiple interfaces
- an interface can extend multiple other interfaces

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

#### Casting object and interfaces
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

### Generics
Introduced in Java 5.
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

#### Arrays and Generics

#### Generic Methods

#### Bounding Generic types

### Nested Classes
Useful for keeping closely related classes together.


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

fully qualified name is OuterName.NestedName
private nested class can be used by the outer class, but by no other classes

A nonstatic nested class (inner class) can only be created from within a nonstatic method of the outer class. The inner instance becomes associated with the outer instance that creates it.
The outer instance can be referenced from within the inner class using `OuterName.this`
Inner instance has private access to all members of its associated outer instance, and can rely on the formal type parameters of the outer class, if generic.


### Exceptions
#### Checked vs Un-Checked exceptions
TODO: understand and take notes on Checked vs Un-Checked exceptions

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

#### Throwing Exceptions
`throw`: from within a method, throw an exception

Usually when throwing an exception a new exception object is created with optional constructor parameters.

#### Catching
```java
try {
    guardedBody
} catch (exceptionType1 variable1) {
    remedyBody1
} catch (exceptionType2 | exceptionType3 variable2) {
    remedyBody2
} catch ...
```

exceptionType: valid exception type extending the Exception class
|: separates multiple exceptions
variable: valid java variable name holding the execption object

#### Creating new Exception types
An exception is a special class extended from the Exception class.
Create a new exception type by extending the Exception class or any of it's subclasses.


### Package management
Group files containing Enums and Classes into packages by:
- all located in directory _packagename_
- first line of every file must be `package packagename;`

By convention:
- packages are lowercase
- classes are camel case
You immediately know if referring to a package or a class within a package.

Reverse URL package names are recommended to avoid name collision.
ie. com.ianedington.comp308.tpa1

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

### Compilation
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

#### ClassPath
Calling `java program.class` the runtime environment locates the packages and class according to a special operating system environment variable named “CLASSPATH”.
This variable defines an order of directories in which to search for the package or class.

```
export CLASSPATH=.:/usr/local/java/lib:/usr/netscape/classes
```

## Object Oriented Programming
### Design Patters
#### Template method
#### Composition
#### Adapter
#### Position
#### Iterator
#### Factory Method
#### Comparator
#### Locator

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

## Testing

- zero, null, '', "", or empty value
- 

## Unit 0: Introducing the Java Platform
### Section 1: Annotations and Java Documentation

**Section Goal and Notes:** Learn about the basics of Java versions and
Java development environment.

The current Java version is Java 6; however this course will require a
minimum of Java version 5. Java 5 was originally called Java 1.5 and
this causes some confusion; we will refer to this version of Java as
Java 5 throughout the course. All programs you submit as assignments
must compile and run with Java 5. In case you are planning to use
features in Java 6, you must inform your tutor in advance. Although Java
is backward compatible with earlier versions, deprecated (outdated)
methods should not be used. You must get your approval from your tutor
in case of absolute necessity.

You must download [Java Development Kit (JDK)](http://scis.athabascau.ca/virtualhelpdesk/topics/java_help/) from
Sun. Do not mix up JDK with JRE. While there are various other products
on the market which *may* serve the purpose, it is your responsibility
to ensure the platform you choose supports Java 5 features.

If you are not familiar with the Java language, we recommend using JDK
alone. For JDK the only tools that are absolutely necessary to complete
the course are the javac compiler and the java interpreter. Both of them
run in the command prompt.

If you are planning to use an IDE (integrated design environment), do
not expect your tutor to be able to support it. There are so many IDEs
on the market that no one person is able to support all of them. You
will find a list of a few popular IDEs in Unit 1 Section 2 for your
reference. Remember, the primary purpose of this course is to learn the
Java language, not IDEs.

### Section 2: Java Language and Platform
**Section Goal: ** Describe the Java language and the various components
of the Java platform.

#### Learning Objective 1: Describe the Java language and platform. and the Java platform.

##### Readings
**Required:**
-   [About the Java Technology](http://library.athabascau.ca/drr/redirect.php?id=8121)

##### Exercises
**Questions**
1.  What buzzwords can be used to describe the Java language?
2.  What is the Java platform?

#### Learning Objective 2: Describe key features of the Java platform.

##### Readings
**Required:**
-   [What Can Java Technology Do? (1 page)](http://library.athabascau.ca/drr/redirect.php?id=8122)

##### Exercises
**Questions**
1.  How does the Java API support many kinds of programs?

#### Learning Objective 3: Outline the advantages of Java.

##### Readings
**Required:**
-   [How will Java technology change my life?](http://library.athabascau.ca/drr/redirect.php?id=8123)

##### Exercises
**Questions**
1.  What are the advantages of Java?



## Unit 1: Getting Started with the Java Programming Language
### Unit Purpose
Design, develop, implement and run a simple
Java application. This unit provides a bit of hands-on experience with
Java programs especially for the complete novice before the course gets
into the intricacies of Java programming.

### Conferencing
Post any questions or comments to the CMC system (conferencing is optional, but is recommended).

### Digital Reading Room
-   [A Checklist](http://library.athabascau.ca/drr/redirect.php?id=11428) [A Checklist](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27614)
-   [Creating Your First Application](http://library.athabascau.ca/drr/redirect.php?id=11480)
  [Creating Your First Application](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27615)
-   [A Closer Look at Hello World Application](http://library.athabascau.ca/drr/redirect.php?id=11482)
  [A Closer Look at Hello World Application](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27616)
0i-   [Getting Started with Applets](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27617)
0i-i   [Applets](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27618)
-   [NetBeans IDE](http://library.athabascau.ca/drr/redirect.php?id=24566) [NetBeans IDE](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27619)
-   [JCreator](http://library.athabascau.ca/drr/redirect.php?id=24567) [JCreator](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27620)
-   [Borland JBuider](http://library.athabascau.ca/drr/redirect.php?id=24568) [Borland JBuider](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27621)
-   [BlueJ](http://library.athabascau.ca/drr/redirect.php?id=24569) [BlueJ](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27622)
-   [JGrasp](http://library.athabascau.ca/drr/redirect.php?id=24570) [JGrasp](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27623)
-   [Eclipse](http://library.athabascau.ca/drr/redirect.php?id=24571) [Eclipse](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27624)


### Section 1: Java Applets and Applications
**Section Goal:**  Compile and run a simple Java application using the
Sun JDK.

#### Learning Objective 1: Confirm that the necessary tools are in place for your first Java Application using the JDK.

##### Readings
**Required:**
-   [A Checklist](http://library.athabascau.ca/drr/redirect.php?id=11428)

**Note**: The current version as posted by Sun is Java 6. Java 6 will
not affect the content of the course and the textbook.

##### Exercises
Review the checklist and install the software if necessary.

#### Learning Objective 2: Create, compile, and run your first Java application using the JDK.

##### Readings
**Required:**
-   [Creating Your First Application](http://library.athabascau.ca/drr/redirect.php?id=11480)

##### Exercises
Complete the reading instructions.

#### Learning Objective 3: Review creating Java applications.

##### Readings
**Required:**
-   [A Closer Look at Hello World Application](http://library.athabascau.ca/drr/redirect.php?id=11482)

##### Exercises
**Questions**

1.  What is the skeleton for any Java program?
2.  What is the entry point for any Java application?
3.  What is the function of the import statement?

### Section 2: (Optional) Introduces popular Java IDEs
**Section Goal and Note**: This section briefly describes the idea of an
IDE. Notice that the use of an IDE is entirely optional in this course.
As noted below it takes time to learn both an IDE and Java at the same
time. Students is advised to use discretion choosing an IDE.

IDE (Integrated Development Environment) is a software tool to assist in
the development of a software product. An IDE normally consists of a
source code editor, debugger and compiler/interpreter as well as many
automated tools. It is usually a good idea to use an IDE for a software
project as it will reduce coding time and helps to maintain a certain
consistency of the software. However, just as with any other software
tool, it takes time to learn to use an IDE. A student who plans to learn
both Java and the IDE must allow sufficient time in the studies. Do not
confuse features of an IDE with features of Java.

You will find a list of IDEs at the end of Unit links.


## Unit 2: Object Oriented Programming with Java
### Unit Purpose
Describe the basics of object-oriented programming
with Java.

### Conferencing

### Section 1: Methods and Parameters
**Section Goal:** Introduce objects in the Java language.

#### Learning Objective 1: Describe the process of abstraction in using objects, hiding implementation details, and re-using objects.

##### Readings
**Required:** Pages 23 to 38 of TIJ

##### Exercises
**Questions**
1.  What are the five characteristics of an object-oriented approach to programming? (See TIJ pages 25 to 26.)
2.  What are two reasons for controlling access to members of objects and how does Java implement control? (See TIJ page 31.)
3.  What are two ways of re-using classes? (See TIJ pages 32 to 33.)

#### Learning Objective 2: Explain the concept and use of polymorphism.

##### Readings
**Required:** Pages 38 to 43 of TIJ

##### Exercises
**Questions**

1.  How does late binding enable upcasting and polymorphism? (See TIJ pages 38 to 43.)

#### Learning Objective 3: Outline object hierarchy, containers, generics, and object lifetime in Java.

##### Readings
**Required:** Pages 43 to 48 of TIJ

##### Exercises
**Questions**
1.  What is a container? What is an advantage of using a container? (See TIJ page 44.)
2.  What is 'parameterized types/generics'? Explain how it eliminates the need for downcasting. (See TIJ pages 45 to 46.)
3.  Where in memory does Java create objects? (See TIJ pages 47 to 48.)

#### Learning Objective 4: Explain how Java handles exceptions and concurrency.

##### Readings
**Required:** Pages 49 to 50 of TIJ

##### Exercises
**Questions**
1.  What is function of exception handling and how does Java reinforce consistent use of handling exceptions? (See TIJ page 49.)
2.  What are the functions of threads in single-processor and multi-processor environments? (See TIJ page 50.)

#### Learning Objective 5: Explain the relationships between Java and the development of the Internet.

##### Readings
**Required:** Pages 50 to 60 of TIJ

##### Exercises
**Questions**
1.  What is the primary idea of a client/server system? (See TIJ page 51.)
2.  How did Web serving lead to client-side programming? (See TIJ pages 52 to 53.)
3.  What is CGI programming and what is its major shortcoming? (See TIJ pages 53 to 54.)
4.  Why is client-side programming efficient for the Web? (See TIJ page 54.)
5.  What is a plugin? (See TIJ page 54.)
6.  What is a scripting language? (See TIJ page 55.)
7.  Compare scripting languages to Java for Web page needs. (See TIJ pages 56 to 57.)
8.  What are the issues of Intranet versus Internet programming? (See TIJ page 58.)
9.  What is the role of Java in server-side programming? (See TIJ pages 59 to 60.)

#### Learning Objective 6: Provide a summary of this section.

##### Readings
**Required:** Page 60 of TIJ

### Section 2: Classes and Objects
**Section Goal**: Describe and analyse the use of objects and classes in
a Java program, and create Java documentation.

#### Learning Objective 1: Describe the creation and use of objects and primitive types in programming with Java.

##### Readings
**Required:** Pages 61 to 69 of TIJ

##### Exercises
**Questions**
1.  What is the difference between an object and its handle? (See TIJ page 61 to 62.)
2.  What are the roles of registers, the stack, the heap, constant storage, and non-RAM storage in Java programming? (See TIJ pages 63 to 64.)
3.  What are the nine primitive types supported by Java? (See TIJ page 65.)
4.  What are two classes of high-precision numbers with no primitive analog? (See TIJ page 66.)
5.  How does scope differ for primitives and objects? (See TIJ pages 68 to 69.)

#### Learning Objective 2: Explain classes, fields, methods, arguments, and return values in Java.

##### Readings
**Required:** Pages 69 to 74 of TIJ

##### Exercises
**Questions**
1.  What are classes, fields and methods? (See TIJ pages 69 to 70.)
2.  What is the difference between default values for primitive types as members of a class and local variables? (See TIJ page 71.)
3.  What are the fundamental parts of a Java method? (See TIJ page 72.)

#### Learning Objective 3: Outline these aspects of building a program in Java: namespaces, using other components, and the use of the static keyword.

##### Readings
**Required:** Pages 74 to 78 of TIJ

##### Exercises
**Questions**
1.  What is the naming convention when creating Java libraries for public distribution? (See TIJ pages 74 to 75.)
2.  What is the purpose of the import keyword? (See TIJ page 75.)
3.  What are the functions of the static keyword? (See TIJ pages 76 to 78.)

#### Learning Objective 4: Write, compile and run a Java program.

##### Readings
**Required:** Pages 78 to 81 of TIJ

##### Exercises
**Questions**
1.  Explain how [HelloDate.java](http://scis.athabascau.ca/html/lo/repos/comp308/programs/c02/HelloDate.java) prints the date. (See TIJ page 78 to 79.)
2.  Explain the lines (See TIJ page 79.)

        Public static void main (string [] args)
            public static void main (String[]) {

3.  Why is **main** static? (see TIJ pages 79 to 80.)

##### Programs
Compile, run, and analyze [HelloDate.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/object/HelloDate.java).

#### Learning Objective 5: Describe comments, documentation facilities, and coding style for Java.

##### Readings
**Required:** Pages 81 to 89 of TIJ

##### Exercises
**Questions**
1.  In Java, what is the standard coding style for classes and methods? (See TIJ pages 88 to 89.)

#### Learning Objective 6: Integrate the material covered in this section in writing programs.

##### Readings
**Required:** Page 89 of TIJ

##### Exercises
Exercise 10 on page 90 of TIJ

##### Answers To Exercises
-   [Answer 10](http://scis.athabascau.ca/html/course/COMP308/Unit_2/Section_2/Ch3ex10.java)


## Quiz 1 (due Dec 16th, 2016)
Complete and return Electronic Quiz 1.

Quiz 1 is scored out of 100 and contributes to 3% of your final grade.

## Unit 3: Program Control

### Unit Purpose
Describe and use the elements of program control in
Java.

### Conferencing
Post any questions or comments to the CMC system (conferencing is optional, but is recommended.)

##### Programs
**Note**: The objectives **Programs** examples are intended to clarify
any problems you have understanding these programs in the text. You do
not have to compile and run every program if you are sure you understand
the function of the programs.

### Section 1: Java Operators
**Section Goal**: Describe Java operators.

#### Learning Objective 1: Use the assignment operator.

##### Readings
**Required:** Pages 93 to 98 of TIJ

##### Exercises
**Questions**

1.  What is the precedence among arithmetic operators? (See TIJ page 95.)
2.  What is the difference in assignment between primitives and objects? (See TIJ pages 95 to 97.)
3.  What is aliasing? (See TIJ pages 97 to 98.)

##### Programs
Compile, run, and analyze programs:

[Assignment.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/operators/Assignment.java)
[PassObject.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/operators/PassObject.java)

#### Learning Objective 2: Use the common Java operators.

##### Readings
**Required:** Pages 98 to 111 of TIJ

##### Exercises
**Questions**
1.  What are the mathematical operators? (See <span>TIJ</span> pages 98 to 101.)
2.  How do auto pre-increment, pre-decrement, post-increment, and post-decrement work? (See <span>TIJ</span> pages 101 to 103.)
3.  What are the relational operators? (See <span>TIJ</span> page 103.)
4.  How does one test for object equivalence? (See <span>TIJ</span> pages 103 to 105.)
5.  What are the logical operators? (See <span>TIJ</span> pages 105 to 106.)
6.  What is short-circuiting? (See <span>TIJ</span> pages 106 to 108.)
7.  How are literals used to specify type in Java? (See <span>TIJ</span> pages 108 to 109.)

##### Programs
Compile, run, and analyze programs:

[MathOps.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/operators/MathOps.java)
[AutoInc.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/operators/AutoInc.java)
[Equivalence.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/operators/Equivalence.java)
[EqualsMethod.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/operators/EqualsMethod.java)
[EqualsMethod2.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/operators/EqualsMethod2.java)
[Bool.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/operators/Bool.java)
[ShortCircuit.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/operators/ShortCircuit.java)

#### Learning Objective 3: Describe the Java bitwise operators.

##### Readings
**Required:** Pages 111 to 116 of TIJ

##### Exercises
**Questions**
1.  What are the bitwise operators? (See TIJ pages 111 to 112.)
2.  What is the shift operator? (See TIJ pages 112 to 113.)

##### Programs
Compile, run, and analyze programs:

[URShift.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/operators/URShift.java)
[BitManipulation.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/operators/BitManipulation.java)

#### Learning Objective 4: Describe other operators used in Java.

##### Readings
**Required:** Pages 116 to 119 of TIJ

##### Exercises
**Questions**
1.  How does the ternary **if-else** operator work? (See TIJ pages 116 to 118.)
2.  What is the function of the **string** + operator? (See TIJ pages 118 to 119.)

##### Programs
Compile, run, and analyze programs:

[TerneryIfElse.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/operators/TernaryIfElse.java)
[StringOperators.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/operators/StringOperators.java)

#### Learning Objective 5: Use Java operators in various situations.

##### Readings
**Required:** Pages 118 to 133 of TIJ

##### Exercises
**Questions**
1.  How does explicit casting work in Java? (See TIJ pages 120 to 121.)

##### Programs
Compile, run, and analyse programs:

[CastingNumbers.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/operators/CastingNumbers.java)
[Literals.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/operators/Literals.java)
[AllOps.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/operators/AllOps.java)
[Overflow.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/operators/Overflow.java)

#### Learning Objective 6: Apply the material covered in this section to the writing of your Java programs.

##### Readings
**Required:** Pages 133 of TIJ

##### Exercises
Exercises 5 and 6 on page 105 of TIJ.

##### Answers To Exercises
-   [Answers 5 and 6](http://scis.athabascau.ca/html/course/COMP308/Unit_3/Section_1/Ch4ex5ex6.java)

### Section 2: Execution Control
**Section Goal:**  Describe execution control in Java programming.

#### Learning Objective 1: Describe execution control using the **if-else** commands.

##### Readings
**Required:** Pages 135 to 137 of TIJ

##### Exercises
**Questions**
1.  What are the two basic forms of **if**? (See TIJ pages 135 to 136.)

##### Programs
Compile, run, and analyze programs:

[IfElse.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/control/IfElse.java)
[IfElse2.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/control/IfElse2.java)

#### Learning Objective 2: Describe execution control using iteration constructs.

##### Readings
**Required:** Pages 137 to 151 of TIJ

##### Exercises
**Questions**
1.  How does **while** differ from **do-while**? (See TIJ pages 137 to 138.)
2.  What is unique to the **for** statement in regard to defining variables? (See TIJ pages 138 to 139.)
3.  What is the function of the comma operator? (See TIJ page 140.)
4.  What is the equivalence of a **for** loop in *foreach syntax*? (See TIJ page 141).
5.  What are the purposes of the **return** keyword? (See TIJ page 143).
6.  How are **break** and **continue** used in Java? (See TIJ pages 144 to 146.)

##### Programs
Compile, run, and analyze programs:

[WhileTest.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/control/WhileTest.java)
[ListCharacters.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/control/ListCharacters.java)
[CommaOperator.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/control/CommaOperator.java)
[BreakAndContinue.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/control/BreakAndContinue.java)
[LabeledFor.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/control/LabeledFor.java)
[LabeledWhile.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/control/LabeledWhile.java)

#### Learning Objective 3: Describe execution control using the **switch** statement.

##### Readings
**Required:** Pages 151 to 154 of TIJ

##### Exercises
**Questions**
1.  How is **break** used within **switch**? (See TIJ page 151 to 152.)

##### Programs
Compile, run, and analyze programs:

[VowelsAndConsonants.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/control/VowelsAndConsonants.java)

#### Learning Objective 4: Apply the material covered in this section to the writing of your Java programs.

##### Readings
**Required:** Page 154 of TIJ

##### Exercises
Exercise 1 on page 139, exercise 7 on page 146 and exercise 8 on page
153 of TIJ

##### Answers To Exercises
-   [Answer 1](http://scis.athabascau.ca/html/course/COMP308/Unit_3/Section_2/Ch5ex1.java)
-   [Answer 7](http://scis.athabascau.ca/html/course/COMP308/Unit_3/Section_2/Ch5ex7.java)
-   [Answer 8a](http://scis.athabascau.ca/html/course/COMP308/Unit_3/Section_2/Ch5ex8a.java)
-   [Answer 8b](http://scis.athabascau.ca/html/course/COMP308/Unit_3/Section_2/Ch5ex8b.java)

### Section 3: Initialization and Clean-up
**Section Goal:** Describe *initialization* and *clean up * in Java
programming.

#### Learning Objective 1: Describe the creation of objects with constructors and overloading.

##### Readings
**Required:** Pages 155 to 172 of TIJ

2. **Note: Cascade**

The Leaf.java program uses a form called cascade in the line

x.increment)..increment)..increment)..print).;

With cascade syntax, the output of each method is passed to the next
method in the cascade.

##### Exercises
**Questions**
1.  What is the purpose of a constructor? (See TIJ page 155.)
2.  How are overloaded methods distinguished from each other? (See TIJ pages 160 to 161.)
3.  What is a default constructor? (See TIJ pages 166 to 167.)
4.  How is the keyword **this** used in Java? (See TIJ pages 167 to 168.)

##### Programs
Compile, run, and analyze programs:

[SimpleConstructor.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/initialization/SimpleConstructor.java)
[SimpleConstructor2.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/initialization/SimpleConstructor2.java)
[Overloading.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/initialization/Overloading.java)
[OverloadingOrder.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/initialization/OverloadingOrder.java)
[PrimitiveOverloading.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/initialization/PrimitiveOverloading.java)
[Demotion.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/initialization/Demotion.java)
[DefaultConstructor.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/initialization/DefaultConstructor.java)
[NoSynthesis.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/initialization/NoSynthesis.java)
[Leaf.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/initialization/Leaf.java)
[Flower.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/initialization/Flower.java)

#### Learning Objective 2: Describe finalization, garbage collection, and cleaning up in Java.

##### Readings
**Required:** Pages 173 to 181 of TIJ

##### Exercises
**Questions**
1.  What is the purpose of **finalize**? (See TIJ pages 173 to 174.)
2.  Why is **finalize** not good as a destructor? (See TIJ pages 173 to 175.)
3.  Why must one perform clean up? (See TIJ page 175.)

##### Programs
Compile, run, and analyze programs:

[TerminationCondition.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/initialization/TerminationCondition.java)

#### Learning Objective 3: Outline and use the process of member initialization.

##### Readings
**Required:** Pages 181 to 193 of TIJ

##### Exercises
**Questions**
1.  What are the initial values of primitives that are encapsulated in an object, and what are the initial values of primitives that are not encapsulated in an object? (See TIJ pages 181 to 183.)
2.  What is the advantage of constructor initialization? (See TIJ page 185.)
3.  When are variables in an object initialized? (See TIJ pages 185 to 186.)
4.  What are the steps in the process of creating an object? (See TIJ page 189.)
5.  What is explicit **static** initialization? (See TIJ pages 190 to 191.)
6.  What is non-**static** instance initialization? (See TIJ pages 191 to 193.)

##### Programs
Compile, run, and analyze programs:

[InitialValues.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/initialization/InitialValues.java)
[InitialValues2.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/initialization/InitialValues2.java)
[OrderOfInitialization.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/initialization/OrderOfInitialization.java)
[StaticInitialization.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/initialization/StaticInitialization.java)
[ExplicitStatic.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/initialization/ExplicitStatic.java)
[Mugs.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/initialization/Mugs.java)

#### Learning Objective 4: Explain how to initialize arrays.

##### Readings
**Required:** Pages 193 to 204 of TIJ

##### Exercises
**Questions:**
1.  What is the advantage of bounds checking? (See TIJ pages 194 to 195.)
2.  What is an array of handles? (See TIJ pages 196 to 197.)

##### Programs
Compile, run and analyse programs

[ArrayOfPrimitives.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/initialization/ArraysOfPrimitives.java)
[ArrayNew.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/initialization/ArrayNew.java)
[ArrayClassObj.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/initialization/ArrayClassObj.java)
[ArrayInit.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/initialization/ArrayInit.java)
[DynamicArray.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/initialization/DynamicArray.java)
[VarArgs.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/initialization/VarArgs.java)
[NewVarArgs.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/initialization/NewVarArgs.java)
[OverloadingVarargs.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/initialization/OverloadingVarargs.java)

#### Learning Objective 5: Explain how to use enumerated types.

##### Readings
**Required:** Pages 204 to 207 of TIJ

##### Exercises
**Questions**
1.  What are the features or methods created automatically when you create an **enum**? (See TIJ page 205.)

##### Programs
Compile, run, and analyze programs:

[EnumOrder.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/initialization/EnumOrder.java)
[Burrito.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/initialization/Burrito.java)

#### Learning Objective 6: Apply material covered in this section to the writing of your Java programs.

##### Readings
**Required:** Pages 207 to 208 of TIJ

##### Exercises
Exercises 3 and 4 on page 167, exercises 10 and 11 on page 177, exercise
19 on page 204 of TIJ

##### Answers To Exercises
-   [Answers 3 and 4](http://scis.athabascau.ca/html/course/COMP308/Unit_3/Section_3/Ch6ex3ex4.java)
-   [Answers 10 and 11](http://scis.athabascau.ca/html/course/COMP308/Unit_3/Section_3/Ch6ex10ex11.java)
-   [Answer 19](http://scis.athabascau.ca/html/course/COMP308/Unit_3/Section_3/Ch6ex19.java)

## Unit 4: Object Oriented Programming and Re-usability

### Unit Purpose
Describe and use the core object-oriented features of
Java.

### Conferencing
Post any questions or comments to the CMC system (conferencing is optional, but is recommended)

### Section 1: Access Control
**Section Goal**: Use the capabilities for organizing, protecting, and
encapsulating classes in Java.

#### Learning Objective 1: Describe and use packages.

##### Readings
**Required:** Pages 209 to 217 of TIJ

##### Exercises
**Questions**
1.  What are the four levels of access specification in Java? (See TIJ page 210.)
2.  What is a compilation unit in Java? (See TIJ page 211.)
3.  What is the meaning of a **package** statement? (See TIJ page 212.)
4.  What is the naming convention for packages? (See TIJ pages 214 to 215.)
5.  How does CLASSPATH work with packages? (See TIJ pages 214 to 215.)
6.  How does CLASSPATH work with JAR files? (See TIJ page 215.)
7.  What is the pitfall of Java's collision detection? (See TIJ page 217.)
8.  How does Java handle collisions between classes in packages? (See TIJ page 217.)

##### Programs
Compile, run, and analyze programs:

[FullQualification.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/access/FullQualification.java)
[LibTest.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/access/LibTest.java)
[QualifiedMyClass.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/access/QualifiedMyClass.java)

#### Learning Objective 2: Explain more advanced issues in using packages.

##### Readings
**Required:** Pages 217 to 221 in TIJ

##### Exercises
**Questions**
1.  How can packages be used to mimic conditional compilation? (See TIJ page 220.)
2.  What is the package caveat? (See TIJ page 220.)

##### Programs
Compile, run, and analyze programs:

[PrintTest.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/access/PrintTest.java)

#### Learning Objective 3: Describe in detail, and use, the access levels.

##### Readings
**Required:** Pages 221 to 228 in TIJ

##### Exercises
**Questions**
1.  What is **package** access? (See TIJ pages 221 to 222.)
2.  What is **public** access? (See TIJ pages 222 to 224.)
3.  What is **private** access? (See TIJ pages 224 to 225.)
4.  What is **protected** access? (See TIJ page 225 to 227.)

##### Programs
Compile, run, and analyze programs:

[Cookie.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/access/cookie2/Cookie.java)
[Dinner.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/access/Dinner.java)
[Cake.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/access/Cake.java)
[Pie.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/access/Pie.java)
[IceCream.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/access/IceCream.java)
[ChocolateChip.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/access/ChocolateChip.java)
[ChocolateChip2.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/access/ChocolateChip2.java)

#### Learning Objective 4: Discuss issues of access in implementation when using Java's protection levels.

##### Readings
**Required:** Pages 228 to 233 in TIJ

##### Exercises
**Questions**
1.  What is the convention for ordering variables by access level? (See TIJ pages 228 to 229.)
2.  What are the constraints on using the **public** access level? (See TIJ pages 229 to 230.)

##### Programs
Compile, run, and analyze programs:

[Lunch.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/access/Lunch.java)

#### Learning Objective 5: Integrate and summarize the material on Java as the object-oriented programming language of the Internet.

##### Readings
**Required:** Pages 233 to 235 of TIJ

##### Exercises
Exercises 5 and 6 on pages 227 to 228, exercise 9 on page 233 of TIJ
(open question)

**Question**
1.  What are the two main reasons for access control? (See TIJ page 234.)

##### Answers To Exercises
-   [Answers 5 and 6](http://scis.athabascau.ca/html/course/COMP308/Unit_4/Section_1/Ch7ex5ex6.java)

### Section 2: Composition and Inheritance
**Section Goal:**  Use composition and inheritance to design re-usable
classes.

#### Learning Objective 1 Describe and use composition.

##### Readings
**Required:** Pages 237 to 241 of TIJ

##### Exercises
**Questions**
1.  What is composition? (See TIJ page 237.)
2.  Where can handles be initialized? (See TIJ pages 239 to 241.)

##### Programs
Compile, run, and analyze programs:

[SprinklerSystem.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/reusing/SprinklerSystem.java)
[Bath.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/reusing/Bath.java)

#### Learning Objective 2 Describe and use inheritance.

##### Readings
**Required:** Pages 241 to 246 of TIJ

##### Exercises
**Questions**
1.  What does the keyword **extends** accomplish? (See TIJ pages 241 to 243.)
2.  How does the base class get initialized in the case of default constructors? (See TIJ page 244 to 246.)
3.  How does the base class get initialized in the case of constructors with arguments? (See TIJ pages 245 to 246.)

##### Programs
Compile, run, and analyze programs:

[Detergent.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/reusing/Detergent.java)
[Cartoon.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/reusing/Cartoon.java)
[Chess.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/reusing/Chess.java)

#### Learning Objective 3: Explain and use *delegation*.

##### Readings
**Required:** Pages 246 to 248 of TIJ

##### Exercises
**Questions**

1.  What is delegation in relation to composition and inheritance? (See TIJ pages 246 to 248.)

##### Programs
Compile, run, and analyze programs:

[SpaceShip.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/reusing/SpaceShip.java)
[SpaceShipDelegation.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/reusing/SpaceShipDelegation.java)

#### Learning Objective 4: Demonstrate, contrast, and compare inheritance and composition.

##### Readings
**Required:** Pages 249 to 262 of TIJ

##### Exercises
**Questions**

1.  Why would a programmer write a clean up method? (See TIJ page 251.)
2.  How does a method in a derived class affect a method in a base class with the same name but a different signature? (See TIJ pages 255 to 256.)
3.  When is composition used compared to when inheritance is used? (See TIJ pages 256 to 258.)
4.  How does **protected** work with inheritance? (See TIJ pages 258 to 259.)
5.  What is the advantage of upcasting? (See TIJ pages 260 to 261.)
6.  What is a good rule for deciding between inheritance and composition? (See TIJ page 261 to 262.)

##### Programs
Compile, run, and analyze programs:

[PlaceSetting.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/reusing/PlaceSetting.java)
[CADSystem.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/reusing/CADSystem.java)
[Hide.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/reusing/Hide.java)
[Car.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/reusing/Car.java)
[Orc.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/reusing/Orc.java)
[Wind.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/reusing/Wind.java)

#### Learning Objective 5: Explain and use **final** in various contexts.

##### Readings
**Required:** Pages 262 to 272 of TIJ

##### Exercises
**Questions**
1.  What are two ways of setting a **final** primitive value? (See page 262 of TIJ.)
2.  What is the difference between **static final** versus **final**? (See pages 262 to 263 of TIJ.)
3.  What is the effect of **final** on objects? (See page 263 to 265 of TIJ.)
4.  What is the advantage of using a blank **final**? (See page 265 to 266 of TIJ.)
5.  How does a **final** argument function? (See pages 266 to 268 of TIJ.)
6.  Why should one be cautious in using **final** method? (See page 270 of TIJ.)

##### Programs
Compile, run, and analyze programs:

[FinalData.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/reusing/FinalData.java)
[BlankFinal.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/reusing/BlankFinal.java)
[FinalArguments.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/reusing/FinalArguments.java)
[FinalOverridingIllusion.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/reusing/FinalOverridingIllusion.java)
[Jurassic.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/reusing/Jurassic.java)

#### Learning Objective 6: Explain the process of initialization and class loading.

##### Readings
**Required:** Pages 272 to 274 of TIJ

##### Exercises
**Questions**
1.  What is the ordering of events in initialization and class loading? (See pages 272 to 274 of TIJ.)

##### Programs
Compile, run, and analyze programs:

[Beetle.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/reusing/Beetle.java)

#### Learning Objective 7: Integrate and summarize the material in this section.

##### Readings
**Required:** Pages 274 to 275 of TIJ

##### Exercises
Exercise 5 on page 245, exercise 7 on page 246, exercises 16 and 17 on
page 262 of TIJ

##### Answers To Exercises
-   [Answer 5](http://scis.athabascau.ca/html/course/COMP308/Unit_4/Section_2/Ch8ex5.java)
-   [Answer 7](http://scis.athabascau.ca/html/course/COMP308/Unit_4/Section_2/Ch8ex7.java)
-   [Answer 16](http://scis.athabascau.ca/html/course/COMP308/Unit_4/Section_2/Ch8ex16.java)
-   [Answer 17](http://scis.athabascau.ca/html/course/COMP308/Unit_4/Section_2/Ch8ex17.java)

### Section 3: Polymorphism
**Section Goal**: Use polymorphism in advanced Java programming.

#### Learning Objective 1: Describe the role of upcasting in polymorphism.

##### Readings
**Required:** Pages 277 to 289 of TIJ

##### Exercises
**Questions**
1.  What is the advantage of upcasting? (See TIJ pages 278 to 281.)
2.  What is the role of *late binding* in polymorphism? (See TIJ pages 281 to 282.)
3.  How is extensibility supported by polymorphism? (See TIJ pages 286 to 289.)

##### Programs
Compile, run, and analyze programs:

[Wind.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/polymorphism/music/Wind.java)
[Music.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/polymorphism/music/Music.java)
[Music2.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/polymorphism/music/Music2.java)
[Shape.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/polymorphism/shape/Shape.java)
[Circle.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/polymorphism/shape/Circle.java)
[Square.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/polymorphism/shape/Square.java)
[Triangle.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/polymorphism/shape/Triangle.java)
[RandomShapeGenerator.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/polymorphism/shape/RandomShapeGenerator.java)
[Music3.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/polymorphism/music3/Music3.java)
[StaticPolymorphism.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/polymorphism/StaticPolymorphism.java)

#### Learning Objective 2: Describe the use of constructors in the context of polymorphism.

##### Readings
**Required:** Pages 293 to 303 of TIJ

##### Exercises
**Questions**
1.  What is the order of constructor calls for base and derived classes? (See TIJ pages 293 to 295.)
2.  What is the order of **finalize** for base and derived classes? (See TIJ pages 295 to 299.)
3.  What is a good rule for using polymorphic methods within a constructor? (See TIJ pages 301 to 303.)

##### Programs
Compile, run, and analyze programs:

[Sandwich.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/polymorphism/Sandwich.java)
[Frog.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/polymorphism/Frog.java)
[ReferenceCounting.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/polymorphism/ReferenceCounting.java)
[PolyConstructors.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/polymorphism/PolyConstructors.java)

#### Learning Objective 3: Explain and use covariant return types.

##### Readings
**Required:** Pages 303 to 304 of TIJ

##### Exercises
**Questions**
1.  What is a *covariant return type*? (See TIJ pages 303 to 304.)

##### Programs
Compile, run, and analyze programs:

[CovariantReturn.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/polymorphism/CovariantReturn.java)

#### Learning Objective 4: Design re-usable programs.

##### Readings
**Required:** Pages 304 to 310 of TIJ

##### Exercises
**Questions**
1.  What advantage does composition have over inheritance? (See TIJ pages 304 to 306.)
2.  How can upcasting be ineffective with extension? (See TIJ pages 306 to 308.)
3.  How is upcasting safe and downcasting not safe with extension? (See TIJ page 308.)
4.  What is RTTI and how does it work with downcasting? (See TIJ pages 308 to 310.)

##### Programs
Compile, run, and analyze programs:

[Transmogrify.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/polymorphism/Transmogrify.java)
[RTTI.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/polymorphism/RTTI.java)

#### Learning Objective 5: Integrate and summarize the material on polymorphism in Java.

##### Readings
**Required:** Pages 310 of TIJ

##### Exercises
Exercise 9 on page 289 of TIJ and exercise 12 on pages 298 to 299 of
TIJ.

##### Answers To Exercises
-   [Answer 9](http://scis.athabascau.ca/html/course/COMP308/Unit_4/Section_3/Ch9ex9.java)
-   [Answer 12](http://scis.athabascau.ca/html/course/COMP308/Unit_4/Section_3/Ch9ex12.java)

### Section 4: Interfaces and Inner Classes
**Section Goal**: Discuss and use interfaces and inner classes in
advanced Java programming.

#### Learning Objective 1: Explain the use of abstract classes in Java.

##### Readings
**Required:** Pages 311 to 315 of TIJ

##### Exercises
**Questions**
1.  What are abstract classes and abstract methods? (See TIJ pages 311 to 312.)

##### Programs
Compile, run, and analyze programs:

[Music4.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/interfaces/music4/Music4.java)

#### Learning Objective 2: Explain the use of interfaces in Java.

##### Readings
**Required:** Pages 316 to 334 of TIJ

##### Exercises
**Questions**
1.  What is the format of a Java interface? (See TIJ pages 316 to 317.)
2.  Describe an example of how an interface can be applied to multiple different implementations. (See TIJ pages 320 to 326.)
3.  How is multiple inheritance dealt with by interfaces? (See TIJ pages 326 to 327.)
4.  How does **extend** differ for interfaces? (See TIJ pages 329 to 330.)
5.  Can a class implement multiple interfaces? (See TIJ pages 330 to 331.)
6.  What is one common use of interface? (See TIJ page 332.)

##### Programs
Compile, run, and analyze programs:

[Music5.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/interfaces/music5/Music5.java)
[Apply.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/interfaces/classprocessor/Apply.java)
[LowPass.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/interfaces/filters/LowPass.java)
[HighPass.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/interfaces/filters/HighPass.java)
[BandPass.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/interfaces/filters/BandPass.java)
[FilterProcessor.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/interfaces/interfaceprocessor/FilterProcessor.java)
[HorrorShow.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/interfaces/HorrorShow.java)
[RandomWords.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/interfaces/RandomWords.java)
[RandomDoubles.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/interfaces/RandomDoubles.java)

#### Learning Objective 3: Discuss other features of Java interface.

##### Readings
**Required:** Pages 335 to 343 of TIJ

##### Exercises
**Questions**
1.  Can an interface be nested within another interface? (See TIJ page 339.)
2.  What is a *Factory Method* design pattern and how does it relate to interface? (See TIJ page 339).
3.  What is the appropriate guideline for choosing between classes and interfaces? (See TIJ page 343).

##### Programs
Compile, run, and analyze programs:

[RandVals.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/interfaces/RandVals.java)
[NestingInterfaces.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/interfaces/nesting/NestingInterfaces.java)
[Factories.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/interfaces/Factories.java)
[Games.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/interfaces/Games.java)

#### Learning Objective 4: Describe the use of inner classes.

##### Readings
**Required:** Pages 345 to 368 of TIJ

##### Exercises
**Questions**
1.  What is an inner class? (See TIJ page 345 to 346.)
2.  What access do inner classes have to the containing class variables and methods? (See TIJ pages 347 to 349.)
3.  What are the meanings of **.this** and **.new&lt;/&gt; in the context of an inner class? (See TIJ pages 350 to 351.)**
4.  **What is the advantage of upcasting to an interface with inner classes? (See TIJ pages 352 to 353.)**
5.  **What is the advantage of defining a class within a method or a scope? (See TIJ pages 354 to 355.)**
6.  **What is an anonymous class? (See TIJ page 357.)**
7.  **How do you initialize fields within an anonymous class? (See TIJ pages 358 to 360.)**
8.  **What is instance initialization? (See TIJ page 361.)**
9.  **What are characteristics of static inner classes? (See TIJ pages 364 to 365.)**
10. How can you use **static** inner classes for testing? (See TIJ pages 366 to 367.)

##### Programs
Compile, run, and analyze programs:

[Parcel1.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/innerclasses/Parcel1.java)
[Parcel2.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/innerclasses/Parcel2.java)
[Sequence.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/innerclasses/Sequence.java)
[TestParcel.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/innerclasses/TestParcel.java)
[Parcel5.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/innerclasses/Parcel5.java)
[Parcel6.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/innerclasses/Parcel6.java)
[Parcel7.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/innerclasses/Parcel7.java)
[Parcel8.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/innerclasses/Parcel8.java)
[Parcel9.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/innerclasses/Parcel9.java)
[AnonymousConstructor.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/innerclasses/AnonymousConstructor.java)
[Parcel10.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/innerclasses/Parcel10.java)
[Parcel11.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/innerclasses/Parcel11.java)
[ClassInInterface.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/innerclasses/ClassInInterface.java)
[MultiNestingAccess.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/innerclasses/MultiNestingAccess.java)

#### Learning Objective 5: Discuss the design issues of inner classes.

##### Readings
**Required:** Pages 369 to 383 of TIJ

##### Exercises
**Questions**
1.  What is the one compelling reason for using an inner class? (See TIJ page 369.)
2.  What is an *application framework*? (See TIJ page 375.)
3.  What is a *control framework*? (See TIJ page 375.)
4.  What are two advantages of inner classes for control frameworks? (See TIJ page 377.)
5.  How do inner classes create a situation that looks like multiple inheritance? (See TIJ pages 378 to 382.)

##### Programs
Compile, run, and analyze programs:

[MultiInterfaces.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/innerclasses/MultiInterfaces.java)
[MultiImplementation.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/innerclasses/MultiImplementation.java)
[Callbacks.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/innerclasses/Callbacks.java)
[Controller.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/innerclasses/controller/Controller.java)
[GreenhouseControls.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/innerclasses/GreenhouseControls.java)
[InheritInner.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/innerclasses/InheritInner.java)

#### Learning Objective 6: Discuss other issues of inner classes.

##### Readings
**Required:** Pages 369 to 383 of TIJ.

##### Exercises
**Questions**
1.  What is a local inner class and what are its features? (See TIJ 385.)
2.  How are inner classes identified? (See TIJ page 387.)

##### Programs
Compile, run, and analyze programs:

[BigEgg.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/innerclasses/BigEgg.java)
[BigEgg2.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/innerclasses/BigEgg2.java)
[LocalInnerClass.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/innerclasses/LocalInnerClass.java)

#### Learning Objective 7: Integrate and summarize the material on interface and inner class in Java.

##### Readings
**Required:** Pages 349 and 388 of TIJ

##### Exercises
Exercise 1 on page 315, exercise 18 on page 342, and exercise 24 on page
382 of TIJ

##### Answers To Exercises
-   [Answer 1](http://scis.athabascau.ca/html/course/COMP308/Unit_4/Section_4/Ch10ex1.java)
-   [Answer 18](http://scis.athabascau.ca/html/course/COMP308/Unit_4/Section_4/Ch10ex18.java)
-   [Answer 24](http://scis.athabascau.ca/html/course/COMP308/Unit_4/Section_4/Ch11ex24.java)

## Tutor Marked Exercise 1 (due Dec 23rd, 2017)
Please complete TME 1 and submit it by electronic mail.

Tutor Marked Exercise 1 is scored out of 100 and contributes to 5% of
your final grade.

## Unit 5: Collections, Arrays, Exceptions and Strings

### Unit Purpose
Describe and use Java containers, arrays, exceptions,
and Strings.

### Conferencing
Post any questions or comments to the CMC system (conferencing is optional, but is recommended)

### Section 1: Collections in Java
**Section Goal**: Explain and use collections in Java.

#### Learning Objective 1
-   Explain what Java containers are.

##### Readings
**Required:** Pages 389 to 401 of TIJ

##### Exercises
**Questions**
1.  What is a type-safe container? (See TIJ page 390 to 393.)
2.  What are the two main concepts underlying the Java 2 collections library? (See TIJ page 394.)

##### Programs
Compile, run, and analyze programs:

[ApplesAndOrangesWithoutGenerics.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/holding/ApplesAndOrangesWithoutGenerics.java)
[ApplesAndOrangesWithGenerics.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/holding/ApplesAndOrangesWithGenerics.java)
[GenericsAndUpcasting.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/holding/GenericsAndUpcasting.java)
[SimpleCollection.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/holding/SimpleCollection.java)
[AddingGroups.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/holding/AddingGroups.java)
[AsListInference.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/holding/AsListInference.java)
[PrintingContainers.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/holding/PrintingContainers.java)

#### Learning Objective 2
-   Explain the use of **List** and **Stack** in Java.

##### Readings
**Required:** Pages 401 to 414 of TIJ

##### Exercises
**Questions**
1.  What are the two types of **List** and what is the difference between them? (See TIJ page 401.)
2.  What is the purpose of an **Iterator**? (See TIJ page 406.)
3.  What are the advantages of a **ListIterator** over an **Iterator**? (See TIJ page 409.)
4.  What are the advantages and disadvantages of **ArrayList** and **LinkedList**? (See TIJ pages 410 to 411.)
5.  What is a **stack**? (See TIJ page 412.)

##### Programs
Compile, run, and analyze programs:

[ListFeatures.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/holding/ListFeatures.java)
[SimpleIteration.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/holding/SimpleIteration.java)
[CrossContainerIteration.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/holding/CrossContainerIteration.java)
[ListIteration.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/holding/ListIteration.java)
[LinkedListFeatures.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/holding/LinkedListFeatures.java)
[StackTest.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/holding/StackTest.java)

#### Learning Objective 3
-   Describe and use **Set**, **Map**, and **Queue** in Java.

##### Readings
**Required:** Pages 415 to 427 of TIJ

##### Exercises
**Questions**
1.  What is the distinctive feature of a **Set**? (See TIJ page 415.)
2.  What are the differences **TreeSet** and **HashSet**? (See TIJ page 416.)
3.  What is the distinctive feature of a **Map**? (See TIJ pages 419 to 420.)
4.  What is a **Queue** and what is a **PriorityQueue**? (See TIJ pages 423 to 425.)

##### Programs
Compile, run, and analyze programs:

[SetOfInteger.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/holding/SetOfInteger.java)
[SortedSetOfInteger.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/holding/SortedSetOfInteger.java)
[SetOperations.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/holding/SetOperations.java)
[UniqueWords.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/holding/UniqueWords.java)
[UniqueWordsAlphabetic.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/holding/UniqueWordsAlphabetic.java)
[Statistics.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/holding/Statistics.java)
[PetMap.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/holding/PetMap.java)
[MapOfList.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/holding/MapOfList.java)
[QueueDemo.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/holding/QueueDemo.java)
[PriorityQueueDemo.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/holding/PriorityQueueDemo.java)

#### Learning Objective 4
-   Discuss the issues of using **Collection** and **Iterator**.

##### Readings
**Required:** Pages 427 to 437 of TIJ

##### Exercises
**Questions**
1.  What is the argument for having an interface over a **Collection**? (See TIJ page 427.)
2.  How does the foreach syntax work with **Iterable**? (See TIJ pages 431 to 433.)

##### Programs
Compile, run, and analyze programs:

[InterfaceVsIterator.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/holding/InterfaceVsIterator.java)
[CollectionSequence.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/holding/CollectionSequence.java)
[NonCollectionSequence.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/holding/NonCollectionSequence.java)
[ForEachCollections.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/holding/ForEachCollections.java)
[IterableClass.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/holding/IterableClass.java)
[ArrayIsNotIterable.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/holding/ArrayIsNotIterable.java)
[AdapterMethodIdiom.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/holding/AdapterMethodIdiom.java)
[MultiIterableClass.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/holding/MultiIterableClass.java)
[ModifyingArraysAsList.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/holding/ModifyingArraysAsList.java)

#### Learning Objective 5
-   Integrate and summarize the material on exceptions in Java.

##### Readings
**Required:** Pages 437 to 441 of TIJ

##### Exercises
Exercise 1 on page 394, exercise 8 on page 409, and exercise 17 on page
422 of TIJ.

**Questions**
1.  Summarize the ways Java provides to hold objects. (See TIJ page 438.)

##### Answers To Exercises
-   [Answer 1](http://scis.athabascau.ca/html/course/COMP308/Unit_5/Section_1/Ch12ex1.java)
-   [Answer 8](http://scis.athabascau.ca/html/course/COMP308/Unit_5/Section_1/Ch12ex8.java)
-   [Answer 17](http://scis.athabascau.ca/html/course/COMP308/Unit_5/Section_1/Ch12ex17.java)

### Section 2: Arrays
**Section Goal:**  Describe and use arrays in Java.

#### Learning Objective 1
-   Use arrays and explain their status as first class objects in Java.

##### Readings
**Required:** Pages 747 to 762 of TIJ

##### Exercises
**Questions**
1.  What are the features that distinguish an array from other types of containers in Java? (See TIJ page 747.)
2.  What are two ways of initializing arrays? (See TIJ page 749.)
3.  What is the use of the **Arrays.deepToString()** method? (See TIJ page 755.)
4.  How is a parameterized array created? (See TIJ pages 759 to 760.)

##### Programs
Compile, run, and analyze programs:

[ContainerComparison.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/arrays/ContainerComparison.java)
[ArrayOptions.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/arrays/ArrayOptions.java)
[IceCream.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/arrays/IceCream.java)
[MultidimensionalPrimitiveArray.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/arrays/MultidimensionalPrimitiveArray.java)
[RaggedArray.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/arrays/RaggedArray.java)
[MultidimensionalObjectArrays.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/arrays/MultidimensionalObjectArrays.java)
[AutoboxingArrays.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/arrays/AutoboxingArrays.java)
[AssemblingMultidimensionalArrays.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/arrays/AssemblingMultidimensionalArrays.java)

#### Learning Objective 2
-   Describe and use various **Arrays** methods to create data.

##### Readings
**Required:** Pages 762 to 775 of TIJ

##### Exercises
**Questions**
1.  What conversion tools are required when using a **Generator** to create an array? (See TIJ page 770.)

##### Programs
Compile, run, and analyze programs:

[FillingArrays.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/arrays/FillingArrays.java)
[GeneratorsTest.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/arrays/GeneratorsTest.java)
[RandomGeneratorsTest.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/arrays/RandomGeneratorsTest.java)
[TestGenerated.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/arrays/TestGenerated.java)
[PrimitiveConversionDemonstration.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/arrays/PrimitiveConversionDemonstration.java)
[TestArrayGeneration.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/arrays/TestArrayGeneration.java)

#### Learning Objective 3
-   Describe and use the **Arrays** class.

##### Readings
**Required:** Pages 775 to 786 of TIJ

##### Exercises
**Questions**
1.  What are the conditions when **Arrays.equals()** returns true? (See TIJ pages 777.)
2.  How do you implement **Comparable** in sorting an array? (See TIJ pages 778 to 782.)
3.  What is the condition of using Arrays.binarySearch()? (See TIJ page 784.)

##### Programs
Compile, run, and analyze programs:

[CopyingArrays.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/arrays/CopyingArrays.java)
[ComparingArrays.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/arrays/ComparingArrays.java)
[CompType.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/arrays/CompType.java)
[Reverse.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/arrays/Reverse.java)
[ComparatorTest.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/arrays/ComparatorTest.java)
[StringSorting.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/arrays/StringSorting.java)
[ArraySearching.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/arrays/ArraySearching.java)
[AlphabeticSearch.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/arrays/AlphabeticSearch.java)

#### Learning Objective 4
-   Integrate and summarize the material on arrays in Java.

##### Readings
**Required:** Pages 786 to 788 of TIJ

##### Exercises
Exercise 5 on page 759, exercise 19 on page 778, and exercise 24 on page
786 of TIJ

##### Answers To Exercises
-   [Answer 5](http://scis.athabascau.ca/html/course/COMP308/Unit_5/Section_2/Ch17ex5.java)
-   [Answer 19a](http://scis.athabascau.ca/html/course/COMP308/Unit_5/Section_2/Ch17ex19a.java)
-   [Answer 19b](http://scis.athabascau.ca/html/course/COMP308/Unit_5/Section_2/Ch17ex19b.java)
-   [Answer 24](http://scis.athabascau.ca/html/course/COMP308/Unit_5/Section_2/Ch17ex24.java)

### Section 3: Exceptions in Java
**Section Goal**: Explain how Java handles exceptions, and write
programs to demonstrate this facility.

#### Learning Objective 1
-   Describe Java's basic exception-handling capability.

##### Readings
**Required**: Pages 443 to 449 of TIJ

##### Exercises
**Questions**
1.  What are the benefits of using exceptions? (See TIJ page 444.)
2.  What happens when you **throw** an exception? (See TIJ page 447.)
3.  What is the advantage of a **try** block? (See TIJ pages 447 to 448.)
4.  What is the function of a **catch** block? (See TIJ pages 448 to 449.)
5.  What are the two basic models used in exception-handling theory? (See TIJ page 449.)

#### Learning Objective 2
-   Create your own Java exceptions.

##### Readings
**Required:** Pages 449 to 468 of TIJ

##### Exercises
**Questions**
1.  What is the simplest way to create your own exceptions? (See TIJ page 449 to 450.)
2.  How do you log the output of an exception? (See TIJ pages 452 to 454.)
3.  What is the idea of *exception chaining*? (See TIJ page 464.)

##### Programs
Compile, run, and analyze programs:

[InheritingExceptions.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/exceptions/InheritingExceptions.java)
[FullConstructors.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/exceptions/FullConstructors.java)
[LoggingExceptions.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/exceptions/LoggingExceptions.java)
[LoggingExceptions2.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/exceptions/LoggingExceptions2.java)
[ExtraFeatures.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/exceptions/ExtraFeatures.java)
[ExceptionMethods.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/exceptions/ExceptionMethods.java)
[WhoCalled.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/exceptions/WhoCalled.java)
[Rethrowing.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/exceptions/Rethrowing.java)
[RethrowNew.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/exceptions/RethrowNew.java)
[DynamicFields.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/exceptions/DynamicFields.java)

#### Learning Objective 3
-   Describe the standard Java exceptions.

##### Readings
**Required:** Pages 468 to 471 of TIJ

##### Exercises
**Questions**
1.  Where can you find descriptions of standard Java exceptions? (See TIJ page 468.)
2.  What happens to **Runtime** errors that are never caught? (See TIJ page 468 to 471.)

##### Programs
Compile, run, and analyze programs:

[NeverCaught.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/exceptions/NeverCaught.java)

#### Learning Objective 4
-   Perform cleanup with **finally**.

##### Readings
**Required:** Pages 471 to 479 of TIJ

##### Exercises
**Questions**
1.  What happens with the **finally** statement when no exception is thrown? (See TIJ pages 471 to 472.)
2.  For what is the **finally** statement used? (See TIJ page 473.)
3.  How does a lost exception occur? (See TIJ pages 477 to 479.)

##### Programs
Compile, run, and analyze programs:

[FinallyWorks.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/exceptions/FinallyWorks.java)
[Switch.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/exceptions/Switch.java)
[WithFinally.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/exceptions/WithFinally.java)
[AlwaysFinally.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/exceptions/AlwaysFinally.java)
[MultipleReturns.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/exceptions/MultipleReturns.java)
[LostMessage.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/exceptions/LostMessage.java)
[ExceptionSilencer.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/exceptions/ExceptionSilencer.java)

#### Learning Objective 5
-   Describe restrictions on exceptions in Java.

##### Readings
**Required:** Pages 479 to 483 of TIJ

##### Exercises
**Questions**
1.  Why is it that a method says it throws an exception but it does not? (See TIJ page 479 to 481.)

##### Programs
Compile, run, and analyze programs:

[StormyInning.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/exceptions/StormyInning.java)

#### Learning Objective 6
-   Use exceptions with constructors.

##### Readings
**Required**: Pages 483 to 500 of TIJ

##### Exercises
**Questions**
1.  What is the problem with using **finally** to handle exceptions in constructors? (See TIJ page 483 to 484.)
2.  How does exception-handling work with derived and base exception classes? (See TIJ pages 489 to 490.)

##### Programs
Compile, run, and analyze programs:

[InputFile.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/exceptions/InputFile.java)
[Cleanup.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/exceptions/Cleanup.java)
[CleanupIdiom.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/exceptions/CleanupIdiom.java)
[Human.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/exceptions/Human.java)
[MainException.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/exceptions/MainException.java)
[TurnOffChecking.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/exceptions/TurnOffChecking.java)

#### Learning Objective 7
-   Write programs that integrate and summarize the material on exceptions in Java.

##### Readings
**Required**: Pages 500 to 501 of TIJ

##### Exercises
Exercise 1 on page 452, exercise 10 on page 468 of TIJ.

**Questions**
1.  Summarize the guidelines of using exceptions. (See TIJ pages 500 to 501.)

##### Answers To Exercises
-   [Answer 1](http://scis.athabascau.ca/html/course/COMP308/Unit_5/Section_3/Ch13ex1.java)
-   [Answer 10](http://scis.athabascau.ca/html/course/COMP308/Unit_5/Section_3/Ch13ex10.java)

### Section 4: Strings in Java
**Section Goal**: Discuss the features of **Strings ** in Java.

#### Learning Objective 1
-   Describe basic characteristics of **String** objects.

##### Readings
**Required**: Pages 503 to 513 of TIJ

##### Exercises
**Questions**
1.  What is the advantage of making **Strings** immutable? (See TIJ pages 503 to 504.)
2.  In what situation will using an explicit **StringBuilder** improve efficiency? (See TIJ pages 508 to 509).

##### Programs
Compile, run, and analyze programs:

[Immutable.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/strings/Immutable.java)
[Concatenation.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/strings/Concatenation.java)
[WhitherStringBuilder.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/strings/WhitherStringBuilder.java)
[UsingStringBuilder.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/strings/UsingStringBuilder.java)
[ArrayListDisplay.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/strings/ArrayListDisplay.java)
[InfiniteRecursion.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/strings/InfiniteRecursion.java)

#### Learning Objective 2
-   Explain and use the formatting features in Java.

##### Readings
**Required**: Pages 514 to 523 of TIJ

##### Exercises
**Questions**
1.  What is the purpose of a **Formatter object**? (See TIJ page 515.)

##### Programs
Compile, run, and analyze programs:

[SimpleFormat.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/strings/SimpleFormat.java)
[Turtle.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/strings/Turtle.java)
[Receipt.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/strings/Receipt.java)
[Conversion.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/strings/Conversion.java)
[DatabaseException.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/strings/DatabaseException.java)

#### Learning Objective 3
-   Explain and use regular expressions **Pattern** and **Matcher**.

##### Readings
**Required**: Pages 523 to 546 of TIJ.

##### Exercises
**Questions**
1.  What is a regular expression? (See TIJ page 524.)
2.  How do you use **Pattern** and **Matcher** classes with regular expressions? (See TIJ page 531.)

##### Programs
Compile, run, and analyze programs:

[IntegerMatch.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/strings/IntegerMatch.java)
[Splitting.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/strings/Splitting.java)
[Replacing.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/strings/Replacing.java)
[Rudolph.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/strings/Rudolph.java)
[TestRegularExpression.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/strings/TestRegularExpression.java)
[Finding.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/strings/Finding.java)
[Groups.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/strings/Groups.java)
[StartEnd.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/strings/StartEnd.java)
[ReFlags.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/strings/ReFlags.java)
[SplitDemo.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/strings/SplitDemo.java)
[TheReplacements.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/strings/TheReplacements.java)
[Resetting.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/strings/Resetting.java)
[JGrep.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/strings/JGrep.java)

#### Learning Objective 4
-   Explain and use **Scanner** and **StringTokenizer**.

##### Readings
**Required**: Pages 546 to 552 of TIJ

##### Exercises
**Questions**
1.  What method of **Scanner** would you call to retrieve the next **StringTtoken**? (See TIJ page 549.)
2.  What is one advantage of **Scanner** over **StringTokenizer**? (See TIJ pages 551 to 552.)

##### Programs
Compile, run, and analyze programs:

[SimpleRead.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/strings/SimpleRead.java)
[BetterRead.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/strings/BetterRead.java)
[ScannerDelimiter.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/strings/ScannerDelimiter.java)
[ThreatAnalyzer.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/strings/ThreatAnalyzer.java)

#### Learning Objective 5
-   Write programs tjat integrate and summarize the material on **Strings** in Java.

##### Readings
**Required**: Page 552 of TIJ

##### Exercises
Exercise 6 on page 523, exercise 8 on page 527, and exercise 20 on page
549 of TIJ.

##### Answers To Exercises
-   [Answer 6](http://scis.athabascau.ca/html/course/COMP308/Unit_5/Section_4/Ch14ex6.java)
-   [Answer 8](http://scis.athabascau.ca/html/course/COMP308/Unit_5/Section_4/Ch14ex8.java)
-   [Answer 20](http://scis.athabascau.ca/html/course/COMP308/Unit_5/Section_4/Ch14ex20.java)

## Tutor Marked Exercise 2 (due Dec 30th, 2017)
Please complete TME 2 and submit it by electronic mail.

Tutor Marked Exercise 2 is scored out of 100 and contributes to 10 per
cent of your final grade.


## Unit 6: Types, Generics and Containers

### Unit Purpose
Discuss Types and Types related features in
Java.


### Conferencing
Post any questions or comments to the CMC system (conferencing is optional, but is recommended)

### Digital Reading Room
Unit 6 links:
-   [jguru: awt](http://library.athabascau.ca/drr/redirect.php?id=8111) [jguru: awt](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27630)
-   [AWT Short Course: Introduction](http://library.athabascau.ca/drr/redirect.php?id=8113) [AWT Short Course: Introduction](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27631)
-   [javabeans (tm) 2](http://library.athabascau.ca/drr/redirect.php?id=8114) [javabeans (tm) 2](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27632)
-   [Download AWT 1.0 Tutorial](http://library.athabascau.ca/drr/redirect.php?id=8115) [Download AWT 1.0 Tutorial](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27633)
-   [Swing: Part I, About This Short Course](http://library.athabascau.ca/drr/redirect.php?id=8116) [Swing: Part I, About This Short Course](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27634)
-   [The Swing Connection](http://library.athabascau.ca/drr/redirect.php?id=8118) [The Swing Connection](http://drr2.lib.athabascau.ca/index.php?c=node&m=detail&n=27635)

### Section 1: Types Information
**Section Goal**: Describe and use RTTI features in Java.

#### Learning Objective 1
-   Outline the need for RTTI (Runtime Type Information).

##### Readings
**Required:** Pages 553 to 556 of TIJ

##### Exercises
**Questions**
1.  What type of programming problem can be solved by using RTTI? Cite an example from the text. (See TIJ pages 555 to 556.)

##### Programs
Compile, run, and analyze programs:

[Shapes.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/typeinfo/Shapes.java)

#### Learning Objective 2
-   Use **Class** objects.

##### Readings
**Required:** Pages 556 to 587 of TIJ

##### Exercises
**Questions**
1.  What is the purpose of a **Class** object? (See TIJ page 556.)
2.  What is a *class loader* and how does it load classes? (See TIJ pages 556 to 557.)
3.  What is the use of **Class.forName**? (See TIJ page 558.)
4.  What is the use of a class literal? (See TIJ pages 562 to 563.)
5.  In Java SE5, why is **Class&lt;?&gt;** preferred over plain **Class**? (See TIJ page 566.)
6.  What is the function of **instanceof**? (See TIJ page 569.)
7.  What is the difference between **instancof** and **Class** objects? (See TIJ pages 586 to 587.)

##### Programs
Compile, run, and analyze programs:

[SweetShop.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/typeinfo/SweetShop.java)
[ToyTest.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/typeinfo/toys/ToyTest.java)
[ClassInitialization.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/typeinfo/ClassInitialization.java)
[GenericClassReferences.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/typeinfo/GenericClassReferences.java)
[WildcardClassReferences.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/typeinfo/WildcardClassReferences.java)
[BoundedClassReferences.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/typeinfo/BoundedClassReferences.java)
[FilledList.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/typeinfo/FilledList.java)
[GenericToyTest.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/typeinfo/toys/GenericToyTest.java)
[ClassCasts.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/typeinfo/ClassCasts.java)
[ForNameCreator.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/typeinfo/pets/ForNameCreator.java)
[PetCount.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/typeinfo/PetCount.java)
[LiteralPetCreator.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/typeinfo/pets/LiteralPetCreator.java)
[PetCount2.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/typeinfo/PetCount2.java)
[PetCount3.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/typeinfo/PetCount3.java)
[PetCount4.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/typeinfo/PetCount4.java)
[RegisteredFactories.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/typeinfo/RegisteredFactories.java)

#### Learning Objective 3
-   Explain the concept of reflection and describe how the class **Class** supports it.

##### Readings
**Required:** Pages 588 to 593 of TIJ

##### Exercises
**Questions**
1.  What are two function of reflection? (See TIJ pages 588 to 589.)
2.  What do the methods **getMethods** and **getConstructors** return? (See TIJ page 592.)

##### Programs
Compile, run, and analyze programs:

[ShowMethods.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/typeinfo/ShowMethods.java)

#### Learning Objective 4
-   Use *dynamic proxies, Null Objects* and interfaces.

##### Readings
**Required**: Pages 593 to 613 of TIJ

##### Exercises
**Questions**
1.  What is the purpose of Java implementation of *dynamic proxy*? (See TIJ pages 594 to 595.)
2.  Do you consider a *Null Object* useful? (Open question. See TIJ pages 598 to 599.)
3.  What is the function of the **private** flag? (See TIJ page 610.)

##### Programs
Compile, run, and analyze programs:

[SimpleProxyDemo.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/typeinfo/SimpleProxyDemo.java)
[SimpleDynamicProxy.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/typeinfo/SimpleDynamicProxy.java)
[SelectingMethods.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/typeinfo/SelectingMethods.java)
[Staff.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/typeinfo/Staff.java)
[SnowRemovalRobot.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/typeinfo/SnowRemovalRobot.java)
[NullRobot.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/typeinfo/NullRobot.java)
[InterfaceViolation.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/typeinfo/InterfaceViolation.java)
[HiddenImplementation.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/typeinfo/HiddenImplementation.java)
[InnerImplementation.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/typeinfo/InnerImplementation.java)
[AnonymousImplementation.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/typeinfo/AnonymousImplementation.java)
[ModifyingPrivateFields.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/typeinfo/ModifyingPrivateFields.java)

#### Learning Objective 5
-   Write programs that integrate and summarize the material on Java RTTI features.

##### Readings
**Required**: Pages 613 to 615 of TIJ

##### Exercises
Exercises 8 and 10 on page 562, and exercise 19 on page 593 of TIJ.

##### Answers To Exercises
-   [Answer 8](http://scis.athabascau.ca/html/course/COMP308/Unit_6/Section_1/Ch15ex8.java)
-   [Answer 10](http://scis.athabascau.ca/html/course/COMP308/Unit_6/Section_1/Ch15ex10.java)
-   [Answer 19](http://scis.athabascau.ca/html/course/COMP308/Unit_6/Section_1/Ch15ex19.java)

### Section 2: Generics
**Section Goal**: Explain and use Java generics.### Learning Objective 1

-   Introduce the generics and parameterized types.

##### Readings
**Required**: Pages 617 to 631 of TIJ

##### Exercises
**Questions**
1.  What is the general concept of generics or parameterized types? (See TIJ pages 617 to 618.)
2.  What is a tuple? How do a generics implement tuples? (See TIJ pages 621 to 622.)

##### Programs
Compile, run and analyse programs

[Holder1.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/Holder1.java)
[Holder3.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/Holder3.java)
[TwoTuple.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/util/TwoTuple.java)
[ThreeTuple.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/util/ThreeTuple.java)
[LinkedStack.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/LinkedStack.java)
[RandomList.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/RandomList.java)
[CoffeeGenerator.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/coffee/CoffeeGenerator.java)
[Fibonacci.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/Fibonacci.java)
[IterableFibonacci.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/IterableFibonacci.java)

#### Learning Objective 2
-   Describe and use generic methods, anonymous inner classes, and complex data structure.

##### Readings
**Required:** Pages 631 to 649 of TIJ

##### Exercises
**Questions**
1.  What is *type argument inference*? Why does a generic method look like an indefinite overloaded method? (See TIJ page 632.)
2.  Give one example of a generic method accepting variable argument list. (See TIJ page 635 to 636.)

##### Programs
Compile, run, and analyze programs:

[GenericMethods.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/GenericMethods.java)
[LimitsOfInference.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/LimitsOfInference.java)
[ExplicitTypeSpecification.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/ExplicitTypeSpecification.java)
[GenericVarargs.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/GenericVarargs.java)
[Generators.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/Generators.java)
[BasicGeneratorDemo.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/BasicGeneratorDemo.java)
[TupleTest2.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/TupleTest2.java)
[WatercolorSets.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/WatercolorSets.java)
[BankTeller.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/BankTeller.java)
[TupleList.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/TupleList.java)
[Store.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/Store.java)

#### Learning Objective 3
-   Discuss the issue of erasure.

##### Readings
**Required:** Pages 650 to 672 of TIJ

##### Exercises
**Questions**
1.  What is meant by *erasure*? Does Java consider **List&lt;String&gt;** and **List&lt;Integer&gt;** the same type?
    (See TIJ page 651.)
2.  What is a *bound* and how does Java implement a bound in generics? Explain the meanings of &lt;T1 extends T2&gt;? (See TIJ page 653.)
3.  What are the problems with erasure when using generics? (See TIJ pages 656 to 657.)
4.  How do you compensate for erasure by using a *type tag*? (See TIJ page 662 to 663.)

##### Programs
Compile, run, and analyze programs:

[LostInformation.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/LostInformation.java)
[Manipulation.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/Manipulation.java)
[ErasureAndInheritance.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/ErasureAndInheritance.java)
[ArrayMaker.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/ArrayMaker.java)
[ListMaker.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/ListMaker.java)
[FilledListMaker.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/FilledListMaker.java)
[SimpleHolder.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/SimpleHolder.java)
[GenericHolder.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/GenericHolder.java)
[ClassTypeCapture.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/ClassTypeCapture.java)
[InstantiateGenericType.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/InstantiateGenericType.java)
[FactoryConstraint.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/FactoryConstraint.java)
[CreatorGeneric.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/CreatorGeneric.java)
[ArrayOfGeneric.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/ArrayOfGeneric.java)
[GenericArray.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/GenericArray.java)
[GenericArray2.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/GenericArray2.java)
[GenericArrayWithTypeToken.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/GenericArrayWithTypeToken.java)

#### Learning Objective 4
-   Discuss *bounds* and *wildcards*.

##### Readings
**Required:** Pages 673 to 694 of TIJ

##### Exercises
**Questions**
1.  How does Java implement multiple bounds? (See TIJ page 673.)
2.  Consider the example given on pages 677 to 680 in TIJ. What is meant by ***List&lt;? extends Fruit&gt;*** and why can **flist** not add a
    new Apple object? (See TIJ pages 677 to 680.)
3.  Referring to the above question, how can you add a new Apple object using *supertype wildcards*? (See TIJ pages 682 to 683.)
4.  What is one situation that requires the use of an *unbounded wildcard*? (See TIJ pages 692 to 693.)

##### Programs
Compile, run, and analyze programs:

[BasicBounds.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/BasicBounds.java)
[InheritBounds.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/InheritBounds.java)
[EpicBattle.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/EpicBattle.java)
[CovariantArrays.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/CovariantArrays.java)
[NonCovariantGenerics.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/NonCovariantGenerics.java)
[GenericsAndCovariance.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/GenericsAndCovariance.java)
[CompilerIntelligence.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/CompilerIntelligence.java)
[Holder.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/Holder.java)
[SuperTypeWildcards.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/SuperTypeWildcards.java)
[GenericWriting.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/GenericWriting.java)
[GenericReading.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/GenericReading.java)
[UnboundedWildcards1.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/UnboundedWildcards1.java)
[UnboundedWildcards2.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/UnboundedWildcards2.java)
[Wildcards.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/Wildcards.java)
[CaptureConversion.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/CaptureConversion.java)

#### Learning Objective 5
-   Discuss issues of generics.

##### Readings
**Required**: Pages 694 to 701 of TIJ

##### Exercises
**Questions**
1.  Explain why a class cannot implement two variants of the same generic interface? (See TIJ page 696.)

##### Programs
Compile, run, and analyze programs:

[ListOfInt.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/ListOfInt.java)
[PrimitiveGenericTest.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/PrimitiveGenericTest.java)
[MultipleInterfaceVariants.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/MultipleInterfaceVariants.java)
[GenericCast.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/GenericCast.java)
[NeedCasting.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/NeedCasting.java)
[ClassCasting.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/ClassCasting.java)
[UseList.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/UseList.java)
[RestrictedComparablePets.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/RestrictedComparablePets.java)

#### Learning Objective 6
-   Describe self-bounded types, dynamic type checking features, Exceptions issues, and the use of Mixins in Java.

##### Readings
**Required**: Pages 701 to 721 of TIJ

##### Exercises
**Questions**
1.  What is a value of self-bounding types? (See TIJ page 706.)
2.  Describe a way to check type dynamically. (See TIJ page 710 to 711.)
3.  Explain why a **catch** clause cannot catch an exception of a generic type. (See TIJ page 711.)
4.  What is a *mixin*? Why is it difficult for Java to implement *mixins*? According to the author of TIJ, what approach in Java is
    closest to a true **mixin**? (See TIJ pages 713 to 715 and 719 to 721.)

##### Programs
Compile, run, and analyze programs:

[CRGWithBasicHolder.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/CRGWithBasicHolder.java)
[Unconstrainted.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/Unconstrained.java)
[SelfBounding.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/SelfBounding.java)
[NotSelfBounded.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/NotSelfBounded.java)
[SelfBoundingMethods.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/SelfBoundingMethods.java)
[GenericsAndReturnTypes.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/GenericsAndReturnTypes.java)
[OrdinaryArguments.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/OrdinaryArguments.java)
[SelfBoundingAndCovariantArguments.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/SelfBoundingAndCovariantArguments.java)
[PlainGenericInheritance.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/PlainGenericInheritance.java)
[CheckedList.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/CheckedList.java)
[ThrowGenericException.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/ThrowGenericException.java)
[Mixins.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/Mixins.java)
[Decoration.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/decorator/Decoration.java)
[DynamicProxyMixin.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/DynamicProxyMixin.java)

#### Learning Objective 7
-   Discuss the issues of latent typing and function objects and how they can be used in Java.

##### Readings
**Required**: Pages 721 to 743 of TIJ

##### Exercises
**Questions**
1.  What is latent typing? What is its advantage? (See TIJ pages 721 to 722.)
2.  How to compensate the lack of latent typing by using adapters? (See TIJ pages 733 to 736.)
3.  What is a *function object* and what are the advantages of using one? (See TIJ page 737.)

##### Programs
Compile, run, and analyze programs:

[Performs.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/Performs.java)
[LatentReflection.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/LatentReflection.java)
[Apply.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/Apply.java)
[SimpleQueue.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/SimpleQueue.java)
[Fill.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/Fill.java)
[Fill2.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/Fill2.java)
[Functional.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/generics/Functional.java)

#### Learning Objective 8
-   Summarize the materials in this section.

##### Readings
**Required**: Pages 743 to 746.

##### Exercises
Exercise2 on page 621, exercise 9 on page 633, exercise 20 on page 654,
exercise 25 on page 677, exercise 28 on pages 685 to 686 of TIJ.

**Questions**
1.  Is casting really so bad? (open question)

##### Answers To Exercises
-   [Answer 2](http://scis.athabascau.ca/html/course/COMP308/Unit_6/Section_2/Ch16ex2.java)
-   [Answer 9](http://scis.athabascau.ca/html/course/COMP308/Unit_6/Section_2/Ch16ex9.java)
-   [Answer 20](http://scis.athabascau.ca/html/course/COMP308/Unit_6/Section_2/Ch16ex20.java)
-   [Answer 25](http://scis.athabascau.ca/html/course/COMP308/Unit_6/Section_2/Ch16ex25.java)
-   [Answer 28](http://scis.athabascau.ca/html/course/COMP308/Unit_6/Section_2/Ch16ex28.java)

### Section 3: Containers and Types
**Section Goal**: Discuss the full functionality of various containers
in Java.### Learning Objective 1

-   Describe the full container taxonomy and ways to fill containers.

##### Readings
**Required**: Pages 791 to 809 of TIJ

##### Exercises
**Questions**
1.  List the new containers implementation added in Java 5. (See TIJ page 792 to 793).
2.  Briefly describe a Flyweight design pattern. How does the use of Abstract class demonstrate the use of Flyweight design pattern? (See TIJ page 800).

##### Programs
Compile, run, and analyze programs:

[FillingLists.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/containers/FillingLists.java)
[CollectionDataTest.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/containers/CollectionDataTest.java)
[CollectionDataGeneration.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/containers/CollectionDataGeneration.java)
[MapDataTest.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/containers/MapDataTest.java)
[Countries.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/net/mindview/util/Countries.java)

#### Learning Objective 2
-   Discuss and use Java **Collection** features.

##### Readings
**Required:** Pages 809 to 817 of TIJ

##### Exercises
**Questions**
1.  What are *optional operations* and why are they unusual? (See TIJ page 813.)

##### Programs
Compile, run, and analyze programs:

[CollectionMethods.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/containers/CollectionMethods.java)
[Unsupported.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/containers/Unsupported.java)

#### Learning Objective 3
-   Discuss and use **Lists, Sets, Queues,** and **Maps**.

##### Readings
**Required**: Pages 817 to 839 of TIJ

##### Exercises
**Questions**
1.  What are the characteristics of different implementations of **Set**? (See TIJ page 821.)
2.  What are the two implementations of **Queue** in Java SE5? (See TIJ page 827.)
3.  What is the basic idea of a **Map** or *associative array*? (See TIJ page 831.)
4.  What is the fundamental issue for **Maps** and what is the advantage of a **HashMap**? (See TIJ pages 833 to 835.)

##### Programs
Compile, run, and analyze programs:

[Lists.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/containers/Lists.java)
[TypesForSets.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/containers/TypesForSets.java)
[SortedSetDemo.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/containers/SortedSetDemo.java)
[QueueBehavior.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/containers/QueueBehavior.java)
[ToDoList.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/containers/ToDoList.java)
[DequeTest.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/containers/DequeTest.java)
[AssociativeArray.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/containers/AssociativeArray.java)
[Maps.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/containers/Maps.java)
[SortedMapDemo.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/containers/SortedMapDemo.java)
[LinkedHashMapDemo.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/containers/LinkedHashMapDemo.java)

#### Learning Objective 4
-   Explain the issues of hashing and hash codes.

##### Readings
**Required**: Pages 839 to 858 of TIJ

##### Exercises
**Questions**
1.  What is one common pitfall when creating customized classes as keys for **HashMaps** and how can you avoid it? (See TIJ pages 840 to 842.)
2.  What are the conditions that must be satisfied when overriding the **equals()** method? (See TIJ page 842.)
3.  What is one scheme to speed up searching within a **Map**? What is a *collision* and how can you resolve it? (See TIJ pages 847 to 848.)
4.  What are the two factors governing a good **hashCode()**? (See TIJ pages 852 to 853.)

##### Programs
Compile, run, and analyze programs:

[Groundhog.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/containers/Groundhog.java)
[Groundhog2.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/containers/Groundhog2.java)
[SlowMap.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/containers/SlowMap.java)
[MapEntry.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/containers/MapEntry.java)
[SimpleHashMap.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/containers/SimpleHashMap.java)
[CountedString.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/containers/CountedString.java)

#### Learning Objective 5
-   Discuss the issues in choosing a particular type of container.

##### Readings
**Required**: Pages 858 to 879 of TIJ

##### Exercises
**Questions**
1.  What is the distinction between different types of containers? Give an example. (See TIJ pages 858 to 859.)
2.  What are the advantages and disadvantages of **ArrayList** and **LinkedList**? (See TIJ page 870.)
3.  What are the advantages and disadvantages of **TreeSet** and **HashSet**? (See TIJ page 874.)
4.  What are the advantages and disadvantages of **TreeMap**, **HashMap**, and **HashTable**? (See TIJ page 877.)
5.  What are the performance factors of a **HashMap**? (See TIJ page 878.)

##### Programs
Compile, run, and analyze programs:

[TestParam.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/containers/TestParam.java)
[Tester.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/containers/Tester.java)
[ListPerformance.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/containers/ListPerformance.java)
[RandomBounds.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/containers/RandomBounds.java)
[SetPerformance.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/containers/SetPerformance.java)
[MapPerformance.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/containers/MapPerformance.java)

#### Learning Objective 6
-   Introduce utilities for containers.

##### Readings
**Required**: Pages 879 to 889 of TIJ

##### Exercises
**Questions**
1.  How do you make a **CollectionMap** unmodifiable? (See TIJ pages 885 to 887.)

##### Programs
Compile, run, and analyze programs:

[Utilities.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/containers/Utilities.java)
[ListSortSearch.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/containers/ListSortSearch.java)
[ReadOnly.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/containers/ReadOnly.java)
[Synchronization.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/containers/Synchronization.java)
[FailFast.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/containers/FailFast.java)

#### Learning Objective 7
-   Introduce different types of References and Java 1.0/1.1 containers.

##### Readings
**Required**: Pages 889 to 900 of TIJ

##### Exercises
**Questions**
1.  What are the three types of **References** and what are their differences? (See TIJ page 890.)

##### Programs
Compile, run, and analyze programs:

[References.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/containers/References.java)
[CanonicalMapping.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/containers/CanonicalMapping.java)
[Enumerations.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/containers/Enumerations.java)
[Stacks.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/containers/Stacks.java)
[Bits.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/containers/Bits.java)

#### Learning Objective 8
-   Summarize the materials in this section and finish the exercises.

##### Readings
**Required**: Page 900 of TIJ

##### Exercises
Exercises 1 and 2 on page 809, exercise 20 on page 851 of TIJ.

##### Answers To Exercises
-   [Answer 1](http://scis.athabascau.ca/html/course/COMP308/Unit_6/Section_3/Ch18ex1.java)
-   [Answer 2](http://scis.athabascau.ca/html/course/COMP308/Unit_6/Section_3/Ch18ex2.java)
-   [Answer 20](http://scis.athabascau.ca/html/course/COMP308/Unit_6/Section_3/Ch18ex20.java)

### Section 4: Enumerated Types
**Section Goal**: Discuss and use Java **enum**  features.

#### Learning Objective 1
-   Discuss and use Java **enum** features.

##### Readings
**Required**: Pages 1011 to 1028 of TIJ

##### Exercises
**Questions**
1.  How is an **enum** used inside a **switch** statement? Give an example. (See TIJ pages 1016 to 1017.)
2.  What is the use of the **values()** method in an **enum**? (See TIJ pages 1017 to 1019.)

##### Programs
Compile, run, and analyze programs:

[EnumClass.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/enumerated/EnumClass.java)
[Spiciness.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/enumerated/Spiciness.java)
[OzWitch.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/enumerated/OzWitch.java)
[SpaceShip.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/enumerated/SpaceShip.java)
[TrafficLight.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/enumerated/TrafficLight.java)
[Reflection.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/enumerated/Reflection.java)
[UpcastEnum.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/enumerated/UpcastEnum.java)
[NonEnum.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/enumerated/NonEnum.java)
[EnumImplementation.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/enumerated/cartoons/EnumImplementation.java)
[RandomTest.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/enumerated/RandomTest.java)
[TypeOfFood.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/enumerated/menu/TypeOfFood.java)
[Meal.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/enumerated/menu/Meal.java)
[SecurityCategory.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/enumerated/SecurityCategory.java)
[Meal2.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/enumerated/menu/Meal2.java)

#### Learning Objective 2
-   Discuss and use **EnumSet** and **EnumMap**.

##### Readings
**Required**: Pages 1028 to 1047 of TIJ

##### Exercises
**Questions**
-   What is an **EnumSet**? (See TIJ pages 1028 to 1030.)
-   What is an **EnumMap**? (See TIJ pages 1030 to 1032.)

##### Programs
Compile, run, and analyze programs:

[EnumSets.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/enumerated/EnumSets.java)
[EnumMaps.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/enumerated/EnumMaps.java)
[ConstantSpecificMethod.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/enumerated/ConstantSpecificMethod.java)
[CarWash.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/enumerated/CarWash.java)
[OverrideConstantSpecific.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/enumerated/OverrideConstantSpecific.java)
[PostOffice.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/enumerated/PostOffice.java)
[Input.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/enumerated/Input.java)
[VendingMachine.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/enumerated/VendingMachine.java)

#### Learning Objective 3
-   Discuss the use of **Enum** in multiple dispatching.

##### Readings
**Required**: Pages 1047 to 1057 of TIJ

##### Exercises
**Questions**
1.  What is the problem with single dispatching? Give an example. (See TIJ pages 1047 to 1048.)

##### Programs
Compile, run, and analyze programs:

[RoShamBo2.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/enumerated/RoShamBo2.java)
[RoShamBo3.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/enumerated/RoShamBo3.java)
[RoShamBo4.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/enumerated/RoShamBo4.java)
[RoShamBo5.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/enumerated/RoShamBo5.java)
[RoShamBo6.java](https://triton2.athabascau.ca/html/courses/comp308/access/samples/enumerated/RoShamBo6.java)

#### Learning Objective 4
-   Summarize the materials in this section and complete the exercises.

##### Readings
**Required**: Pages 1057 to 1058 of TIJ

##### Exercises
Exercise 4 on page 1027 of TIJ

##### Answers To Exercises
-   [Answer 4](http://scis.athabascau.ca/html/course/COMP308/Unit_6/Section_4/Ch20ex4.java)

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

## Tutor Marked Exercise 3 (due Jan 6th, 2017)
Please complete TME 3 and submit it by electronic mail.

Tutor Marked Exercise 3 is scored out of 100 and contributes to 12 per
cent of your final grade.

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
This unit introduces annotation and metadata, Java
documentation, and deployment issues of Java applications.

### Section 1: Annotations
**Section goal**: This section explains a formalized way to add
information to your Java codes so that you can use easily use the data
later.

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

## Tutor Marked Exercise 4 (due Jan 13th, 2017)
Please complete TME 4 and submit it by electronic mail.

Tutor Marked Exercise 4 is scored out of 100 and contributes to 20% of
your final grade.

## Final Exam (due Jan 23rd, 2017)

The exam will be a closed-book online examination three hours in length.
- Nine percent of the mark will be for analyzing a program and describing its output.
- Thirty percent of the mark will be for 10 short-answer questions (100 words or less) from the questions in the Study Guide.
- Twenty-seven percent of the mark will be for three questions relating to the tutor-marked exercises (TMEs).
- Twenty-four percent of the mark will be for programming questions. You will not be expected to have the syntax totally correct nor memorize all the class libraries you have used in the course. However, you should be able to make it clear what classes and methods you are using, and you should be familiar with any classes you used in the tutor marked exercises (TMEs). The question will give details on the classes you must use and on some you may wish to use.
- Five percent of the mark will be for your assessment, in 500 words or less, of Java as a programming language from both a technical and a market viewpoint and your view of the future of Java.
- Five percent of the mark will be for your assessment, in 500 words or less, of Java generics.
