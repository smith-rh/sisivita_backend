from dotenv import load_dotenv
import os

load_dotenv()

user = os.environ["USER"]
password = os.environ["PASSWORD"]
host = os.environ["HOST"]
database = os.environ["DATABASE"]


DATABASE_CONNECTION_URI = "postgresql://sisvita_bd2_user:xKWliyT0gOLdjGWBnzUCKtG03WHdr5mT@dpg-cq136gbv2p9s73cl1a3g-a.oregon-postgres.render.com/sisvita_bd2"
#print(DATABASE_CONNECTION_URI)