# hackerrank - Day 6 Let's Review


# Objective
Today we're expanding our knowledge of Strings and combining it with what we've already learned about loops. Check out the Tutorial tab for learning materials and an instructional video!

# Task
Given a string, _**S**_, of length _**N**_ that is indexed from _**0**_ to _**N - 1**_, print its even-indexed and odd-indexed characters as _**2**_ space-separated strings on a single line (see the Sample below for more detail).

Note: _**0**_ is considered to be an even index.

# Input Format
The first line contains an integer, _**T**_  (the number of test cases).
Each line _**i**_ of the _**T**_ subsequent lines contain a String, _**S**_.

# Constraints
* 1 <= T <= 10
* 2 <= length of S <= 1000

# Output Format
For each String _**Sj**_ (where _**0**_), print _**Sj**_ 's even-indexed characters, followed by a space, followed by _**Sj**_'s odd-indexed characters.


# Sample Input
`2`
`hacker`
`Rank`

# Explation 

Test case 0: `S = 'hacker'`
S[0] = 'H'
S[1] = 'A'
S[2] = 'C'
S[3] = 'K'
S[4] = 'E'
S[5] = 'R'

The even indices are _**0**_,_**2**_ , and _**4**_ , and the odd indices are _**1**_ ,_**3**_ , and _**5**_. We then print a single line of _**2**_ space-separated strings; the first string contains the ordered characters from _**S**_'s even indices (_**Hce**_), and the second string contains the ordered characters from _**S**_'s odd indices (_**akr**_).

Test Case 1: `S = 'Rank`
S[0] = 'R'
S[1] = 'A'
S[2] = 'N'
S[3] = 'K'

The even indices are _**0**_ and _**2**_, and the odd indices are _**1**_ and _**3**_. We then print a single line of _**2**_ space-separated strings; the first string contains the ordered characters from _**S**_'s even indices( _**RN**_), and the second string contains the ordered characters from  _**S**_'s odd indices ( _**sk**_).
