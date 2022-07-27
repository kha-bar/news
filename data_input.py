# python manage.py sqlflush



from django.db import models
from django.contrib.auth.models import User

from news_2.models import *


User.objects.create_user(username='username1', password='username1')
User.objects.create_user(username='username2', password='username2')


LocalUser.objects.create_user(username='author1', password='author1')
LocalUser.objects.create_user(username='author2', password='author2')


Author.objects.create(author_user_id=24)
Author.objects.create(author_user_id=25)


Category.objects.create(name_category='Спорт')
Category.objects.create(name_category='Политика')
Category.objects.create(name_category='Образование')
Category.objects.create(name_category='Культура')


Post.objects.create(post_type=Post.news, post_author_id=1, post_text='''Согласно имеющимся данным,
мессенджер JusTalk быстро развивается и в настоящее время им пользуются более
20 млн человек по всему миру. Сервис убеждает пользователей в использовании
сквозного шифрования, благодаря чему пересылаемые данные доступны только участникам чатов.
На официальном сайте мессенджера сказано, что даже сотрудники JusTalk не имеют доступа
к пересылаемым пользователями данным.''')

Post.objects.create(post_type=Post.news, post_author_id=1, post_text='''Однако утечка большого количества данных указывает на то, что заявления JusTalk о высоком
уровне защите данных не соответствуют действительности. Об этом говорят миллионы сообщений
пользователей сервиса, оказавшиеся в свободном доступе. Помимо текста посланий, указана точная
дата их отправления, а также телефонные номера отправителей и получателей. В дополнение к этому
утечка содержит немало записей видеозвонков, сделанных через приложение JusTalk.''')

Post.objects.create(post_type=Post.title, post_author_id=2, post_text='''Специалист по информационной безопасности Анураг Сен (Anurag Sen), который первым обнаружил
утечку данных пользователей JusTalk, пытался связаться с разработчиком мессенджера в лице
китайской компании Juphoon. Там ему сообщили, что в настоящее время сервис принадлежит компании
Ningbo Jus, с представителями которой пока связаться не удалось. Исследователь отмечает,
что обнаруженный им кеш также содержит данные пользователей детского приложения JusTalk Kids
и JusTalk Phone Number, которое позволяет генерировать виртуальные телефонные номера.''')


Post.objects.get(id=1).post_category.add(Category.objects.get(id=2))
Post.objects.get(id=1).post_category.add(Category.objects.get(id=4))
Post.objects.get(id=2).post_category.add(Category.objects.get(id=3))


Comment.objects.create(comment_text='ok', post_id=2, user_id=22)
Comment.objects.create(comment_text='ssoosos', post_id=2, user_id=23)
Comment.objects.create(comment_text='okdddddd', post_id=1, user_id=24)
Comment.objects.create(comment_text='odfggfk', post_id=3, user_id=25)


Post.objects.get(id=1).like()
Post.objects.get(id=1).dislike()

Comment.objects.get(id=1).like()
Comment.objects.get(id=1).dislike()

Author.objects.get(id=1).update_rating_author()
Author.objects.get(id=2).update_rating_author()


Author.objects.all().aggregate(Max('_author_rating')).filter(user__username='username')

User.objects.filter(localuser__user_ptr=id('username')).filter(author__author_user=id('username')).aggregate(Max('_author_rating')).values('username', 'author_rating')

Author.objects.filter(user__id=id('author_user'))


Author.objects.filter(Author.objects.aggregate(Max('_author_rating'))).values()





