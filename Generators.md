# Generator Functions in Python 

Generators Functions in Python are the functions that allow us to write a function that can send back a value and later resume to pick up where it left off. These are used to create [iterators](https://www.geeksforgeeks.org/iterators-in-python/).

Suppose, we want to return squares of numbers from 1 to 10, one by one then, we create a function that returns a list of squares of numbers and iterate over the returned list of numbers then print the numbers one by one: 

```
def num_function():
    num_list = []
    for i in range(1, 11):
        num_list.append(i**2)
    return num_list

for i in num_function():
    print(i)
```
The above function will print the squares of numbers from 1 to 10 line by line. Here, we are using list here to append the result into it. But, don't you think this storing the elements into a list and the again iterating over the list to print the squares of numbers one by one is quite enefficient? If you also think so, then python has a solution for it and there it comes the generator funtions to help. Now, to understand how to use generator functions, let's create above same function but in a generator function style:

```
def num_gen_function():
    for i in range(1, 11):
        yield(i**2)

for i in num_gen_function():
    print(i)
```

Here, you will get same result but with memory efficiency. Also, here you see the `yield keyword`. This yield keyword just like the return keyword, returns the value but it is quite different than return keyword. Now, we know that the return keyword returns a value at the end of the excution of the program but here yield acts differently. The yield returns a value somewhere in the middle of executing the function and it just pauses that function then returns value. After returning a value, the function resumes where it left off and the new value will the next of that previously returned value. This is the difference between the yield and return. The yield is very much handy when we want to return some values and after returning the values, we want to execute the remaining function. 

Now, if you are thinking that, we have restricted the use of list but we are still using the for loop to iterate over. For this also we have one solution which it next() function. Let's use it to access elements genereted from above num_gen_function(). 

```
g = num_gen_function()
print(next(g)) # will print 1
print(next(g)) # will print 4
print(next(next(g))) # will print 16 why?
```
Here, we have assigned a variable to function and used next() function to get the value in the iterator. The next() function is used to fetch next item from the collection.

## Think about the fact:
Let's dig at how range() function works. We know that range() function is used for iteration purpose. The range() function remembers the last number iterated and after iteration it continues from the next of that last number. This part of remembering is very important here and the idea this `remembering` is what is used in forming the generators. But, one more thing is we can't access elements in range() using next() function because it's a class of immutable iterable objects. For more information visit [here](https://stackoverflow.com/a/13092317/12552274).