# Install dependencies with --no-cache-dir to reduce size
pip install --no-cache-dir -r requirements.txt

# Collect static files and apply migrations
python manage.py collectstatic --noinput
python manage.py migrate
