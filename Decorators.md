In python, we can assign variables to functions. For example let's create a function,

```
def hello():
    print("Hello India!")
```
Now, let's assign a variable to above function,
```
greet = hello
print(greet)
```
This will print the result as `<function hello at 0x7fcb3da3f830>`. And, when we do following:
```
greet = hello
print(greet())
```
This will print the result as `Hello India!`. 

So, in this way can assign variables to functions. As we can assign the variables to functions that implies we can also pass one to another by assigning variables to functions. We can use this idea to create decorators in python. 

Decorators are just the extra functionality that we want to assign to a function but not everytime we want that extra functionality. We will use that extra functionality whenever we need. This is where decorators come into handy. Using decorators we can reduce the function size as well achieve code re-usability. 

Now, let's create a function inside another function:
```
def decorator_function(function_name):
    # some code
    def wrapper_function():
        # some code
        print('wrapper executed this before {}'.format(function_name.__name__))
        return function_name()
    return wrapper_function
```
Above function returns the wrapper_function as a variable. Now, let's create another function,
```
def display_function():
    print('Hello from Display Function')
```

Now, if we want to first run wrapper_function() before the display_function i.e. we want wrap some functionality before executing our main function(display_function() here) then we have to pass this display_function() to decorator_function(). So let's do it: 
```
decorated_variable = decorator_function(display)
decorated_variable()
```
Above will achieve the functionality we want that is wrapper_function() will execute some code first and call display_function(). Using above two lines of code we can make use of decorator functions but python has simple way to call wrapper_function() before any function we want to call(display_function() here). We have do as follow while defining a function itself:
```
@decorator_function
def display_function():
    print('Hello from Display Function')
```
And, now you can call display_function() directly to execute wrapper_function() code before display_function() itself. 