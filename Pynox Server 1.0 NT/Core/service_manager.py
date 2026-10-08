import os
from services.network import network_status 
from services.storage import status 
from services.process import process
from services.system import system
from services.program import program
from services.time import date_time
class Service_manager:
    def list_service(self):
        print("Available services")
        print("-----------------")
        Service_path = os.path.join(os.path.dirname(__file__),"services")
        services = os.listdir(Service_path)
        for service in services:
            if service.endswith(".py"):
                print(service[:-3])
    def network(self):
        network_status()
    def storage(self):
        status()
    def process(self):
        process()
    def system(self):
        system()
    def program(self,User):
        program(User)
    def time(self):
        date_time()