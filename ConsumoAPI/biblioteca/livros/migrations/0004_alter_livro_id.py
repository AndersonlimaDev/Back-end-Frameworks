# Generated by Django 4.1.7 on 2023-05-28 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0003_alter_livro_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
