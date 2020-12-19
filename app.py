from flask import Flask,render_template,redirect,url_for,request,session,flash
import numpy as np
import pickle
app=Flask(__name__)
app.secret_key="lucky"
@app.route("/")
def home():
        return render_template("home.html")
@app.route('/predict',methods=['POST'])
def predict():
     if request.method == "POST":
         session.permanent = True
         vals=[]
         location_map={'Karjat': 0,'Bhavnagar': 1,'Rudrapur': 2,'Palghar': 3,'Junagadh': 4,'Durgapur': 5,'Ratnagiri': 6,
                       'Bharuch': 7,'Vapi': 8,'Neemrana': 9,'Bhiwadi': 10,'Valsad': 11,'Bhilai': 12,'Navsari': 13,'Asansol': 14,
                       'Vizianagaram': 15,'Jamnagar': 16,'Haridwar': 17,'Mathura': 18,'Raigad': 19,'Meerut': 20,'Sindhudurg': 21,
                       'Bilaspur': 22,'Solan': 23,'Dhanbad': 24,'Bhopal': 25,'Aurangabad': 26,'Nellore': 27,'Hubli': 28,'Raipur': 29,
                       'Amravati': 30,'Ajmer': 31,'Dharuhera': 32,'Solapur': 33,'Kolhapur': 34,'Siliguri': 35,'Gwalior': 36,'Others': 37,
                       'Ahmednagar': 38,'Agra': 39,'Udupi': 40,'Aligarh': 41,'Jodhpur': 42,'Gandhinagar': 43,'Guntur': 44,'Anand': 45,
                       'Bahadurgarh': 46,'Belgaum': 47,'Indore': 48,'Jamshedpur': 49,'Margao': 50,'Rajkot': 51,'Palakkad': 52,'Madurai': 53,
                       'Sonipat': 54,'Kota': 55,'Vijayawada': 56,'Jabalpur': 57,'Pondicherry': 58,'Guwahati': 59,'Jalandhar': 60,'Allahabad': 61,
                       'Tirupati': 62,'Udaipur': 63,'Secunderabad': 64,'Vadodara': 65,'Visakhapatnam': 66,'Ghaziabad': 67,'Jaipur': 68,'Thrissur': 69,
                       'Patna': 70,'Faridabad': 71,'Bhubaneswar': 72,'Surat': 73,'Shimla': 74,'Varanasi': 75,'Mysore': 76,'Mangalore': 77,'Dehradun': 78,
                       'Nagpur': 79,'Coimbatore': 80,'Ernakulam': 81,'Ludhiana': 82,'Panchkula': 83,'Lucknow': 84,'Chandigarh': 85,'Kolkata': 86,'Kanpur': 87,
                       'Kottayam': 88,'Panaji': 89,'Jalgaon': 90,'Mohali': 91,'Pune': 92,'Kochi': 93,'Ranchi': 94,'Noida': 95,'Chennai': 96,'Bangalore': 97,
                       'Goa': 98,'Lalitpur': 99,'Mumbai': 100,'Maharashtra': 101,'Gurgaon': 102}
         posted_map = {'Owner': 0, 'Dealer': 1, 'Builder': 2}
         yes_map = {"Yes": 1, "No": 0}
         posted = request.form["posted"]
         vals.append(posted_map[posted])
         rera=request.form["rera"]
         vals.append(yes_map[rera])
         rooms=request.form["rooms"]
         vals.append(rooms)
         square_foot=request.form["foot"]
         vals.append(square_foot)
         ready=request.form["ready_to_move"]
         vals.append(yes_map[ready])
         resale=request.form["resale"]
         vals.append(yes_map[resale])
         location=request.form["location"]
         vals.append(location_map[location])
         with open("my_model.pkl","rb") as f:
             model=pickle.load(f)
         with open("my_scalar.pkl","rb") as f:
             scalar=pickle.load(f)
         vals=scalar.transform([vals])
         res=model.predict(vals)
         for val in res:
             flash(f"The Price of the House is around {int(val)} Lacs","info")
         return render_template("index.html")
if __name__=="__main__":
    app.run(debug=True)
