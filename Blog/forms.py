from django import forms
from django.core.validators import ValidationError

from Blog.models import Message


class ContactUSform(forms.Form):
    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    FAVORITE_COLORS_CHOICES = [
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'), ]
    text = forms.CharField(max_length=10, label="Enter your text my friend")
    name = forms.CharField(max_length=10, label="Enter your name my friend")
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    color = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES)

    def clean(self):
        name = self.cleaned_data.get('name')
        text = self.cleaned_data.get('text')
        # if 'a' in name:
        #     self.add_error('name','a can not in name')

        if name == text:
            raise ValidationError('name and text are same', code='name_text_same')

    # def clean_name(self):
    #     name = self.cleaned_data.get('name')
    #     if 'a' in name:
    #         raise ValidationError('a can not in name', code='a_in_name')
    #     return name


# class MessageForm(forms.Form):
#     title = forms.CharField(max_length=100)
#     text = forms.CharField(widget=forms.Textarea())
#     email = forms.EmailField()


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        # exclude = ('title',)
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "enter your title",
                "style": "max-width : 300px"
            }),
            "text": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "enter your text",
            }),



        }
