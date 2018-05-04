from django.db import models

# Create your models here.
class User (models.Model):
	user_name = models.CharField(max_length = 50)
	Email = models.EmailField(unique = True)
	#password = models.PasswordField(max_length = 50)
	age = models.IntegerField(null = True)
	phone_num = models.IntegerField(unique = True,null = True)
	works_at = models.CharField(max_length = 50,null = True)
	address = models.CharField(max_length = 50,null=True)
	birth_date = models.DateField('Birthday', null = True)

	def __str__ (self):
		return self.user_name

class Group (models.Model):
	name = models.CharField(max_length = 50)
	admin = models.ForeignKey(User,on_delete = models.CASCADE,related_name = "group_admin")

	def __str__(self):
		return self.name

class Post (models.Model):
	Choices = (('T','timeline'),('G','group'))
	body = models.TextField()
	user = models.ForeignKey(User, on_delete = models.CASCADE,related_name = "Post_publisher")
	scope = models.CharField(max_length = 1,choices = Choices,default = 'T')
	group = models.ForeignKey(Group, on_delete = models.CASCADE,related_name = "post_group")

	def __str__(self):
		return self.body

class Comment(models.Model):
	post = models.ForeignKey(Post,on_delete = models.CASCADE)
	user = models.ForeignKey(User,on_delete = models.CASCADE,related_name = "comment_owner")
	body = models.TextField()

	def __str__(self):
		return self.body


class Like(models.Model):
	Choices = (('P','post'),('C','comment'))
	user = models.ForeignKey(User,on_delete = models.CASCADE,related_name = "like_owner")
	post = models.ForeignKey(Post,on_delete = models.CASCADE,related_name = "liked_post")
	comment = models.ForeignKey(Comment,on_delete = models.CASCADE,related_name = "liked_comment")
	scope = models.CharField(max_length = 1,choices = Choices,default = 'P')
	
	def __str__(self):
		return self.User
