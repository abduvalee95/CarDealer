from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(max_length=255,verbose_name="Название", help_text="названия компанию")
    logo = models.ImageField(upload_to="logo/",verbose_name="Логотип")
    logo2 = models.ImageField(upload_to="logo/",verbose_name="Логотип2", blank=True)
    adress = models.CharField(max_length=255)
    tel = models.CharField(max_length=50)
    work_time = models.CharField(max_length=100, verbose_name="Время работа", help_text="09:00 - 20:00, ПН-ПТ")


    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Настройка"
        verbose_name_plural="Настройки"
