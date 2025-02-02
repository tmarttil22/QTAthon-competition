# Task 2 - Valid Number

## Description

Consider a string `s`, that might contain any sequence of characters,
write a program that can verify if it is a valid number.

A valid number will be either an integer number that might be followed by an optional exponent, or a
decimal number followed by an exponent as well.

A valid number can have an optional negative ('-') or positive ('+') sign initially, and exponents
as well.

A valid decimal number might consider the previous definitions, but also needs to consider digits
followed by a dot '.', or digits followed by a dot '.' and other digits, and reciprocally, a dot '.'
followed by digits.

For the exponent notation, you need to consider both 'e' and 'E', followed by an optional sign and
digits.

A couple of cases for valid numbers of the previous rules are:

* Leading zeroes: `06`, `0089`,
* Negative and positive: `-1`, `+22.34`,
* Scientific notation: `-6e-2`, `+11E5`,
* Implicit zero in decimal: `-.1`, `+54.`


## Input and output

* Input: `02e-2`
* Output: true

In that case, the `02` is a valid integer part of the number, and the exponent has a negative sign,
so it's a valid number.

* Input: `-.e9`
* Output: false

Following the definition, the dot '.' needs to have either a digit on the left or right, which is
not present in order to continue evaluating the exponential.

## Example test cases

* Input: `0`
* Output: true

* Input: `e`
* Output: false

* Input: `-.`
* Output: false

* Input: `22a34e32`
* Output: false

* Input: `+53.1e9`
* Output: true

* Input: `-.9`
* Output: true
