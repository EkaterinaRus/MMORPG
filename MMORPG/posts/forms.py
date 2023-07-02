from django.forms import ModelForm
from .models import Post, Category
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostForm(forms.ModelForm):
    # content = forms.CharField(widget=CKEditorUploadingWidget())
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      empty_label="Категория не выбрана",
                                      label="Категории",
                                      widget=forms.Select(attrs={'class': 'form__category'}))

    class Meta:
        model = Post
        fields = ['title', 'text', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form__title', 'placeholder': 'Введите заголовок'}),
            'text': forms.Textarea(attrs={'class': 'form__text',  'placeholder': 'Введите текст', 'rows': "10", 'cols': "60"}),
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()





