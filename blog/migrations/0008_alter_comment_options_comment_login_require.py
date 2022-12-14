# Generated by Django 4.1 on 2022-12-06 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_date']},
        ),
        migrations.AddField(
            model_name='comment',
            name='login_require',
            field=models.BooleanField(default=False),
        ),
    ]
