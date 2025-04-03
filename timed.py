# Добавляем пользователей
user1 = User(username='alice', email='alice@example.com', password='password')
user2 = User(username='bob', email='bob@example.com', password='secret')

# Добавляем посты
post1 = Post(title='First post', content='This is my first post!', user=user1)
post2 = Post(title='Second post', content='This is another post.', user=user2)

# Сохраняем изменения в базу данных
session.add(user1)
session.add(user2)
session.add(post1)
session.add(post2)
session.commit()