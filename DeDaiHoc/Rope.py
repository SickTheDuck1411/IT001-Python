def calculateRectange(rope):
    halfRope= int(rope/2)
    maxArea=0
    xmax=0
    ymax=0
    for i in range(0,int(halfRope/2)+1):
        area = i*(50-i)
        if maxArea< area:
            maxArea= area
            xmax= i
            ymax= halfRope-i
    return [xmax, ymax, maxArea]



xmax, ymax,maxArea =  calculateRectange(100)  
print(xmax, ymax, maxArea)