from website.models import contact , Newsletter
from django import forms
from captcha.fields import CaptchaField


class contactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = contact
        
        fields = '__all__'
    
class NewsletterForm(forms.ModelForm):
    
    class Meta:
        model = Newsletter
        fields = '__all__'