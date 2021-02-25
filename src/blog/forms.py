from django import forms

from .models import BlogPost

class BlogPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)

class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'image', 'slug', 'content', 'publish_date']

        def clean_title(self, *args, **kwargs):
            instance = self.instance
            title = self.cleaned_data.get('email')
            qs = BlogPost.objects.filter(title_iexact=title)
            if instance is not None:
                qs = qs.excclude(pk=instance.pk) # id=instance.id
            if qs.exists():
                raise forms.ValidationError("This isnkt balid title")
            return title