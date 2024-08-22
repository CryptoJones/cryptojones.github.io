##Forgot Domain Admin Password Windows Server 2022

--Boot to recovery mode with ISO

-- Click Next, Then "Repair my computer"

-- Click Troubleshoot, then click the Command Prompt option

-- list disks by opening diskpart, then "list volume"

--run "select volume 1" (assuming 1 is your main hdd)

--run "assign letter C"

--run "exit" to leave diskpart

--run "C:" to switch to your main hard drive

--run "cd \\Winddows\\System32" in order to change directories

--run "rename Utilman.exe Utilman.bak" to backup the utility

--run "copy cmd.exe utilman.exe"

--run "D:"

--run "bcdedit /set {bootmgr} timeout 15"

--run "bcdedit /set {bootmgr} displaybootmenu yes"

--exit and reboot computer after removing the iso

--select windows in the boot menu then hit enter

--go to login but instead of typing a username and password click the accesibility icon to get a command prompt

--in the command prompt run "net user" to list the accounts

--to change the password on one of the accounts type "net user username password /domain"
