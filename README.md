# Python-_prac_01
#This Document is uesd to Learning some basic algorithm by Python.



#Binary_search.py

This is a quick way can find a number which you what in a list.

1. Compare x with the middle element.
2. If x matches with the middle element, we return the mid index.
3. Else if x is greater than the mid element, then x can only lie in the right (greater) half subarray after the mid element. Then we apply the algorithm again for the right half.
4. Else if x is smaller, the target x must lie in the left (lower) half. So we apply the algorithm for the left half.
