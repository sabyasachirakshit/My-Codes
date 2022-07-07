# import sys
# from PyQt5.QtWidgets import QMainWindow,QApplication
# from location import *
# class MyForm(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.ui= Ui_MainWindow()
#         self.ui.setupUi(self)
#         self.ui.pushButton.clicked.connect(self.locate)
#         self.show()
#
#     def locate(self):
#         a1=self.ui.dropdown.currentText()
#         a="36811"
#         b="12130"
#         if a==a1:
#             print("afridi")
#         elif b==a1:
#             print("Rakhit")
#
#

# if __name__ == "__main__":
#     app =QApplication(sys.argv)
#     w=MyForm()
#     w.show()
#     sys.exit(app.exec_())
# Python program to find live train
# status using RAILWAY API

# import required modules
# import requests
# import json
#
# # enter your api key here
# api_key = "ae88c1141e41bb3cfe8a059c94deba05 "
#
# # base_url variable to store url
# # base_url = "https://api.railwayapi.com/v2/live/train/"
# base_url = "http://indianrailapi.com/api/v2/livetrainstatus"

# http://indianrailapi.com/api/v2/livetrainstatus/apikey/<apikey>/trainnumber/<train_number>/date/<yyyymmdd>/

# enter train_number here
# train_number = "12056"

# enter current date in dd-mm-yyyy format
# current_date = "20201002"

# complete_url variable to
# store complete url address
# complete_url = base_url + train_number + "/date/" + current_date + "/apikey/" + api_key + "/"
# complete_url = base_url + "/apikey/" + api_key + "/trainnumber/" + train_number + "/date/" + current_date +"/"

# get method of requests module
# return response object
# response_ob = requests.get(complete_url)

# json method of response object convert
# json format data into python format data
# result = response_ob.json()

# Now result contains list of nested dictionaries
# Check the value of "response_code" key is equal
# to "200" or not if equal that means record is
# found otherwise record is not found
# if result["response_code"] == 201:
#
#     # train name is extracting from
#     # the result variable data
#     train_name = result["train"]["name"]
#
#     # store the value or data of
#     # "route" key in variable y
#     y = result["route"]
#
#     # source station name is extracting
#     # from the y variable data
#     source_station = y[0]["station"]["name"]
#
#     # destination station name is
#     # extracting from the y varibale data
#     destination_station = y[len(y) - 1]["station"]["name"]
#
#     # store the value of "position"
#     # key in variable position
#     position = result["position"]
#
#     # print following values
#     print(" train name : " + str(train_name)
#           + "\n source station : " + str(source_station)
#           + "\n destination station : " + str(destination_station)
#           + "\n current status : " + str(position))
#
# else:
#     print("record is not found for given request")
from pyinrail import pyinrail
enq = pyinrail.RailwayEnquiry(src='kolkata', dest='mumbai', date='02-10-2020')
train_detail = enq.get_train_status(12958, as_df=True)
print(train_detail)
