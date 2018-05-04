from django.db import models

# Create your models here.
class User (models.Model):
	user_name = models.CharField(max_length = 50)
	Email = models.EmailField(unique = True)
	passwrd = models.PassWordField(max_length = 50)
	age = models.IntegerField(max_length = 3, null = True)
	phone_num = models.IntegerField(unique = True,null = True)
	works_at = models.CharField(max_length = 50,null = True)
	address = models.CharField(max_length = 50,null=True)
	birth_date = models.DateField('Birthday', null = True)

	def __str__ (self):
		return self.user_name


class Post (models.Model):
	choices = 'timeline'
	body = models.TextField()
	user = models.ForiegnKey(User, on_delete = models.CASCADE)
	scope = models.ChoiceField()
	group = models.ForiegnKey(Group, on_delete = models.CASCADE)

	def __str__(self):
		return self.body

class Comment(models.Model):
	post = models.ForiegnKey(Post,on_delete = CASCADE)
	user = models.ForiengKey(User,on_delete = CASCADE)
	body = models.TextField()

	def __str__(self):
		return self.body

class Group (models.Model):
	name = models.CharField(max_length = 50)
	post = models.ForiegnKey(models,on_delete = CASCADE)
	admin = models.ForiegnKey(models,on_delete = CASCADE)
	user = models.ForiegnKey(models,on_delete = CASCADE)

	def __str__(self):
		return self.name

class Like(models.Model):
	user = models.ForiegnKey(User,on_delete = CASCADE)
	post = models.ForiegnKey(Post,on_delete = CASCADE)
	comment = models.ForiegnKey(Comment,on_delete = CASCADE)

	def __str__(self):
		return self.User
