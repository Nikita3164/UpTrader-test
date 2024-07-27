from django.db import models

# Create your models here.
class Menu(models.Model):
    menu_name = models.TextField()
    lvl_1 = models.TextField()
    lvl_2 = models.TextField()
    lvl_2_ref = models.TextField()
    class Meta:
        db_table = 'Menu'

    def __str__(self):
        return f"Меню {self.menu_name}: пункт 1-го ур. {self.lvl_1}, пункт 2-го ур. {self.lvl_2}"
