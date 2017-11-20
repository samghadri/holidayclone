from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields =('username','email','password1','password2')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label= 'Create Username'
        self.fields['email'].label= 'Enter Email'
        self.fields['password1'].label= 'Password'
        self.fields['password2'].label= 'Repeat Password'
