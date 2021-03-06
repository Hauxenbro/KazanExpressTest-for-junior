# Generated by Django 4.0.4 on 2022-05-28 13:06

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('amount', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('images', models.ImageField(blank=True, null=True, upload_to='Product_images/')),
                ('active', models.BooleanField(default=False)),
                ('description', models.ManyToManyField(to='API.category')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('imageUrl', models.ImageField(blank=True, null=True, upload_to='shop_photos/')),
                ('description', models.ManyToManyField(blank=True, related_name='shop_products', to='API.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='shop',
            field=models.ManyToManyField(to='API.shop'),
        ),
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.ManyToManyField(blank=True, related_name='category_products', to='API.product'),
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='API.category'),
        ),
    ]
