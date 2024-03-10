#leetcode 11
#container with most water
height = [1,8,6,2,5,4,8,3,7]
left = 0
right = len(height)-1
maxvolume = 0
while left < right:
    distance = right - left
    working_height = min(height[left], height[right])
    workingvolume = distance * working_height
    if workingvolume > maxvolume:
        maxvolume = workingvolume
    if height[left] <= height[right]:
        left += 1
    else: 
        right -=1
    

print(maxvolume)
