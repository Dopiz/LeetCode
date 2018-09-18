# My Progress - Uploading ... 
<table>
  <tr>
    <th>Todo:</th>
    <td>795</td>
  </tr>
  <tr>
    <th>Solved:</th>
    <td>106 / 901</td>
  </tr>
  <tr>
    <th>Attempted:</th>
    <td>0</td>
  </tr>
</table>

# Python Note

- Time Complexity / [link](https://wiki.python.org/moin/TimeComplexity)
  - 使用 `in` 尋找元素時 `list` 需要 O(n)、`set` 需要 O(1)
  
- Python Object 的 mutable 與 imbutalbe / [link](http://wsfdl.com/python/2013/08/14/%E7%90%86%E8%A7%A3Python%E7%9A%84mutable%E5%92%8Cimmutable.html)
  - 常見的 immutable objects: `Numeric types: int, float、String、tuple`
  - 常見的 mutable objects: `list、dict、set`
  - Python 的 `=` 是引用而非賦值，所以 `x = 1` 實際上是建立一個值為 `1` 的物件，再將 `x` 指向此物件。
  
- `map()` 概念：接收一個函數 `f()` 與一個 `list`，並將 `f()` 依序作用在 `list` 中的每個元素上。
  ```python
  nums = [[1,2], [2,3], [3,4]]
  list( map(max, nums) )
  Output = [2, 3, 4]
  ```
  
- `filter()` 概念：按照傳入的函式 `f()` 規則，返回在 `list` 中進行篩選後的值。
  ```python
  nums = [1, 2, 3, 4, 5]
  list( filter(lambda x: x % 2, nums) )
  Output: [1, 3, 5]
  ```
  
- `reduce()` 概念：依序將 `list` 中的值進行傳入函式 `f()` 的累加運算。
  ```python
  nums = [1, 2, 3, 4, 5]
  reduce(lambda x, y: x + y, nums)
  Output: 1+2+3+4+5 = 15
  ```
  
- `zip()` 概念：將兩個 `list` 對應的元素打包成一個 `tuple`，並返回這些 `tuples` 組成的 `list`。
  - 可以利用 `zip(*)` 來進行解壓，返回原先的 `list`。
  ```python
  list_1 = [1, 3, 5]
  list_2 = [2, 4, 6]
  ziped = zip(list_1, list_2)
  Output: [(1, 2), (3, 4), (5, 6)]
  zip(*ziped)
  Output: [(1, 3, 5), (2, 4, 6)]
  ```
  
- `itertools.combinations()` 用法類似排列組合。
  ```python
  combinations('ABCD', 2)
  Output: AB AC AD BC BD CD
  ```
  
- 樹的值 `inorder` 走法概念：
  ```python
  def inorder(root):
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []
  ```
  
- 最長子字串 LCS 走法：
  ```python
  def lcs(s1, s2):
    if not s1 or not s2:
        return ""
    x, nx, y, ny = s1[0], s1[1:], s2[0], s2[1:]
    if x == y:
        return x + lcs(nx, ny)
    else:
        return max(lcs(s1, ny), lcs(nx, s2), key=len)
  ```
  
- Sort:
    - Quick Sort: O(nlogn)
    ```python
    def quickSort(nums):
        if len(nums) <= 1:
            return nums

        base = nums[0]
        left = [n for n in nums[1:] if n < base]
        right = [n for n in nums[1:] if n >= base]

        return quickSort(left) + [base] + quickSort(right)
    ```
    - Insertion Sort: O(n^2)
    ```python
    def insertionSort(nums):
        for i in range(1, len(nums)):
            j, fixed = i - 1, nums[i]
            while j >= 0 and nums[j] > fixed:
                nums[j + 1] = nums[j]
                j = j - 1
            nums[j + 1] = fixed
        return nums
    ```
    - Selection Sort: O(n^2)
    ```python
    def selectionSort(nums):
        for i in range(len(nums)):
            minIdx = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[minIdx]:
                    minIdx = j
            nums[i], nums[minIdx] = nums[minIdx], nums[i]
        return nums
    ```
    - Bubble Sort: O(n^2)
    ```python
    def bubbleSort(nums):
        flag = False
        while not flag:
            flag = True
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    flag = False
        return nums
    ```
    - Merge Sort: O(nlogn)
    ```python
    def mergeSort(nums):
        def merge(left, right):
            res = []
            leftIdx, rightIdx = 0, 0
            for _ in range(len(left) + len(right)):
                if leftIdx == len(left):
                    res.append(right[rightIdx])
                    rightIdx += 1
                elif rightIdx == len(right):
                    res.append(left[leftIdx])
                    leftIdx += 1
                elif left[leftIdx] < right[rightIdx]:
                    res.append(left[leftIdx])
                    leftIdx += 1
                elif right[rightIdx] <= left[leftIdx]:
                    res.append(right[rightIdx])
                    rightIdx += 1

            return res

        if len(nums) > 1:
            left = mergeSort(nums[:len(nums)//2])
            right = mergeSort(nums[len(nums)//2:])
            return merge(left, right)

        return nums
    ```