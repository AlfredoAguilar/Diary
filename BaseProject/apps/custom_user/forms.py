from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields["email"].widget.attrs["class"] = "form-control"
        self.fields["email"].widget.attrs["placeholder"] = "Correo"
        self.fields["password"].widget.attrs["class"] = "form-control"
        self.fields["password"].widget.attrs["class"] = "Contraseña"
