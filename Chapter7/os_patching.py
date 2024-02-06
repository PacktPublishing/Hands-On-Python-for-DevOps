import subprocess 

import platform 

def update_os(): 

    system = platform.system().lower() 

    if system == 'linux' or system == 'linux2': 

        if 'debian' in platform.linux_distribution()[0].lower() or 'ubuntu' in platform.linux_distribution()[0].lower(): 

            update_command = "sudo apt update && sudo apt upgrade -y" 

        else: 

            update_command = "sudo dnf update -y" 	subprocess.run(update_command, shell=True) 

  

    elif system == 'windows': 

        update_command = 'powershell -Command "Start-Service -Name wuauserv; Get-WindowsUpdate; Install-WindowsUpdate;"' 

        subprocess.run(update_command, shell=True) 

   

if __name__ == "__main__": 

    update_os() 
