sorting = [1, 4, 6, 8, 7, 3, 5, 2]

print("Data sebelum diurutkan: ", sorting)
banyak_data = len(sorting)
print("Banyak data: ",banyak_data)

for i in range(banyak_data-1):
    for j in  range(banyak_data-1):
        if sorting[j] > sorting[j+1]:
            temp = sorting[j]
            sorting[j] = sorting[j+1]
            sorting[j+1] = temp
print("Data setelah diurutkan: ", sorting)
