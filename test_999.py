import psycopg2
import random as rd

bd_password = input("Введите пароль от Базы Данных: ")

postgres = psycopg2.connect(
    dbname='main',
    user='postgres',
    password=f'{bd_password}',
    host='localhost'
)

cursor = postgres.cursor()

product_types = (
    '(\'Molochnoe\')',
    '(\'Vipechka\')',
    '(\'Shokolad\')',
    '(\'Alkogol\')',
    '(\'Ovoshi\')',
    '(\'Frukti\')',
)



catalog = {
    "molochnoe": ('Airan','Kaimak','Moloko','Kumis','Shoro','Cheese','Yougurt',),
    "vipechka": ('Hleb','Bulochki','Pizza','Boorsoki','Pirojki','Chebureki','Cakes',),
    "shokolad": ('Snikers','Twix','Kit Kat','Yashkino','Nutella','Alpen Gold','Bounty',),
    "alkogol": ('Whiskey','Rom','Vodka','Pivo','Kaniyak','Liker','Vino',),
    "ovoshi": ('Pomidori','Piyaz','Kartoshka','Morkovka','Baklajani','Tikva','Redka',),
    "frukti": ('Yabloki','Vishnya','Bananni','Ananas','Mango','Kivi','Grushi',),
}

product_types_table = '''CREATE TABLE product_types(
    product_type_id SERIAL PRIMARY KEY, 
    product_type_name VARCHAR(30)
);'''

globus_table = '''CREATE TABLE globus(
    product_id SERIAL PRIMARY KEY,
    product_type_id SMALLINT NOT NULL,
    product_name VARCHAR(50) NOT NULL,
    product_amount INT NOT NULL,
    day_to_expire SMALLINT NOT NULL,
    date_delivered TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_product_type
    FOREIGN KEY (product_type_id)
    REFERENCES product_types(product_type_id)
);'''


narodnii_table = '''CREATE TABLE narodnii(
    product_id SERIAL PRIMARY KEY,
    product_type_id SMALLINT NOT NULL,
    product_name VARCHAR(50) NOT NULL,
    product_amount INT NOT NULL,
    day_to_expire SMALLINT NOT NULL,
    date_delivered TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_product_type
    FOREIGN KEY (product_type_id)
    REFERENCES product_types(product_type_id)
);'''



product_type_query = 'INSERT INTO product_types (product_type_name) VALUES '
globus_insert_query = 'INSERT INTO globus(product_type_id, product_name, product_amount, day_to_expire ) VALUES '
narodnii_insert_query = 'INSERT INTO narodnii(product_type_id, product_name, product_amount, day_to_expire) VALUES '

ck = tuple(catalog.keys())

for _ in range(200):
    rd_num = rd.randint(0, len(ck)-1)
    tp = ck[rd_num]
    globus_insert_query += f'(\'{rd_num+1}\', \'{catalog.get(tp)[rd.randint(0,len(catalog.get(tp))-1)]}\', \'{rd.randint(1,1000)}\', \'{rd.randint(1,10)}\'),'
    narodnii_insert_query += f'(\'{rd_num+1}\', \'{catalog.get(tp)[rd.randint(0,len(catalog.get(tp))-1)]}\', \'{rd.randint(1,1000)}\', \'{rd.randint(1,10)}\'),'
else:
    globus_insert_query = globus_insert_query[:-1] + ';'
    narodnii_insert_query = narodnii_insert_query[:-1] + ';'

values = ','.join(product_types)
product_type_query += values + ';'


cursor.execute(product_types_table)
postgres.commit()

cursor.execute(globus_table)
cursor.execute(narodnii_table)
postgres.commit()

cursor.execute(product_type_query)
postgres.commit()

cursor.execute(globus_insert_query)
cursor.execute(narodnii_insert_query)
postgres.commit()