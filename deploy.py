#!/usr/bin/env python3

import os
import dropbox

token = os.environ['DROPBOX_ACCESS_TOKEN']
dbx = dropbox.Dropbox(token)

file_name = os.environ['PDF_FILE_NAME']
with open(file_name, 'rb') as f:
    data = f.read()
dbx.files_upload(data, '/{}'.format(file_name), mode=dropbox.files.WriteMode('overwrite'))

print('PDF file {} uploaded to Dropbox'.format(file_name))
