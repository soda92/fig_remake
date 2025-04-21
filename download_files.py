import ftplib
import os

ftp_host = 'ftp.sra.ebi.ac.uk'
ftp_user = 'anonymous'
ftp_password = ''
remote_file = '/vol1/fastq/SRR181/007/SRR1810907/SRR1810907.fastq.gz'
local_file = 'SRR1810907.fastq.gz'

try:
    with ftplib.FTP(ftp_host) as ftp:
        ftp.login(ftp_user, ftp_password)

        rest_position = 0
        if os.path.exists(local_file):
            rest_position = os.path.getsize(local_file)
            print(f"Resuming download from byte: {rest_position}")
            ftp.sendcmd(f"REST {rest_position}")

        with open(local_file, 'ab') as lf:
            def callback(data):
                lf.write(data)

            ftp.retrbinary(f'RETR {remote_file}', callback)

        print("Download complete!")

except ftplib.all_errors as e:
    print(f"FTP error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")