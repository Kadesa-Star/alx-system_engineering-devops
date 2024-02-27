How to Connect with SFTP
By default, SFTP uses the SSH protocol to authenticate and establish a secure connection. Because of this, the same authentication methods are available that are present in SSH.

Although you can authenticate with passwords by default, we recommend you create SSH keys and transfer your public key to any system that you need to access. This is much more secure and can save you time in the long run.

Please see this guide to set up SSH keys in order to access your server if you have not done so already.

If you can connect to the machine using SSH, then you have completed all of the necessary requirements necessary to use SFTP to manage files. Test SSH access with the following command:

ssh sammy@your_server_ip_or_remote_hostname
If that works, exit back out by typing:
exit

Now we can establish an SFTP session by issuing the following command:
sftp sammy@your_server_ip_or_remote_hostname

you will connect the the remote system and your prompt will change to an SFTP prompt.

If you are working on a custom SSH port (not the default port 22), then you can open an SFTP session as follows:

sftp -oPort=custom_port sammy@your_server_ip_or_remote_hostname

