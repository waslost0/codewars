def dig_pow(n, p):
    sum = 0
    for i, num in enumerate(str(n)):
        sum += pow(int(num), p+i)

    return sum/n if (sum/n)%1==0 else -1