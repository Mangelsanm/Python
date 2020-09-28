def duplicado(nums):
    tortoise = nums[0]
    hare = nums[0]

    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        print(tortoise)
        print(hare)
        if tortoise == hare:
            break

duplicado([3, 0, 2, 1, 1])