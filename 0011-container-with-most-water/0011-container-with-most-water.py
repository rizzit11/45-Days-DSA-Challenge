class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0
        
        while l < r:
            lh = height[l]
            rh = height[r]
            min_h = min(lh, rh)
            max_area = max(max_area, min_h * (r - l))
            
            if lh < rh:
                l += 1
            else:
                r -= 1
        
        return max_area

#Approach: Pehle mujhe laga ki mujhe har possible pair of lines ko consider karna padega aur unke beech ka area calculate karna padega taaki maximum area find kar saku. Is tarah se, agar array ka size n ho, toh mujhe n*(n-1)/2 pairs check karne padenge, jo ki O(n²) time complexity hai. Lekin agar array bada ho, toh yeh approach inefficient ho jayega aur time zyada lagega. Phir maine socha ki kya hum is problem ko optimize kar sakte hain. Mujhe yaad aaya ki agar hum array ke dono ends se start karein, toh shayad hum kuch clever moves kar sakte hain. Toh maine Two-Pointer Technique ka idea apnaya. Is approach mein, hum do pointers use karte hain—ek array ke start par (left) aur dusra end par (right). Har step par, hum in dono pointers ke beech ka area calculate karte hain aur maximum area ko update karte hain. Fir, hum jis pointer ki height chhoti hai, usko move karte hain kyunki height kam hone se area limited hota hai, aur shayad aage chal kar zyada height mil sake.

#Logic: Logic simple hai—hum two pointers use karte hain: ek left end (l) aur ek right end (r) se start karte hain. Dono pointers ke beech jo minimum height hogi, woh area ke calculation ke liye important hoti hai, kyunki container ka paani us height tak hi fill hoga. Area ko calculate karte hain using the formula: (r - l) * min(height[l], height[r]). Fir agar left height chhoti hoti hai, toh hum left pointer ko aage badhate hain (l += 1), kyunki hume higher height chahiye to maximize area. Agar right height chhoti hoti hai, toh hum right pointer ko peeche le jaate hain (r -= 1). Yeh process tab tak repeat karte hain jab tak dono pointers mil na jaayein. This logic ensures ki hum saare potential areas efficiently explore karte hain without redundant calculations.