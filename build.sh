# create a virtual environment named 'venv' if it doesn't already exist
python3.10 -m venv venv

# activate the virtual environment
source venv/bin/activate
# Install dependencies with --no-cache-dir to reduce size
pip3 install --no-cache-dir -r requirements.txt

# Collect static files and apply migrations
python3 manage.py collectstatic --noinput
python3 manage.py migrate
