from flask import render_template, request, redirect, url_for, flash, send_file, session
from PIL import Image, ImageFilter, ImageFont, ImageDraw
import textwrap
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
import zipfile

from clipmock.helpers import get_dominant_color, mockup, responsive_font
from clipmock.constants import OBJECTS, APPAREL, BCARDS, CREDITS
from clipmock import app, db
from clipmock.models import Users, Images
import qrcode
import os

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.context_processor
def inject_menu():
    
    try:
      menu = {"user_id": session["user_id"]}
    except KeyError:
      menu = {"user_id" : 0} # using 0 for None for easy javascript processing (user id starts from 1 anyways)
    return dict(menu=menu)


@app.route("/")
def index():
  return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "POST":

    username = request.form.get("username")
    if not username:
      flash("Enter username")
      return redirect("/login")
    
    password = request.form.get("password")
    if not password:
      flash("Enter password")
      return redirect("/login")
    
    check_user = Users.query.filter_by(username=username).first()
    if check_user:
      if check_password_hash(check_user.password, password):
        session["user_id"] = check_user.id
        flash("successfully logged in!")
        return redirect("/")
      else:
        flash("username and password don't match")
        return redirect("/login")
    else:
      flash("user doesn't exist, you may want to register")
      return redirect("/login")
  else:
    return render_template("login.html")

@app.route("/logout")
def logout():

  session.clear()
  flash("You've logged out")
  return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
  if request.method == "POST":
    username = request.form.get("username")
    if not username:
      flash("Enter Username")
      return redirect("/register")
    password = request.form.get("password")
    if not password:
      flash("Enter password")
      return redirect("/register")
    confirm = request.form.get("confirm")
    if not confirm:
      flash("Please re-enter password")
      return redirect("/register")
    if password != confirm:
      flash("The passwords don't match")
      return redirect("/register")
    
    found_user = Users.query.filter_by(username=username).first()

    if found_user:
      flash("username already exists")
      return redirect("/register")
    else:
      password = generate_password_hash(password)
      add_usr = Users(username, password)
      db.session.add(add_usr)
      db.session.commit()
      flash("Successfully registered!")
      return redirect("/login")

  else:
    return render_template("register.html") 


@app.route("/apparel", methods=['GET', 'POST'])
def apparel():
  if request.method == "POST":
    if 'file' not in request.files:
      print("file not found")
  
    file = request.files['file']
    if file.filename == '':
      flash("File not selected")
      return redirect(url_for("apparel"))
    
    if not(file and allowed_file(file.filename)):
      flash("Please upload the following formats only - jpeg, jpg, png")
      return redirect(url_for("apparel"))

    list = []
    for key, value in APPAREL.items():
      mockup(name=key, logofile=file, details=value, remove_bg=request.form.get("rembg"))
      list.append("static/after/"+key+".png")

    return render_template("apparel.html", list=list)

  else:
    list = []
    for key, value in APPAREL.items():
      list.append("static/before/"+key+".png")
      print(list)
    return render_template("apparel.html", list=list)

@app.route("/objects", methods=['GET', 'POST'])
def objects():
  if request.method == "POST":
    if 'file' not in request.files:
      print("file not found")
  
    file = request.files['file']
    if file.filename == '':
      flash('No selected file')
      return redirect(url_for("objects"))
    
    if not(file and allowed_file(file.filename)):
      flash("Please upload the following formats only - " + (i for i in ALLOWED_EXTENSIONS))
      return redirect(url_for("objects"))


    list = []
    for key, value in OBJECTS.items():
      mockup(name=key, logofile=file, details=value, remove_bg=request.form.get("rembg"))
      list.append("static/after/"+key+".png")

    return render_template("objects.html", list=list)

  else:
    list = []
    for key, value in OBJECTS.items():
      list.append("static/before/"+key+".png")
      print(list)
    return render_template("objects.html", list=list)
  

@app.route("/collection", methods=['GET'])
def collection():
  try:
    userid = session["user_id"]
  except KeyError:
    flash("login to access your collections")
    return redirect(request.referrer)
  
  username = Users.query.filter_by(id=session["user_id"]).first()
  username = username.username
  collection_images = Images.query.filter_by(user_id=session["user_id"]).all()
  # list that'll be sent to html
  to_be_sent = []
  for image in collection_images:
    img_name = image.imagename
    to_be_sent.append(img_name)

  return render_template("collection.html", list = to_be_sent, username=username)

@app.route("/delete", methods=["POST"])
def delete():
  filename = request.form.get("delete_filename")
  Images.query.filter_by(user_id=session["user_id"], imagename=filename).delete()
  db.session.commit()
  return redirect("/collection")

@app.route("/download", methods=['POST'])
def download():
  # creating zip file
  my_zip = zipfile.ZipFile('clipmock/collection.zip', 'w')

  # accessing user's collection from the db
  all_images = Images.query.filter_by(user_id=session["user_id"]).all()
  # adding respective image files to zip
  if len(all_images): 
    for image in all_images:
      my_zip.write("clipmock/" + image.imagename)
    my_zip.close()
    return send_file('collection.zip')
  else:
    flash("Add design to your collections to download")
    return redirect(request.referrer)

@app.route("/credits")
def credits():
  return render_template("credits.html", credits=CREDITS)


@app.route("/bcards", methods=['GET', 'POST'])
def bcards():
  if request.method == "POST":

    max_length = {
      "firstname" : 25,
      "lastname" : 25,
      "title" : 25, 
      "email" : 50,
      "website" : 50,
      "address" : 100,
      "phone" : 15,
      "companyname" : 25,
      "companydesc" : 25,
      "qrdata" : 200
    }

    for key, value in max_length.items():
      if len(request.form.get(key)) > value:
        flash(f"{key}'s length exceeds limit")
        return redirect(request.referrer)

    details = {}

    #loading form info to a dictionary
    details["name"] = request.form.get("firstname").upper() + " " + request.form.get("lastname").upper()
    details["title"] = request.form.get("title").upper()
    details["web"] = request.form.get("email").upper() + "\n" + request.form.get("website").upper()
    details["address"] = request.form.get("address").upper()
    details["phone"] = request.form.get("phone").upper()
    details["companyname"] = request.form.get("companyname").upper()
    details["companydesc"] = request.form.get("companydesc").upper()

    #formatting to fit image width
    details["address"] = textwrap.fill(details["address"], width=25)

    list = []
    second_img = {}
    for card_name, attributes in BCARDS.items():

      more = Image.open("clipmock/static/before/"+card_name+"_more.png")
      less = Image.open("clipmock/static/before/"+card_name+"_less.png")
      draw_more = ImageDraw.Draw(more)
      draw_less = ImageDraw.Draw(less)

      for detail, values in attributes.items():

        if detail == "qrcode":
          qr = qrcode.QRCode(
              version=1,
              error_correction=qrcode.constants.ERROR_CORRECT_L,
              box_size=10,
              border=1,
          )
          qr.add_data('some data')
          qr.make(fit=True)

          qr_img = qr.make_image(fill_color="black", back_color="white")
          qr_img = qr_img.resize((160, 160))
          more.paste(qr_img, values)
          continue

        font_size = responsive_font(text=details[detail.replace("less_", "")], max_size= 40 if values[2] == 'H' else 25)
        if values[2] == 'H':
          font = ImageFont.truetype("clipmock/static/fonts/Unisans-Trial-Heavy.ttf", size = font_size)
        else:
          font = ImageFont.truetype("clipmock/static/fonts/Unisans-Trial-Book.ttf", size = font_size)
        if detail.startswith("less"):
          draw_less.text(values[0], details[detail.replace("less_", "")], font = font, fill = values[1])
        else:
          draw_more.text(values[0], details[detail], font = font, fill = values[1])

      more.save("clipmock/static/after/"+card_name+"_more.png")
      list.append("static/after/"+card_name+"_more.png")
      less.save("clipmock/static/after/"+card_name+"_less.png")
      second_img["static/after/"+card_name+"_more.png"] = "static/after/"+card_name+"_less.png"

    return render_template("bcards.html", list=list, second_img=second_img)
  else:
    list=[]
    second_img = {}
    for key, value in BCARDS.items():
      list.append("static/before/"+key+"_more.png")
      second_img["static/before/"+key+"_more.png"] = "static/before/"+key+"_less.png"
    return render_template("bcards.html", list=list, second_img=second_img)


# add to collection 
@app.route("/add/<filename>", methods=['POST'])
def add(filename):
  filename = "clipmock/" + filename.replace("@", "/")
  pil_image = Image.open(filename)
  second_img = None

  # for getting primary key which is used for image saving
  image = Images(imagename="for_rollback", user_id=session["user_id"])
  db.session.add(image)
  db.session.flush()
  primary_key = image.id
  db.session.rollback()

  # storing file with primary key
  stored_filename = "static/collection/" + str(primary_key) + ".png"
  image = Images(imagename=stored_filename, user_id=session["user_id"])
  db.session.add(image)
  pil_image.save("clipmock/"+stored_filename)

  # adding both views of business cards 
  if "more" in filename:
    try:
      second_img = Image.open(filename.replace("more", "less"))
      second_filename = "static/collection/" + str(primary_key+1) + ".png"
      image2 = Images(imagename=second_filename, user_id=session["user_id"])
      second_img.save("clipmock/"+second_filename)
      db.session.add(image2)
    except IOError:
      pass

  db.session.commit()
  return redirect(request.referrer)
