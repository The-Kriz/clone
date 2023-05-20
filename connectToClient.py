import paramiko

def ssh_run_command(hostname, username, password, command, input_data=None):
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
    output = stdout.read().decode('utf-8')

    # Close the SSH connection
    ssh.close()

    return output

# Example usage
hostname = 'pics.local'  # Replace with the actual hostname or IP address
username = 'pics'  # Replace with your SSH username
password = 'pi'  # Replace with your SSH password
command = 'python client.py'  # Replace with the command you want to run
input_data = input("Enter IP address: ")

output = ssh_run_command(hostname, username, password, command, input_data)
print(output)
