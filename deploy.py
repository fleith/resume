#!/usr/bin/env python3

import os
import dropbox

token = os.environ['DROPBOX_ACCESS_TOKEN']
dbx = dropbox.Dropbox(token)

#TODO: get file name from arguments or environment
with open('resume.pdf', 'rb') as f:
    data = f.read()
dbx.files_upload(data, '/resume.pdf', mode=dropbox.files.WriteMode('overwrite'))

print('nice deploy')
