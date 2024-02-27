from django.shortcuts import render
import csv
from django.core.mail import send_mail
# Create your views here.
def send_emails(request):
    csv_file_path = r'C:\PFSD\pythonProject\djangoproject\ttm\static\sendmail.csv'
    with open(csv_file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            recipient_email = row['email']
            subject = 'Hello KLUian'  # Set your subject here
            message_body = 'Hey, come to college on time guys'  # Set your email content here
            send_mail(
                subject,
                message_body,

                'nandinikurmapython8@gmail.com',
                [recipient_email],
                fail_silently=False,
            )
            print(f'Sent email to {recipient_email}')
    return render(request, 'Emails_sent_successfully.html')