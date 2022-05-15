from django.db import models

# Create your models here.

class Brand(models.Model):
    brand_title = models.CharField(max_length=150,verbose_name="Название модел", help_text="Mersedes Benz" )

    def __str__(self):
        return self.brand_title

    class Meta:
        verbose_name = "название машину"
        verbose_name_plural= "Название машины"

class Fuel(models.Model):
    fuels = models.CharField(max_length=150, verbose_name="Тип топлива", help_text="Безин,Газ,Дизел,Электомобил")

    def __str__(self):
        return self.fuels

    class Meta:
        verbose_name = "Тип топлива"
        verbose_name = "Типы топлива"

class Transmission(models.Model):
    type_transmission = models.CharField(max_length=150,verbose_name="Тип коробка передача", help_text="Auto")
    
    def __str__(self):
        return self.type_transmission

    class Meta:
        verbose_name = "Тип коробки передач"
        verbose_name = "Типы коробок передач"

class DriveType(models.Model):
    type_drive = models.CharField(max_length=150,verbose_name="Привод Машин", help_text="Передний,Задний,4x4")

    def __str__(self):
        return self.type_drive

    class Meta:
        verbose_name = "Тип привода"
        verbose_name = "Типы приводов"

class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Название машин", help_text="Mersedes")
    fuel_type = models.ForeignKey(Fuel, on_delete=models.CASCADE, verbose_name="Тип топлива", related_name="car_fuel_type")
    drive_type = models.ForeignKey(DriveType, on_delete=models.CASCADE, verbose_name="Привод машин", help_text="Передний")
    transmission = models.ForeignKey(Transmission, on_delete=models.CASCADE, verbose_name="Тип коробка передача", help_text="Auto & Stick")
    mileage = models.PositiveIntegerField(default=0, verbose_name="Пробег", help_text="123456")
    year = models.PositiveIntegerField(default=2000, verbose_name="Год выпуск", help_text="2001")
    color = models.CharField(max_length=150,verbose_name="Цвет машин", help_text="Black")
    color_interior = models.CharField(max_length=150,verbose_name="Цвет интерьера", help_text="Black and White")
    vin = models.CharField(max_length=150,verbose_name="VIN номер", help_text="ABCDEFG123")
    engine = models.CharField(max_length=150,verbose_name="Двигатель", help_text="V8  4.7")


    def __str__(self):
        return self.brand

    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машины"