import PIL.Image as Img

size = (128, 128)
img = Img.open("python_logo.png")
re_img = img.resize(size)
re_img.show()