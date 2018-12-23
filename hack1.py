import random
import re
import sys

def sockMerchant(n, ar):
    from collections import Counter
    socks_dict= Counter(ar)
    socks = list(socks_dict.keys())
    count = 0

    for pair in socks:
        if (socks_dict[pair] < 2):
            continue
        if (socks_dict[pair] % 2 == 0):
            count = count + int(socks_dict[pair]/2)
        else:
            count = count + (int(socks_dict[pair] - 1))/2
    return (int(count))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()