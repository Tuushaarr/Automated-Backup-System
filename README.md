Project Title: Automated Backup System on Server

Project Overview:
This project aims to develop an automated system for backing up files on a Linux operating system. The system ensures that both an original and a compressed version of specified files are created and stored in a designated backup directory. Additionally, an email notification is sent to the user upon successful completion of the backup process.

Key Features:

File Backup:

Creates an exact duplicate of the specified file in the backup directory.
Generates a compressed version of the file to save storage space.
Backup Directory:

Allows users to specify the target directory for storing backups.
Ensures the backup directory structure is maintained and files are systematically organized.
Email Notification:

Sends an email notification to the user after the backup process is completed.
Includes details such as file name, backup location, and completion time.
Technical Implementation:

Shell Scripting and Python:

Utilizes shell scripts and Python for file operations, compression, and email notifications.
Ensures efficient and reliable execution of backup tasks.
Cron Jobs:

Automates regular backups using cron jobs.
Allows users to schedule backups at specified intervals without manual intervention.
Email Configuration:

Uses Linux mail utilities to send notifications.
Compatible with various email providers.
