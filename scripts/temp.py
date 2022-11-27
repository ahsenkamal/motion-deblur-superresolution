from PIL import Image, ImageDraw
im = Image.new('RGBA', (512, 512), (0, 0, 0, 255)) 
draw = ImageDraw.Draw(im) 
draw.line((256,256, 256,300), fill=(255, 255, 255, 255), width=1)
im.save('h.png')