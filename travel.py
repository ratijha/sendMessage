__author__ = 'ratijha'

import requests
import json

API_KEY='3a2826056fffa622e4f20bfec321b474'
app_id = '279882b0'


def travel(source, destination, date):
      url = "http://developer.goibibo.com/api/bus/search/?app_id={0}&app_key={1}&" \
            "source={2}&destination={3}&dateofdeparture={4}".format(app_id, API_KEY, source, destination, date)
      # print(url)
      # url = "https://www.redbus.in/search?fromCityName={0}&toCityName={1}&onward={2}&opId=0&busType=Any#".format(source, destination, date)
      dat = requests.get(url).json()
      # print(dat)
      # return dat
      res = []
      for detail in dat['data']['onwardflights']:
          # print(detail)
          det = []
          if detail['BusType'] == 'A/C Sleeper (2+1)' and float(detail['fare']['totalbasefare']) < 1400:
              det.append(detail['fare']['totalbasefare'],)
              # det.append(detail['RouteSeatTypeDetail']['list'][0]['availabilityStatus'],)
              det.append(detail['TravelsName'])
              res.append(det)

      return res



    # print("\n")