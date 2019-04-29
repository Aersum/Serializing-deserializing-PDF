import json
from pprint import pprint
from base64 import b64encode, b64decode
with open('label.pdf', 'rb') as label_file:
    content = label_file.read()
attach_obj = {'type': 'pdf', 'name': 'return', 'content': content}
json_obj = json.dumps({k: b64encode(v) for k, v in attach_obj.items()})
# ********************
# Dumping successful now try to load and write file
b64_dict = json.loads(json_obj)
label = {k: b64decode(v) for k, v in b64_dict.items()}
print 'File type: {}'.format(label['type'])
print 'File name: {}'.format(label['name'])
print 'label content type: {}'.format(type(label['content']))
pprint(label['content'])
# Writing output file
with open(label['name']+'.pdf', 'wb') as file:
    file.write(label['content'])
print '___'*10
