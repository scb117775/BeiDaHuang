import paramiko
from datetime import datetime
import gzip

def extract_gz_file(filepath, extraction_path):
    with gzip.open(filepath, 'rb') as gz_file:
        with open(extraction_path, 'wb') as extracted_file:
            extracted_file.write(gz_file.read())

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
else:
    month = str(month)
if day < 10:
    day = str(day)
    day = '0'+day
else:
    day = str(day)

# SSH连接信息
host = '39.98.42.253'
port = 22
username = 'root'
password = '2com65a@!&('  # 或者使用SSH密钥

name_C = 'vip_bdhdswd-'+year+'-'+month+'-'+day+'.sql'
name_C_gz = 'vip_bdhdswd-'+year+'-'+month+'-'+day+'.sql.gz'
name_B = 'vip_bdhdswdgyl-'+year+'-'+month+'-'+day+'.sql'
name_B_gz = 'vip_bdhdswdgyl-'+year+'-'+month+'-'+day+'.sql.gz'
# C仓源文件和目标路径
source_file_C = '/data/backup/'+name_C_gz
destination_path_C = 'D:/杂文件/阿里云备份/'+name_C_gz
# 教委源文件和目标路径
source_file_B = '/data/backupb/'+name_B_gz
destination_path_B = 'D:/杂文件/阿里云备份/教委-B平台/'+name_B_gz

# 创建SSH客户端
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=host, port=port, username=username, password=password)

print('正在传输',name_C_gz)

# 使用SFTP传输文件_C库
sftp = ssh.open_sftp()
sftp.get(source_file_C, destination_path_C)
sftp.close()

print('正在传输',name_B_gz)

# 使用SFTP传输文件_教委
sftp = ssh.open_sftp()
sftp.get(source_file_B, destination_path_B)
sftp.close()

print('下载压缩包完成！')

# # 解压C仓的sql
# extract_gz_file('D:/杂文件/阿里云备份/'+name_C_gz,'D:/杂文件/阿里云备份/'+name_C)
# # 解压教委的sql
# extract_gz_file('D:/杂文件/阿里云备份/教委-B平台/'+name_B_gz,'D:/杂文件/阿里云备份/教委-B平台/'+name_B)
# print('解压压缩包完成')



