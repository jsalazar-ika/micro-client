import os

from .secrets import get_secret


# get data from environment variables
db_name = os.getenv("NAME_DB")
db_user = get_secret("db-user")
db_password = get_secret("db-password")
db_ip = os.getenv("IP_DB")
db_port = os.getenv("PORT_DB")

class Config:
    SQL_ALCHEMY_DATABASE_URI=f"mysql+pymysql://{db_user}:{db_password}@{db_ip}:{db_port}/{db_name}"
    SQL_ALCHEMY_TRACK_MODIFICATION=False
