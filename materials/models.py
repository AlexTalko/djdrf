from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название курса', help_text='Укажите название курса')
    image = models.ImageField(upload_to='course/images', verbose_name='картинка',
                              help_text='Добавьте превью изображения', **NULLABLE)
    description = models.TextField(verbose_name='описание курса', help_text='Укажите описание курса')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name="Автор")
    link = models.URLField(max_length=300, verbose_name="ссылка на видео", help_text="Укажите ссылку", **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'
        permissions = [
            ('can_view_course', 'Может просматривать курсы'),
            ('can_edit_course', 'Может редактировать курсы'),
        ]


class Lesson(models.Model):
    title = models.CharField(max_length=200, verbose_name='название урока', help_text='Укажите название урок')
    description = models.TextField(verbose_name='описание урока', help_text='Укажите описание урока')
    image = models.ImageField(upload_to='lesson/images', verbose_name='картинка',
                              help_text="Добавьте превью изображения", **NULLABLE)
    link = models.URLField(max_length=300, verbose_name='ссылка на видео', help_text='Укажите ссылку', **NULLABLE)
    course = models.ForeignKey('Course', on_delete=models.SET_NULL, verbose_name='Название курса',
                               help_text='Выберите курс', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name="Автор")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
        permissions = [
            ('can_view_lesson', 'Может просматривать уроки'),
            ('can_edit_lesson', 'Может редактировать уроки'),
        ]


class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
    course = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name='Курс')

    def __str__(self):
        return f'{self.user.email} - {self.course.title}'

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
