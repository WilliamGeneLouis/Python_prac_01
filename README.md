<!--
 * @Author: William
 * @Date: 2022-01-13 21:13:13
 * @LastEditTime: 2022-01-15 17:20:25
 * @LastEditors: Please set LastEditors
 * @Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 * @FilePath: /Python_prac_01/README.md
-->
# Python-_prac_01
### This Document is uesd to Learning some basic algorithm by Python.



## Binary_search.py

This is a quick way can find a number which you what in a list.

1. Compare x with the middle element.
2. If x matches with the middle element, we return the mid index.
3. Else if x is greater than the mid element, then x can only lie in the right (greater) half subarray after the mid element. Then we apply the algorithm again for the right half.
4. Else if x is smaller, the target x must lie in the left (lower) half. So we apply the algorithm for the left half.

# 内存的工作原理
    数组和链表是两种基本的存储方式。

## 数组
    使用数组意味着所有的元素在内存中是相连的。