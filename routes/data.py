import csv
from fastapi import APIRouter, HTTPException, UploadFile, File
from io import StringIO
from app.db import database
from models.transaction import Transaction
from fastapi.responses import StreamingResponse

router = APIRouter()

# Import CSV file
@router.post("/import")
async def import_csv(file: UploadFile = File(...), db: AsyncSession = Depends(get_db)):
    content = await file.read()
    csv_data = StringIO(content.decode("utf-8"))
    reader = csv.DictReader(csv_data)

    for row in reader:
        db_transaction = Transaction(
            amount=float(row['amount']),
            description=row['description'],
            date=datetime.fromisoformat(row['date'])
        )
        db.add(db_transaction)
    await db.commit()
    return {"message": "Data imported successfully"}

# Export CSV file
@router.get("/export")
async def export_csv(db: AsyncSession = Depends(get_db)):
    transactions = await db.execute(select(Transaction))
    transactions_list = transactions.scalars().all()

    csv_output = StringIO()
    writer = csv.writer(csv_output)
    writer.writerow(['id', 'amount', 'description', 'date'])
    for t in transactions_list:
        writer.writerow([t.id, t.amount, t.description, t.date.isoformat()])

    csv_output.seek(0)
    return StreamingResponse(csv_output, media_type="text/csv", headers={"Content-Disposition": "attachment; filename=transactions.csv"})
