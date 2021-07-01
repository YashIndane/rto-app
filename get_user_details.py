import requests
import xmltodict
import json

def user_details(number, user):

  r = requests.get(f"http://www.regcheck.org.uk/api/reg.asmx/CheckIndia?RegistrationNumber={number}&username={user}")
  data = xmltodict.parse(r.content)
  jdata = json.dumps(data)
  df = json.loads(jdata)
  df1 = json.loads(df['Vehicle']['vehicleJson'])

  return [df1["Description"],
          df1["RegistrationYear"],
          df1["EngineSize"]["CurrentTextValue"],
          df1["NumberOfSeats"]["CurrentTextValue"],
          df1["VechileIdentificationNumber"],
          df1["EngineNumber"],
          df1["FuelType"]["CurrentTextValue"],
          df1["RegistrationDate"],
          df1["Location"]]      