from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100, verbose_name='Пользователь')
    email = models.EmailField(unique=True, verbose_name='Email')
    password = models.CharField(max_length=128, verbose_name='Пароль')
    password_repeat = models.CharField(max_length=128, verbose_name='Повторение пароля')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Регистрация'
        verbose_name_plural = 'Регистрация'


class Events(models.Model):
    date = models.DateField(verbose_name='Дата')
    event_name = models.CharField(max_length=100, verbose_name='Название события')
    year = models.PositiveIntegerField(verbose_name='Год')

    class Meta:
        verbose_name = 'Календарь'
        verbose_name_plural = 'Календарь'

    def __str__(self):
        return f"{self.date} - {self.event_name}"


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages', verbose_name='Отправитель')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages', verbose_name='Получатель')
    subject = models.CharField(max_length=100, verbose_name='Тема')
    body = models.TextField(verbose_name='Текст сообщения')
    sent_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')
    read = models.BooleanField(default=False, verbose_name='Прочитано')
    photo = models.ImageField(upload_to='profile_photos/', blank=True, verbose_name='Фото')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return self.subject


class Profile(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    country = models.CharField(max_length=100, verbose_name='Страна')
    email = models.EmailField()
    phone = models.CharField(max_length=20, verbose_name='номер телефона')
    photo = models.ImageField(upload_to='profile_photos/', blank=True, verbose_name='Фото')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Template(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название Шаблона')
    description = models.TextField(verbose_name='описание')
    photo = models.ImageField(upload_to='profile_photos/', blank=True, verbose_name='Фото')


    def __str__(self):
        return self.name
