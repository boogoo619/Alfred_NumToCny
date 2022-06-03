import NumToCny
import json
import sys

transNum = sys.argv[1]

def parse(strs):
    res = { "title": strs, "subtitle": "Copy to clipboard","arg": strs, "icon": "icon.png" }
    return { "items": [res] }

ret = NumToCny.to_rmb_upper(transNum)

response = (json.dumps(parse(ret)))

sys.stdout.write(response)
