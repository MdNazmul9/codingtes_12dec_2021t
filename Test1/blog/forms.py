
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
class PostForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField(widget=CKEditorUploadingWidget())