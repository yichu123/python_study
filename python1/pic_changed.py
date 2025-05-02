from PIL import Image
#im = Image.open('D:\\pic\\2025-01-29-12-36-14-1152x646.png')

image = Image.open(r"D:\\pic\\2025-01-29-12-36-14-1152x646.png") 
image.load() 
r, g, b, a = image.split() 
  
# merge funstion used 
im1 = Image.merge( 'RGB', (r, g, b)) 
im1.show()
