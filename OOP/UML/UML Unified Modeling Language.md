## UML Unified Modeling Language
- Visuallize modeling language for software visualization purpose
- used to make communication between classes of the system
## Classes relationships

### ITS COMPOSED OF 4 PARTS :

- Association : user_borrow => book

- Aggregation : Department has employes

- Compostition : car has an engine or wheels

or university has departments

- Inheritance : circle is a Shape , car is a vehicle => somthing general
### Compostition relationship :

- parts of car has no value without the car itself or walls of room has no value without the room itself

- Car , engine , doors logic

### Aggregation relationship

- its a weak "has a" relationship

- depatment has profs if department is closed profs still exist

- whole class or some other class can create object

- if its destroyed its still used by other with no effect

  

### Generalization

  

A generalization is a binary taxonomic (i.e. related to classification) directed relationship between a more general classifier (superclass) and a more specific classifier (subclass).

Each instance of the specific classifier is also an indirect instance of the general classifier, so that we can say "Patient is a Person", "Savings account is an Account", etc. Because of this, generalization relationship is also informally called "Is A" relationship.
Generalization is owned by the specific classifier.

A generalization is shown as a line with a hollow triangle as an arrowhead between the symbols representing the involved classifiers. The arrowhead points to the symbol representing the general classifier. This notation is referred to as the "separate target style."

Generalization relationships that reference the same general classifier can also be connected together in the "shared target style."


## Multiplicity

**Multiplicity** is a definition of **cardinality** - i.e. **number of elements** - of some collection of elements by providing an inclusive interval of non-negative integers to specify the allowable number of instances of described element. Multiplicity interval has some **lower bound** and (possibly infinite) **upper bound**:

multiplicity-range ::= [ lower-bound '..' ] upper-bound  
lower-bound ::= natural-value-specification  
upper-bound ::= natural-value-specification | '*'

Lower and upper bounds could be natural constants or constant expressions evaluated to natural (non negative) number. Upper bound could be also specified as asterisk '*' which denotes unlimited number of elements. Upper bound should be greater than or equal to the lower bound.

**Note**, that [[UML 2.4.1 Specification]](https://www.uml-diagrams.org/references.html#ref-uml-24-super "UML 2.4.1 - Superstructure") is not very consistent describing multiplicity. For example, it says that the lower bound must be a non-negative integer literal, and later - that it may be specified by value specification, such as (side-effect free, constant) expression. Another issue is that asterisk as upper bound in one place means unlimited (and not infinity) number of elements while in the other you can read the (possibly infinite) upper bound. You can feel the difference in the two sentences: "Doctor may have unlimited number of patients." and "Doctor may have infinite number of patients."

Some typical examples of multiplicity:

![[Pasted image 20250425194537.png]]

If the multiplicity is associated with an element whose notation is a text string (such as a [class attribute](https://www.uml-diagrams.org/property.html#classifier-attribute)), the multiplicity range is placed within square brackets as part of that text string.
![[Pasted image 20250425194828.png]]

If the multiplicity is associated with an element that appears as a symbol (such as [use case](https://www.uml-diagrams.org/use-case.html) or class), the multiplicity range is displayed without square brackets.

![[Pasted image 20250425194842.png]]

_____

## Multiplicity Element

Multiplicity element defines some **collection** of elements, and includes both [multiplicity](https://www.uml-diagrams.org/multiplicity.html#multiplicity) as well as a specification of order and uniqueness of the collection elements.

Some subclasses of multiplicity element are [structural feature](https://www.uml-diagrams.org/uml-core.html#structural-feature), [operation](https://www.uml-diagrams.org/operation.html), **parameter**, **pin**.

Collection properties could be described with the following non-normative syntax rules:

collection-type ::= multiplicity-range  [ '{' collection-options '}' ]

Collection options specify whether the values in an instantiation of the element should be **unique** and/or **ordered**:

collection-options ::= order-designator [ ','  uniqueness-designator ] |  uniqueness-designator [ ','  order-designator ]  
order-designator ::= 'ordered' | 'unordered'  
uniqueness-designator ::= 'unique' | 'nonunique'

| Collection Type | isOrdered | isUnique |
| --------------- | --------- | -------- |
| Multiset, bag   | false     | false    |
| Sequence, array | true      | false    |
| Set             | false     | true     |
| Ordered set     | true      | true     |

If multiplicity element is multivalued and specified as **ordered**, then the collection of values in an instantiation of this element is sequentially ordered. By default, collections are **not ordered**.

If multiplicity element is multivalued and specified as **unique**, then each value in the collection of values in an instantiation of this element must be unique. By default, each value in collection is **unique**.

![Example of ordered multiplicity of class attributes.](https://www.uml-diagrams.org/class-diagrams/class-attribute-multiplicity-ordered.png "Example of ordered  multiplicity of class attributes.")

Data Source could have a Logger and has ordered pool  
of min to max Connections. Each Connection is unique (by default)

![Example of ordered adornment multiplicity.](https://www.uml-diagrams.org/class-diagrams/class-adornment-multiplicity.png "Example of ordered adornment multiplicity.")

Customer has none to many purchases.  
Purchases are in specific order and each one is unique (by default)

![Next](https://www.uml-diagrams.org/images/arrow-next.png "Next")  [Visibility](https://www.uml-diagrams.org/visibility.html "UML visibility")
____
### Relationships 
![hero-img](https://creately.com/static/assets/guides/class-diagram-relationships/hero.webp)

[Class diagrams](https://creately.com/lp/online-class-diagram-tool/) are the main building blocks of object-oriented modeling so it is important that you understand the various class diagram relationships and how they affect your solution. We have listed them below with examples.

[Creately](https://creately.com/) simplifies creating class diagrams by showing the logical relationship based on context.

[Create a class diagram >>](https://creately.com/diagram-type/class-diagram/)

## **Class Diagram** **Relationships**

Classes are interrelated to each other in specific ways. In particular, relationships in class diagrams include different types of logical connections. The following are such types of logical connections 

![Class Diagram Relationships (UML)](https://creately.com/static/assets/guides/class-diagram-relationships/uml-class-diagram-relationships.webp)

Relationships in UML Class Diagrams

### Association

![Association - One of the most common in class diagram relationships](https://creately.com/static/assets/guides/class-diagram-relationships/association.webp)

is a broad term that encompasses just about any logical connection or relationship between classes. For example, passengers and airline may be linked as above.

### Directed Association

![Directed Association Relationship in UML Class diagram](https://creately.com/static/assets/guides/class-diagram-relationships/directed-association.webp)

refers to a [directional relationship](https://creately.com/diagram/example/QntZ3BLMuEE/uml-class) represented by a line with an arrowhead. The arrowhead depicts a container-contained directional flow.

### Reflexive Association

![Reflexive Association Relationship in UML Class diagrams](https://creately.com/static/assets/guides/class-diagram-relationships/reflexive-association.webp)

This occurs when a class may have multiple functions or responsibilities. For example, a staff member working in an airport may be a pilot, aviation engineer, ticket dispatcher, guard, or maintenance crew member. If the maintenance crew member is managed by the aviation engineer there could be a managed by relationship in two instances of the same class.

### Multiplicity

![Multiplicity Relationship in UML Class diagrams](https://creately.com/static/assets/guides/class-diagram-relationships/multiplicity.webp)

is the active [logical association](https://creately.com/diagram-community/all/t/class-diagram) when the cardinality of a class in relation to another is being depicted. For example, one fleet may include multiple airplanes, while one commercial airplane may contain zero to many passengers. The notation 0..* in the diagram means “zero to many”.

### Aggregation

![Aggregation Relationship](https://creately.com/static/assets/guides/class-diagram-relationships/aggregation.webp)

refers to the formation of a particular class as a result of one class being aggregated or built as a collection. For example, the class “library” is made up of one or more books, among other materials. In aggregation, the contained classes are not strongly dependent on the lifecycle of the container. In the same example, books will remain so even when the library is dissolved. To show aggregation in a diagram, draw a line from the parent class to the child class with a diamond shape near the parent class.

To show [aggregation](https://creately.com/diagram/example/icbqu3z82/person-class-diagram) in a diagram, draw a line from the parent class to the child class with a diamond shape near the parent class.

### Composition

![Composition Relationship in Class Diagrams](https://creately.com/static/assets/guides/class-diagram-relationships/composition.webp)

The composition relationship is very similar to the aggregation relationship. with the only difference being its key purpose of emphasizing the dependence of the contained class to the life cycle of the container class. That is, the contained class will be obliterated when the container class is destroyed. For example, a shoulder bag’s side pocket will also cease to exist once the shoulder bag is destroyed.

To show a composition relationship in a [UML diagram](https://creately.com/lp/uml-diagram-tool), use a directional line connecting the two classes, with a filled diamond shape adjacent to the container class and the directional arrow to the contained class.

### Inheritance/Generalization

![Inheritance Relationship in UML Class diagrams](https://creately.com/static/assets/guides/class-diagram-relationships/inheritance-generalization.webp)

refers to a type of relationship wherein one associated class is a child of another by virtue of assuming the same functionalities of the parent class. In other words, the child class is a specific type of the parent class. To show inheritance in a UML diagram, a solid line from the child class to the parent class is drawn using an unfilled arrowhead.

### Realization

![Realization Relationship in UML Class diagrams](https://creately.com/static/assets/guides/class-diagram-relationships/realization.webp)

		denotes the implementation of the functionality defined in one class by another class. To show the relationship in [UML](https://creately.com/diagram-type/uml-diagram), a broken line with an unfilled solid arrowhead is drawn from the class that defines the functionality of the class that implements the function. In the example, the printing preferences that are set using the printer setup interface are being implemented by the printer.
____


# Must Read  : https://www.geeksforgeeks.org/unified-modeling-language-uml-introduction/



