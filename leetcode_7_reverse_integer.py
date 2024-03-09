
#leetcode number 7: reverse integer 
# "Given a signed 32-bit integer x, 
# return x with its digits reversed. If reversing x 
# causes the value to go outside the signed 32-bit 
# integer range [-231, 231 - 1], then return 0."
x = 123
negative = None
new_num = ""
answer = ""
if x < 0:
    x = x * -1
    negative = True 
        
y = str(x)
for i in range(len(y)-1, -1, -1):
    new_num += y[i]
new_num = int(new_num)
if new_num > -2**31:
    if new_num < 2**31:
        if negative:
            answer = 0 - new_num
            print(answer)
        else:
            answer = new_num
            print(answer)
    else:
        print(0)
else:
    print(0)
