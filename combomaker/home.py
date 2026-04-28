from flask import Blueprint, render_template

bp = Blueprint('home', __name__)

@bp.route('/')
def index():

    list_buttons_2xko = {
    "Heavy": "combomaker/static/TWOXKO Notation PNGs/buttons/2XKO_Heavy_Input_icon.png",
    "Light": "combomaker/static/TWOXKO Notation PNGs/buttons/2XKO_Light_Input_icon.png",
    "Medium": "combomaker/static/TWOXKO Notation PNGs/buttons/2XKO_Medium_Input_icon.png",
    "S1": "combomaker/static/TWOXKO Notation PNGs/buttons/2XKO_S1_Input_icon.png",
    "S2": "combomaker/static/TWOXKO Notation PNGs/buttons/2XKO_S2_Input_icon.png"
    }

    list_movement_2xko = {
        "Back" : "" , 
        "DoubleBack" : "" ,
        "Down" : "" ,
        "DownBack" : "" ,
        "DownForward" : "" ,
        "Forward" : "" ,
        "Up" : "" ,
        "UpBack" : "" ,
        "UpForward" : "" , 

    }

    list_special_2xko = {
        "Sequence" : "",
        "Tag" : "",
    }

    list_buttons_tekken = { 
        "0" : "",
        "1" : "",
        "1+2" : "",
        "1+2+3" : "",
        "1+2+3+4" : "",
        "1+2+4" : "",
        "1+3" : "",
        "1+3+4" : "",
        "1+4" : "",
        "2" : "",
        "2+3" : "",
        "2+3+4" : "",
        "2+4" : "",
        "3" : "",
        "3+4" : "",
        "4" : "",
    }

    list_movement_tekken = {
        "b" : "" ,
        "bhold" : "",
        "d" : "" ,
        "db" : "",
        "dbhold" : "",
        "df" : "",
        "dfhold" : "",
        "dhold" : "",
        "f" : "" ,
        "fhold" : "",
        "n" : "",
        "u" : "",
        "ub" : "",
        "ubhold" : "",
        "uf" : "",
        "ufhold" : "",
        "uhold" : "",
    }

    list_special_tekken = {
        "Balconybreak" : "",
        "bracketl" : "",
        "bracketr" : "",
        "chip" : "",
        "Floorblast" : "",
        "Floorbreak" : "",
        "forcecrouch" : "",
        "heat" : "",
        "homing" : "",
        "powercrush" : "",
        "tornado" : "",
        "Wallblast" : "",
        "Wallbound" : "",
        "Wallbreak" : "",
    }

    list_movement_sf6 = {
        "key-d" : "" ,
        "key-dc" : "" ,
        "key-dl" : "" ,

    }

    list_buttons_sf6 = {
        "kick_h" : "",
        "kick_l" : "",
        "kick_m" : "",
        "kick": "",
        "punch_h" : "",
        "punch_l" : "",
        "punch_m" : "",
        "punch" : "",
    }

    list_special_sf6 = {
    }



    

    return render_template('home.html')


