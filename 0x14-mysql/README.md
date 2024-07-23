# MySQL Primary-Replica Cluster and Backup Strategy

## Introduction
This project focuses on setting up a MySQL primary-replica cluster and developing a robust database backup strategy. The primary goal is to ensure high availability, load balancing, and data redundancy. Additionally, implementing a reliable backup strategy is crucial for data recovery in case of failures.

## Learning Objectives
By the end of this project, you should be able to explain:
1. **The main role of a database**: Databases store, manage, and retrieve data efficiently.
2. **What a database replica is**: A database replica is a copy of the primary database that is kept in sync.
3. **The purpose of a database replica**: Replicas are used for load balancing, high availability, and disaster recovery.
4. **Why database backups need to be stored in different physical locations**: To protect against data loss due to localized failures (e.g., natural disasters, hardware failures).
5. **Regular operations to ensure the effectiveness of your backup strategy**: Regularly perform backup restoration tests to verify that backups are working correctly.

## Requirements
- **Editors**: `vi`, `vim`, or `emacs`.
- **System**: All files will be interpreted on Ubuntu 16.04 LTS.
- **File standards**:
  - Files should end with a new line.
  - Include a mandatory `README.md` file.
  - Bash scripts must be executable and pass Shellcheck (version 0.3.7-5~ubuntu16.04.1).
  - First line of Bash scripts: `#!/usr/bin/env bash`.
  - Second line: A comment explaining what the script does.

## Servers
You will be working with three servers:
- **Primary Server**: `439424-web-01` (IP: `100.25.202.17`)
- **Replica Server**: `439424-web-02` (IP: `34.207.62.126`)
- **Load Balancer**: `439424-lb-01` (IP: `34.224.94.13`)

## Setting Up Primary-Replica Cluster
1. **Configure MySQL on the Primary Server**:
    - Install MySQL.
    - Edit the MySQL configuration file (`/etc/mysql/my.cnf`) to enable binary logging and set the server ID.
    - Create a replication user with the necessary permissions.

2. **Set Up Replication on the Replica Server**:
    - Install MySQL.
    - Edit the MySQL configuration file to set the server ID and configure it as a replica.
    - Connect to the primary server and start the replication process.

3. **Ensure Data Consistency**:
    - Use the `SHOW MASTER STATUS` and `SHOW SLAVE STATUS` commands to monitor replication.
    - Perform tests to ensure that data changes on the primary server are replicated to the replica server.

## Backup Strategy
1. **Using `mysqldump` for Backups**:
    - `mysqldump` is a utility for creating logical backups by dumping a database or a collection of databases into SQL files.

2. **Automating Backups with Bash Scripts**:
    - Create a script to perform daily backups and store them in a specified directory.
    - Ensure the script includes error handling and logging.

3. **Storing Backups in Different Physical Locations**:
    - Use cloud storage or remote servers to store backup copies.
    - Implement automated transfer of backup files to these locations.

## Example Bash Script for Backup
```bash
#!/usr/bin/env bash
# This script performs a MySQL database backup using mysqldump

# Define database credentials
USER="your_username"
PASSWORD="your_password"
HOST="localhost"
DB_NAME="your_database_name"

# Define backup directory and file name
BACKUP_DIR="/path/to/backup/directory"
DATE=$(date +"%Y%m%d%H%M%S")
BACKUP_FILE="$BACKUP_DIR/$DB_NAME-$DATE.sql"

# Perform the backup
mysqldump -u $USER -p$PASSWORD -h $HOST $DB_NAME > $BACKUP_FILE

# Check if the backup was successful
if [ $? -eq 0 ]; then
  echo "Backup successful: $BACKUP_FILE"
else
  echo "Backup failed"
  exit 1
fi

