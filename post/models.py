from django.db import models
from users.models import User
# Create your models here.
class Post(models.Model):
    class Meta:
        db_table = 'post'
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256,null=False)
    postdate = models.DateTimeField(null=False)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __repr__(self):
        return "<post>:{}{}{}".format(self.title,self.postdate,self.author)
    __str__ = __repr__
class Content(models.Model):
    class Meta:
        db_table = 'content'
    title = models.OneToOneField(Post,on_delete=models.CASCADE)
    content = models.TextField(null=False)

    def __repr__(self):
        return "<content>:{}{}".format(self.title,self.content[0:20])
    __str__ = __repr__