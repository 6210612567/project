from django.db import models




# Model for custom field
class CustomGradeField(models.Model):
    name = models.CharField(max_length=100 ,blank=False, null=False)
    value = models.CharField(max_length=255,blank=True, null=True)

    @property
    def context_data(self):
        return {
            'name': self.name,
            'value': self.value,

        }

    def __str__(self):
        return f"Name : {self.name} Value : {self.value}"


# Model for grade
class Grade(models.Model):
    name = models.CharField(max_length=100 ,blank=False, null=False)
    subject = models.CharField(max_length=100 ,blank=False, null=False)
    grade = models.CharField(max_length=100)
    midterm = models.CharField(max_length=100)
    final = models.CharField(max_length=100)
    customfield = models.ManyToManyField(CustomGradeField)

    # @property
    # def context_data(self):
    #     return {
    #         'name': self.name,
    #         'desc': self.desc,
    #         'status': self.status,
    #         'user': self.user,

    #     }

    def __str__(self):
        return f"Name : {self.name} Subject : {self.subject} Grade : {self.grade} Midterm : {self.midterm} Final : {self.final} Customfield : {self.customfield}"