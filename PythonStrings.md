# Strings in Python

Strings in python is a sequence of characters. A single character also treated as a string in python with length equal to one. There is no separate data type 'char' for character in python. 
In python, string is generally quoted in single, double & even in triple quotes.
for example:  country = "India" or country = 'India' or country = """India""" are same.

### NOTE: 
	Generally, triple quotes is used for multiline string & also for documentation purpose.

	
As I mentioned earlier, the string in python is a sequence of charaters. So, in string each character can be accessed by using is position. The position of characters in string starts from 0 ranging to n-1 where n is the length of string(called as forward indexing). Also, there is one more way by which we can position the characters in string in python, that is negative indexing(or forward indexing). The negative indexing starts from the end[(n-1)th element] with index of -1, second last element with index of -2 & so on. 
Let's take an example string: s = "India"
Now, above string has length 5. So, index of last element will be 4(n-1) & also -1.Similarly, now first element will have index 0 as well as -5. 

## Operation on strings: 
1. Combine two strings: Using concatenation that is using '+' operator. 
	Example: s1 = "Hello,"
		 s2 = " India"
		 s3 = s1 + s2
		 print(s3)
	Output: "Hello, India"
2. Length of a string: Length of string is calculated by using python's in-built function len().
	Example: s = "India"
		 length = len(s)
		 print(length)
	Output: 5



## Extracting substrings from string:
In python, extracting substring/s from a string is referred as slicing. So, slicing is a very interesting yet useful thing in python. We will learn it through the examples: 
	Example1: s = "India"
		  sub = s[0:3]
		  print(sub)
	Output: "Ind"
In above example, slicing will start from index equal to number before colon & end to index equal to (number-1) after colon.

### NOTE: 
In general, if we want to say for s[i:j], substring formed will start at s[0] & end at s[j-1]. Also, for s[:j], substring formed will start at s[0] & end at s[j-1]. Similarly, for s[i:], substring formed will start at s[i] & end at s[length(s)-1].


