from PIL import Image, ImageFilter
import blend_modes
import numpy
import os
from math import ceil
import rembg


def responsive_font(text, max_size):
  if '\n' in text:
    text = text.split('\n')
    text = text[0] if len(text[0]) > len(text[1]) else text[1]

  length = len(text)
  # function to generate font size from length
  font_size = (0.0177286 * (length ** 2)) - (1.73234 * length) + 53.1347

  # if generated font size is more than our preferred max size
  if font_size > max_size:
    return max_size
  else:
    return ceil(font_size)



# finding dominant color to apply suitable blend mode in mockup function
def get_dominant_color(pil_img):
    img = pil_img.copy()
    img = img.convert("RGBA")
    img = img.resize((1, 1), resample=0)
    dominant_color = img.getpixel((0, 0))
    return dominant_color

def mockup(name, logofile, details, remove_bg):
  
  # design uploaded by the user 
  logo = Image.open(logofile)
  logo = logo.convert("RGBA")
  if remove_bg:
    logo = rembg.remove(logo)
  logo = logo.filter(ImageFilter.GaussianBlur(radius=0.5))

  # base image
  background_img_raw = Image.open(os.path.join("clipmock/static/subjects/"+name+".png"))
  background_img_raw = background_img_raw.convert("RGBA")
  background_img = numpy.array(background_img_raw)
  background_img_float = background_img.astype(float) 

  color = get_dominant_color(background_img_raw)
  color = int((color[0] + color[1] + color[2]) / 3)

  logo_size = details[0]
  # resizing design to fit inside a square of side logo_size
  if logo.width > logo.height:
    logo = logo.resize((logo_size, ceil((logo_size / logo.width) * logo.height)))
  else:
    logo = logo.resize((ceil((logo_size / logo.height) * logo.width), logo_size))
  foreground_img_raw = Image.new("RGBA", background_img_raw.size, (0, 0, 0, 0))
  foreground_img_raw.paste(logo, details[1], mask=logo)
  foreground_img = numpy.array(foreground_img_raw)
  foreground_img_float = foreground_img.astype(float) 

  opacity = 1
  if color > 100:
    blended_img_float = blend_modes.multiply(background_img_float, foreground_img_float, opacity) # for white
  else:
    blended_img_float = blend_modes.grain_merge(background_img_float, foreground_img_float, opacity) # for black

  overlay = Image.open(os.path.join(os.getcwd(), "clipmock/static/backgrounds/"+name+".png"))
  blended_img = numpy.uint8(blended_img_float)  
  blended_img_raw = Image.fromarray(blended_img) 
  blended_img_raw.paste(overlay, (0, 0), mask=overlay)
  blended_img_raw.save(os.path.join(os.getcwd(), "clipmock/static/after/"+name+".png"))