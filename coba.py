from app import app, db, UploadGambar
with app.app_context():
    uploads = UploadGambar.query.limit(5).all()
    for u in uploads:
        print('='*50)
        print(f'ID: {u.id}')
        print(f'Public ID: {u.public_id}')
        print(f'Cloudinary URL: {u.cloudinary_url}')
        print(f'Original filename: {u.original_filename}')
