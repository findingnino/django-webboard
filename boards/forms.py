from django import forms
from .models import Topic, Post

class NewTopicForm(forms.ModelForm):
	max_length = 4000
	message = forms.CharField(
		widget=forms.Textarea(
			attrs={'rows': 2, 'placeholder': "What's on your mind?"}
		),
		max_length=max_length,
		help_text="The max length of this message is {0} characters".format(max_length)
	)

	class Meta:
		model = Topic
		fields = ['subject', 'message']

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['message', ]