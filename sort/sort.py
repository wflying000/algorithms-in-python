
import random

def selection_sort(nums):
    if not nums:
        return
    n = len(nums)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]


def insertion_sort(nums):
    if not nums:
        return
    n = len(nums)
    for i in range(1, n):
        j = i
        while j > 0 and nums[j] < nums[j - 1]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1


def bubble_sort(nums):
    if not nums:
        return

    n = len(nums)

    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break
                

def merge_sort(nums):
    if not nums:
        return
    
    merge_sort_core(nums, 0, len(nums) - 1)

def merge(nums, left, mid, right):
    tmp = []
    i, j = left, mid + 1
    while i <= mid and j <= right:
        if nums[i] <= nums[j]:
            tmp.append(nums[i])
            i += 1
        else:
            tmp.append(nums[j])
            j += 1

    if i <= mid:
        tmp += nums[i : mid + 1]
    elif j <= right:
        tmp += nums[j : right + 1]

    # n = right - left + 1
    # for k in range(n):
    #     nums[left + k] = tmp[k]
    
    nums[left : right + 1] = tmp

def merge_sort_core(nums, left, right):
    if left >= right:
        return
    mid = (right - left) // 2 + left
    merge_sort_core(nums, left, mid)
    merge_sort_core(nums, mid + 1, right)
    merge(nums, left, mid, right)
    

def quick_sort(nums):
    if not nums:
        return
    quick_sort_core(nums, 0, len(nums) - 1)

def quick_sort_core(nums, left, right):
    if left >= right:
        return
    
    idx = partition(nums, left, right)
    quick_sort_core(nums, left, idx - 1)
    quick_sort_core(nums, idx + 1, right)

def partition(nums, left, right):
    pivot = nums[left]
    i, j = left, right
    while i < j:
        while i < j and nums[j] >= pivot:
            j -= 1
        while i < j and nums[i] <= pivot:
            i += 1
        nums[i], nums[j] = nums[j], nums[i]

    nums[i], nums[left] = nums[left], nums[i]

    return i

def quick_sort_3way(nums):
    quick_sort_3way_core(nums, 0, len(nums) - 1)


def quick_sort_3way_core(nums, left, right):
    if left >= right:
        return 
    low, high = partition_3way(nums, left, right)
    quick_sort_3way_core(nums, left, low - 1)
    quick_sort_3way_core(nums, high + 1, right)

def partition_3way(nums, left, right):
    pivot = nums[left]
    low, mid, high = left, left, right
    while mid <= high:
        if nums[mid] < pivot:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] > pivot:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
        else:
            mid += 1

    return low, high 
        
def max_heapify(nums, i, n):
    j = 2 * i + 1
    while j < n:
        if j + 1 < n and nums[j + 1] > nums[j]:
            j += 1
        if nums[i] >= nums[j]:
            return 
        nums[i], nums[j] = nums[j], nums[i]
        i = j
        j = 2 * i + 1

def build_max_heap(nums):
    n = len(nums)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(nums, i, n)

def heap_sort(nums):
    n = len(nums)
    build_max_heap(nums)
    for end in range(n - 1, 0, -1):
        nums[0], nums[end] = nums[end], nums[0]
        max_heapify(nums, 0, end)



def test_selection_sort():
    nums = [random.randint(0, 100) for _ in range(10)]
    nums_sorted = sorted(nums)
    selection_sort(nums)
    assert nums == nums_sorted


def test_insertion_sort():
    nums = [random.randint(0, 100) for _ in range(10)]
    nums_sorted = sorted(nums)
    print(f"before sorted, nums: {nums}")
    insertion_sort(nums)
    print(f"after sorted, nums: {nums}")
    assert nums == nums_sorted

def test_bubble_sort():
    nums = [random.randint(0, 100) for _ in range(10)]
    nums_sorted = sorted(nums)
    print(f"before sorted, nums: {nums}")
    bubble_sort(nums)
    print(f"after sorted, nums: {nums}")
    assert nums == nums_sorted

def test_merge_sort():
    nums = [random.randint(0, 100) for _ in range(10)]
    nums_sorted = sorted(nums)
    print(f"before sorted, nums: {nums}")
    merge_sort(nums)
    print(f"after sorted, nums: {nums}")
    assert nums == nums_sorted

def test_quick_sort():
    nums = [random.randint(0, 100) for _ in range(10)]
    nums_sorted = sorted(nums)
    print(f"before sorted, nums: {nums}")
    quick_sort(nums)
    print(f"after sorted, nums: {nums}")
    assert nums == nums_sorted

def test_quick_sort_3way():
    nums = [random.randint(0, 100) for _ in range(10)]
    nums_sorted = sorted(nums)
    print(f"before sorted, nums: {nums}")
    quick_sort_3way(nums)
    print(f"after sorted, nums: {nums}")
    assert nums == nums_sorted
    

def test_heap_sort():
    nums = [random.randint(0, 100) for _ in range(10)]
    nums_sorted = sorted(nums)
    print(f"before sorted, nums: {nums}")
    heap_sort(nums)
    print(f"after sorted, nums: {nums}")
    assert nums == nums_sorted
        


def main():
    # test_selection_sort()
    # test_insertion_sort()
    # test_bubble_sort()
    # test_merge_sort()
    # test_quick_sort()
    # test_quick_sort_3way()
    test_heap_sort()

if __name__ == "__main__":
    main()
