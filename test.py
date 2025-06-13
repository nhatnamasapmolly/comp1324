def canMakeEqual(nums,k) :
        b = 1
        a = 0
        count = 0
        while b < len(nums):
            if nums[a] != nums[b]:
                count += 1
            b += 1
            a += 1
        print(count)
        
        return count <= 2 * k
            
        


print(canMakeEqual([-1,-1,-1,1,1,1], 5))