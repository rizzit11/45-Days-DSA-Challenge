class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        remainder_count = {0: 1}
        running_sum = 0
        count = 0

        for num in nums:

            running_sum += num

            remainder = running_sum % k

            if remainder < 0:
                remainder += k

            if remainder in remainder_count:
                count += remainder_count[remainder]

            remainder_count[remainder] = remainder_count.get(remainder, 0) + 1

        return count

# Approach: Pehle mujhe laga ki mujhe har subarray ka sum calculate karke check karna padega, but mujhe samajh aaya ki yeh approach kaafi inefficient ho jayegi, especially bade arrays ke liye. Isliye maine prefix sum aur hashmap ka use kiya. Yeh approach mein hum **running sum** ko maintain karte hain aur uska remainder (`% k`) calculate karte hain. Agar same remainder pehle aaya hai, toh iska matlab hai ki un dono points ke beech ka subarray `k` se divisible hoga. Isliye hum **hashmap** mein har remainder ki frequency track karte hain taaki jaldi pata chale ki kitne subarrays divisible hain.

#Logic: Hum running sum calculate karte hain aur har step pe `running_sum % k` ko check karte hain. Agar remainder pehle se hashmap mein ho, toh iska matlab hai ki ek valid subarray mil gaya hai jo `k` se divisible hai, toh hum count increase karte hain. Iske liye hum pehle `{0: 1}` se hashmap initialize karte hain taaki beginning se hi divisible subarrays ko handle kar sakein. Har remainder ko hashmap mein store karte hain aur jab same remainder phir se milta hai, toh uski frequency se count ko update karte hain. Yeh approach **O(n)** time complexity mein kaam karti hai, kyunki hum array ko sirf ek baar traverse karte hain.