"""
Merge sort is a sorting algorithm that follows the divide-and-conquer approach.
It works by recursively dividing the input array into smaller subarrays
and sorting those subarrays
then merging them back together to obtain the sorted array.

In simple terms, we can say that the process of merge sort is
to divide the array into two halves, sort each half,
and then merge the sorted halves back together.
This process is repeated until the entire array is sorted.

Link: https://www.geeksforgeeks.org/merge-sort/

Steps:
1. Divide: Divide the list or array recursively into two halves
           until it can no more be divided.
2. Conquer: Each subarray is sorted individually
            using the merge sort algorithm.
3. Merge: The sorted subarrays are merged back together in sorted order.
          The process continues until all elements
          from both subarrays have been merged.
"""


def merge(lst: list[int], i_left: int, i_mid: int, i_right: int) -> None:
    """
        [...,3,4,5,6,7,...]
             l   m   r
    """
    n1 = i_mid - i_left + 1
    n2 = i_right - i_mid

    res = [None] * (n1+n2)

    i = i_left
    j = i_mid + 1
    k = 0
    while (i < i_mid + 1) and (j < i_right + 1):
        if lst[i] < lst[j]:
            res[k] = lst[i]
            i += 1
        else:
            res[k] = lst[j]
            j += 1
        k += 1
    # insert the rest of the items that we did not use in the while loop
    while i < i_mid + 1:
        res[k] = lst[i]
        i += 1
        k += 1
    while j < i_right + 1:
        res[k] = lst[j]
        j += 1
        k += 1
    lst[i_left:i_right+1] = res


def merge_sort(lst: list[int], i_left: int, i_right: int) -> None:
    # sort lst from i_left to including i_right
    if i_left < i_right:
        """
            [0,1] -> i_mid = 0 -> left=(0-0) right=(1-1)
            [0,1,2] -> i_mid = 1 -> left (0-1), right=(2-2)
        """
        i_mid = (i_left + i_right) // 2
        merge_sort(lst, i_left, i_mid)
        merge_sort(lst, i_mid + 1, i_right)
        merge(lst, i_left, i_mid, i_right)


if __name__ == "__main__":
    lst = [12, 11, 13, 5, 6, 7]
    lst = [-7, 1, 4, 4, -8]
    merge_sort(lst, 0, len(lst) - 1)
    print(lst)
