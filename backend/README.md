# This is the backend. 
# run the following commands from root

## db setup
python backend/setup.py

## Running the backend
uvicorn backend.app.main:app --reload