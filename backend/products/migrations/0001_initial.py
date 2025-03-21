# Generated by Django 5.1.7 on 2025-03-18 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='product_images/')),
                ('pdf_file', models.FileField(upload_to='product_pdfs/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('hover_image', models.ImageField(blank=True, null=True, upload_to='product_images/')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
