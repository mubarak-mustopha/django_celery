from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from feedback.forms import FeedbackForm


class FeedbackFormView(FormView):
    template_name = "feedback/feedback.html"
    form_class = FeedbackForm
    success_url = "/success/"

class SuccessView(TemplateView):
    template_name = "feedback/success.html"
