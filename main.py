import subprocess
import re
import pymp
import numpy as np
from parameters import MANGAS

# Catch html of page
url = "http://www.mangapanda.com/{}/{}/{}"

def get_url_img(thread):
    a_tag = subprocess.run(["grep", str('id="img".*'), "file_{}.html".format(thread)], capture_output = True)
    x = a_tag.stdout.decode("utf-8")
    return re.search('https.*jpg', x).group(0)

def get_file_name(manga, cap, pag):
    return "downloads/{}/{}/{}.jpg".format(manga, str(cap).zfill(3), str(pag).zfill(3))

subprocess.run(["mkdir", "downloads"])

for manga_tuple in MANGAS:
    manga = manga_tuple[0]
    subprocess.run(["mkdir", "downloads/{}".format(manga)])
    with pymp.Parallel(NUM_THREAD) as p:
        for cap in p.xrange(manga_tuple[1], manga_tuple[2]):
            a_tag = subprocess.run(["mkdir", "downloads/{}/{}".format(manga, str(cap).zfill(3))])
            for pag in range(1,200):
                url_pag = url.format(manga, cap, pag)
                result = subprocess.run(["wget", url_pag, "-O", "file_{}.html".format(cap)], capture_output = True)
                if result.returncode:
                    break
                url_img = get_url_img(cap)
                file_name = get_file_name(manga, cap, pag)
                subprocess.run(["wget", url_img, "-O", file_name])
            subprocess.run(["rm", "file_{}.html".format(cap)])

