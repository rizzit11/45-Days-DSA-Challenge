class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1, p2, p = m - 1, n - 1, m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

# Approach: Pehle mujhe laga ki mujhe dono arrays ko merge karke ek naya sorted array bana lena chahiye, lekin problem mein specifically bola gaya hai ki humein nums1 ko hi modify karna hai. Isliye maine ek reverse order merging approach socha. Maine three pointers use kiye: p1 pointing to the end of valid elements in nums1, p2 pointing to the end of nums2, aur p pointing to the last position in nums1 (including zeros). Hum comparison karte hain p1 aur p2 ke elements ka, aur jo bhi bada hota hai usse p position par rakhte hain, aur fir pointers ko adjust karte hain. Iss tarah hum end se merge karte hain taaki kisi bhi value ko overwrite na karna pade.

# Logic: We start with three pointers—p1 = m - 1 pointing to the last valid element of nums1, p2 = n - 1 pointing to the last element of nums2, and p = m + n - 1 pointing to the last position in nums1. We compare nums1[p1] and nums2[p2] and place the larger one at nums1[p]. Depending on which value is



