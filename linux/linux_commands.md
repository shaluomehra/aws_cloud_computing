## Useful Linux Commands

`uname` gives you your system name <br> 
`uname -a` gives you all the info on the system <br> 
`uname -p` gives you the processor information <br>
`whoami` gives you the username <br>
`cat /etc/shells` gives you the list of valid login shells available <br>
`history` gives you the last 500 commands inputted <br> 
`curl` used to transfer data use `--output <filename>` to store it <br>
`file <filename>` to check the details of the file <br>
`mv <file>` can be used to move files and folders <br>
`mv <file> <rename file>` can also be used to rename files <br>
`cp <file>` will copy a file <br>
`rm <file>` will remove a file <br>
`rm -r <folder>` will removed folders <br>
`mkdir` will make a directory <br>
`cd ..` will go back a directory <br>
`touch` will make a blank file <br>
`cat` will output the contents of a file <br>
`nano` will open nano text editor with file specified. If file doesn't exist it'll create a new file with that name <br>
`head -<number>` gives you the top number of lines in the file <br>
`tail <number>` gives you the bottom number of lines in the file <br>
`nl` numbers the lines in a file (not including blank lines) <br>
`grep` Used after | , will print out lines that contain the words you specify <br>
`sudo su` changes the user to the root user <br>
`exit` to break out of user or exit out of root user <br>
`clear` clears the command line <br>
`ps` gives user process in one session <br>
`PID` is the process id <br>
`ps -- help simple` gives most useful flags <br>
`ps -A` gives all processes <br>
`ps aux`gives everything verbose <br>
`top` lives readout of processes that are running <br>
`q` to quit out <br>
`sleep` makes a dummy program on the front end that sleeps <br>
`ctrl+z or ctrl+c` to exit out of a process on the front end <br>
`kill -1 <PID>` soft kill <br>
`kill -15 <PID>` force kills processes <br>
`kill -9 <PID>` brute force kills processes <br>
`ls -l` gives detailed information about files and folders <br>

### Permissions

`rwxrwxrwx` - split this into three sections, first three letters are the owner, the second three are the group and the final 3 are the public <br>

`chmod` to change permissions <br>
`chmod u+x` owner can now execute <br>
`chmod g+x` group can now execute <br>
`chmod +x` everyone can now execute <br>
**Same goes for 'r' and 'w'** <br>

`chmod 777` all permissions to all users <br>
`chmod`: +4 read, +2 write, +1 execute <br>

### Environment variables

`printenv` to see all the environment variables <br>
**To create a local variable:** <br>
```
MYNAME=Shaluo
```
***To create an environment variable:** <br>
```
export MY_NAME=Shaluo
```


