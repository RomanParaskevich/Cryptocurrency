from django.dispatch import receiver
from django.db.models.signals import post_save
import smtplib
from .models import Mail, Subscribers, Sender


@receiver(post_save, sender=Mail)
def post_save_mail(created, **kwargs):
    if created:
        queryset = Sender.objects.all()
        instance = kwargs['instance']
        sender = queryset[0].sender
        password = queryset[0].password
        server = smtplib.SMTP(queryset[0].smtp_server, queryset[0].port)
        server.starttls()
        for item in Subscribers.objects.all():
            try:
                server.login(sender, password)
                server.sendmail(sender, item.email, f"Subject: {instance.title}\n{instance.text}")
            except Exception as ex:
                return print(ex)
