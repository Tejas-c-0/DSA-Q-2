# DSA-Q-2
# Palindrome Number

## Problem
Given an integer `x`, return `true` if `x` is a palindrome, otherwise return `false`.

A palindrome reads the same forward and backward.

---

## Approach 1: String Method (O(n))
- Convert integer to string
- Reverse the string
- Compare original and reversed

### Code
```python
def isPalindrome(x):
    s = str(x)
    return s == s[::-1]
