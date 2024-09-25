import requests

GF_Latin_All = "https://github.com/googlefonts/glyphsets/raw/main/GF_glyphsets/Latin/glyphs/CustomFilter_GF_Latin.plist"
dest = "sources/CustomFilter_GF_Latin_All.plist"

r = requests.get(GF_Latin_All)
with open(dest, "wb") as f:
    f.write(r.content)
