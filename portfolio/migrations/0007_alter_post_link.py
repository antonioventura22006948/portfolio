# Generated by Django 4.0.4 on 2022-05-28 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_post_image_alter_post_link_alter_project_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
