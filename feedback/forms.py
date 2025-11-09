from time import sleep

from django import forms
from django.conf import settings
from django.core.mail import send_mail

class FeedbackForm(forms.Form):
    email = forms.EmailField(label="Email Address")
    message = forms.CharField(
            label="Message", widget=forms.Textarea(attr={"rows"=5})
    )

    def send_email(self):
        sleep(20)
        send_mail(
                "Your Feedback",
                f"\t{self.cleaned['message']}\n\nThank you!",
                settings.EMAIL_HOST_USER,
                [self.cleaned["email"]],
                fail_silently=False,
        )
