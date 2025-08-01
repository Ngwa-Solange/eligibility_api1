from models import BloodDonation
from sqlalchemy.orm import Session

def bulk_insert_donations(db: Session, df):
    for _, row in df.iterrows():
        record = BloodDonation(
            blood_type=row["blood_type"],
            donation_date=row["donation_date"],
            volume = row['collection_volume_ml'],
            temperature=row["temperature"],
            donor_age=row["donor_age"],
            location=row["location"],
            shelf_life_days=row["shelf_life_days"],
        )
        db.add(record)
    db.commit()
