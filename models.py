from sqlalchemy import Column, Integer, String, Float, Date
from database import Base

class BloodDonation(Base):
    __tablename__ = "donations"

    id = Column(Integer, primary_key=True, index=True)
    blood_type = Column(String)
    donation_date = Column(Date)
    volume = Column(Float)
    temperature = Column(Float)
    donor_age = Column(Integer)
    location = Column(String)
    shelf_life_days = Column(Float)
