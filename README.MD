# Create a virtualenv folder
python3 -m venv smart

# Activate your virtualenv folder
source smart/bin/activate

# Installing App dependencies
pip3 install -r requirements.txt

# Running the server:
uvicorn main:app --reload