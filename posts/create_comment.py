from .models import Comment 
from django import forms 


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment 
        fields = ('context',)
        widgets = {
            'context': forms.Textarea(attrs={'rows':2, 'cols':5})
        }

    
    

    