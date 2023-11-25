from django.db import models
from django.urls import reverse
from django.utils.html import format_html
from django.utils.text import slugify


class Message(models.Model):
    name = models.CharField(max_length=57, verbose_name="نام")
    email = models.EmailField(verbose_name="ایمیل")
    title = models.CharField(max_length=107, verbose_name="عنوان")
    body = models.TextField(verbose_name="بدنه")
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name="ایجاد شده")

    class Meta:
        verbose_name = "پیام"
        verbose_name_plural = "پیام ها"

    def __str__(self):
        return self.title


class ProjectCategories(models.Model):
    title = models.CharField(max_length=50, verbose_name="عنوان")
    created = models.DateTimeField(auto_now_add=True, verbose_name="ایجاد شده")

    class Meta:
        verbose_name = "دسته بندی پروژه"
        verbose_name_plural = "دسته بندی های پروژه"

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=50, verbose_name="عنوان")
    category = models.ManyToManyField(ProjectCategories, related_name='projects', verbose_name="دسته بندی")
    image = models.ImageField(upload_to='projects/images', verbose_name="عکس")
    image2 = models.ImageField(upload_to='projects/images', verbose_name="عکس 2")
    image3 = models.ImageField(upload_to='projects/images', verbose_name="عکس 3")
    image4 = models.ImageField(upload_to='projects/images', verbose_name="عکس 4")
    image5 = models.ImageField(upload_to='projects/images', verbose_name="عکس 5")
    image6 = models.ImageField(upload_to='projects/images', verbose_name="عکس 6")
    image7 = models.ImageField(upload_to='projects/images', verbose_name="عکس 7")
    body = models.TextField(verbose_name="بدنه")
    extra_details = models.TextField(verbose_name="جزئیات بیشتر")
    created = models.DateTimeField(auto_now_add=True, verbose_name="ایجاد شده")
    updated = models.DateTimeField(auto_now=True, verbose_name="به روز شده")
    customer = models.CharField(max_length=50, verbose_name="مشتری")
    about_customer = models.TextField(verbose_name="درباره مشتری")
    status = models.BooleanField(default=True, verbose_name="وضعیت")
    slug = models.SlugField(blank=True, null=True, unique=True, verbose_name="اسلاگ")

    class Meta:
        verbose_name = "پروژه"
        verbose_name_plural = "پروژه ها"

    def save(self, force_insert=False, force_update=False,
             using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(Project, self).save()

    def show_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="47px" height="37px">')
        else:
            return format_html('<h3 style="color: red">بدون تصویر</h3>')

    show_image.short_description = ' تصویر'

    def get_absolut_url(self):
        return reverse('blog:article_details', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
