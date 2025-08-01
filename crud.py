from sqlalchemy.orm import Session
import pandas as pd
import datetime
import models

def bulk_insert_donations(db: Session, df: pd.DataFrame):
    for _, row in df.iterrows():
        # Convert donation_date string to a Python date object
        if isinstance(row["donation_date"], str):
            donation_date_obj = datetime.datetime.strptime(row["donation_date"], "%Y-%m-%d").date()
        else:
            # If it's already a datetime or date object
            donation_date_obj = row["donation_date"]
            if hasattr(donation_date_obj, 'date'):
                donation_date_obj = donation_date_obj.date()

        donation = models.BloodDonation(
            donation_date=donation_date_obj,
            blood_type=row["blood_type"],
            collection_volume_ml=row["collection_volume_ml"],
            hemoglobin_g_dl=row["hemoglobin_g_dl"],
            donor_age=row["donor_age"],
            donor_gender=row["donor_gender"],
            shelf_life_days=row["shelf_life_days"]
        )
        db.add(donation)
    db.commit()
