from django.db import connection
from functions import dictfetchall

def get_notification_detail(self, user_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT *
            FROM notification
            WHERE user_id = %s;
        """, [user_id])
        data = dictfetchall(cursor)
    return {"data": data}

def add_notification(self, data):
    text = data['text']
    url = data['url']
    user_id = data['user_id']

    with connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO notification (text, url, user_id)
            VALUES (%s, %s, %s)
            """, [text, url, user_id])
    return 0

def delete_notification(self, id):
    with connection.cursor() as cursor:
        cursor.execute("""
            DELETE FROM notification
            WHERE notification_id = %s
        """, [id])
    return 0