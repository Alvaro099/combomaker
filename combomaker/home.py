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
        "Back" : "combomaker/static/TWOXKO Notation PNGs/movement/2XKO_Back_Input_icon.png" , 
        "DoubleBack" : "combomaker/static/TWOXKO Notation PNGs/movement/2XKO_DoubleBack_Input_icon.png" ,
        "DoubleForward" : "combomaker/static/TWOXKO Notation PNGs/movement/2XKO_DoubleForward_Input_icon.png" ,
        "Down" : "combomaker/static/TWOXKO Notation PNGs/movement/2XKO_Down_Input_icon.png" ,
        "DownBack" : "combomaker/static/TWOXKO Notation PNGs/movement/2XKO_DownBack_Input_icon.png" ,
        "DownForward" : "combomaker/static/TWOXKO Notation PNGs/movement/2XKO_DownForward_Input_icon.png" ,
        "Forward" : "combomaker/static/TWOXKO Notation PNGs/movement/2XKO_Forward_Input_icon.png" ,
        "Up" : "combomaker/static/TWOXKO Notation PNGs/movement/2XKO_Up_Input_icon.png" ,
        "UpBack" : "combomaker/static/TWOXKO Notation PNGs/movement/2XKO_UpBack_Input_icon.png" ,
        "UpForward" : "combomaker/static/TWOXKO Notation PNGs/movement/2XKO_UpForward_Input_icon.png" , 

    }

    list_special_2xko = {
        "Sequence" : "combomaker/static/TWOXKO Notation PNGs/special/2XKO_Sequence_icon.png ",
        "Tag" : "combomaker/static/TWOXKO Notation PNGs/special/2XKO_Tag_input_icon.png",
    }

    list_buttons_tekken = { 
        "0" : "combomaker/static/Tekken Notation PNGs/buttons/0.png",
        "1" : "combomaker/static/Tekken Notation PNGs/buttons/1.png",
        "1+2" : "combomaker/static/Tekken Notation PNGs/buttons/1+2.png",
        "1+2+3" : "combomaker/static/Tekken Notation PNGs/buttons/1+2+3.png",
        "1+2+3+4" : "combomaker/static/Tekken Notation PNGs/buttons/1+2+3+4.png",
        "1+2+4" : "combomaker/static/Tekken Notation PNGs/buttons/1+2+4.png",
        "1+3" : "combomaker/static/Tekken Notation PNGs/buttons/1+3.png",
        "1+3+4" : "combomaker/static/Tekken Notation PNGs/buttons/1+3+4.png",
        "1+4" : "combomaker/static/Tekken Notation PNGs/buttons/1+4.png",
        "2" : "combomaker/static/Tekken Notation PNGs/buttons/2.png",
        "2+3" : "combomaker/static/Tekken Notation PNGs/buttons/2+3.png",
        "2+3+4" : "combomaker/static/Tekken Notation PNGs/buttons/2+3+4.png",
        "2+4" : "combomaker/static/Tekken Notation PNGs/buttons/2+4.png",
        "3" : "combomaker/static/Tekken Notation PNGs/buttons/3.png",
        "3+4" : "combomaker/static/Tekken Notation PNGs/buttons/3+4.png",
        "4" : "combomaker/static/Tekken Notation PNGs/buttons/4.png",
    }

    list_movement_tekken = {
        "b" : "combomaker/static/Tekken Notation PNGs/movement/b.png" ,
        "bhold" : "combomaker/static/Tekken Notation PNGs/movement/bhold.png",
        "d" : "combomaker/static/Tekken Notation PNGs/movement/d.png" ,
        "db" : "combomaker/static/Tekken Notation PNGs/movement/db.png",
        "dbhold" : "combomaker/static/Tekken Notation PNGs/movement/dbhold.png",
        "df" : "combomaker/static/Tekken Notation PNGs/movement/df.png",
        "dfhold" : "combomaker/static/Tekken Notation PNGs/movement/dfhold.png",
        "dhold" : "combomaker/static/Tekken Notation PNGs/movement/dhold.png",
        "f" : "combomaker/static/Tekken Notation PNGs/movement/f.png" ,
        "fhold" : "combomaker/static/Tekken Notation PNGs/movement/fhold.png",
        "n" : "combomaker/static/Tekken Notation PNGs/movement/n.png",
        "u" : "combomaker/static/Tekken Notation PNGs/movement/u.png",
        "ub" : "combomaker/static/Tekken Notation PNGs/movement/ub.png",
        "ubhold" : "combomaker/static/Tekken Notation PNGs/movement/ubhold.png",
        "uf" : "combomaker/static/Tekken Notation PNGs/movement/uf.png",
        "ufhold" : "combomaker/static/Tekken Notation PNGs/movement/ufhold.png",
        "uhold" : "combomaker/static/Tekken Notation PNGs/movement/uhold.png",
    }

    list_special_tekken = {
        "Balconybreak" : "combomaker/static/Tekken Notation PNGs/special/Balconybreak.png",
        "bracketl" : "combomaker/static/Tekken Notation PNGs/special/bracketl.png",
        "bracketr" : "combomaker/static/Tekken Notation PNGs/special/bracketr.png",
        "chip" : "combomaker/static/Tekken Notation PNGs/special/chip.png",
        "Floorblast" : "combomaker/static/Tekken Notation PNGs/special/Floorblast.png",
        "Floorbreak" : "combomaker/static/Tekken Notation PNGs/special/Floorbreak.png",
        "forcecrouch" : "combomaker/static/Tekken Notation PNGs/special/forcecrouch.png",
        "heat" : "combomaker/static/Tekken Notation PNGs/special/heat.png",
        "homing" : "combomaker/static/Tekken Notation PNGs/special/homing.png",
        "powercrush" : "combomaker/static/Tekken Notation PNGs/special/powercrush.png",
        "tornado" : "combomaker/static/Tekken Notation PNGs/special/tornado.png",
        "Wallblast" : "combomaker/static/Tekken Notation PNGs/special/Wallblast.png",
        "Wallbound" : "combomaker/static/Tekken Notation PNGs/special/Wallbound.png",
        "Wallbreak" : "combomaker/static/Tekken Notation PNGs/special/Wallbreak.png",
    }

    list_movement_sf6 = {
        "key-d" : "combomaker/static/Street Fighter 6 Notation PNGs/movement/key-d.png" ,
        "key-dc" : "combomaker/static/Street Fighter 6 Notation PNGs/movement/key-dc.png" ,
        "key-dl" : "combomaker/static/Street Fighter 6 Notation PNGs/movement/key-dl.png" ,
        "key-dr" : "combomaker/static/Street Fighter 6 Notation PNGs/movement/key-dr.png" ,
        "key-l" : "combomaker/static/Street Fighter 6 Notation PNGs/movement/key-l.png" ,
        "key-lc" : "combomaker/static/Street Fighter 6 Notation PNGs/movement/key-lc.png" ,
        "key-r" : "combomaker/static/Street Fighter 6 Notation PNGs/movement/key-r.png" ,
        "key-u" : "combomaker/static/Street Fighter 6 Notation PNGs/movement/key-u.png" ,
    }

    list_buttons_sf6 = {
        "kick_h" : "combomaker/static/Street Fighter 6 Notation PNGs/buttons/icon_kick_h.png",
        "kick_l" : "combomaker/static/Street Fighter 6 Notation PNGs/buttons/icon_kick_l.png",
        "kick_m" : "combomaker/static/Street Fighter 6 Notation PNGs/buttons/icon_kick_m.png",
        "kick": "combomaker/static/Street Fighter 6 Notation PNGs/buttons/icon_kick.png",
        "punch_h" : "combomaker/static/Street Fighter 6 Notation PNGs/buttons/icon_punch_h.png",
        "punch_l" : "combomaker/static/Street Fighter 6 Notation PNGs/buttons/icon_punch_l.png",
        "punch_m" : "combomaker/static/Street Fighter 6 Notation PNGs/buttons/icon_punch_m.png",
        "punch" : "combomaker/static/Street Fighter 6 Notation PNGs/buttons/icon_punch.png",
    }

    list_special_sf6 = {

        "arrow_3" : "combomaker/static/Street Fighter 6 Notation PNGs/special/arrow_3.png",
        "f" : "combomaker/static/Street Fighter 6 Notation PNGs/special/f.png",
        "key-nutral" : "combomaker/static/Street Fighter 6 Notation PNGs/special/key-nutral.png" , 
        "key-plus" : "combomaker/static/Street Fighter 6 Notation PNGs/special/key-plus.png",
        "modern_dl" : "combomaker/static/Street Fighter 6 Notation PNGs/special/modern_dl.png",
        "modern_sp" : "combomaker/static/Street Fighter 6 Notation PNGs/special/modern_sp.png",
    }



    

    return render_template('home.html',
        list_movement_2xko=list_movement_2xko,
        list_buttons_2xko=list_buttons_2xko,
        list_special_2xko=list_special_2xko,
        list_movement_tekken=list_movement_tekken,
        list_buttons_tekken=list_buttons_tekken,
        list_special_tekken=list_special_tekken,
        list_movement_sf6=list_movement_sf6,
        list_buttons_sf6=list_buttons_sf6,
        list_special_sf6=list_special_sf6
    )


