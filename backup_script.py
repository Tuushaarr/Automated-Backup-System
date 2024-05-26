
import shutil

import tarfile

import smtplib
import subprocess
import os

#from email.message import EmailMessage

# Error handling logic

try:
    # Copy tushar.txt to the backup directory
    source_file = '/root/tushar.txt'
    backup_directory = '/root/mybackup'
    backup_filename = 'tushar_backup.txt'

    if not os.path.exists(backup_directory):
        os.makedirs(backup_directory)

    if os.path.exists(source_file):
        shutil.copy(source_file, os.path.join(backup_directory, backup_filename))
        print(f"Backup of {source_file} successful.")

    else:
        print(f"File {source_file} does not exist.")

    #Compression logic
    with tarfile.open(os.path.join(backup_directory, 'backup.tar.gz'), 'w:gz') as tar:
        tar.add(backup_directory, arcname='backup')

    #Notification logic
    email_command = 'echo "Tushar saini - Backup process completed." | mail -s "Backup Status" theblurryface2019@gmail.com'
    subprocess.run(email_command, shell=True)

 #   msg = smtplib.EmailMessage()
  #  msg.set_content('Backup process completed.')
   # msg['Subject'] = 'Backup Status'
   # msg['From'] = 'theblurryface2019@gmail.com'
   # msg['To'] = 'theblurryface2019@gmail.com'

   # s = smtplib.SMTP('tusharGhost')
   # s.send_message(msg)
   # s.quit()
   

except Exception as e:
    with open(os.path.join(backup_directory, 'error.log'), 'a') as f:
        f.write(f"Backup failed: {str(e)}\n")
