from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from Cart.models import Orderz




class CheckOutForm(ModelForm):
    class Meta:
        model = Orderz
        fields = ['name','email','mobile','address','city','state','pin','country']
        widgets ={
            'name' : forms.TextInput(attrs={'placeholder':'john M. Doe'}),
            'email' : forms.TextInput(attrs={'placeholder':'john@example.com'}),
            'mobile' : forms.TextInput(attrs={'placeholder':'Mobile Number'}),
            'address': forms.TextInput(attrs={'placeholder':'542 W. 15th Street'}),
            'city' : forms.TextInput(attrs={'placeholder':'Newyork'}),
            'state' : forms.Select(attrs={"class":"custom-select d-block w-100"}),
            'pin' : forms.TextInput(attrs={'placeholder':'10001'}),
            'country' :forms.Select(attrs={"class":"custom-select d-block w-100"})
        }

    
    # name = forms.CharField(required=True, max_length=20,widget=forms.TextInput(attrs={'placeholder':'john M. Doe'}))
    # email = forms.EmailField(required=False, widget=forms.TextInput(attrs={'placeholder':'john@example.com'}))
    # mobile = forms.IntegerField(required=True, max_value=10, widget=forms.TextInput(attrs={'placeholder':'Mobile Number'}))
    # address = forms.CharField(required=True, max_length=500, widget=forms.TextInput(attrs={'placeholder':'542 W. 15th Street'}))
    # city = forms.CharField(required=True, max_length=20, widget=forms.TextInput(attrs={'placeholder':'New York'}))
    # state = forms.ChoiceField(choices=STATE_CHOICES, widget=forms.Select(attrs={'class':'custom-select d-block w-100'}),required=True)
    # pin = forms.IntegerField(max_value=6, widget=forms.TextInput(attrs={'placeholder':'10001'}))
    # country = CountryField(blank_label='(select country)').formfield(widget=CountrySelectWidget(attrs={'class':'custom-select d-block w-100'}))
    # same_billing_address = forms.BooleanField(widget=forms.CheckboxInput())
    # payment_option = forms.ChoiceField(widget=forms.RadioSelect(), choices=PAYMENT_CHOICES)


