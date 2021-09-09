installation: pip install yadisk or pip3 install yadisk

# create new app: 
https://oauth.yandex.ru/
# get token: 
https://oauth.yandex.ru/authorize?response_type=token&client_id=YOUR_ID
# * * * * * * *  commands:  * * * * * * *   # 


import yadisk

y = yadisk.YaDisk(token="<token>")
# or
# y = yadisk.YaDisk("<application-id>", "<application-secret>", "<token>")

# Check if the token is valid
print(y.check_token())

# Get disk information
print(y.get_disk_info())

# Print files and directories at "/some/path"
print(list(y.listdir("/some/path")))

# Upload "file_to_upload.txt" to "/destination.txt"
y.upload("file_to_upload.txt", "/destination.txt")

# Same thing
with open("file_to_upload.txt", "rb") as f:
    y.upload(f, "/destination.txt")

# Download "/some-file-to-download.txt" to "downloaded.txt"
y.download("/some-file-to-download.txt", "downloaded.txt")

# Permanently remove "/file-to-remove"
y.remove("/file-to-remove", permanently=True)

# Create a new directory at "/test-dir"
print(y.mkdir("/test-dir"))