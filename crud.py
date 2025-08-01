from sqlalchemy.orm import Session
import pandas as pd
import models

def bulk_insert_donations(db: Session, df: pd.DataFrame):
    for _, row in df.iterrows():
        donation = models.BloodDonation(
            donation_date=row["donation_date"],
            blood_type=row["blood_type"],
            volume=row["collection_volume_ml"],  # <-- Use correct column name
            hemoglobin=row["hemoglobin_g_dl"],
            donor_age=row["donor_age"],
            donor_gender=row["donor_gender"],
            shelf_life_days=row["shelf_life_days"]
        )
        db.add(donation)
    db.commit()
