APPAREL = {
  #image -> [0]box size within which logo should fit, [1]postion (x, y)
  "tshirt": [520, (380, 370)],
  # "hoodie": [300, (475, 520)],
  #  "cap": [340, (460, 500)],
  "sweatshirt": [400, (430, 440)],
  "white_tshirt_model" : [410, (460, 700)],
  "beige_tshirt_model" : [430, (430, 515)],
  "man_in_hoodie" : [445, (525, 430)],
  "green_bg_hoodie" : [305, (375, 415)] 
}

OBJECTS = {
  #image -> [0]box size within which logo should fit, [1]postion (x, y)
  "mug": [545, (295, 455)],
  "totebag": [480, (405, 690)],
  "notebook": [650, (340, 330)],
  "case": [510, (380, 415)],
  "mug_with_background": [435, (533, 575)],
  "woman_with_bag" : [490, (450, 570)],
  "cup_with_bg" : [360, (490, 660)],
  "advert" : [360, (735, 195)]
}

# card_name -> dict with attributes
BCARDS = {
        # each attribute -> position(x, y), fill_color (R, G, B, A), font_weight (heavy or thin)
  "b1" : {
          "name" : [(660, 100), (240, 160, 84, 255), "H"],
          "title" : [(660, 70), (240, 160, 84, 255), "T"],
          "address" : [(720, 425), (240, 160, 84, 255), "T"],
          "web" : [(720, 350), (240, 160, 84, 255), "T"],
          "phone" : [(720, 285), (240, 160, 84, 255), "T"],
          "less_companydesc" : [(750, 475), (34,34,34,255), "T"],
          "less_companyname" : [(750, 500), (34,34,34,255), "H"],
        },

  "b2" : {
        "name" : [(82, 70), (238,44,56,255), "H", 11],
        "companyname" : [(650, 445), (238,44,56,255), "H", 14],
        "companydesc" : [(650, 490), (27,31,42,255), "T", 14],
        "title" : [(82, 105), (27,31,42,255), "T", 24],
        "address" : [(175, 480), (27,31,42,255), "T", 100],
        "web" : [(175, 395), (27,31,42,255), "T", 18],
        "phone" : [(177, 315), (27,31,42,255), "T", 15],
        "less_companydesc" : [(450, 280), (255,255,255,255), "T", 14],
        "less_companyname" : [(450, 300), (238,44,56,255), "H", 14],
      },

  "b3" : {
        "name" : [(80, 80), (1, 1, 1, 255), "H", 11],
        "companyname" : [(755, 75), (1, 1, 1, 255), "H", 14],
        "companydesc" : [(755, 120), (1, 1, 1, 255), "T", 14],
        "title" : [(80, 120), (1, 1, 1, 255), "T", 24],
        "address" : [(170, 500), (1, 1, 1, 255), "T", 100],
        "web" : [(170, 415), (1, 1, 1, 255), "T", 18],
        "phone" : [(170, 335), (1, 1, 1, 255), "T", 15],
        "less_companydesc" : [(445, 275), (1, 1, 1, 255), "T", 14],
        "less_companyname" : [(445, 235), (1, 1, 1, 255), "H", 14],
        "qrcode" : (730, 365)
      },

  "b4" : {
        "name" : [(610, 70), (255, 255, 255, 255), "H", 11],
        "companyname" : [(80, 370), (1, 1, 1, 255), "H", 14],
        "companydesc" : [(80, 340), (1, 1, 1, 255), "T", 14],
        "title" : [(610, 105), (105, 203, 224, 255), "T", 24],
        "address" : [(605, 460), (255, 255, 255, 255), "T", 100],
        "web" : [(605, 335), (255, 255, 255, 255), "T", 18],
        "phone" : [(605, 240), (255, 255, 255, 255), "T", 15],
        "less_companydesc" : [(685, 365), (105, 203, 224, 255), "T", 14],
        "less_companyname" : [(685, 330), (105, 203, 224, 255), "H", 14],
        "qrcode" : (120, 160)
      }
}



CREDITS = {
    "white_tshirt_model" : '<a href="https://www.freepik.com/free-photo/young-brunet-man-wearing-white-t-shirt_11264820.htm#query=white%20tshirt%20model&position=37&from_view=search&track=ais">Image by wayhomestudio</a> on Freepik',

    "beige_tshirt_model" : '<a href="https://www.freepik.com/free-photo/young-handsome-man-posing-quarry_18036306.htm#query=young-handsome-man-posing-quarry&position=0&from_view=search&track=sph">Image by senivpetro</a> on Freepik',

    "man_in_hoodie" : '<a href="https://www.freepik.com/free-psd/simple-white-hoodie-mockup-psd-comfortably-sporty-menswear_14323283.htm#query=man-white-hoodie-streetwear-men-s-apparel-fashion&position=0&from_view=search&track=sph">Image by rawpixel.com</a> on Freepik',

    "sweatshirt" : '<a href="https://www.freepik.com/free-photo/white-sweater-front-back_13237338.htm#query=sweat%20shirt%20mockup&     position=8&from_view=search&track=ais">Image by Vectonauta</a> on Freepik',

    "tshirt" : '<a href="http://www.michaelhoss.com/blog/how-to-create-a-t-shirt-mock">Image from Michael Hoss</a>',

    # "hoodie" : '<a href="https://www.etnvs.site/2022/01/hallo-guys-thank-you-for-visiting-this.html">ENTRAINVERSE</a>',

    "design_b1" : '<a href="https://youtu.be/5TUt_dFJ9Is">Fanky</a>',

    "design_b2" : '<a href="https://youtu.be/R6aTzk-0zIM">Fanky</a>',

    "design_b2" : '<a href="https://graphicsfamily.com/">Graphics family</a>',

    "design_b4" : '<a href="https://youtu.be/mkOhUBGLLW4">Fanky</a>',

    "cup_with_bg" : '<a href="https://www.freepik.com/free-psd/mockup-disposable-coffee-cup_3574781.htm#query=mockup-disposable-coffee-cup&position=0&from_view=search&track=sph">Image by rawpixel.com</a> on Freepik',

    "woman_with_bg" : '<a href="https://www.freepik.com/free-photo/woman-carrying-white-reusable-shopping-bag-studio-shoot_15476285.htm#page=3&query=woman%20with%20tote%20bag&position=14&from_view=search&track=ais">Image by rawpixel.com</a> on Freepik',

    "mug_with_background" : '<a href="https://www.freepik.com/free-psd/coffee-mug-mockup_2566703.htm#query=mug%20mockup&position=28&        from_view=search&track=ais">Image by rawpixel.com</a> on Freepik', 

    "totebag" : '<a href="https://www.pexels.com/photo/person-holding-white-tote-bag-4068314/">pexels</a>',

    "mug" : '<a href="pexels.com>pexels</a>',

    "case" : '<a href="freepik.com">freepik</a>',

    "notebook" : '<a href="freepik.com">freepik</a>',

    "advert" : 'Image by <a href="https://www.freepik.com/free-photo/blank-advertisement-billboard-with-blurred-traffic-lights-night_3274486.htm#query=blank-advertisement-billboard-with-blurred-traffic-lights-night&position=1&from_view=search&track=sph">Freepik</a>'
}   





