import imageio.v3 as iio

img_filenames = ["freak2017x_1.jpg", "freak2017x_2.jpg"]
img_data = [ ]

for file in img_filenames:
    img_data.append(iio.imread(file))

iio.imwrite("2017x.gif", img_data, duration = 500, loop = 0)