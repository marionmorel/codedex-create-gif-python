import imageio.v3 as iio

filenames = ['team-pic1.png', 'team-pic2.png']
images = [ ]

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('team.gif', images, duration = 500, loop = 0)

filenames2 = ['dino1.png', 'dino2.png', 'dino3.png', 'dino4.png']
images2 = [ ]

for filename in filenames2:
    images2.append(iio.imread(filename))

iio.imwrite('dino.gif', images2, duration = 200, loop = 0)