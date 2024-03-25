def read_numbers(file):
    with open(file, 'r') as f:
        numbers = [int(line.strip()) for line in f]
    return numbers

def sum_with_commas(n):
    return format(n, ',d')

# Read input
numbers = read_numbers('input.txt')

# Kalkulasi
sum = 0
for n in numbers:
    sum += n

# Print hasil
print(f"Total penjumlahan di input.txt: {sum_with_commas(sum)}")