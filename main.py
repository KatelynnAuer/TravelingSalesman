# Katelynn Auer 001445658

from app import start_app
from wgups.schedule import schedule_delivery

packages, trucks = schedule_delivery()

start_app(packages, trucks)
