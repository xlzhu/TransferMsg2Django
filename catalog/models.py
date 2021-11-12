from django.db import models
from django.urls import reverse
from django.utils import timezone
import uuid

# Create your models here.
class Genre(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class Book(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file.
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    isbn = models.CharField('ISBN',max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title


    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('book-detail', args=[str(self.id)])


class BookInstance(models.Model):
    """
    Model representing a specific copy of a book (i.e. that can be borrowed from the library).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability')

    class Meta:
        ordering = ["due_back"]


    def __str__(self):
        """
        String for representing the Model object
        """
        return '%s (%s)' % (self.id, self.book.title)

class Author(models.Model):
    """
    Model representing an author.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('author-detail', args=[str(self.id)])


    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.last_name, self.first_name)

class Msg(models.Model):
    msg_username = models.CharField(max_length=100,verbose_name = "客户名称")
    msg_userphone = models.CharField(max_length=50,verbose_name = "联系电话")
    msg_userage = models.CharField(max_length=20,verbose_name = "年龄")
    msg_userSIage = models.CharField(max_length=20,verbose_name = "社保")
    msg_useredu = models.CharField(max_length=20,verbose_name = "学历")
    msg_webID = models.CharField(max_length=10)
    msg_url = models.CharField(max_length=200,verbose_name = "来源地址")
    msg_remarks = models.CharField(max_length=200,verbose_name = "备注")
    msg_other = models.CharField(max_length=200)
    msg_datetime = models.DateTimeField(auto_now_add=True,verbose_name = "添加日期")
    """
    姓名、电话、年龄、社保、学历、URL 能够在列表就看到
    列表可以提供按日期筛选并导出功能
    表单提交以后，能够有提示成功，提示语：提交成功，稍后请注意接受信息或电话解答（内容较多时）
    hhmsg.gdedurh.cn
    /www/wwwroot/hhzikao/public_html
    """

    def __str__(self):
        return '%s %s %s %s %s %s %s' % (self.msg_username, self.msg_userphone, self.msg_userage, self.msg_userSIage, self.msg_useredu, self.msg_url, timezone.localtime(self.msg_datetime))

    def display_title(self):
        return '%s %s %s %s %s %s %s' % (self.msg_username, self.msg_userphone, self.msg_userage, self.msg_userSIage, self.msg_useredu, self.msg_url, timezone.localtime(self.msg_datetime))
 