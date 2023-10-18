from django import forms

class ApiKkeyForm(forms.Form):
    key = forms.CharField(label="输入apikey", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
#    captcha = CaptchaField(label='验证码')