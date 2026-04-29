from flask import Blueprint, render_template

bp = Blueprint('home', __name__)

@bp.route('/')
def index():

    return render_template('home.html'
    )




@bp.route('/combos/2xko')
def combos_2xko():

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
        "Tag" : "combomaker/static/TWOXKO Notation PNGs/special/2XKO_Tag_Input_icon.png",
    }

    return render_template('combos_2xko.html', list_buttons_2xko=list_buttons_2xko, list_movement_2xko=list_movement_2xko, list_special_2xko=list_special_2xko)


@bp.route('/combos/tekken')
def combos_tekken():

    list_buttons_tekken = { 
        "0" : "combomaker/static/Tekken Notation PNGs/buttons/0.png",
        "1" : "combomaker/static/Tekken Notation PNGs/buttons/1.png",
        "1+2" : "combomaker/static/Tekken Notation PNGs/buttons/1plus2.png",
        "1+2+3" : "combomaker/static/Tekken Notation PNGs/buttons/1plus2plus3.png",
        "1+2+3+4" : "combomaker/static/Tekken Notation PNGs/buttons/1plus2plus3plus4.png",
        "1+2+4" : "combomaker/static/Tekken Notation PNGs/buttons/1plus2plus4.png",
        "1+3" : "combomaker/static/Tekken Notation PNGs/buttons/1plus3.png",
        "1+3+4" : "combomaker/static/Tekken Notation PNGs/buttons/1plus3plus4.png",
        "1+4" : "combomaker/static/Tekken Notation PNGs/buttons/1plus4.png",
        "2" : "combomaker/static/Tekken Notation PNGs/buttons/2.png",
        "2+3" : "combomaker/static/Tekken Notation PNGs/buttons/2plus3.png",
        "2+3+4" : "combomaker/static/Tekken Notation PNGs/buttons/2plus3plus4.png",
        "2+4" : "combomaker/static/Tekken Notation PNGs/buttons/2plus4.png",
        "3" : "combomaker/static/Tekken Notation PNGs/buttons/3.png",
        "3+4" : "combomaker/static/Tekken Notation PNGs/buttons/3plus4.png",
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

    return render_template('combos_tekken.html', list_buttons_tekken=list_buttons_tekken, list_movement_tekken=list_movement_tekken, list_special_tekken=list_special_tekken)


@bp.route('/combos/sf6')
def combos_sf6():

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

    return render_template('combos_sf6.html', list_buttons_sf6=list_buttons_sf6, list_movement_sf6=list_movement_sf6, list_special_sf6=list_special_sf6)


@bp.route('/combos/generico')
def combos_generico():
    return render_template('combos_generico.html')


@bp.route('/combos/fatal_fury')
def combos_fatal_fury():

    list_buttons_fatal_fury = { 
        "ico1" : "combomaker/static/Fatal Fury Notation PNGs/buttons/ico_explanation01.png",
        "ico2" : "combomaker/static/Fatal Fury Notation PNGs/buttons/ico_explanation02.png",
        "ico3" : "combomaker/static/Fatal Fury Notation PNGs/buttons/ico_explanation03.png",
        "ico4" : "combomaker/static/Fatal Fury Notation PNGs/buttons/ico_explanation04.png",
        "ico7" : "combomaker/static/Fatal Fury Notation PNGs/buttons/ico_explanation07.png",
        "ico8" : "combomaker/static/Fatal Fury Notation PNGs/buttons/ico_explanation08.png",
        "ico9" : "combomaker/static/Fatal Fury Notation PNGs/buttons/ico_explanation09.png",
        "ico10" : "combomaker/static/Fatal Fury Notation PNGs/buttons/ico_explanation10.png",
        "ico16" : "combomaker/static/Fatal Fury Notation PNGs/buttons/ico_explanation16.png",
        "ico17" : "combomaker/static/Fatal Fury Notation PNGs/buttons/ico_explanation17.png",
    }

    list_movement_fatal_fury = { 
        "2QCF_Input" : "combomaker/static/Fatal Fury Notation PNGs/movement/2QCF_Input.webp",
        "360_Input" : "combomaker/static/Fatal Fury Notation PNGs/movement/360_Input.webp",
        "Back_Input" : "combomaker/static/Fatal Fury Notation PNGs/movement/Back_Input.webp",
        "Double_Down_Input" : "combomaker/static/Fatal Fury Notation PNGs/movement/Double_Down_Input.webp",
        "Down_Forward_Input" : "combomaker/static/Fatal Fury Notation PNGs/movement/Down_Forward_Input.webp",
        "Down_Input" : "combomaker/static/Fatal Fury Notation PNGs/movement/Down_Input.webp",
        "Down_Up_Input" : "combomaker/static/Fatal Fury Notation PNGs/movement/Down_Up_Input.webp",
        "EX_OK" : "combomaker/static/Fatal Fury Notation PNGs/movement/EX_OK.webp",
        "Forward_Input" : "combomaker/static/Fatal Fury Notation PNGs/movement/Forward_Input.webp",
        "HCB_Input" : "combomaker/static/Fatal Fury Notation PNGs/movement/HCB_Input.webp",
        "HCBF_Input" : "combomaker/static/Fatal Fury Notation PNGs/movement/HCBF_Input.webp",
        "HCF_Input" : "combomaker/static/Fatal Fury Notation PNGs/movement/HCF_Input.webp",
        "Neutral_Input" : "combomaker/static/Fatal Fury Notation PNGs/movement/Neutral_Input.webp",
        "QCB_Input" : "combomaker/static/Fatal Fury Notation PNGs/movement/QCB_Input.webp",
        "QCBHCF_Input" : "combomaker/static/Fatal Fury Notation PNGs/movement/QCBHCF_Input.webp",
        "QCF_Input" : "combomaker/static/Fatal Fury Notation PNGs/movement/QCF_Input.webp",
        "QCFHCB_Input" : "combomaker/static/Fatal Fury Notation PNGs/movement/QCFHCB_Input.webp",
        "RZ_Input" : "combomaker/static/Fatal Fury Notation PNGs/movement/RZ_Input.webp",
        "Z_Input" : "combomaker/static/Fatal Fury Notation PNGs/movement/Z_Input.webp",
    }

    list_special_fatal_fury = { 
        "ico5" : "combomaker/static/Fatal Fury Notation PNGs/special/ico_explanation05.png",
        "ico11" : "combomaker/static/Fatal Fury Notation PNGs/special/ico_explanation11.png",
        "ico12" : "combomaker/static/Fatal Fury Notation PNGs/special/ico_explanation12.png",
        "ico13" : "combomaker/static/Fatal Fury Notation PNGs/special/ico_explanation13.png",
        "ico14" : "combomaker/static/Fatal Fury Notation PNGs/special/ico_explanation14.png",
        "ico15" : "combomaker/static/Fatal Fury Notation PNGs/special/ico_explanation15.png",
    }

    return render_template('combos_fatal_fury.html', list_buttons_fatal_fury=list_buttons_fatal_fury, list_movement_fatal_fury=list_movement_fatal_fury, list_special_fatal_fury=list_special_fatal_fury)  



@bp.route('/combos/kofxv')
def combos_kofxv():

    list_buttons_kofxv = { 
        "icn9" : "combomaker/static/KOFXV Notation PNGs/buttons/icn9.png",
        "icn10" : "combomaker/static/KOFXV Notation PNGs/buttons/icn10.png",
        "icn12" : "combomaker/static/KOFXV Notation PNGs/buttons/icn12.png",
        "icn13" : "combomaker/static/KOFXV Notation PNGs/buttons/icn13.png",
        "icn14" : "combomaker/static/KOFXV Notation PNGs/buttons/icn14.png",
        "icn15" : "combomaker/static/KOFXV Notation PNGs/buttons/icn15.png",
        
        
    }

    list_movement_kofxv = { 

        "2QCF_Input" : "combomaker/static/KOFXV Notation PNGs/movement/2QCF_Input.webp",
        "360_Input" : "combomaker/static/KOFXV Notation PNGs/movement/360_Input.webp",
        "Back_Input" : "combomaker/static/KOFXV Notation PNGs/movement/Back_Input.webp",
        "Double_Down_Input" : "combomaker/static/KOFXV Notation PNGs/movement/Double_Down_Input.webp",
        "Down_Forward_Input" : "combomaker/static/KOFXV Notation PNGs/movement/Down_Forward_Input.webp",
        "Down_Input" : "combomaker/static/KOFXV Notation PNGs/movement/Down_Input.webp",
        "Down_Up_Input" : "combomaker/static/KOFXV Notation PNGs/movement/Down_Up_Input.webp",
        "Forward_Input" : "combomaker/static/KOFXV Notation PNGs/movement/Forward_Input.webp",
        "HCB_Input" : "combomaker/static/KOFXV Notation PNGs/movement/HCB_Input.webp",
        "HCBF_Input" : "combomaker/static/KOFXV Notation PNGs/movement/HCBF_Input.webp",
        "HCF_Input" : "combomaker/static/KOFXV Notation PNGs/movement/HCF_Input.webp",
        "Neutral_Input" : "combomaker/static/KOFXV Notation PNGs/movement/Neutral_Input.webp",
        "QCB_Input" : "combomaker/static/KOFXV Notation PNGs/movement/QCB_Input.webp",
        "QCBHCF_Input" : "combomaker/static/KOFXV Notation PNGs/movement/QCBHCF_Input.webp",
        "QCF_Input" : "combomaker/static/KOFXV Notation PNGs/movement/QCF_Input.webp",
        "QCFHCB_Input" : "combomaker/static/KOFXV Notation PNGs/movement/QCFHCB_Input.webp",
        "RZ_Input" : "combomaker/static/KOFXV Notation PNGs/movement/RZ_Input.webp",
        "Z_Input" : "combomaker/static/KOFXV Notation PNGs/movement/Z_Input.webp",
        
    }

    list_special_kofxv = { 

        "icn1" : "combomaker/static/KOFXV Notation PNGs/specials/icn1.png",
        "icn2" : "combomaker/static/KOFXV Notation PNGs/specials/icn2.png",
        "icn3" : "combomaker/static/KOFXV Notation PNGs/specials/icn3.png",
        "icn4" : "combomaker/static/KOFXV Notation PNGs/specials/icn4.png",
        "icn5" : "combomaker/static/KOFXV Notation PNGs/specials/icn5.png",
        "icn6" : "combomaker/static/KOFXV Notation PNGs/specials/icn6.png",
        "icn7" : "combomaker/static/KOFXV Notation PNGs/specials/icn7.png",
        "icn8" : "combomaker/static/KOFXV Notation PNGs/specials/icn8.png",
        "icn18" : "combomaker/static/KOFXV Notation PNGs/specials/icn18.png",
        "icn19" : "combomaker/static/KOFXV Notation PNGs/specials/icn19.png",
        "icn20" : "combomaker/static/KOFXV Notation PNGs/specials/icn20.png",
        "icn21" : "combomaker/static/KOFXV Notation PNGs/specials/icn20.png",
        
    }


    return render_template('combos_kofxv.html', list_buttons_kofxv=list_buttons_kofxv, list_movement_kofxv=list_movement_kofxv, list_special_kofxv=list_special_kofxv)  


@bp.route('/combos/ggst')
def combos_ggst():

    list_buttons_ggst = { 

        "D" : "combomaker/static/Strive Notation PNGs/buttons/22px-GGST_D_Prompt.png",
        "H" : "combomaker/static/Strive Notation PNGs/buttons/22px-GGST_H_Prompt.png",
        "K" : "combomaker/static/Strive Notation PNGs/buttons/22px-GGST_K_Prompt.png",
        "P" : "combomaker/static/Strive Notation PNGs/buttons/22px-GGST_P_Prompt.png",
        "S" : "combomaker/static/Strive Notation PNGs/buttons/22px-GGST_S_Prompt.png",
        
    }

    list_movement_ggst = { 
        "inputicon_1" : "combomaker/static/Strive Notation PNGs/movement/24px-InputIcon_1.png",
        "inputicon_2" : "combomaker/static/Strive Notation PNGs/movement/24px-InputIcon_2.png",
        "inputicon_3" : "combomaker/static/Strive Notation PNGs/movement/24px-InputIcon_3.png",
        "inputicon_4" : "combomaker/static/Strive Notation PNGs/movement/24px-InputIcon_4.png",
        "inputicon_5" : "combomaker/static/Strive Notation PNGs/movement/24px-InputIcon_5.png",
        "inputicon_6" : "combomaker/static/Strive Notation PNGs/movement/24px-InputIcon_6.png",
        "inputicon_7" : "combomaker/static/Strive Notation PNGs/movement/24px-InputIcon_7.png",
        "inputicon_8" : "combomaker/static/Strive Notation PNGs/movement/24px-InputIcon_8.png",
        "inputicon_9" : "combomaker/static/Strive Notation PNGs/movement/24px-InputIcon_9.png",
        "inputicon_214" : "combomaker/static/Strive Notation PNGs/movement/24px-InputIcon_214.png",
        "inputicon_236" : "combomaker/static/Strive Notation PNGs/movement/24px-InputIcon_236.png",
        "inputicon_360" : "combomaker/static/Strive Notation PNGs/movement/24px-InputIcon_360.png",
        "inputicon_623" : "combomaker/static/Strive Notation PNGs/movement/24px-InputIcon_623.png",
        "inputicon_41236" : "combomaker/static/Strive Notation PNGs/movement/24px-InputIcon_41236.png",
        "inputicon_63214" : "combomaker/static/Strive Notation PNGs/movement/24px-InputIcon_63214.png",
        
    }

    list_special_ggst = { 

        "icn1" : "combomaker/static/Strive Notation PNGs/specials/icn1.webp",
        "icn2" : "combomaker/static/Strive Notation PNGs/specials/icn2.webp",
        "icn3" : "combomaker/static/Strive Notation PNGs/specials/icn3.webp",
        "icn4" : "combomaker/static/Strive Notation PNGs/specials/icn6.png",
    }


    return render_template('combos_ggst.html', list_buttons_ggst=list_buttons_ggst, list_movement_ggst=list_movement_ggst, list_special_ggst=list_special_ggst)  


@bp.route('/combos/dbfz')
def combos_dbfz():

    list_buttons_dbfz = { 
        
    }

    list_movement_dbfz = { 
        
    }

    list_special_dbfz = { 
        
    }


    return render_template('combos_dbfz.html', list_buttons_dbfz=list_buttons_dbfz, list_movement_dbfz=list_movement_dbfz, list_special_dbfz=list_special_dbfz)  