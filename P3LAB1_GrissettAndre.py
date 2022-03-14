red = int(input())
green = int(input())
blue = int(input())

min_list = (red, green, blue)
grey_val = min(min_list) 

if (red >= grey_val):
    red = red - grey_val

if (green >= grey_val):
    green = green - grey_val

if (blue >= grey_val):
    blue = blue - grey_val
   
print(str(red), str(green), str(blue))