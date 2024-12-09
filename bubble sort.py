data = [6, 5, 3, 1, 8, 7, 2, 4]
print("Array sebelum diurutkan:", data)

# Proses merge sort
if len(data) > 1:
    # Membagi array menjadi dua bagian
    mid = len(data) // 2
    left_half = data[:mid]
    right_half = data[mid:]

    # Sort bagian kiri
    if len(left_half) > 1:
        mid_left = len(left_half) // 2
        left_left = left_half[:mid_left]
        left_right = left_half[mid_left:]

        # Mengurutkan bagian kiri
        left_left.sort()
        left_right.sort()

        # Menggabungkan bagian kiri
        sorted_left = []
        i = j = 0
        while i < len(left_left) and j < len(left_right):
            if left_left[i] < left_right[j]:
                sorted_left.append(left_left[i])
                i += 1
            else:
                sorted_left.append(left_right[j])
                j += 1
        sorted_left.extend(left_left[i:])
        sorted_left.extend(left_right[j:])
        left_half = sorted_left

    # Sort bagian kanan
    if len(right_half) > 1:
        mid_right = len(right_half) // 2
        right_left = right_half[:mid_right]
        right_right = right_half[mid_right:]

        # Mengurutkan bagian kanan
        right_left.sort()
        right_right.sort()

        # Menggabungkan bagian kanan
        sorted_right = []
        i = j = 0
        while i < len(right_left) and j < len(right_right):
            if right_left[i] < right_right[j]:
                sorted_right.append(right_left[i])
                i += 1
            else:
                sorted_right.append(right_right[j])
                j += 1
        sorted_right.extend(right_left[i:])
        sorted_right.extend(right_right[j:])
        right_half = sorted_right

    # Menggabungkan bagian kiri dan kanan
    result = []
    i = j = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            result.append(left_half[i])
            i += 1
        else:
            result.append(right_half[j])
            j += 1
    result.extend(left_half[i:])
    result.extend(right_half[j:])
    data = result

print("Array setelah diurutkan:", data)
