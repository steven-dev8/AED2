def multi_manual():
    while True:
        a = input("X: ").strip()
        b = input("Y: ").strip()

        try:
            int(a)
            int(b)
            break
        except (ValueError):
            print("Invalid input! Only int number!")
            continue

    result_final = 0
    shift_b = 1
    for i in a[::-1]:
        i = int(i)

        shift_a = 1
        result = 0

        for j in b[::-1]:
            j = int(j)

            result += (i * j) * shift_a
            shift_a *= 10

        result_final += result * shift_b
        shift_b *= 10

    return result_final

print(multi_manual())
