import os
from datetime import datetime, timedelta

from django.contrib.auth.models import AbstractUser
from django.contrib.sites.models import Site
from django.db import models
from django.template.defaultfilters import slugify
from tinymce.models import HTMLField

from core.enums import UserTypes, MediaTypes, SocialMediaTypes, SocialMediaUrls, SocialMediaIcons
from timi import main_settings
from django.core.cache import cache
from timi.main_settings import BASE_DIR
from core.utils import format_phone_number


def image_directory(instance, filename):
    split = filename.split('.')
    filename = slugify(instance.name) + '.' + split[1]
    return 'content/{0}'.format(filename)


def user_avatar_directory(instance, filename):
    split = filename.split('.')
    filename = instance.username + '.' + split[1]
    return '{0}/avatar/{1}'.format(instance.get_user_type_display().lower(), filename)


def media_file_directory(instance, filename):
    return '{0}/{1}'.format(slugify(instance.get_media_type_display().lower()), filename)


def media_thumbnail_directory(instance, filename):
    return '{0}/thumbnail/{1}'.format(slugify(instance.get_media_type_display().lower()), filename)


def remove_old_file_save(instance):
    for field in instance._file_watch_list:
        try:
            orig = '_original_%s' % field
            if getattr(instance, orig) != getattr(instance, field):
                os.remove(os.path.join(BASE_DIR, getattr(instance, orig).path))
        except Exception as e:
            print(str(e))


def remove_old_file_delete(instance):
    for field in instance._file_watch_list:
        try:
            getattr(instance, field).delete()
        except Exception as e:
            print(str(e))


# Create your models here.


class Setting(models.Model):
    site = models.OneToOneField(Site, on_delete=models.CASCADE, db_column="site")
    name = models.CharField(max_length=50, default="Embed Systems")
    number = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    address = models.TextField(null=True, blank=True)

    favicon = models.ImageField('Icon that shows on browser tabs', upload_to='settings/favicon/', null=True, blank=True)
    logo_default = models.ImageField('Dark Logo Version', upload_to='settings/logo/', null=True, blank=True)
    logo_light = models.ImageField('White Logo Version', upload_to='settings/logo/', null=True, blank=True)
    summary = models.TextField('A brief description of what the company is about', null=True, blank=True)

    index_page_background = models.ImageField('Index Page: Background image', upload_to='settings/index/', null=True,
                                              blank=True)

    about_page_name = models.CharField('About Page: Name ex. Dr. Timileyin Adebayo', max_length=100, null=True,
                                       blank=True)
    about_page_position = models.CharField('About Page: Position ex. CEO, Lead Engineer', max_length=100, null=True,
                                           blank=True)
    about_page_photo = models.ImageField('About Page: Image', upload_to='settings/about/', null=True, blank=True)
    about_page_quote = models.CharField('About Page: Quote', max_length=100, null=True, blank=True)
    about_page_text = HTMLField('About Page: Text', null=True, blank=True)

    first_slider_title = models.CharField(max_length=30, help_text='Slider 1 title', null=True, blank=True)
    first_slider_content = models.CharField(max_length=100, help_text='Slider 1 content', null=True, blank=True)
    second_slider_title = models.CharField(max_length=30, help_text='Slider 2 title', null=True, blank=True)
    second_slider_content = models.CharField(max_length=100, help_text='Slider 2 content', null=True, blank=True)
    third_slider_title = models.CharField(max_length=30, help_text='Slider 3 title', null=True, blank=True)
    third_slider_content = models.CharField(max_length=100, help_text='Slider 3 content', null=True, blank=True)

    service_text = models.TextField('Home Page: What we do text', null=True, blank=True)

    portfolio_page_text = models.TextField('Portfolio Page: Top Text', null=True, blank=True)

    class Meta:
        db_table = 'settings'

    def __str__(self):
        return self.name

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._file_watch_list = ['favicon', 'logo_default', 'logo_light', 'index_page_background', 'about_page_photo']
        for field in self._file_watch_list:
            setattr(self, '_original_%s' % field, getattr(self, field))

    def save(self, *args, **kwargs):
        try:
            self.number = format_phone_number(self.number)
            remove_old_file_save(self)
        except:
            pass
        super(Setting, self).save(*args, **kwargs)

    def delete(self, **kwargs):
        remove_old_file_delete(self)
        super(Setting, self).delete(**kwargs)


class SocialMedia(models.Model):
    setting = models.ForeignKey(Setting, on_delete=models.CASCADE, related_name='socials', db_column="setting")
    social_media_type = models.IntegerField(choices=SocialMediaTypes.choices())
    handle = models.CharField(max_length=100)
    url = models.URLField('Do not edit, value is automatic', null=True, blank=True, editable=False)
    icon = models.CharField('Do not edit, value is automatic', max_length=50, null=True, blank=True, editable=False)

    class Meta:
        db_table = 'social_media'

    def __str__(self):
        return self.handle

    def save(self, *args, **kwargs):
        url = SocialMediaUrls.get_name(self.social_media_type)
        self.url = f"{url}{self.handle}"
        icon = SocialMediaIcons.get_name(self.social_media_type)
        self.icon = f"{icon}"
        super(SocialMedia, self).save(*args, **kwargs)


class Category(models.Model):
    # group = models.ForeignKey(Group, on_delete=models.CASCADE, db_column='group')
    name = models.CharField('', max_length=100)
    slug = models.SlugField('Do not edit, value is automatic', unique=True, editable=False)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = 'category'
        ordering = ['-created_at']
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Service(models.Model):
    setting = models.ForeignKey(Setting, on_delete=models.CASCADE, related_name='services', db_column="setting")
    title = models.CharField('Title of the service', max_length=100)
    sub_title = models.CharField('Sub title of the service', max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='services/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = 'service'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._file_watch_list = ['image']
        for field in self._file_watch_list:
            setattr(self, '_original_%s' % field, getattr(self, field))

    def save(self, *args, **kwargs):
        remove_old_file_save(self)
        super(Service, self).save(*args, **kwargs)

    def delete(self, **kwargs):
        remove_old_file_delete(self)
        super(Service, self).delete(**kwargs)


class Project(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='projects', db_column="category")
    title = models.CharField('Title of the project', max_length=200)
    slug = models.SlugField('Do not edit, value is automatic', unique=True, editable=False)
    image = models.ImageField(upload_to='projects/')
    content = HTMLField('Project Page Content', null=True, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = 'project'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._file_watch_list = ['image']
        for field in self._file_watch_list:
            setattr(self, '_original_%s' % field, getattr(self, field))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        remove_old_file_save(self)
        super(Project, self).save(*args, **kwargs)

    def delete(self, **kwargs):
        remove_old_file_delete(self)
        super(Project, self).delete(**kwargs)


class User(AbstractUser):
    user_type = models.IntegerField(choices=UserTypes.choices(), null=True,
                                    blank=True)
    number = models.CharField(unique=True, max_length=13, null=True, blank=True)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to=user_avatar_directory, default='user.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = 'user'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.get_full_name()}'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._file_watch_list = ['avatar', ]
        for field in self._file_watch_list:
            setattr(self, '_original_%s' % field, getattr(self, field))

    def save(self, *args, **kwargs):
        try:
            self.number = format_phone_number(self.number)
            if self.user_type == UserTypes.SUPERUSER:
                self.is_staff = True
                self.is_superuser = True
            remove_old_file_save(self)
        except:
            pass
        super(User, self).save(*args, **kwargs)

    def delete(self, **kwargs):
        remove_old_file_delete(self)
        super(User, self).delete(**kwargs)

    def last_seen(self):
        return cache.get('seen_%s' % self.username)

    def online(self):
        if self.last_seen():
            now = datetime.now()
            if now > self.last_seen() + timedelta(
                    seconds=main_settings.USER_ONLINE_TIMEOUT):
                return False
            else:
                return True
        else:
            return False


class UserSetting(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, db_column='user')
    receive_email = models.BooleanField(default=True)
    receive_sms = models.BooleanField(default=True)
    enable_music = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = 'user_setting'

    def __str__(self):
        return f'{self.user}\'s settings'


class OTP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, db_column='user')
    code = models.CharField(max_length=6, default='000000')
    expiry = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    status = models.BooleanField(default=False)

    class Meta:
        db_table = 'otp'

    def __str__(self):
        return f'{self.user}\'s otp - {self.code}'


class Media(models.Model):
    media_type = models.IntegerField(choices=MediaTypes.choices(), default=MediaTypes.IMAGE)
    file = models.FileField(upload_to=media_file_directory)
    thumbnail = models.ImageField(upload_to=media_thumbnail_directory, null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = 'media'

    def __str__(self):
        return f'{self.title}'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._file_watch_list = ['file']
        for field in self._file_watch_list:
            setattr(self, '_original_%s' % field, getattr(self, field))

    def save(self, *args, **kwargs):
        remove_old_file_save(self)
        super(Media, self).save(*args, **kwargs)

    def delete(self, **kwargs):
        remove_old_file_delete(self)
        super(Media, self).delete(**kwargs)

    @property
    def extension(self):
        name, extension = os.path.splitext(self.file.name)
        return extension.replace('.', '')
