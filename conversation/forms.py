from django import forms

from .models import ConversatioNmessage


class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversatioNmessage
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border',
            })
        }
