# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-11 15:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('wagtailcore', '0040_page_draft_title'),
        ('opensource_clubs', '0012_auto_20170911_1306'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourcesPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('heading_text', wagtail.wagtailcore.fields.RichTextField(blank=True, verbose_name='Text')),
                ('mentors_description', wagtail.wagtailcore.fields.StreamField((('info', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(help_text='General content field, appropriate for questions, titles etc (max 150 chars)', max_length=150)), ('text', wagtail.wagtailcore.blocks.RichTextBlock(blank=True, default='', help_text='WYSIWYG Editor for general purpose content, (max 1000 chars)', max_length=1000, required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(help_text='Optional field - accepts a URL (max 200 chars)', max_length=200, required=False)), ('link_title', wagtail.wagtailcore.blocks.CharBlock(help_text='Optional field - Title of the link, (max 100 chars)', max_length=100, required=False))), required=True)),))),
                ('resources_title', models.CharField(blank=True, default='', max_length=50, verbose_name='Title')),
                ('resources_cta_text', models.CharField(blank=True, default='', max_length=50, verbose_name='CTA Text')),
                ('resources_cta_link', models.URLField(blank=True, default='', verbose_name='Link')),
                ('guides', wagtail.wagtailcore.fields.RichTextField(blank=True, verbose_name='Guides')),
                ('heading_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AddField(
            model_name='clubprofile',
            name='is_mentor',
            field=models.BooleanField(default=False),
        ),
    ]
