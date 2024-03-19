import paramiko
from datetime import date
import gzip

# 获取当前日期
today = date.today()

# 获取月和日
month = today.month
day = today.day
# 连接到Linux主机
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('39.98.42.253', 22, 'root', '2com65a@!&(')

# 创建SFTP客户端
sftp = ssh.open_sftp()

# 下载文件
sftp.get('/data/backup/vip_bdhdswd-2024-'+str(month)+'-'+str(day)+'.sql.gz', 'D:/杂文件/vip_bdhdswd-2024-'+str(month)+'-'+str(day)+'.sql.gz')

# 关闭连接
sftp.close()
ssh.close()

# 打开.gz文件
with gzip.open('D:/杂文件/vip_bdhdswd-2024-'+str(month)+'-'+str(day)+'.sql.gz', 'rb') as f_in:
    # 读取解压后的内容
    content = f_in.read()

# 将解压后的内容写入到另一个文件中
with open('D:/杂文件', 'wb') as f_out:
    f_out.write(content)