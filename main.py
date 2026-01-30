from sqlalchemy import create_engine, Integer, String, DateTime, func, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from datetime import datetime


engine = create_engine("sqlite:///dev.db")


class Base(DeclarativeBase):
    pass


class Teacher (Base):
    __tablename__="students"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    subject: Mapped[str] = mapped_column(Integer)
    experience : Mapped[int] = mapped_column(String)
    
    def __str__(self):
        return f"{self.id} {self.name}-{self.age}-{self.grade}"
    
    def __repr__(self):
        return f"{self.id} {self.name}-{self.age}-{self.grade}\n"
    
Base.metadata.create_all(engine)

with Session(engine) as session:
    teacher = Teacher(name="Anvar", subject="Matematika", grade=5)
    teacher1 = Teacher(name="Nilufar", subject="Fizika", grade=8)
    teacher2 = Teacher(name="Rustam", subject="Kimyo", grade=3)
    
    session.add_all([teacher, teacher1, teacher2])
    
    session.commit()
    
    students = session.query(Teacher).all()   #3. Barcha teacherlarni chiqarib bering.    
    print(students)
    
    student = session.query(Teacher).filter(Teacher.subject=="Fizika").first() #4. Faqat subject = "Fizika" bo‘lgan teacherni toping.
    print(student)
    
    student = session.query(Teacher).filter(Teacher.experience>=5)  #5. experience >= 5 bo‘lgan teacherlarni chiqaring.
    print(student)
    
    studen = session.query(Teacher).filter(Teacher.name, Teacher.subject)  #6. Faqat name va subject ustunlarini chiqarib bering.
    print(studen)
    
    studentlar = session.query(Teacher.id==2) #7. id = 2 bo‘yicha teacherni toping.   
    print(studentlar)
    
    studentlar = session.query(Teacher.experience).order_by("-experience") #8. experience bo‘yicha kamayish tartibida teacherlarni chiqarib bering.   
    print(studentlar)
    
    count = session.query(Teacher).count() #9. Jadvalda nechta teacher borligini aniqlang.
    print(count)
    
    sub = session.query(Teacher).filter(Teacher.subject=="Kimyo").all() #4. subject = "Kimyo" bo‘lgan teacherni toping va ularni chiqarib bering.
    print(sub)
    
    