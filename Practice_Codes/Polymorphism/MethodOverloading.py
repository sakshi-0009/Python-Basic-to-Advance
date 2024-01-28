'''
Python does not support method overloading in the traditional scene as seen in some other programming languages like JAVA pr C++.
In languages that support method overloading, ou can define multiple methods with the same name in class, each having different set of parameters.
The compiler or runtime envirinment then determines which method to call based on the number and types of arguments provided.

However, in Python, if you try to define multiple methods with the same name in class,
the last one defined will override the previous ones.

Python relies on dynamic typing and is more flexible when it comes to functions and method signature.
You can achieve similar functionality in python through default parameter values,
variable-length argument lists or using *args and **kwargs to handle different parameter scenarios within a single method.

'''