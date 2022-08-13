from django.db import models
import string, pytz, datetime
import random



## characters to generate password from


def generate_random_password():
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
    ## length of password from the user
    length = 15

    ## shuffling the characters
    random.shuffle(characters)

    ## picking random characters from the list
    password = []
    for i in range(length):
        password.append(random.choice(characters))

    ## shuffling the resultant password
    random.shuffle(password)

    ## converting the list to string
    ## printing the list
    return "".join(password)



# Create your models here.
class Levels(models.Model):
    name = models.CharField(verbose_name="المرحلة", max_length=254)

    def __str__(self):
        return self.name + " | id :" + str(self.id)
    
class BlodsType(models.Model):
    blodTypeName = models.CharField(verbose_name="فصيلة الدم", max_length=254)
    
    def __str__(self):
        return self.blodTypeName + " | id :" + str(self.id)
    
class UserProfile(models.Model):
    username = models.CharField(verbose_name="اسم الطالب", max_length=254)
    school = models.CharField(verbose_name="اسم المدرسة", max_length=254)
    level = models.ForeignKey(Levels, related_name="levels", verbose_name="المرحلة", on_delete=models.SET_NULL, null=True)
    born = models.CharField(verbose_name="المواليد", max_length=254)
    GuardianNumber = models.CharField(verbose_name="رقم ولي الامر واتس اب", max_length=254, blank=True, null=True)
    importentNumber = models.CharField(verbose_name="رقم اخر ولي الامر مهم", max_length=254, blank=True, null=True)
    blodType = models.ForeignKey(BlodsType, verbose_name="فصيلة الدم", related_name="blodType", on_delete=models.SET_NULL, null=True)
    diseases = models.CharField(verbose_name="الامراض المزمنة", max_length=254, blank=True, null=True)
    note = models.TextField(verbose_name="ملاحظات مهمة", blank=True, null=True)
    pass_id = models.CharField(verbose_name="كلمة المرور عند المرور", max_length=254, default=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5)), unique=True)
    is_Enabled = models.BooleanField(default=True, verbose_name="هل هذا الملف الشخصي مفعل")
    created_date = models.DateTimeField(default=datetime.datetime.now(pytz.timezone('Asia/Baghdad')), verbose_name="تاريخ انشاء الملف الشخصي", null=True)
    def __str__(self):
        return self.username + " | id :" + str(self.id)
    class Meta:
        ordering = ['-created_date']

class PassData(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="ملف الشخصي للمستخدم", on_delete=models.CASCADE)
    username = models.CharField(max_length=254, verbose_name="اسم الطالب")
    school = models.CharField(verbose_name="اسم المدرسة", max_length=254)
    GuardianNumber = models.CharField(verbose_name="رقم ولي الامر", max_length=254)
    is_Definded = models.BooleanField(verbose_name="هل هو موجود في جهات الاتصال واتساب", default=False)
    passDate = models.DateTimeField(default=datetime.datetime.now(pytz.timezone('Asia/Baghdad')), verbose_name="تاريخ المرور")
    is_sended = models.BooleanField(default=False, verbose_name="هل تم ارسال الرسالة عبر الواتس")
    
    def __str__(self):
        return self.username

class DefindedNumbers(models.Model):
    number = models.CharField(max_length=254, verbose_name="الرقم")
    
    def __str__(self):
        return self.number