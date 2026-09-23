from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea(attrs={"rows": 5}))
    rating = forms.IntegerField(
        required=False,
        min_value=1,
        max_value=5,
        help_text="Optional: 1 (low) to 5 (high)",
    )

    def clean_message(self):
        message = self.cleaned_data["message"]
        if len(message) < 10:
            raise forms.ValidationError(
                "Message is too short. Please write at least 10 characters."
            )
        return message
