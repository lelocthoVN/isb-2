from math import sqrt
from scipy.special import erfc
from scipy.special import gammaincc

bit = '11110001111000100101000111101011111011000110100010100101010100000001000011000000000111101011110010001100000101110110011100000011'

def frequency_bit() -> None:
    # вычисляем количество единиц и нулей в последовательности
    sum = 0
    for i in bit:
        if i == "1":
            sum += 1
        else:
            sum -= 1
    s = sum / sqrt(len(bit))
    # вычисляем значение статистики теprobability = erfc(SUM / sqrt(2))
    probability = erfc(s / sqrt(2))
    print(probability)
    if (probability < 0.01):
        print("Failed")
    else:
        print("Success")


def identical_bit() -> None:
    # вычисляем количество единиц и нулей в последовательности
    fre1 = bit.count('1') / 128
    runs = [bit[0]]
    for i in range(1, 128):
        if bit[i] != bit[i - 1]:
            runs.append(bit[i])
    num = len(runs)
    # вычисляем Вероятность
    probability_2 = erfc(abs(num - 2 * 128 * fre1 * (1 - fre1)) / (2 * sqrt(2 * 128) * fre1 * (1 - fre1)))
    print(probability_2)
    if (probability_2 < 0.01):
        print("Failed")
    else:
        print("Success")

def longest_sequence() -> None:
    mas_count = []
    for i in range(16):
        block = bit[i * 8: (i + 1) * 8]
        one = 0
        max_one_in_block = 0
        max_run = 0
        for bits in block:
            if bits == '1':
                one += 1
                max_one_in_block = max(max_one_in_block, one)
            else:
                one = 0
        max_run = max(max_run, max_one_in_block)
        mas_count.append(max_run)
    v1 = sum(x <= 1 for x in mas_count)
    v2 = sum(x == 2 for x in mas_count)
    v3 = sum(x == 3 for x in mas_count)
    v4 = sum(x > 4 for x in mas_count)
    k0 = 0.2148
    k1 = 0.3672
    k2 = 0.2305
    k3 = 0.1875
    X = ((v1-16*k0)**2)/(16*k0)+((v2-16*k1)**2)/(16*k1) + \
        ((v3-16*k2)**2)/(16*k2)+((v4-16*k3)**2)/(16*k3)
    probability_3 = gammaincc(3/2,X/2)
    print(probability_3)
    if (probability_3 < 0.01):
        print("Failed")
    else:
        print("Success")

if __name__ == "__main__":
    frequency_bit()
    identical_bit()
    longest_sequence()