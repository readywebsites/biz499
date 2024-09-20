from django import forms
from marketing.models import Job_applications,Open_posts

class NewjobForm(forms.ModelForm):
  name = forms.TextInput()
  email = forms.EmailField()
  contact = forms.IntegerField()
  post= forms.ModelChoiceField(
        queryset=Open_posts.objects.all(),
        to_field_name='post',
        required=True,  
        widget=forms.Select(attrs={'class': 'form-control'}))

  resume = forms.FileField()

  class Meta:
      model = Job_applications
      fields = "__all__"

  def __init__(self, *args, **kwargs):
    super(NewjobForm, self).__init__(*args, **kwargs)
    for visible in self.visible_fields():
        visible.field.widget.attrs['class'] = 'form-control'
