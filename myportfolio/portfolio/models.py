from django.db import models

class Detail(models.Model):
  name = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)

  def __str__(self):
        return f"{self.name}{self.phone}"
  
class Contact(models.Model):
      detail = models.ForeignKey(Detail, on_delete=models.CASCADE),
      name = models.CharField(max_length=255)
      email = models.CharField(max_length=100)
      wa = models.IntegerField(null=True)

      def __str__(self):
            return f"{self.name}{self.email}"
          
     