from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from qa.models import Question, Answer

class AskForm(forms.Form) :
	title = forms.CharField(max_length=255)
	text = forms.CharField(widget=forms.Textarea)
	author = 1
	
	def clean_title(self) :
		title = self.cleaned_data['title']
		return title

	def clean_text(self) :
		text = self.cleaned_data['text']
		return text
		
	def save(self) :
		if self._user.is_anonymous():
			self.cleaned_data['author_id'] = 1
		else:
			self.cleaned_data['author'] = self._user
		ask = Question(**self.cleaned_data)
		ask.save()
		return ask
	
class AnswerForm(forms.Form) :
	text = forms.CharField(widget=forms.Textarea)
	question = forms.IntegerField(widget=forms.HiddenInput)
	author = 1
	
	def clean_text(self) :
		text = self.cleaned_data['text']
		return text
		
	def clean_question(self) :
		try :
			quest_id = int(self.cleaned_data['question'])
		except ValueError :
			raise forms.ValidationError('fail input')
		return quest_id
	
	def save(self) :
		self.cleaned_data['question'] = get_object_or_404(Question, pk=self.cleaned_data['question'])
  
		if self._user.is_anonymous():
		  self.cleaned_data['author_id'] = 1
		else:     
		  self.cleaned_data['author'] = self._user
		post = Answer(**self.cleaned_data)
		post.save()
		return post
		
class SignupForm(forms.Form) :
	username = forms.CharField(max_length=50)
	email = forms.EmailField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput)
	_pass = ""
	
	def set_password(self, password) :
		self._pass = password
		return password
	
	def clean_username(self) :
		username = self.cleaned_data['username']
		return username
		
	def clean_email(self) :
		email = self.cleaned_data['email']
		return email
		
	def clean_password(self) :
		password = self.cleaned_data['password']
		
	def save(self) :
		user = User.objects.create_user(self.clean_username(), self.clean_email(), self._pass)
		return user
	
	def loginUser(self, request) :
		user = authenticate(username=self.clean_username(), password=self._pass)
		login(request, user)
		return user
		
class LoginForm(forms.Form) :
	username = forms.CharField(max_length=50)
	password = forms.CharField(widget=forms.PasswordInput)
	_pass = ""
	
	def set_password(self, password) :
		self._pass = password
		return password
	
	def clean_username(self) :
		username = self.cleaned_data['username']
		return username
		
	def clean_password(self) :
		password = self.cleaned_data['password']
		
	def loginUser(self, request) :
		user = authenticate(username=self.clean_username(), password=self._pass)
		login(request, user)
		return user