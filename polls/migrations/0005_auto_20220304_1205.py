# Generated by Django 2.0 on 2022-03-04 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='produto',
            name='categoria',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='polls.Categoria'),
            preserve_default=False,
        ),
    ]