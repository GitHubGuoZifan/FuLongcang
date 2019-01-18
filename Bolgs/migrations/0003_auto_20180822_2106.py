# Generated by Django 2.0.6 on 2018-08-22 13:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Bolgs', '0002_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='parent_comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='content',
            field=models.TextField(default=1, verbose_name='评论内容'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='date_publish',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='评论时间'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Bolgs.Article', verbose_name='父级评论'),
        ),
    ]
