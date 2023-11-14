from django import forms


class UniForm(forms.Form):
    COURSE_CHOICES = (
		(1, 'web development'),
		(2, 'System Programming'),
		(3, 'Data Science')
	)
    
    name = forms.CharField()
    age = forms.IntegerField()
    subject = forms.ChoiceField(
        choices=COURSE_CHOICES,
        widget=forms.RadioSelect()
        )
    date_of_birth = forms.DateField()