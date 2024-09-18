fav_num = {
    'chloe': [5, 4, 2, 5 ,1],
    'mike': [2, 6, 1, 7, 5, 1],
    'joe': [3, 6, 1, 5, 78, 1],
    'tem': [23, 6, 12, 2, 55, 1],
    'golan': [11, 5, 77, 3, 21],
    }


for name, nums in fav_num.items():
    print(f"\n{name.title()}'s favourite numbers are: ")
    for num in nums:
        if num == nums[-1]:
            print(f"and their final number is: {num}")
        else:
            print(f"{num}")





"""for key, val in fav_num.items():
    print(f"{key.title()}'s favourite number is {val}")"""