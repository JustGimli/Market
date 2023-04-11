from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Boolean, Text

metadata = MetaData()

table_item = Table('ShopItems', metadata,
                   Column('id', Integer, primary_key=True, nullable=False),
                   Column('name', String(50)),
                   Column('price', Integer),
                   Column('description', Text, default='None'),
                   Column('isActive', Boolean, default=True),
                   )

user = Table('Users', metadata,
             Column('id', Integer, primary_key=True),
             Column('name', String(40), nullable=False),
             Column('surname', String(40), nullable=False),
             Column('phone', String(10), nullable=False),
             Column('isAdmin', Boolean, default=False),
             )

login_data = Table('Logins', metadata,
                   Column('id', Integer, ForeignKey('Users.id')),
                   Column('login', String(50), nullable=False),
                   Column('password', String(150), nullable=False)
                   )
