x = input()
y = input()
m = input()
sum = (x)/(m)

if sum == 0:
    sum = sum + 0.50
while(sum > 0):
    y = y - sum
    print(y)
