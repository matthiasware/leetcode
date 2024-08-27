def insertion_sort(lst):
    n = len(lst)
    if n <= 1:
        return
    for idx_forward in range(1, n):
        idx_backward = idx_forward - 1
        key = lst[idx_forward]
        while idx_backward >= 0 and lst[idx_backward] > key:
            lst[idx_backward], lst[idx_backward+1] = lst[idx_backward + 1], lst[idx_backward]
            idx_backward -= 1


def quick_sort(lst: list[int], i_start: int = None, i_end: int = None) -> None:
    """
        idcs are incluse
    """
    i_start = 0 if i_start is None else i_start
    i_end = len(lst) - 1 if i_end is None else i_end

    if i_end - i_start < 1:
        return
    
    i_part = partition(lst, i_start, i_end)
    quick_sort(lst, i_start, i_part - 1)
    quick_sort(lst, i_part + 1, i_end)


def partition(lst: list[int], i_start: int, i_end: int) -> int:
    i_pivot = i_end
    i_part = i_start
    for i in range(i_start, i_end):
        if lst[i] <= lst[i_pivot]:
            lst[i_part], lst[i] = lst[i], lst[i_part]
            i_part += 1
    lst[i_part], lst[i_pivot] = lst[i_pivot], lst[i_part]
    return i_part


if __name__ == "__main__":
    lst = [1, 2, 4, 5, 3]
    quick_sort(lst)