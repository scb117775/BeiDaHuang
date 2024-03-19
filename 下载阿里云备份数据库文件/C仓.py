import paramiko
from datetime import datetime

# 获取当前时间
now = datetime.now()

# 获取年月日
year = now.year
month = now.month
day = now.day
year = str(year)
if month < 10:
    month = str(month)
    month = '0'+month
if day < 10:
    day = str(day)
    day = '0'+day

name = 'vip_bdhdswd-'+year+'-'+month+'-'+day+'.sql.gz'
# SSH连接信息
host = '39.98.42.253'
port = 22
username = 'root'
password = '2com65a@!&('  # 或者使用SSH密钥

# 源文件和目标路径
source_file = '/data/backup/'+name
destination_path = 'D:/杂文件/阿里云备份/'+name

# 创建SSH客户端
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=host, port=port, username=username, password=password)

# 使用SFTP传输文件
sftp = ssh.open_sftp()
sftp.get(source_file, destination_path)
sftp.close()

print("文件下载成功！")

