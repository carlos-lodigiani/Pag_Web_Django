# Generated by Django 3.2.7 on 2021-09-11 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='name',
            new_name='name_of_books',
        ),
        migrations.AddField(
            model_name='book',
            name='name_of_user',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
