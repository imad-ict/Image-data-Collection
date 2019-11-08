
imshape = (256, 256, 3)
mode = 'multi'

hues = {'star': 30,
        'square': 0,
        'circle': 90,
        'triangle': 60}

labels = sorted(hues.keys())

if mode == 'binary':
    n_classes = 1

elif mode == 'multi':
    n_classes = len(labels) + 1

assert imshape[0]%32 == 0 and imshape[1]%32 == 0,\
    "imshape should be multiples of 32. comment out to test different imshapes."
