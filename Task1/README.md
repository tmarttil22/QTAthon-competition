# Task 1 - Longest valid parenthesis

## Description

Considering the round parenthesis '(' and ')', write a program that can read a string that contains
a combination of those two characters, and return the length of longest valid parenthesis pairs '()'
from the sequence.

## Input and output


In the following example:

```
)()())
```
you can see that the middle `()()` is the longest sequence,
hence the output of the program is `4`.

## Example test cases

Other cases you can consider to check the correctness of the problem:

* Input: `()`
* Output: 2

* Input: `(())`
* Output: 2

* Input: `(((`
* Output: 0

* Input: `)()()()(((()()()())))`
* Output: 8

* Input: ``
* Output: 0

> [!NOTE]
> When testing, you will have to pass the argument within quotation marks
> Example: `./Test1/build/Main "()"`
> Example: `python ./Test1/main.py "()"`
