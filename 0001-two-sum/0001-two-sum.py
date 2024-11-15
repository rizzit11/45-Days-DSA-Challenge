class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
    
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in hashmap:
                return [hashmap[complement], i]

            hashmap[num] = i

#Approach : Mujhe sabse pehle laga ki shayad mujhe ek ek pair check karna padega to find the solution, but phir mujhe samajh aaya ki yeh approach inefficient hogi, especially jab array ka size bada ho. Instead, maine ek hashmap use kiya jahan pe main numbers ko unke indices ke saath store kar sakta hoon, taaki mujhe efficiently pata chale ki mujhe target achieve karne ke liye kaunsa number chahiye. Maine array ko ek baar iterate kiya aur har number ka complement (jo target tak pahunchne ke liye chahiye) calculate kiya. Agar wo complement hashmap mein already exist karta hai, toh mujhe wahi do indices mil gaye jo target tak pahunch sakte hain. 

# Logic: Final approach mein, ek hashmap use hota hai jo ki har number aur uske index ko store karta hai. Jab bhi hum ek naya number dekhte hain, hum uska complement calculate karte hain aur check karte hain ki wo hashmap mein hai ya nahi. Agar hai, toh hum turant do indices return kar dete hain. Agar nahi hai, toh current number ko hashmap mein add kar dete hain. Yeh approach single pass mein solution nikal deti hai.