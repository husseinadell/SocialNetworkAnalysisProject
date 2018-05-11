from django.contrib import admin

from .models import User
from .models import Post
from .models import Group
from .models import Comment
from .models import Like
from .models import friendShip
from .models import groupMembers

admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Group)
admin.site.register(User)
admin.site.register(Post)
admin.site.register(friendShip)
admin.site.register(groupMembers)
