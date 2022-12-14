# Generated by Django 3.2.13 on 2022-12-14 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mbti', '0002_auto_20221214_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mbti',
            name='board',
            field=models.CharField(choices=[('상대법', '상대법'), ('주의할 점', '주의할 점'), ('특징', '특징')], max_length=50),
        ),
        migrations.AlterField(
            model_name='mbti',
            name='mbti',
            field=models.CharField(choices=[('ENTJ', 'ENTJ'), ('ISFP', 'ISFP'), ('ESTP', 'ESTP'), ('INFJ', 'INFJ'), ('ENFP', 'ENFP'), ('ISFJ', 'ISFJ'), ('ISTP', 'ISTP'), ('INTJ', 'INTJ'), ('ESFP', 'ESFP'), ('ENFJ', 'ENFJ'), ('ISTJ', 'ISTJ'), ('INTP', 'INTP'), ('ESTJ', 'ESTJ'), ('ENTP', 'ENTP'), ('ESFJ', 'ESFJ'), ('INFP', 'INFP')], max_length=50),
        ),
    ]