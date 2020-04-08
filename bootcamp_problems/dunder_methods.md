# Dunder or magic methods in Python

Dunder or magic methods in Python are the methods having two prefix and suffix underscores in the method name. Dunder here means “Double Under (Underscores)”. These are commonly used for operator overloading. Few examples for magic methods are: __init__, __add__, __len__, __repr__ etc.

The __init__ method for initialization is invoked without any call, when an instance of a class is created, like constructors in certain other programming languages such as C++, Java, C#, PHP etc. These methods are the reason we can add two strings with ‘+’ operator without any explicit typecasting. 

# Dunder Methods list: 
- Object Representation: __str__, __repr__:
    It’s common practice in Python to provide a string representation of your object for the consumer of your class (a bit like API documentation.) 
- Iteration: __len__, __getitem__, __reversed__:
    In order to iterate over our account object I need to add some transactions. So first, I’ll define a simple method to add transactions.
- Operator Overloading for Comparing Accounts: __eq__, __lt__
- Operator Overloading for Merging Accounts: __add__
- Callable Python Objects: __call__
- Context Manager Support and the With Statement: __enter__, __exit__