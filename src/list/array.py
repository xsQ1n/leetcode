from collections import Counter
import sys
# 快速排序
def quick_sort(array: list, start_index, end_index) -> list:
    if array is None or len(array) <= 1 or start_index >= end_index:
        return

    base_data = array[start_index]
    left = start_index
    right = end_index

    while left < right:
        while left < right and base_data <= array[right]:
            right -= 1
        array[left] = array[right]

        while left < right and base_data > array[left]:
            left += 1
        array[right] = array[left]

    array[right] = base_data
    quick_sort(array, start_index, left - 1)
    quick_sort(array, right + 1, end_index)


# 归并排序
def merge_sort(array: list) -> None:
    if len(array) <= 1:
        return

    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1


def removeDuplicates(nums: List[int]) -> int:
    """
    删除有序数组的重复项
    """
    ## 方法：快慢指针
    if len(nums) == 0:
        return 0

    slow, fast = 0, 1

    while fast < len(nums):
        if nums[slow] != nums[fast]:
            slow += 1
            nums[slow] = nums[fast]
        fast += 1

    # slow从零开始，所以返回+1
    return slow + 1


def moveZeroes(nums: List[int]) -> None:
    """
    移动零
    """
    if not nums:
        return None
    slow, fast = 0, 0

    while fast < len(nums):
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1

    while slow < len(nums) :
        nums[slow] = 0
        slow += 1

    return nums


def twoSum(numbers: List[int], target: int) -> List[int]:
    """
    两数之和 II - 输入有序数组
    """
    ## 方法1：双指针
    left, right = 0, len(numbers) - 1

    while left < right:
        sum = numbers[left] + numbers[right]
        if sum == target:
            return [left + 1, right + 1]
        elif sum < target:
            left += 1
        elif sum > target:
            right -= 1

    # return [-1, -1]
    ## 方法2： 暴力破解
    # for i in range(len(numbers) -1 ):
    #     for j in range(i+1, len(numbers)):
    #         sum = numbers[i] + numbers[j]
    #         if sum == target:
    #             return [i+1, j+1]
    # return [-1, -1]

    ## 方法3： 哈希表
    # memo = {}
    # for i, num in enumerate(numbers):
    #     tmp = target - num
    #     if tmp in memo:
    #         return [memo[tmp]+1 , i+1]
    #     memo[num] = i
    # return [-1, -1]


    def reverseString(self, s: List[str]) -> None:
        """
        反转字符串
        """
        left, right = 0 , len(s) - 1

        while left < right:
            # tmp = s[left]
            # s[left] = s[right]
            # s[right] = tmp

            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


    def isPalindrome(s: str):
        """
        判断回文串
        """
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


    def longestPalindrome(s: str) -> str:
        """
        最长回文子串
        """
        def helper(s, l, r):
            while l>=0 and r< len(s) and s[r] == s[l]:
                l -= 1
                r += 1
            # 此处 l+1 是因为使用的while循环
            # r保持不动 是因为列表取值只会到 r-1
            return s[l+1:r]

        res = ""
        for i in range(0, len(s)):
            s1 = helper(s, i, i)
            s2 = helper(s, i, i+1)
            res = s1 if len(res) < len(s1) else res
            res = s2 if len(res) < len(s2) else res

        return res


    def minWindow(self, s: str, t: str) -> str:
        """
        最小覆盖子串
        """
        ## 方法1： 暴力破解
        # res = ""
        # dict_t = Counter(t)
        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         # 注意这个j+1
        #         dict_sub = Counter(s[i:j+1])
        #         if all(dict_sub[char] >= dict_t[char] for char in dict_t):
        #             if res == "":
        #                 res = s[i:j+1]
        #             elif len(res) > len(s[i:j+1]):
        #                 res = s[i:j+1]

        # return res

        ## 方法2：滑动窗口
        # need用存储t中每个字符的次数，可以调用Counter方法获取
        # window滑动窗口
        need, window = {}, {}
        for c in t:
            need[c] = need.get(c, 0) + 1
        ## 左右指针
        left, right = 0, 0
        # 用于记录符合要求的字符的left值，因为上面的left变量还会移动
        start = 0
        # 用于记录符合的字符串长度，也和start用于返回值
        lenght = sys.maxsize
        # 记录当前窗口符合字符的数量
        valid = 0
        while right < len(s):
            push_char = s[right]
            right += 1
            if push_char in need:
                window[push_char] = window.get(push_char, 0) + 1
                if (window[push_char] == need[push_char]):
                    valid += 1
            while valid == len(need):
                if right - left< lenght:
                    start = left
                    length = right - left
                pop_char = s[left]
                left +=1
                if pop_char in need:
                    if window[pop_char] == need[pop_char]
                        valid -= 1
                    window[pop_char] -= 1

        return "" if lenght == sys.maxsize else s[start: start+length]





if __name__ == '__main__':
    array_1 = [1, 3, 5, 2, 4, 6]
    array_2 = [1, 3, 5, 2, 4, 6]
    quick_sort(array_1, 0 , len(array_1) - 1)
    print(f"快速排序结果：{array_1}")
    merge_sort(array_2)
    print(f"归并排序结果：{array_2}")
