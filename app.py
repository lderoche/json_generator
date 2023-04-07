from flask import *
import json
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        dictionary = {
            "Design_Variations":{
                "{}".format(request.form["Name"]):{
                    "Color":"RGBA{}".format(tuple(int(request.form["Color"].lstrip('#')[i:i+2], 16) for i in (0, 2, 4))+(1,)),
                    "Font":"{}".format(request.form["Font"]),
                    "Size":"{}".format(request.form["Size"]),
                    "BorderColor":"RGBA{}".format(tuple(int(request.form["BorderColor"].lstrip('#')[i:i+2], 16) for i in (0, 2, 4))+(1,)),
                    "Fill":"RGBA{}".format(tuple(int(request.form["Fill"].lstrip('#')[i:i+2], 16) for i in (0, 2, 4))+(1,)),
                    "{}_Button".format(request.form["Name"]):{
                        "BorderThickness":"{}".format(request.form["BorderThickness"]),
                        "RadiusTopLeft":"{}".format(request.form["RadiusTopLeft"]),
                        "RadiusTopRight":"{}".format(request.form["RadiusTopRight"]),
                        "RadiusBottomLeft":"{}".format(request.form["RadiusBottomLeft"]),
                        "RadiusBottomRight":"{}".format(request.form["RadiusBottomRight"])
                    }
                }
            }
        }
        json_object = json.dumps(dictionary, indent=4)
        with open("elements.json","w") as outfile:
            outfile.write(json_object)
        print(json_object)
        return json_object
    return render_template("home.html")


if __name__ == "__main__":
    app.run()