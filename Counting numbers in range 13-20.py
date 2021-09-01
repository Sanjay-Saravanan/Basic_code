a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
num_count = {}
for i in range(13, 20):
    count = a.count(i)
    num_count[i] = count

print(num_count)

count = num_count.values()
total_num = sum(count)
print(f'The total count of numbers is {total_num}')
