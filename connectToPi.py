import paramiko

def ssh_run_command(input_data=None):

    hostname = 'pics.local'  # Replace with the actual hostname or IP address
    username = 'pics'  # Replace with your SSH username
    password = 'pi'  # Replace with your SSH password
    command = 'python client.py'  # Replace with the command you want to run
    # SSH into the remote device
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, username=username, password=password)

    # Run the command
    stdin, stdout, stderr = ssh.exec_command(command)

    # Pass input if provided
    if input_data:
        stdin.write(input_data)
        stdin.flush()

    # Read the output from stdout
    print(stdout)
    ssh.close()

