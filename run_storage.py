from download import DownloadFiles
from mycloud.bucket import MyStorage

cloud_storage = MyStorage()

## download and send to storage
download = DownloadFiles()
download.start_download()