import base64
from random import uniform
from time import sleep

import numpy as np
import cv2
import pandas as pd
from a_cv_imwrite_imread_plus import open_image_in_cv,save_cv_image
from a_cv2_easy_resize import add_easy_resize_to_cv2
from a_cv_imwrite_imread_plus import add_imwrite_plus_imread_plus_to_cv2
add_imwrite_plus_imread_plus_to_cv2()
add_easy_resize_to_cv2()

def base64toimg(x):
    try:
        return cv2.imdecode(
            np.frombuffer(base64.b64decode(x.split(",", maxsplit=1)[-1]), np.uint8),
            cv2.IMREAD_COLOR,
        )
    except Exception:
        return pd.NA

def get_screenshot_whole_page_with_scroll(driver, sleepinterval=(0.2, 0.7), save_path=None):

    docuwidth = driver.execute_script("return document.documentElement.scrollWidth")
    docuheight = driver.execute_script("return document.documentElement.scrollHeight")
    screenshotforsize = base64toimg(driver.get_screenshot_as_base64())
    screenheight = screenshotforsize.shape[0]
    executeloops, restpixel = divmod(docuheight, screenheight)
    cutfromlastimage = screenheight - restpixel
    allscreenshots = []
    for _ in range(executeloops + 1):
        driver.execute_script(f"window.scrollTo(0, {int(screenheight) * _});")
        sleep(uniform(sleepinterval[0], sleepinterval[1]))
        allscreenshots.append(base64toimg(driver.get_screenshot_as_base64()).copy())
    validimages = allscreenshots[: executeloops + 1].copy()
    validimages[-1] = validimages[-1][cutfromlastimage:].copy()
    joined = np.vstack(validimages)
    joined = joined[:, 0:docuwidth]
    pic5 = cv2.easy_resize_image(open_image_in_cv(joined,channels_in_output=3,bgr_to_rgb=False), width=docuwidth, height=docuheight, percent=None, interpolation=cv2.INTER_AREA)
    if save_path is not None:
        save_cv_image(save_path,pic5)
    return pic5

