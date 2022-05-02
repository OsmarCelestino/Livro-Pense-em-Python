def ack(m,n):
    if m == 0:
        result = n = n+1
    if m > 0 and n == 0:
        result = ack(m - 1,1)
    if m > 0 and n > 0:
       result = ack(m-1,ack(m,n-1))
    return result
x = ack(3,4)
print(x)