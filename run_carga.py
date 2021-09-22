from download import DownloadFiles
from cloud.bucket import MyStorage

cloud_storage = MyStorage()

## download and send to storage
download = DownloadFiles()
download.start_download()