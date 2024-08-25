def containsDuplicate(nums):

    hash_set = set()

    for i in nums:
        if i in hash_set:
            return True
        hash_set.add(i)

    return False

print(containsDuplicate([1,2,3]))