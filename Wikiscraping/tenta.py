def search(x,nums):
    return recBinSearch(x, nums, 0, len(nums)-1)

def linear_search(x,nums):
    for i in range(len(nums)):
        if nums[i] == x:
            return i
    return -1

def binary_search(x,nums):
    nums.sort()
    low = 0
    high = (len(nums)) - 1
    while low <= high:
        mid = (low+high)//2
        print(mid)
        item = nums[mid]
        print("detta är item", item)
        if x == item:
            return mid
        elif x < item:
            high = mid - 1
            print("hej jag är här")
        else:
            low = mid + 1
    return -1

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

def reverse(s):
    if s == "":
        print(s, "nu är s tom")
        return s
    else:
        print(s)
        x = reverse(s[1:]) + s[0]
        print(x)
        return x

def anagrams(s):
    if s == "":
        return [s]
    else:
        ans = []
        for w in anagrams(s[1:]):
            print(w)
            for pos in range(len(w)+1):
                ans.append(w[:pos]+s[0]+w[pos:])
            return ans


def recPower(a,n): # raises a to the int power n
    if n == 0:
        return 1
    else:
        print(n//2, " detta är n//2")
        factor = recPower(a, n//2)
        print(factor, "detta är faktorn wiho")
        if n%2 == 0: # n is even
            print("i iffen",factor,factor)
            return factor * factor
            
        else:
            print(factor, "nu ör factir")
            print("nu är jag i elsen", factor * factor * a)
            return factor * factor * a

def recBinSearch(x,nums,low,high):
    if low > high:
        return -1
    mid = (low + high //2)
    item = nums[mid]
    if item == x:
        return mid
    elif x < item:
        return recBinSearch(x,nums,low,mid-1)
    else:
        return recBinSearch(x,nums,mid+1,high)




def fib(n):
    if n == 3:
        print("Computing fib(",n)
    if n < 3:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    


def isPalindrome(s):
    if len(s) == 0:
        return s
    else:
        return isPalindrome(s[1:])+s[0]
    

def checkPalindrome(result,s):
    if result[0] ==  s[0] and  result[-1] ==  s[-1]:
        print("You have a palindrome")
        print(result, "and", s)
    else:
        print("Not a palindrome")


def maximum(nums):
    print(nums)
    if len(nums) == 1:
        return nums[0]
    else:
        return max(nums[0],maximum(nums[1:]))
    

fib_cache = {}
def fib(x):
    if x < 2:
        return 1
    else:
        return fib(x-1) + fib(x-2)


def fact(n):
    return n < 2 or n*fact(n-1)


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2 #identify the middle of the list
        L = arr[:mid] #lower part of list
        R = arr[mid:] # hoigher part of list

        merge_sort(L)

        merge_sort(R) # Vi bryter ner siffrorna till lägsta nivå. ( Separerar allt)
        print(L, "hej!")
        

        # i = j = k = 0

        
        # while i < len(L) and j < len(R): 
        #     if L[i] < R[j]:
        #         arr[k] = L[i]
        #         i += 1
        #     else:
        #         arr[k] = R[j]
        #         j += 1
        #     k += 1
  
        # # Checks if any elemens left
        # while i < len(L):
        #     arr[k] = L[i]
        #     i += 1
        #     k += 1
        # while j < len(R):
        #     arr[k] = R[j]
        #     j += 1
        #     k += 1

def fib_2(x):
    if x < 2:
        return 1
    else:
        result = fib_2(x-1) + fib_2(x-2)
        return result
 

def summa(arr):
    if len(arr) > 1:
        print(arr,"ghe")
        return arr.pop(0)+ summa(arr)
    else:
        return arr[0] 

def main():
    arr = [3,2,1,4]
    print(arr)
    merge_sort(arr)
    print(arr)

main()