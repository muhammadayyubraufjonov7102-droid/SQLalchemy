from sqlalchemy import create_engine, Integer, String, DateTime, func, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from datetime import datetime


engine = create_engine("sqlite:///dev.db")


class Base(DeclarativeBase):
    pass


class Teacher (Base):
    __tablename__="teachers"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    subject: Mapped[str] = mapped_column(String)
    experience : Mapped[int] = mapped_column(Integer)
    
    def __repr__(self):
        return f"{self.id} | {self.name} | {self.subject} | {self.experience} yil"
    
Base.metadata.create_all(engine)

with Session(engine) as session:
    teacher = Teacher(name="Anvar", subject="Matematika", experience=5)
    teacher1 = Teacher(name="Nilufar", subject="Fizika", experience=8)
    teacher2 = Teacher(name="Rustam", subject="Kimyo", experience=3)
    
    session.add_all([teacher, teacher1, teacher2])
    
    session.commit()
    
    a = session.query(Teacher).all()   #3. Barcha teacherlarni chiqarib bering.    
    print(a)
    
    a2 = session.query(Teacher).filter(Teacher.subject=="Fizika").first() #4. Faqat subject = "Fizika" bo‘lgan teacherni toping.
    print(a2)
    
    a3 = session.query(Teacher).filter(Teacher.experience>=5).all()  #5. experience >= 5 bo‘lgan teacherlarni chiqaring.
    print(a3)
    
    a4 = session.query(Teacher.name, Teacher.subject).all()  #6. Faqat name va subject ustunlarini chiqarib bering.
    print(a4)
    
    studentlar = session.get(Teacher, 2) #7. id = 2 bo‘yicha teacherni toping.   
    print(studentlar)
    
    a5 = session.query(Teacher.experience).order_by(Teacher.experience.desc()).all() #8. experience bo‘yicha kamayish tartibida teacherlarni chiqarib bering.   
    print(a5)
    
    a6 = session.query(Teacher).count() #9. Jadvalda nechta teacher borligini aniqlang.
    print(a6)
    
    a7 = session.query(Teacher).filter(Teacher.subject=="Kimyo").all() #10. subject = "Kimyo" bo‘lgan teacherni toping va ularni chiqarib bering.
    print(a7)
    
    
    
    # ###################################################################################
    
# 2-bosqich: SQLAlchemy ORM – UPDATE amallari2-bosqich: SQLAlchemy ORM – UPDATE amallari 

with Session(engine) as session:
    b1 = session.query(Teacher).filter(Teacher.name=="Anvar").first()  #1.name = "Anvar" bo‘lgan teacherning experience ustunini 6 ga o‘zgartiring.
    b1.experience = 6
    
    b2 = session.get(Teacher, 3)
    b2.subject="Biologiya"  #2.id = 3 bo‘lgan teacherning subject ustunini "Biologiya" ga o‘zgartiring.
    
    b3 = session.query(Teacher).filter(Teacher.experience<5).all() #3.experience < 5 bo‘lgan barcha teacherlarning subject ustunini "Informatika" ga yangilang.
    for n in b3:
        n.subject="Informatika"
    
    b4 = session.query(Teacher).filter(Teacher.name=="Nilufar").first()  #4.name = "Nilufar" bo‘lgan teacherning experience ustunini 10 ga yangilang.
    b4.experience = 10
    
    b5 = session.get(Teacher, 1)  #5.id = 1 bo‘lgan teacherni topib, name = "Anvarbek" va experience = 7 qilib yangilang.
    b5.name="Anvarbek"
    b5.experience=7
    
    b6 = session.query(Teacher).filter(Teacher.experience>=8).all()  #6.experience >= 8 bo‘lgan teacherlarni topib subject ustunini "Fizika-Advanced" ga yangilang.
    
    for i in b6:
        i.subject="Fizika-Advanced"
    
    
    
    b7 = session.get(Teacher, 2)  #5.id = 1 bo‘lgan teacherni topib, name = "Anvarbek" va experience = 7 qilib yangilang.
    b7.name=""
    
# 3-bosqich: SQLAlchemy ORM – DELETE amallari

    d1 = session.get(Teacher, 1)  #1. id = 1 bo‘lgan teacherni bazadan o‘chiring.
    session.delete(d1)
    
    
    d2 = session.query(Teacher).filter(Teacher.experience<5).all()  #2. experience < 5 bo‘lgan barcha teacherlarni bazadan o‘chiring.

    for u in d2:
        session.delete(u)
        
    session.query(Teacher).filter(Teacher.subject=="Fizika").delete()  #3.subject != "Fizika" bo‘lgan teacherlar qoladigan qilib, qolganlarini o‘chiring.

    session.query(Teacher).delete()  #4.Bazadagi barcha teacherlarni o‘chirib tashlang.
    
    session.query(Teacher).filter(Teacher.experience>=7).delete()  #5.experience >= 7 bo‘lgan teacherlarni topib o‘chiring.
    
    session.commit()
    


