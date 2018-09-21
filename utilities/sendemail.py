"""
@package utilities
Send Emails
"""
import win32com.client as win32
outlook = win32.Dispatch('outlook.application')

def send_notification():
    mail = outlook.CreateItem(0)
    mail.To = 'enrique.decoss@wolterskluwer.com'
    mail.Subject = 'Message subject'
    mail.Body = 'Message body'
    #mail.HTMLBody = '<h2>HTML Message body</h2>'  # this field is optional

    # To attach a file to the email (optional):
    attachment = "WKQArep.html"
    mail.Attachments.Add(attachment)
    mail.Send()

