# Generated by Django 3.2.13 on 2022-12-13 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MBTI', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mbti',
            name='character',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mbti',
            name='summary',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mbti',
            name='board',
            field=models.CharField(choices=[('상대법', '상대법'), ('특징', '특징'), ('주의할 점', '주의할 점')], max_length=50),
        ),
        migrations.AlterField(
            model_name='mbti',
            name='mbti',
            field=models.CharField(choices=[('INTP', 'INTP'), ('ESTP', 'ESTP'), ('INFP', 'INFP'), ('ESFP', 'ESFP'), ('ISFP', 'ISFP'), ('ISTJ', 'ISTJ'), ('ESTJ', 'ESTJ'), ('ENTJ', 'ENTJ'), ('ENFJ', 'ENFJ'), ('INFJ', 'INFJ'), ('ISFJ', 'ISFJ'), ('ENTP', 'ENTP'), ('ISPT', 'ISTP'), ('INTJ', 'INTJ'), ('ESFJ', 'ESFJ'), ('ENFP', 'ENFP')], max_length=50),
        ),
    ]