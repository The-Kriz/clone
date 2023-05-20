import paramiko
#pip install paramiko
# SSH credentials
hostname = 'pics.local'
username = 'pics'
password = 'pi'

# SSH into the remote server
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, username=username, password=password)
print("hi")

# Run the command: python client.py
command = 'python client.py'

stdin, stdout, stderr = ssh.exec_command(command)
print("hi2")
output = stdout.read().decode('utf-8')
print(output)
print("hi3")

