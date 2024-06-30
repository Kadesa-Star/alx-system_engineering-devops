# 0x0B. SSH
## Description
# AirBnB Clone Project

## Description

This project is an AirBnB clone implemented using MySQL and Bash scripting on an Ubuntu 20.04 LTS environment. The project involves configuring and connecting to a remote server using SSH and an RSA key, as well as creating executable Bash scripts with specific formatting. The project adheres to strict guidelines for coding, documentation, and testing.

## Learning Objectives

By the end of this project, you will be able to:

- Understand what a server is and where servers usually reside.
- Explain SSH and its uses.
- Create an SSH RSA key pair.
- Connect to a remote host using an SSH RSA key pair.
- Explain the advantage of using `#!/usr/bin/env bash` instead of `/bin/bash` in scripts.

## Requirements

- **Editors**: vi, vim, emacs
- **Environment**: Ubuntu 20.04 LTS
- **File Requirements**:
  - All files should end with a new line.
  - A `README.md` file at the root of the project is mandatory.
  - All Bash script files must be executable.
  - The first line of all Bash scripts should be `#!/usr/bin/env bash`.
  - The second line of all Bash scripts should be a comment explaining the script's purpose.

## Setup and Configuration

### Accessing the Server

1. **Generate an RSA Key Pair**:
    ```bash
    ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
    ```

2. **Configure SSH**:
    Edit the `~/.ssh/config` file to add your server details:
    ```plaintext
    Host my-server
        HostName <server_ip>
        User <username>
        IdentityFile ~/.ssh/id_rsa
    ```

3. **Connect to the Server**:
    ```bash
    ssh my-server
    ```

### Creating Executable Bash Scripts

1. Create a new script file:
    ```bash
    vim script.sh
    ```

2. Add the following content:
    ```bash
    #!/usr/bin/env bash
    # This script does XYZ
    
    echo "Hello, World!"
    ```

3. Make the script executable:
    ```bash
    chmod +x script.sh
    ```

4. Run the script:
    ```bash
    ./script.sh
    ```

## Resources

- **Reading**:
  - [What is a (physical) server - text](#)
  - [SSH essentials](#)
  - [SSH Config File](#)
  - [Public Key Authentication for SSH](#)
  - [How Secure Shell Works](#)
  - [SSH Crash Course](#)
- **References**:
  - [Understanding the SSH Encryption and Connection Process](#)
  - [Secure Shell Wiki](#)
  - [IETF RFC 4251 (Description of the SSH Protocol)](#)
  - [Internet Engineering Task Force](#)
  - [Request for Comments](#)
- **Man or Help Pages**:
  - `ssh`
  - `ssh-keygen`
  - `env`

## Author
Kadesa 
