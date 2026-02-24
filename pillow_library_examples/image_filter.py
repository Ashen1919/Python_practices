import PIL.Image as Img
import PIL.ImageFilter as IFill

img = Img.open("python_logo.png")
blurred_img = img.filter(IFill.BLUR)
blurred_img.save("blurred_img.png")
blurred_img.show()