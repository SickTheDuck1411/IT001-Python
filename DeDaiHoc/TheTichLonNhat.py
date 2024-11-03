def findMaxVolume(x,y):
    MaxVolume=0 
    height = 0
    rangeHeight = min(int(x/2)+1, int(y/2)+1)
    for i in range(1,rangeHeight):
        volume = (x - 2*i)*(y- 2*i)*i
        if volume > MaxVolume:
            MaxVolume = volume
            height = i 
    return [height, x-2*height, y-2*height, MaxVolume]


x = int(input("Enter your rectangle width:"))
y  = int(input("Enter your rectangle length:"))
h,w,l, maxVolume= findMaxVolume(x,y) 
print(maxVolume, h, w, l)



