def dec2bin(N):
    if N == 0:
        return ""
    return dec2bin(N//2)+str(N%2)

print(dec2bin(10))
