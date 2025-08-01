from sqlalchemy import Column, Integer, String, Float, Date
from database import Base

class BloodDonation(Base):
    __tablename__ = "blood_donations"

    id = Column(Integer, primary_key=True, index=True)
    donation_date = Column(Date)
    blood_type = Column(String)
    volume = Column(Float)  # <-- Maps to collection_volume_ml
    hemoglobin = Column(Float)  # <-- Maps to hemoglobin_g_dl
    donor_age = Column(Integer)
    donor_gender = Column(String)
    shelf_life_days = Column(Integer)
