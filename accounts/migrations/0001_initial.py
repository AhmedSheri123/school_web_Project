# Generated by Django 4.0.5 on 2022-06-09 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=254, verbose_name='اسم الطالب')),
                ('school', models.CharField(max_length=254, verbose_name='اسم المدرسة')),
                ('born', models.CharField(max_length=254, verbose_name='المواليد')),
                ('GuardianNumber', models.CharField(max_length=254, verbose_name='رقم ولي الامر')),
                ('importentNumber', models.CharField(max_length=254, verbose_name='رقم اخر مهم')),
                ('diseases', models.CharField(max_length=254, verbose_name='الامراض المزمنة')),
                ('note', models.TextField(verbose_name='ملاحظات مهمة')),
            ],
        ),
    ]