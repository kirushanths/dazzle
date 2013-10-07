from boto import connect_s3
from boto.s3.key import Key  

from dazzle.libs.utils import constants as Constants
from dazzle.libs.model.result import Result

def s3_upload (folder_name, file_names, file_contents):
    if not folder_name:
        raise ValueError('folder not provided')
        
    if not file_names:
        raise ValueError('No files provided')

    if not file_contents:
        raise ValueError('No files provided')

    if len(file_names) != len(file_contents):
        raise AssertionError('Given names are not one-for-one with content')

    conn = connect_s3(Constants.S3_ACCESS_KEY, Constants.S3_SECRET_KEY)
    bucket = conn.get_bucket(Constants.S3_BUCKET)
    k = Key(bucket)

    if not k:
        return Result(success=False, message='S3 connection error')

    files = zip(file_names, file_contents)

    for name, content in files:
        k.key = Constants.S3_TEMPLATE_FOLDER + '/' + folder_name + '/' + name
        k.set_contents_from_string(content, replace=True) 
        k.make_public()

    return Result(success=True)