## Tuples in Python
Tuples are a fundamental data structure in Python, offering a collection of ordered and immutable elements. They are defined by enclosing elements in parentheses () and separating them with commas.

**Advantages of Tuples**
*Memory Efficiency*: Tuples are more memory-efficient than lists because they are immutable, meaning their size cannot change once created.
*Speed*: Accessing elements in a tuple is faster than in a list because of their immutable nature.
*Security*: Since tuples cannot be modified after creation, they are safer to use in scenarios where data integrity is crucial.

**Disadvantages of Tuples**
*Limited Modification*: You cannot add or remove elements from a tuple after it has been created.
*Fewer Built-in Methods*: Compared to lists, tuples have fewer built-in methods for manipulation.
*Allows Duplicates*: Tuples can contain duplicate elements, which might not be desirable in all use cases.

**Properties of Tuples**
*Ordered*: Elements in a tuple have a specific order that is maintained.
*Immutable*: Once a tuple is created, its elements cannot be changed.
*Can Contain Different Data Types*: Tuples can store elements of various data types, including integers, strings, and even other tuples.

**Applications of Tuples**
*Storing Collections of Data*: Tuples are ideal for storing collections of data that should not be changed, such as the coordinates of a point in a 2D space.
Returning Multiple Values from Functions: When a function needs to return more than one value, tuples can be used to package these values together.
