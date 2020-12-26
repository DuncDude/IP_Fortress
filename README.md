** IP_Fortress
A python base program that sets linux firewall rules to block all IPs from txt files, with the option to download public malcious IP lists.**

**Installing Necessary Dependencies and Python libraries**
You likely already have these installed on your computer but incase you dont you can install these on you computer using
`sudo apt-get install ufw`
`pip install pycopy-fnmatch`

**Running IP Fortress**
To run IP Fotress open a new terminal window and navigate to the directory that IP Fortress is in. Launch IP Fortress by typing
`python IP_Fortress`

**Downloading Malcious IP lists to block with your firewall**
To download pre approved community audited list of bad IPs you can navigate to the 2nd option in the main menu.
'[2]. Update lists'
The lists are downloaded from the github repository  https://github.com/stamparm/ipsum.
The lists will automaticlly be downloaded using 'wget'. If you have already downloaded lists from this repository, this will update those lists.

**Blocking the IPs**
Finally to block each IP on each list, navigate to the 1st option from the main menu
*[1]. Apply lists '
A drop down list of all *.txt* files in the current directory will appear. To apply a list of IPs to be blocked, enter the list name for
example '6.txt'. IP Fortress will loop through each line of the *.txt* file selected and add them to a list of blocked incoming and outgoing traffic
to each IP Address on the list.
