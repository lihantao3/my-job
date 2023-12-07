from PIL import Image


image = Image.open('D:\download\pics\phone_11.jpg')
image.format, image.size, image.mode
('JPEG', (500, 750), 'RGB')
image.show()
