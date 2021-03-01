from PIL import Image, ImageDraw

w, h = 600, 400

img = Image.new('RGB', (w, h), (241, 241, 241))


korea = Image.New('RGB', (h // 2, h // 2), color = (241, 241, 241))

draw = ImageDraw.Draw(korea)

draw.pieslice((0,0, h // 2, h // 2 ), start = 180, end = 360, fill = (205, 49, 58))

draw.pieslice((0,0, h // 2, h // 2 ), start = 0, end = 180, fill = (0, 71, 160))

draw.eclipse((0, h // 8, h // 4 , h * 3 // 8), fill = (205, 49, 58))

draw.pieslice((h // 4, h // 8, h // 2, h * 3 // 8 ), fill = (205, 49, 58))

korea = korea.rotate(-33.69, fillcolor = (241, 241, 241))

img.paste(korea, (h // 2, h // 4))

sky = Image.New('RGB', (h // 4, h // 6), color = (14, 14, 14))

draw = ImageDraw.Draw(sky)

draw.rectangle((0, h * 2 // 48, h // 4, h * 3 // 48 ), fill = (241, 241, 241))

draw.rectangle((0, h * 5 // 48, h // 4, h * 6 // 48 ), fill = (241, 241, 241))

sky = sky.rotate(90 - 33.69, expand = True, fillcolor = (241, 241, 241))

img.paste(sky, (h * 22 // 96, h * 9 // 96))

earth = Image.new('RGB', (h // 4, h // 6), color = (14, 14, 14))

draw = ImageDraw.Draw(earth)

draw.rectangle((0, h * 2 // 48, h // 4, h * 3 // 48 ), fill = (241, 241, 241))

draw.rectangle((0, h * 5 // 48, h // 4, h * 6 // 48 ), fill = (241, 241, 241))

draw.rectangle((h * 11 // 96, 0, h * 13 // 96, h * 2 // 48), fill = (241, 241, 241))

draw.rectangle((h * 11 // 96, h * 3 // 48, h * 13 // 96, h * 5 // 48), fill = (241, 241, 241))

draw.rectangle((h * 11 // 96, h * 6 // 48, h * 13 // 96, h * 8 // 48), fill = (241, 241, 241))

earth = earth.rotate(90 - 33.69, expand = True, fillcolor=(241, 241, 241))

img.paste(earth, (h * 96 // 96, h * 59 // 96))

water = Image.new('RGB', (h // 4, h // 6), color = (14, 14, 14))

draw = ImageDraw.Draw(water)

draw.rectangle((0, h * 2 // 48, h // 4, h * 3 // 48 ), fill = (241, 241, 241))

draw.rectangle((0, h * 5 // 48, h // 4, h * 6 // 48 ), fill = (241, 241, 241))

draw.rectangle((h * 11 // 96, 0, h * 13 // 96, h * 2 // 48), fill = (241, 241, 241))

draw.rectangle((h * 11 // 96, h * 6 // 48, h * 13 // 96, h * 8 // 48), fill = (241, 241, 241))

water = water.rotate(90 + 33.69, expand = True, fillcolor=(241, 241, 241))

img.paste(water, (h * 96 // 96, h * 9 // 96))


fire = Image.new('RGB', (h // 4, h // 6), color = (14, 14, 14))

draw = ImageDraw.Draw(fire)

draw.rectangle((0, h * 2 // 48, h // 4, h * 3 // 48 ), fill = (241, 241, 241))

draw.rectangle((0, h * 5 // 48, h // 4, h * 6 // 48 ), fill = (241, 241, 241))

draw.rectangle((h * 11 // 96, h * 3 // 48, h * 13 // 96, h * 5 // 48), fill = (241, 241, 241))

fire = fire.rotate(90 + 33.69, expand = True, fillcolor=(241, 241, 241))

img.paste(fire, (h * 22 // 96, h * 59 // 96))

img.show()
