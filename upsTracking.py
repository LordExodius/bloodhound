# Oscar Yu (LordExodius)
# June 5th 2021
# UPS Tracking Module for bloodhound

from ClassicUPS import UPSConnection
from dotenv import load_dotenv
import os

load_dotenv()
AccessKey = os.getenv("UPSAccessKey")
UserID = os.getenv("UPSid")
Password = os.getenv("UPSpassword")

