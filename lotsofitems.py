#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Menu, Movie, Series, User, Item
import sys

engine = create_engine('sqlite:///bigtv.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

session = DBSession()

#https://www.python.org/dev/peps/pep-0263/
reload(sys)
sys.setdefaultencoding('utf-8')

# Create Admin user
User1 = User(name="Website Admin", email="mahmod.hagzy@gmail.com")
session.add(User1)
session.commit()

# Menu for Series
type1 = Menu(menu_type="Series")
session.add(type1)
session.commit()

series1 = Series(name="The End", description="In 2120 an engineer tries to solve the energy problem that threatens the survival of the human race",
                  hero="youssef el sherif" ,
                  image="https://elwekalanews.net/wp-content/uploads/2020/04/%D9%85%D8%B3%D9%84%D8%B3%D9%84-%D8%A7%D9%84%D9%86%D9%87%D8%A7%D9%8A%D8%A9.jpg",
                  url='test.html', date='5/24/2020',
                  ep1='//ok.ru/videoembed/1344782207682',
                  ep2='//ok.ru/videoembed/1472119441986',
                  ep3='//ok.ru/videoembed/1724586134091',
                  ep4='//ok.ru/videoembed/2504808532684',
                  ep5='//ok.ru/videoembed/1475410463298',
                  ep6='//ok.ru/videoembed/1377466387005',
                  ep7='//ok.ru/videoembed/1729532594763',
                  ep8='//ok.ru/videoembed/1731037956683',
                  ep9='//ok.ru/videoembed/1480086456898',
                  ep10='//ok.ru/videoembed/1382036539965',
                  
                  ep11='//ok.ru/videoembed/1632351685145',
                  ep12='//ok.ru/videoembed/1483443014210',
                  ep13='//ok.ru/videoembed/1630699915831',
                  ep14='//ok.ru/videoembed/1631906171447',
                  ep15='//ok.ru/videoembed/1631906171447',
                  ep16='//ok.ru/videoembed/1631906171447',
                  ep17='//ok.ru/videoembed/1631906171447',
                  ep18='//ok.ru/videoembed/1631906171447',
                  ep19='//ok.ru/videoembed/1631906171447',
                  ep20='//ok.ru/videoembed/1631906171447',
                  ep21='//ok.ru/videoembed/1631906171447',
                  ep22='//ok.ru/videoembed/1631906171447',
                  ep23='//ok.ru/videoembed/1631906171447',
                  ep24='//ok.ru/videoembed/1631906171447',
                  ep25='//ok.ru/videoembed/1631906171447',
                  ep26='//ok.ru/videoembed/1631906171447',
                  ep27='//ok.ru/videoembed/1631906171447',
                  ep28='//ok.ru/videoembed/1631906171447',
                  ep29='//ok.ru/videoembed/1631906171447',
                  ep30='//ok.ru/videoembed/1631906171447',                  
                  menu=type1)

session.add(series1)
session.commit()


episode1 = Item(name="مسلسل النهاية الحلقة 1", server1 ="//ok.ru/videoembed/1344782207682",
                  server2 ="//ok.ru/videoembed/1344782207682",
                  server3 ="//ok.ru/videoembed/1344782207682",
                  server4 ="//ok.ru/videoembed/1344782207682",
                  image="https://media.alalamtv.net/uploads/855x495/2020/05/06/158876354946112600.jpg",
                  ep_number=1,
                  tag1="1 النهاية", tag2="مسلسل النهاية 1",
                  tag3="مشاهدة النهاية 1", tag4="مسلسل يوسف الشريف الحلقة 1",
                  tag5="مشاهدة مسلسل النهاية الحلقة 1", tag6="مشاهدة النهاية الحلقة الاولي",
                  tag7="الحلقة الاولي النهاية", tag8="النهاية الحلقة الاولي",
                  tag9="النهاية يوسف الشريف 1", tag10="مشاهدة النهاية 1 اونلاين",
                  tag11="حلقة مسلسل النهاية الاولي", tag12="النهاية 1 جودة عالية",
                  tag13="مسلسل النهاية الحلقة الاولي hd", tag14="الحلقة الاولي من النهاية جودة عالية",
                  tag15="النهاية 1 رمضان 2020", tag16="مسلسل النهاية 1 جودة HD",
                  tag17="حلقة 1 النهاية",
                  series=series1)

session.add(episode1)
session.commit()

episode1 = Item(name="مسلسل النهاية الحلقة 2", server1 ="//ok.ru/videoembed/1344782207682",
                  server2 ="//ok.ru/videoembed/1344782207682",
                  server3 ="//ok.ru/videoembed/1344782207682",
                  server4 ="//ok.ru/videoembed/1344782207682",
                  image="https://media.alalamtv.net/uploads/855x495/2020/05/06/158876354946112600.jpg",
                  ep_number=1,
                  tag1="2 النهاية", tag2="مسلسل النهاية 2",
                  tag3="مشاهدة النهاية 2", tag4="مسلسل يوسف الشريف الحلقة 2",
                  tag5="مشاهدة مسلسل النهاية الحلقة 2", tag6="مشاهدة النهاية الحلقة الثانية",
                  tag7="الحلقة الثانية النهاية", tag8="النهاية الحلقة الثانية",
                  tag9="النهاية يوسف الشريف 2", tag10="مشاهدة النهاية 2 اونلاين",
                  tag11="حلقة مسلسل النهاية الثانية", tag12="النهاية 2 جودة عالية",
                  tag13="مسلسل النهاية الحلقة الثانية hd", tag14="الحلقة الثانية من النهاية جودة عالية",
                  tag15="النهاية 2رمضان 2020", tag16="مسلسل النهاية 2 جودة HD",
                  tag17="حلقة 2 النهاية",
                  series=series1)

session.add(episode1)
session.commit()

episode1 = Item(name="مسلسل النهاية الحلقة 3", server1 ="//ok.ru/videoembed/1344782207682",
                  server2 ="//ok.ru/videoembed/1344782207682",
                  server3 ="//ok.ru/videoembed/1344782207682",
                  server4 ="//ok.ru/videoembed/1344782207682",
                  image="https://media.alalamtv.net/uploads/855x495/2020/05/06/158876354946112600.jpg",
                  ep_number=1,
                  tag1="3 النهاية", tag2="مسلسل النهاية 3",
                  tag3="مشاهدة النهاية 3", tag4="مسلسل يوسف الشريف الحلقة 3",
                  tag5="مشاهدة مسلسل النهاية الحلقة 3", tag6="مشاهدة النهاية الحلقة الثالثة",
                  tag7="الحلقة الثالثة النهاية", tag8="النهاية الحلقة الثالثة",
                  tag9="النهاية يوسف الشريف 3", tag10="مشاهدة النهاية 3 اونلاين",
                  tag11="حلقة مسلسل النهاية الثالثة", tag12="النهاية 3 جودة عالية",
                  tag13="مسلسل النهاية الحلقة الثالثة hd", tag14="الحلقة الثالثة من النهاية جودة عالية",
                  tag15="النهاية 3 رمضان 2020", tag16="مسلسل النهاية 3 جودة HD",
                  tag17="حلقة 3 النهاية",
                  series=series1)

session.add(episode1)
session.commit()

episode1 = Item(name="مسلسل النهاية الحلقة 4", server1 ="//ok.ru/videoembed/1344782207682",
                  server2 ="//ok.ru/videoembed/1344782207682",
                  server3 ="//ok.ru/videoembed/1344782207682",
                  server4 ="//ok.ru/videoembed/1344782207682",
                  image="https://media.alalamtv.net/uploads/855x495/2020/05/06/158876354946112600.jpg",
                  ep_number=1,
                  tag1="4 النهاية", tag2="مسلسل النهاية 4",
                  tag3="مشاهدة النهاية 4", tag4="مسلسل يوسف الشريف الحلقة 4",
                  tag5="مشاهدة مسلسل النهاية الحلقة 4", tag6="مشاهدة النهاية الحلقة الرابعة",
                  tag7="الحلقة الرابعة النهاية", tag8="النهاية الحلقة الرابعة",
                  tag9="النهاية يوسف الشريف 4", tag10="مشاهدة النهاية 4 اونلاين",
                  tag11="حلقة مسلسل النهاية الرابعة", tag12="النهاية 4 جودة عالية",
                  tag13="مسلسل النهاية الحلقة الرابعة hd", tag14="الحلقة الرابعة من النهاية جودة عالية",
                  tag15="النهاية 4 رمضان 2020", tag16="مسلسل النهاية 4 جودة HD",
                  tag17="حلقة 4 النهاية",
                  series=series1)

session.add(episode1)
session.commit()

episode1 = Item(name="مسلسل النهاية الحلقة 5", server1 ="//ok.ru/videoembed/1344782207682",
                  server2 ="//ok.ru/videoembed/1344782207682",
                  server3 ="//ok.ru/videoembed/1344782207682",
                  server4 ="//ok.ru/videoembed/1344782207682",
                  image="https://media.alalamtv.net/uploads/855x495/2020/05/06/158876354946112600.jpg",
                  ep_number=1,
                  tag1="5 النهاية", tag2="مسلسل النهاية 5",
                  tag3="مشاهدة النهاية 5", tag4="مسلسل يوسف الشريف الحلقة 5",
                  tag5="مشاهدة مسلسل النهاية الحلقة 5", tag6="مشاهدة النهاية الحلقة الخامسة",
                  tag7="الحلقة الخامسة النهاية", tag8="النهاية الحلقة الخامسة",
                  tag9="النهاية يوسف الشريف 5", tag10="مشاهدة النهاية 5 اونلاين",
                  tag11="حلقة مسلسل النهاية الخامسة", tag12="النهاية 5 جودة عالية",
                  tag13="مسلسل النهاية الحلقة الخامسة hd", tag14="الحلقة الخامسة من النهاية جودة عالية",
                  tag15="النهاية 5 رمضان 2020", tag16="مسلسل النهاية 5 جودة HD",
                  tag17="حلقة 5 النهاية",
                  series=series1)

session.add(episode1)
session.commit()

episode1 = Item(name="مسلسل النهاية الحلقة 6", server1 ="//ok.ru/videoembed/1344782207682",
                  server2 ="//ok.ru/videoembed/1344782207682",
                  server3 ="//ok.ru/videoembed/1344782207682",
                  server4 ="//ok.ru/videoembed/1344782207682",
                  image="https://media.alalamtv.net/uploads/855x495/2020/05/06/158876354946112600.jpg",
                  ep_number=1,
                  tag1="6 النهاية", tag2="مسلسل النهاية 6",
                  tag3="مشاهدة النهاية 6", tag4="مسلسل يوسف الشريف الحلقة 6",
                  tag5="مشاهدة مسلسل النهاية الحلقة 6", tag6="مشاهدة النهاية الحلقة السادسة",
                  tag7="الحلقة السادسة النهاية", tag8="النهاية الحلقة السادسة",
                  tag9="النهاية يوسف الشريف 6", tag10="مشاهدة النهاية 6 اونلاين",
                  tag11="حلقة مسلسل النهاية السادسة", tag12="النهاية 6 جودة عالية",
                  tag13="مسلسل النهاية الحلقة السادسة hd", tag14="الحلقة السادسة من النهاية جودة عالية",
                  tag15="النهاية 6 رمضان 2020", tag16="مسلسل النهاية 6 جودة HD",
                  tag17="حلقة 6 النهاية",
                  series=series1)

session.add(episode1)
session.commit()

episode1 = Item(name="مسلسل النهاية الحلقة 7", server1 ="//ok.ru/videoembed/1344782207682",
                  server2 ="//ok.ru/videoembed/1344782207682",
                  server3 ="//ok.ru/videoembed/1344782207682",
                  server4 ="//ok.ru/videoembed/1344782207682",
                  image="https://media.alalamtv.net/uploads/855x495/2020/05/06/158876354946112600.jpg",
                  ep_number=1,
                  tag1="7 النهاية", tag2="مسلسل النهاية 7",
                  tag3="مشاهدة النهاية 7", tag4="مسلسل يوسف الشريف الحلقة 7",
                  tag5="مشاهدة مسلسل النهاية الحلقة 7", tag6="مشاهدة النهاية الحلقة السابعة",
                  tag7="الحلقة السابعة النهاية", tag8="النهاية الحلقة السابعة",
                  tag9="النهاية يوسف الشريف 7", tag10="مشاهدة النهاية 7 اونلاين",
                  tag11="حلقة مسلسل النهاية السابعة", tag12="النهاية 7 جودة عالية",
                  tag13="مسلسل النهاية الحلقة السابعة hd", tag14="الحلقة السابعة من النهاية جودة عالية",
                  tag15="النهاية 7 رمضان 2020", tag16="مسلسل النهاية 7 جودة HD",
                  tag17="حلقة 7 النهاية",
                  series=series1)

session.add(episode1)
session.commit()

episode1 = Item(name="مسلسل النهاية الحلقة 8", server1 ="//ok.ru/videoembed/1344782207682",
                  server2 ="//ok.ru/videoembed/1344782207682",
                  server3 ="//ok.ru/videoembed/1344782207682",
                  server4 ="//ok.ru/videoembed/1344782207682",
                  image="https://media.alalamtv.net/uploads/855x495/2020/05/06/158876354946112600.jpg",
                  ep_number=1,
                  tag1="8 النهاية", tag2="مسلسل النهاية 8",
                  tag3="مشاهدة النهاية 8", tag4="مسلسل يوسف الشريف الحلقة 8",
                  tag5="مشاهدة مسلسل النهاية الحلقة 8", tag6="مشاهدة النهاية الحلقة الثامنة",
                  tag7="الحلقة الثامنة النهاية", tag8="النهاية الحلقة الثامنة",
                  tag9="النهاية يوسف الشريف 8", tag10="مشاهدة النهاية 8 اونلاين",
                  tag11="حلقة مسلسل النهاية الثامنة", tag12="النهاية 8 جودة عالية",
                  tag13="مسلسل النهاية الحلقة الثامنة hd", tag14="الحلقة الثامنة من النهاية جودة عالية",
                  tag15="النهاية 8 رمضان 2020", tag16="مسلسل النهاية 8 جودة HD",
                  tag17="حلقة 8 النهاية",
                  series=series1)

session.add(episode1)
session.commit()

episode1 = Item(name="مسلسل النهاية الحلقة 9", server1 ="//ok.ru/videoembed/1344782207682",
                  server2 ="//ok.ru/videoembed/1344782207682",
                  server3 ="//ok.ru/videoembed/1344782207682",
                  server4 ="//ok.ru/videoembed/1344782207682",
                  image="https://media.alalamtv.net/uploads/855x495/2020/05/06/158876354946112600.jpg",
                  ep_number=1,
                  tag1="9 النهاية", tag2="مسلسل النهاية 9",
                  tag3="مشاهدة النهاية 9", tag4="مسلسل يوسف الشريف الحلقة 9",
                  tag5="مشاهدة مسلسل النهاية الحلقة 9", tag6="مشاهدة النهاية الحلقة التاسعة",
                  tag7="الحلقة التاسعة النهاية", tag8="النهاية الحلقة التاسعة",
                  tag9="النهاية يوسف الشريف 9", tag10="مشاهدة النهاية 9 اونلاين",
                  tag11="حلقة مسلسل النهاية التاسعة", tag12="النهاية 9 جودة عالية",
                  tag13="مسلسل النهاية الحلقة التاسعة hd", tag14="الحلقة التاسعة من النهاية جودة عالية",
                  tag15="النهاية 9 رمضان 2020", tag16="مسلسل النهاية 9 جودة HD",
                  tag17="حلقة 9 النهاية",
                  series=series1)

session.add(episode1)
session.commit()

episode1 = Item(name="مسلسل النهاية الحلقة 10", server1 ="//ok.ru/videoembed/1344782207682",
                  server2 ="//ok.ru/videoembed/1344782207682",
                  server3 ="//ok.ru/videoembed/1344782207682",
                  server4 ="//ok.ru/videoembed/1344782207682",
                  image="https://media.alalamtv.net/uploads/855x495/2020/05/06/158876354946112600.jpg",
                  ep_number=1,
                  tag1="10 النهاية", tag2="مسلسل النهاية 10",
                  tag3="مشاهدة النهاية 10", tag4="مسلسل يوسف الشريف الحلقة 10",
                  tag5="مشاهدة مسلسل النهاية الحلقة 10", tag6="مشاهدة النهاية الحلقة العاشرة",
                  tag7="الحلقة  العاشرة النهاية", tag8="النهاية الحلقة العاشرة",
                  tag9="النهاية يوسف الشريف 10", tag10="مشاهدة النهاية 10 اونلاين",
                  tag11="حلقة مسلسل النهاية العاشرة", tag12="النهاية 10 جودة عالية",
                  tag13="مسلسل النهاية الحلقة العاشرة hd", tag14="الحلقة العاشرة من النهاية جودة عالية",
                  tag15="النهاية 10 رمضان 2020", tag16="مسلسل النهاية 10 جودة HD",
                  tag17="حلقة 10 النهاية",
                  series=series1)

session.add(episode1)
session.commit()

episode1 = Item(name="مسلسل النهاية الحلقة 11", server1 ="//ok.ru/videoembed/1344782207682",
                  server2 ="//ok.ru/videoembed/1344782207682",
                  server3 ="//ok.ru/videoembed/1344782207682",
                  server4 ="//ok.ru/videoembed/1344782207682",
                  image="https://media.alalamtv.net/uploads/855x495/2020/05/06/158876354946112600.jpg",
                  ep_number=1,
                  tag1="11 النهاية", tag2="مسلسل النهاية 11",
                  tag3="مشاهدة النهاية 11", tag4="مسلسل يوسف الشريف الحلقة 11",
                  tag5="مشاهدة مسلسل النهاية الحلقة 11", tag6="مشاهدة النهاية الحلقة الحادية عشر",
                  tag7="الحلقة الحادية عشر النهاية", tag8="النهاية الحلقة الحادية عشر",
                  tag9="النهاية يوسف الشريف 11", tag10="مشاهدة النهاية 11 اونلاين",
                  tag11="حلقة مسلسل النهاية الحادية عشر", tag12="النهاية 11 جودة عالية",
                  tag13="مسلسل النهاية الحلقة الحادية عشر hd", tag14="الحلقة الحادية عشر من النهاية جودة عالية",
                  tag15="النهاية 11 رمضان 2020", tag16="مسلسل النهاية 11 جودة HD",
                  tag17="حلقة 11 النهاية",
                  series=series1)

session.add(episode1)
session.commit()

episode1 = Item(name="مسلسل النهاية الحلقة 12", server1 ="//ok.ru/videoembed/1344782207682",
                  server2 ="//ok.ru/videoembed/1344782207682",
                  server3 ="//ok.ru/videoembed/1344782207682",
                  server4 ="//ok.ru/videoembed/1344782207682",
                  image="https://media.alalamtv.net/uploads/855x495/2020/05/06/158876354946112600.jpg",
                  ep_number=1,
                  tag1="12 النهاية", tag2="مسلسل النهاية 12",
                  tag3="مشاهدة النهاية 12", tag4="مسلسل يوسف الشريف الحلقة 12",
                  tag5="مشاهدة مسلسل النهاية الحلقة 12", tag6="مشاهدة النهاية الحلقة الثانية عشر",
                  tag7="الحلقةالثانية عشر النهاية", tag8="النهاية الحلقة الثانية عشر",
                  tag9="النهاية يوسف الشريف 12", tag10="مشاهدة النهاية 12 اونلاين",
                  tag11="حلقة مسلسل النهاية الثانية عشر", tag12="النهاية 12 جودة عالية",
                  tag13="مسلسل النهاية الحلقة الثانية عشر hd", tag14="الحلقة الثانية عشر من النهاية جودة عالية",
                  tag15="النهاية 12 رمضان 2020", tag16="مسلسل النهاية 12 جودة HD",
                  tag17="حلقة 12 النهاية",
                  series=series1)

session.add(episode1)
session.commit()

episode1 = Item(name="مسلسل النهاية الحلقة 13", server1 ="//ok.ru/videoembed/1344782207682",
                  server2 ="//ok.ru/videoembed/1344782207682",
                  server3 ="//ok.ru/videoembed/1344782207682",
                  server4 ="//ok.ru/videoembed/1344782207682",
                  image="https://media.alalamtv.net/uploads/855x495/2020/05/06/158876354946112600.jpg",
                  ep_number=1,
                  tag1="13 النهاية", tag2="مسلسل النهاية 13",
                  tag3="مشاهدة النهاية 13", tag4="مسلسل يوسف الشريف الحلقة 13",
                  tag5="مشاهدة مسلسل النهاية الحلقة 13", tag6="مشاهدة النهاية الحلقة الثالثة عشر",
                  tag7="الحلقة الثالثة عشر النهاية", tag8="النهاية الحلقة الثالثة عشر",
                  tag9="النهاية يوسف الشريف 13", tag10="مشاهدة النهاية 1 اونلاين",
                  tag11="حلقة مسلسل النهاية الثالثة عشر", tag12="النهاية 13 جودة عالية",
                  tag13="مسلسل النهاية الحلقة الثالثة عشر hd", tag14="الحلقة الثالثة عشر من النهاية جودة عالية",
                  tag15="النهاية 13 رمضان 2020", tag16="مسلسل النهاية 13 جودة HD",
                  tag17="حلقة 13 النهاية",
                  series=series1)

session.add(episode1)
session.commit()

episode1 = Item(name="مسلسل النهاية الحلقة 14", server1 ="//ok.ru/videoembed/1344782207682",
                  server2 ="//ok.ru/videoembed/1344782207682",
                  server3 ="//ok.ru/videoembed/1344782207682",
                  server4 ="//ok.ru/videoembed/1344782207682",
                  image="https://media.alalamtv.net/uploads/855x495/2020/05/06/158876354946112600.jpg",
                  ep_number=1,
                  tag1="14 النهاية", tag2="مسلسل النهاية 14",
                  tag3="مشاهدة النهاية 14", tag4="مسلسل يوسف الشريف الحلقة 14",
                  tag5="مشاهدة مسلسل النهاية الحلقة 14", tag6="مشاهدة النهاية الحلقة الرابعة عشر",
                  tag7="الحلقة  الرابعة عشر النهاية", tag8="النهاية الحلقة الرابعة عشر",
                  tag9="النهاية يوسف الشريف 14", tag10="مشاهدة النهاية 14 اونلاين",
                  tag11="حلقة مسلسل النهاية الرابعة عشر", tag12="النهاية 14 جودة عالية",
                  tag13="مسلسل النهاية الحلقة الرابعة عشر hd", tag14="الحلقة الرابعة عشر من النهاية جودة عالية",
                  tag15="النهاية 14 رمضان 2020", tag16="مسلسل النهاية 14 جودة HD",
                  tag17="حلقة 14 النهاية",
                  series=series1)

session.add(episode1)
session.commit()



                 
                  
series2 = Series(name="The Prince", description="that the story of Prince is similar to the story of our master Joseph, peace be upon him, and Kabeel,Habeel and Noble stories are from ancient times, but they are repeated tshroughout the ages.",
                  hero="Mohamed Ramdan" ,
                  image="https://s3-eu-west-1.amazonaws.com/static.jbcgroup.com/amd/pictures/0e628cc7d4a56975552bd9d75efd35f0.jpg",
                  url='test.html', date='5/24/2020',
                  menu=type1)

session.add(series2)
session.commit()

series3 = Series(name="Valentino", description="He plays the role of Noor Abdul Majeed, the mighty artist Adel Imam, and he has a private school he owns, married to Dalal Abdel Aziz and he has three children",
                  hero="Adel Amam",
                  image="https://images.akhbarelyom.com/images/images/large/20200503092638730.jpg",
                  url='test.html', date='5/24/2020',
                  menu=type1)

session.add(series3)
session.commit()


# Menu for Movies
type2 = Menu(menu_type="Movies")
session.add(type1)
session.commit()


series1 = Movie(name="Joker", description="The movie, which represents the story of the origin of the Joker, was re-released in 1981 and follows Arthur Flick, a failed comedian who turns to a life of crime.",
                  hero="Joaquin Phoenix",
                  image="https://upload.wikimedia.org/wikipedia/ar/8/82/Joker_2019_ME_poster.png",
                  url='test.html', date='10/2/2020',
                  menu=type1)

session.add(series1)
session.commit()

series1 = Movie(name="The Legend of Tarzan",
                  description="The Tarzan Legend is an action movie produced in the United States and released in 2016. The film is directed by David Yates and written by Stuart Betty.",
                  hero="alexander skarsgard" ,
                  image="https://ww.mycima.co/wp-content/uploads/2019/04/The-Legend-Of-Tarzan-2016-.jpg",
                  url='test.html', date='5/24/2020',
                  menu=type1)

session.add(series1)
session.commit()

series1 = Movie(name="The Blue Elephant", description="The Blue Elephant has a 2014 Egyptian drama and mystery film, directed by Marwan Hamed and written by Ahmed Murad",
                  hero="Adel Amam" ,
                  image="https://media.linkonlineworld.com/img/large/2015/4/1/2015_4_1_12_49_51_303.jpg",
                  url='test.html', date='5/24/2020',
                  menu=type1)

session.add(series1)
session.commit()


print "added menu items!"


