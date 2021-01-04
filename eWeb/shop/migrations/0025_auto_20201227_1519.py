# Generated by Django 3.1.2 on 2020-12-27 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0024_auto_20201222_2344'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=100),
        ),
    ]