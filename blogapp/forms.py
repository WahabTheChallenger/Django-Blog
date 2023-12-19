from django import forms 
from .models import Post , Category

# choices = [(),(),(coding,coding)]
choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post 
        fields = ('title','title_tag','author','category','body','description')

        widgets = {
            'title': forms.TextInput(attrs={'class':' form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list,attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control','rows':5}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post 
        fields = ('title','title_tag','body','category','description')

        widgets = {
            'title': forms.TextInput(attrs={'class':' form-control','placeholder':'This is title placeholder'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list,attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control','rows':5}),
        }

