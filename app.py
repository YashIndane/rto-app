from flask import Flask, render_template, request
from number_plate_detect import save_plate
from get_plate_number import get_number
from get_user_details import user_details

app = Flask("rto-app")

def upload_file():
  file = request.files['file']
  file.save(file.filename)

@app.route("/input")
def get_image():
   return render_template("home.html")

@app.route("/get_details", methods = ["POST", "GET"])
def get_details():

   # upload file in working directory
   upload_file()  

   # save the cropped image of number plate
   save_plate()

   # get the numbers from plate
   number_ = get_number()

   print(number_)
   
   # get the details
   # this is username of http://www.regcheck.org.uk/api/reg.asmx/CheckIndia
   user = ""
   details = user_details(number_, user)

   return render_template(
                 "out.html", 
                 model = details[0],
                 regyear = details[1],
                 engsize = details[2],
                 sea = details[3],
                 idfi = details[4],
                 engnum = details[5],
                 fuelt = details[6],
                 regdate = details[7],
                 loc = details[8]
         )
         

app.run(host = "0.0.0.0", port = "98")