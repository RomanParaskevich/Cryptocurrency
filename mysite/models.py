from django.db import models


class Sorting(models.Model):
    sort = models.IntegerField(null=True, blank=True)

    class Meta:
        abstract = True


class Header(Sorting):
    description = models.CharField(max_length=50, verbose_name='Название')
    url = models.CharField(max_length=124)

    class Meta:
        ordering = ['sort']

    def __str__(self):
        return self.description


class Advertising(Sorting):
    header = models.CharField(max_length=124, verbose_name='Заголовок')
    description = models.CharField(max_length=124, verbose_name='Описание')
    image = models.FileField(upload_to='uploads/', blank=True, verbose_name='Иконка')
    alt = models.CharField(max_length=124, blank=True)

    class Meta:
        verbose_name = 'Преимущества'
        verbose_name_plural = 'Преимущества'
        ordering = ['sort']

    def __str__(self):
        return self.header


class Coins(models.Model):
    header = models.CharField(max_length=124, verbose_name='Заголовок')
    tag = models.CharField(max_length=124)
    description = models.CharField(max_length=1240, verbose_name='Описание')
    image = models.FileField(upload_to='uploads/', verbose_name='Иконка')
    url = models.CharField(max_length=124, blank=True)
    div_class = models.CharField(max_length=124, blank=True)
    alt = models.CharField(max_length=124, blank=True)
    card_information_title = models.CharField(max_length=124, blank=True)
    p_class = models.CharField(max_length=124, blank=True)
    card_info = models.CharField(max_length=124, blank=True)

    class Meta:
        verbose_name = 'Монеты'
        verbose_name_plural = 'Монеты'

    def __str__(self):
        return self.header


class MainInfo(Sorting):
    header = models.CharField(max_length=124, verbose_name='Заголовок')
    description = models.CharField(max_length=1240, verbose_name='Описание')
    url = models.CharField(max_length=124, blank=True)

    class Meta:
        verbose_name = 'Информация'
        verbose_name_plural = 'Информация'
        ordering = ['sort']

    def __str__(self):
        return self.header


class Footer(Sorting):
    description = models.CharField(max_length=124)
    div_class = models.CharField(max_length=124, blank=True)
    ul_class = models.CharField(max_length=124, blank=True)

    class Meta:
        ordering = ['sort']

    def __str__(self):
        return self.description


class InlineFooter(Sorting):
    header = models.CharField(max_length=124, verbose_name='Заголовок')
    url = models.CharField(max_length=124)
    footer = models.ForeignKey(Footer, on_delete=models.CASCADE, related_name='inline')
    image = models.FileField(upload_to='uploads/', blank=True, verbose_name='Иконка')
    li_class = models.CharField(max_length=124, blank=True)

    class Meta:
        ordering = ['sort']

    def __str__(self):
        return self.header


class SocialNetworks(Sorting):
    header = models.CharField(max_length=124, verbose_name='Заголовок')
    url = models.CharField(max_length=124)
    image = models.FileField(upload_to='uploads/', verbose_name='Иконка', blank=True)

    class Meta:
        ordering = ['sort']

    def __str__(self):
        return self.header


class Subscribers(models.Model):
    email = models.EmailField()

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписка'

    def __str__(self):
        return self.email


class Mail(models.Model):
    title = models.CharField(max_length=124)
    text = models.TextField()

    def __str__(self):
        return self.title


class Sender(models.Model):
    sender = models.CharField(max_length=124)
    password = models.CharField(max_length=124)
    smtp_server = models.CharField(max_length=124)
    port = models.IntegerField()

    class Meta:
        verbose_name = 'Отправитель рассылки'
        verbose_name_plural = 'Отправитель рассылки'

    def __str__(self):
        return self.sender
