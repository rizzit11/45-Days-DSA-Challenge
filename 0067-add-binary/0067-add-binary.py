class Solution:
    def addBinary(self, a: str, b: str) -> str:

        a_int = int(a, 2)
        b_int = int(b, 2)
        
        total = a_int + b_int
        
        return bin(total)[2:]

# Approach: Initially, maine socha ki dono binary strings ko manually add karne ke liye ek loop likhu, jisme carry bhi handle karun, lekin mujhe laga ki Python ka int() function zyada efficient rahega. Maine dono strings ko binary se integer mein convert kiya, unhe add kiya, aur phir result ko wapis binary string mein convert kiya. Isse mujhe carry operations ya manual addition logic ke baare mein tension lene ki zaroorat nahi rahi.

# Logic: Dono binary strings ko integer form mein convert karte hain using int(a, 2) and int(b, 2). Yeh function base-2 (binary) ko base-10 (integer) mein convert karta hai. Fir in integers ko add kar ke humara total aata hai. Uske baad, hum bin(total)[2:] use karke result ko wapas binary string mein convert karte hain, jaha [2:] prefix ko remove karne ke liye hai. Is tarah humara final binary sum mil jata hai bina manually bitwise operations likhne ke.