from PIL import Image
from PIL import ImageFilter

cloud_image = Image.open("cloud.jpg")
desperate_img = Image.open("desperate.jpg")

print('cloud size:', cloud_image.size)
print('desperate size:', desperate_img.size)

print('cloud format:', cloud_image.format)
print('desperate format', desperate_img.format)

# Creates a temporary file and then open the file with the pcs default program
#cloud_image.show()


#Cropping an image
"""
area = (100, 100, 375, 200)
cropped_image = cloud_image.crop(area)
cropped_image.show()
"""

#Pasting image into another
"""
To paste it, the image size must exactly match, otherwise it gives and error
area = (100, 100, 900+100, 440+100)
desperate_img.paste(cloud_image, area)
desperate_img.show()
"""


#Getting individual channels
"""
#split method, split the images channels into it's individual bands(ex: in mode RGB: split it into r, g and b) as a tuple
print('cloud mode:', desperate_img.mode)
r, g, b = desperate_img.split()
r.show()
"""

#Merge
"""
r1, g1, b1 = desperate_img.split()
#Merge method also doesn't work if the sizes doesn't match
newImage = Image.merge("RGB", (r1, g1, b1))
#newImage.show()
newImage = Image.merge("RGB", (b1, r1, g1))
#newImage.show

new_desperate = desperate_img.crop((200, 200, 900+200, 440+200))
r2, g2, b2 = new_desperate.split()
r3, g3, b3 = cloud_image.split()
newImage2 = Image.merge("RGB", (r3, g2, b3))
newImage2.show()
"""

#Transposing
"""
ocean_img = Image.open("ocean.png")

print('ocean size:', ocean_img.size)

resized_ocean = ocean_img.resize((640, 480), None)
transposed_ocean = ocean_img.transpose(Image.FLIP_LEFT_RIGHT)
rotated_ocean = ocean_img.transpose(Image.ROTATE_90)
#resized_ocean.show()
#transposed_ocean.show()
#rotated_ocean.show()
"""

blur = desperate_img.filter(ImageFilter.BLUR)
#blur.show()
detail = desperate_img.filter(ImageFilter.DETAIL)
#detail.show()
edges = desperate_img.filter(ImageFilter.FIND_EDGES)
#edges.show()



