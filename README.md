## A simple FTP Python script

Very simple way to use file transfer protocol with Python.

### Goals:
- Create a simple FTP program using Python. &#x2705;
- Refactor it to a SFTP program using SSH. (IT & Cybersecurity)
- Develop an app with a user interface to make it user-friendly. (UI/UX)

### How to use the simple FTP:
1. Start up 2 different Terminals, Command Prompts or Bash terminals.
2. Locate your project folder on both.
3. On 1 Command Prompt, change directory to the 'receive' folder.

You should now have 2 different Command Prompts (Terminals on IOS or BASH on Linux) open and ready to start.

4. On 1 command prompt, open the python file 'server.py'. This prints the name of your current PC host and awaits any socket connections.
5. On the other command prompt (the one in the 'receive' folder) open the python file 'client.py'. You should see a prompt for a host address.
6. Enter the name the server printed for you into the client prompt. You should now see the server reacting and giving you connection on the socket port 8080.
7. The server asks for a name of the file that is to be transmitted from, write it in but DO NOT press enter yet. 
   If you have the same filenames as me, it's 'transfer.txt'
8. The client asks for a name of the file that is to be transmitted to, write in any name you want, just remember to use .txt type at the end. 
9. Now, press enter on the Server prompt, and then the Client prompt. You should see the server print if it was a successful transmission  and the client print if it was a successful receival.
10. Now locate your 'recieve' folder using your OS filesystem. Inside should be the file you just created, and the text in it is from the transfer.txt file.

### Structure:
<pre>
simple-sftp-python
│   server.py
│   transfer.txt
│
└───receive
        client.py
        received.txt
</pre>
