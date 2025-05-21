def majority_element(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    for num, cnt in count.items():
        if cnt > len(nums) // 2:
            return num
    return None

# Пример использования
nums = [3, 2, 3]
print(majority_element(nums))  # Вывод: 3
