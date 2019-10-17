
'''
DOWNLOAD EVERY BOB ROSS PAINTING
Jeff Thompson | 2017 | jeffreythompson.org

Downloads all 411 paintings by Bob Ross from the
site Two Inch Brush.

xdmds: Modified to work in python3
'''

import os
import urllib.request

num_images = 411
output_dir = '../data'

for i in range(1, num_images):
    try:
        print('downloading painting ' + str(i) + '/' + str(num_images) + '...')
        filename = str(i) + '.png'
        url = 'http://www.twoinchbrush.com/images/painting' + filename
        urllib.request.urlretrieve(url, os.path.join(output_dir, filename))
    except Exception as e:
        print(e)
