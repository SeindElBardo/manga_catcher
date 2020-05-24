# manga_catcher
A litle script of python for download images from web sites. Concretly, for download pages of manga in mangapanda.com

## How to install

`
$> pip install -r ../requirements.txt
`

## How to use
In `parameters.py` write the name of manga that you want to collect, the start chapter and the end chapter in a tuple in the list` MANGAS`. The name must be the same name that appears in url web.

### Example
I want to collect the manga "Tate No Yuusha No Nariagari" from chapter 1 to chapter 10. The url in * mangapanda * is `http://www.mangapanda.com/tate-no-yuusha-no-nariagari/1/ 1`
My parameters file it would see like:

`
SLEEVES = [
    ("tate-no-yuusha-no-nariagari", 1, 10)
    ]
`
* Remember add comma if you add more of one manga *

Save file and execute `main.py`

`
$> python main.py
`