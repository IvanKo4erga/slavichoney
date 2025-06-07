# create a virtual environment named 'venv' if it doesn't already exist
#python3.10 -m venv venv

# activate the virtual environment
#source venv/bin/activate
# Install dependencies with --no-cache-dir to reduce size
pip install --no-cache-dir -r requirements.txt

# Collect static files and apply migrations
python manage.py collectstatic --noinput
python manage.py migrate
