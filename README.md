ZAP Docker VAPT Scan Automation

This Python script automates the process of running a VAPT (Vulnerability Assessment and Penetration Testing) scan using ZAP (OWASP Zed Attack Proxy) Docker, generates a PDF report, and emails the report to specified recipients.

Prerequisites

1. Docker

Ensure that Docker is installed and running on your system. The script uses Docker to run the ZAP scan.

2. Python Libraries

The script requires the following Python libraries:

os and glob: For handling file and directory operations.
pdfkit: For converting HTML reports to PDF.
smtplib: For sending emails.
email.message: For composing email messages.
datetime: For generating the current date.
pathlib: For handling file paths.
You can install pdfkit using:

#bash #pip install pdfkit

You will also need to install wkhtmltopdf for pdfkit to work:

On Ubuntu:

#bash

#sudo apt-get install wkhtmltopdf

On macOS (with Homebrew):

#bash

#brew install --cask wkhtmltopdf

Script Overview

Variables

In the script, some variables need to be configured:

PROJ: The project name.
SCAN_URL: The URL to be scanned using ZAP.
ZAP_SERVER_IP: The IP address of the ZAP server (if applicable).
EMAIL_ADDRESS: The email address that will be used to send the report.
EMAIL_PASSWORD: The password for the email address used for authentication.
RECIPS: A list of recipient email addresses.
Functions

DockerCmd()

This function runs a ZAP full scan on the specified SCAN_URL using Docker. The scan report is saved as an HTML file inside the .Report directory.

The Docker command mounts the .Report directory to the ZAP container to store the scan results.
It runs the zap-full-scan.py script using the ZAP Docker image from ghcr.io.
GenerateReport()

This function converts the latest HTML report generated by the ZAP scan into a PDF using pdfkit. The PDF is saved in the .Report directory with the format: PROJECTNAME-DDMMYYYY.pdf.

The script searches for HTML files in the .Report directory and picks the most recent one for conversion.
The generated PDF is then used for sending in the email.
MailAlert()

This function sends the generated PDF report to the recipients listed in RECIPS using SMTP.

It composes an email with the subject containing the project name and date.
The generated PDF report is attached to the email.
The email is sent through the xmail.xerago.com SMTP server using the provided credentials.
Usage

Clone the repository or download the script.

Install the required Python libraries (pdfkit) and ensure wkhtmltopdf is installed on your system.

Configure the following variables in the script:

PROJ: Your project name.
SCAN_URL: The URL to be scanned.
EMAIL_ADDRESS: The email address from which to send the report.
EMAIL_PASSWORD: The password for the sending email account.
RECIPS: The list of recipient email addresses.
Run the script:

#bash

#python vapt-scan.py

The script will:

Run a ZAP Docker scan on the specified URL.
Generate a PDF report from the scan results.
Email the PDF report to the specified recipients.
Error Handling

If no HTML report is generated after the ZAP scan, the script will print "No HTML report files found." and terminate.
The script has basic error handling for missing reports and ensures that the email is only sent if a valid PDF file is generated.
Notes

Ensure the .Report directory exists and has the correct permissions for Docker to write files.
Update the SMTP server and email credentials in the MailAlert function to match your email provider if different.
