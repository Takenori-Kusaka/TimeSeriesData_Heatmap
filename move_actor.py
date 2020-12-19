import pandas as pd
import cv2
import glob

def concat_image(base: str, add: str, top: int, left: int):
    base_img = cv2.imread(base)
    add_img = cv2.imread(add)
    req_top = top
    req_left = left

    b_h, b_w = base_img.shape[:2]
    a_h, a_w = add_img.shape[:2]

    if req_top > b_h:
        req_top = b_h
    if req_left > b_w:
        req_left = b_w

    if (a_h + req_top) <= b_h and (a_w + req_left) <= b_w:
        base_img[req_top:a_h + req_top, req_left:a_w + req_left] = add_img
    elif (a_h + req_top) > b_h and (a_w + req_left) > b_w:
        base_img[b_h - a_h - 1:b_h, b_w - a_w - 1:a_w] = add_img
    elif (a_h + req_top) > b_h and (a_w + req_left) <= b_w:
        base_img[b_h - a_h - 1:b_h, req_left:a_w + req_left] = add_img
    else:
        base_img[req_top:a_h + req_top, b_w - a_w - 1:a_w] = add_img

    return base_img

df = pd.read_csv('map_log.csv', index_col=0, parse_dates=[0]).resample('20ms').mean().interpolate(method="linear")
img_array = []

i = 0
for index, row in df.iterrows():
    img = concat_image('map_google_embed.png', 'upper_body-2.png', int(row['x']), int(row['y']))
    height, width, layers = img.shape
    size = (width, height)
    cv2.imwrite('./img/img{:0>8}.png'.format(i), img)
    #img_array.append(img)
    i = i + 1