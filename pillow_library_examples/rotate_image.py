import PIL.Image as Img

angel = 90
img = Img.open("python_logo.png")
r_img = img.rotate(angel)
r_img.show()