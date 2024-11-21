class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Step 1 mai hum variables initialize karnege. Prefix sum ko track karne ke liye ek hashmap banate hain, jisme {0: 1} se start karte hain.
        # Yeh {0: 1} humein beginning se koi subarray milne par handle karne mein help karta hai.
        prefix_sum_count = {0: 1}
        running_sum = 0  # Yeh running sum ko track karta hai as we move through nums
        count = 0  # Yeh count karega kitne subarrays ka sum k ke barabar hai

        # Our step 2 is Iterating through each element in nums 
        for num in nums:
            # Har element ko running_sum mein add karte hain
            running_sum += num

            # Step 3 is to check : Agar (running_sum - k) hashmap mein exist karta hai, toh iska matlab hai ki ek subarray hai jiska sum k ke barabar hai
            if (running_sum - k) in prefix_sum_count:
                count += prefix_sum_count[running_sum - k]  # Hum count mein iss frequency ko add kar dete hain

            # Step 4 is current running_sum ko prefix_sum_count mein update ya increment karte hain
            prefix_sum_count[running_sum] = prefix_sum_count.get(running_sum, 0) + 1

        # Finally step 5 mai count return karte hain jo total subarrays ko track karta hai jinka sum k hai
        return count

# Approach: To be honest, pehle mujhe laga ki mujhe har possible subarray ka sum nikalna padega aur check karna padega if it’s equal to k. But phir socha ki agar array ka size bada ho toh yeh kaafi inefficient ho jayega. Toh phir maine ek better idea socha—prefix sum with a hashmap. Basically, hum ek running sum track karenge as we move through the array, aur ek hashmap se track karenge ki kaunse prefix sums hum pehle dekh chuke hain. Jab bhi running_sum - k hashmap mein mil jaye, iska matlab hai ki ek valid subarray exist karta hai jiska sum k ke barabar hai. Is approach se hum saare possible subarrays ka check nahi karte, bas efficiently unhe track karte hain jinka sum humein chahiye.

#Logic: Logic simple hai—hum running sum maintain karte hain to keep a cumulative track of the array values as we iterate. Jab bhi hum running_sum nikalte hain, hum check karte hain ki running_sum - k hashmap mein already hai ya nahi. Agar hai, toh hum count ko increment kar dete hain kyunki iska matlab hai ki us point tak ek valid subarray hai jiska sum k hai. Humne prefix_sum_count ko {0: 1} se initialize kiya, jisse handle ho jaye wo subarrays jo shuru se hi k ka sum banate hain. Fir har new running_sum ko hashmap mein store karte hain, aur jab bhi woh value wapas milti hai, uski frequency ko add kar dete hain to get the total count. Yeh method O(n) time mein kaam karta hai, toh it’s super efficient for finding the number of subarrays.

