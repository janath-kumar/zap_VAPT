from fileinput import filename
import os
import glob
import pdfkit
import smtplib
from email.message import EmailMessage
from datetime import date
from pathlib import Path

### Variables ###
today = date.today()
d1 = today.strftime("%d%m%Y")
PROJ = "xerago-test" # Enter Project Name
SCAN_URL = "URL"
ZAP_SERVER_IP = "IP"
### Variables ###

### Docker ZAP Scan ###
def DockerCmd():
    print("Docker Running ...", end='\r', flush=True)
    Path(".Report").mkdir(parents=True, exist_ok=True)
    Path(".Report").chmod(0o777)
    #command =  f'docker run -v $(pwd)/.Report:/zap/wrk/:rw -t owasp/zap2docker-stable zap-full-scan.py -t "{SCAN_URL}" -g gen.conf -r $(date +"%Y%m%d").html >/dev/null 2>&1'
    command =  f'docker run -v $(pwd)/.Report:/zap/wrk/:rw -t ghcr.io/zaproxy/zaproxy:stable zap-full-scan.py -t "{SCAN_URL}" -g gen.conf -r $(date +"%Y%m%d").html'
    p = os.system(command)
    p = os.system(command)
    print("Docker Completed ...", end='', flush=True)
    print()
### Docker ZAP Scan ###

### Generate ZAP Scan Report ###
def GenerateReport():
    print("Report Generating ...", end='\r', flush=True)
    list_of_html_files = glob.glob('.Report/*.html')
    if not list_of_html_files:
        print("No HTML report files found.")
        return
    latest_file_html = max(list_of_html_files, key=os.path.getctime)
    global pdf_filename
    global PROJ
    pdf_filename = (f".Report/{PROJ}-{d1}.pdf")
    pdfkit.from_file(latest_file_html, pdf_filename)
    print("Report Generated ...", end='', flush=True)
    print()
### Generate ZAP Scan Report ###

### Mail Alert the ZAP Scan Report ###
def MailAlert():
    EMAIL_ADDRESS = 'support@xerago.com' # Enter Email Address
    EMAIL_PASSWORD = 'Xmail$531' # Enter Email Password
    RECIPS = ['janathkumar@gmail.com'] # Enter Recipients Address

    msg = EmailMessage()
    msg['Subject'] = f'VAPT Report for {PROJ} {today.strftime("%d-%m-%Y")}'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = ", ".join(RECIPS)
    msg.set_content(f'''Hi all,

Please find the VAPT scan report attachment for {PROJ} taken on {today.strftime("%d-%m-%Y")}.

Thanks,
ALM Team.''')
    print("Mail Started ...", end='\r', flush=True)
    files = [pdf_filename]
    for file in files:
        with open(file, 'rb') as f:
            file_data = f.read()
            file_name = f.name
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=os.path.basename(file_name))

    with smtplib.SMTP('xmail.xerago.com', 587) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
    print("Mail Sent ...", end='', flush=True)

### Mail Alert the ZAP Scan Report ###

DockerCmd()
GenerateReport()
MailAlert()
