from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys

#APIキーの情報
key = "4757626a5e32e1f3fb093c75238fa92f"
secret = "0b3e4b30d52bf43f"
wait_time = 1

#保存フォルダの指定
foodname = sys.argv[1]
savedir = "./" + foodname

flickr = FlickrAPI(key, secret, format="parsed-json")
result = flickr.photos.search(
    text = foodname,
    per_page = 400,
    media = "photos",
    sort = "relevance",
    safe_search = 1,
    extras = "url_q, licence"
)

photos = result["photos"]
#返り値を表示する
#pprint(photos)

for i, photo in enumerate(photos["photo"]):
    url_q = photo["url_q"]
    filepath = savedir + "/" + photo["id"] + ".jpg"
    if os.path.exists(filepath): continue
    urlretrieve(url_q, filepath)
    time.sleep(wait_time)
