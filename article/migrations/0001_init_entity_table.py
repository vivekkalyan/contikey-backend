# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 07:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
      ('channel', '0001_init_entity_table')
    ]

    operations = [
      migrations.RunSQL(
        """CREATE TABLE article (
            article_id INT AUTO_INCREMENT PRIMARY KEY,
            url VARCHAR(500) NOT NULL,
            caption VARCHAR(500),
            preview_image VARCHAR(500),
            preview_title VARCHAR(100),
            preview_text VARCHAR(500),
            channel_id INT,
            shared_from_article_id INT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (channel_id) REFERENCES channel(channel_id)
                ON UPDATE CASCADE
                ON DELETE SET NULL,
            FOREIGN KEY (shared_from_article_id) REFERENCES article(article_id)
                ON UPDATE CASCADE
                ON DELETE SET NULL,
            CONSTRAINT different_article CHECK (shared_from_article_id != article_id)
        );""",
        "DROP TABLE article"
      )
    ]