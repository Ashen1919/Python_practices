import PIL.Image as Img

input_img = "python_logo.png"
output_img = "compressed_loss_img.png"

try:
    img = Img.open(input_img)
    img.save(output_img, format='PNG', quality=10)
    img.show()

    print("Image compressed successful")
except Exception as e:
    print("An error occurred")