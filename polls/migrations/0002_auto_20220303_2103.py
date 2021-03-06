# Generated by Django 2.0 on 2022-03-03 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nomeMarca', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='produto',
            name='marca',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='polls.Marca'),
            preserve_default=False,
        ),
    ]
