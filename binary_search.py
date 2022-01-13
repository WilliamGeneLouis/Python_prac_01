'''
Author: William
Date: 2022-01-13 15:10:05
LastEditTime: 2022-01-13 20:31:07
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /undefined/Users/guister.iu/Documents/Python _prac_01/Two_sum.py
'''




def binary_search(list,item):  #定义二分查找函数
    low = 0                     #初始化 lwo 值
    high = len(list) - 1        #将数组长度减一
    while low <= high:          #设置while循环
        mid = (low + high) // 2     #找出中间值 Python3中需要使用 // 除以整数
        guess = list[mid]          
        if guess == item:       
            return mid
        if guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return None      #Python中none代表返回None

my_list = [1 , 3 , 5 , 7 , 9 , 10]  

result = binary_search(my_list, 9 )
print(result)
