sudo apt update
sudo apt install python3.12-venv -y
python3 -m venv venv
source venv/bin/activate
pip install apache-airflow
pip install pandas 
pip install s3fs
pip install tweepy