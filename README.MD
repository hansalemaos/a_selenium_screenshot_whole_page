# Takes a screenshot from a whole page (same size as page / no repeating parts)

```python
# Tested with:
# https://github.com/ultrafunkamsterdam/undetected-chromedriver
# Python 3.9.13
# Windows 10


$pip install a-selenium-screenshot-whole-page

from auto_download_undetected_chromedriver import download_undetected_chromedriver
import undetected_chromedriver as uc
from a_selenium_screenshot_whole_page import get_screenshot_whole_page_with_scroll
from time import sleep

if __name__ == "__main__":
    folderchromedriver = "f:\\seleniumdriver2"
    path = download_undetected_chromedriver(
        folder_path_for_exe=folderchromedriver, undetected=True
    )
    driver = uc.Chrome(driver_executable_path=path)
    driver.get(
        r"https://github.com/hansalemaos/a_cv2_easy_resize"
    )
    sleep(2)
    get_screenshot_whole_page_with_scroll(driver,sleepinterval=(0.2,0.8), save_path='f:\\testwholescreenshot.png')
    
    
```

<img src="https://github.com/hansalemaos/screenshots/raw/main/testwholescreenshot.png"/>



