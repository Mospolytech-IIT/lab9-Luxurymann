from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Создаем базу данных
engine = create_engine('sqlite:///database.db', echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    password = Column(String(100))

    # Связь с постами
    posts = relationship("Post", back_populates="author")

class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    content = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))

    # Обратная связь с автором поста
    author = relationship("User", back_populates="posts")

# Создаем таблицы
Base.metadata.create_all(engine)

# Инициализация сессии
Session = sessionmaker(bind=engine)
session = Session()

