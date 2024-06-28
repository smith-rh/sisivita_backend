from dotenv import load_dotenv
import os

load_dotenv()

user = os.environ["USER"]
password = os.environ["PASSWORD"]
host = os.environ["HOST"]
database = os.environ["DATABASE"]


DATABASE_CONNECTION_URI = "postgresql://sisvita_bd_user:JqNkHbyNiqHW1Y9675Btom1HKwvvFCRu@dpg-cpd3idgcmk4c73dqr45g-a.oregon-postgres.render.com/sisvita_bd"
#print(DATABASE_CONNECTION_URI)