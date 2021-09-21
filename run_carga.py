from download import DownloadFiles
from storage.bucket import Storage

cloud_storage = Storage()

## download and send to storage
download = DownloadFiles()
download.start_download()


