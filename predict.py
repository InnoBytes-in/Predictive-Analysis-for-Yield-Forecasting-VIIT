import pickle
import numpy as np
from enum import Enum

filename = "Maharashtra_Model.sav"
model = pickle.load(open(filename, "rb"))


class District(Enum):
    AKOLA = "District_Name_AKOLA"
    AMRAVATI = "District_Name_AMRAVATI"
    AURANGABAD = "District_Name_AURANGABAD"
    BEED = "District_Name_BEED"
    BHANDARA = "District_Name_BHANDARA"
    BULDHANA = "District_Name_BULDHANA"
    CHANDRAPUR = "District_Name_CHANDRAPUR"
    DHULE = "District_Name_DHULE"
    GADCHIROLI = "District_Name_GADCHIROLI"
    GONDIA = "District_Name_GONDIA"
    HINGOLI = "District_Name_HINGOLI"
    JALGAON = "District_Name_JALGAON"
    JALNA = "District_Name_JALNA"
    KOLHAPUR = "District_Name_KOLHAPUR"
    LATUR = "District_Name_LATUR"
    MUMBAI = "District_Name_MUMBAI"
    NAGPUR = "District_Name_NAGPUR"
    NANDED = "District_Name_NANDED"
    NANDURBAR = "District_Name_NANDURBAR"
    NASHIK = "District_Name_NASHIK"
    OSMANABAD = "District_Name_OSMANABAD"
    PALGHAR = "District_Name_PALGHAR"
    PARBHANI = "District_Name_PARBHANI"
    PUNE = "District_Name_PUNE"
    RAIGAD = "District_Name_RAIGAD"
    RATNAGIRI = "District_Name_RATNAGIRI"
    SANGLI = "District_Name_SANGLI"
    SATARA = "District_Name_SATARA"
    SINDHUDURG = "District_Name_SINDHUDURG"
    SOLAPUR = "District_Name_SOLAPUR"
    THANE = "District_Name_THANE"
    WARDHA = "District_Name_WARDHA"
    WASHIM = "District_Name_WASHIM"
    YAVATMAL = "District_Name_YAVATMAL"


class Season(Enum):
    Kharif = "Season_Kharif     "
    Rabi = "Season_Rabi       "
    Summer = "Season_Summer     "
    WholeYear = "Season_Whole Year "


class Crop(Enum):
    Bajra = "Crop_Bajra"
    Cotton = "Crop_Cotton(lint)"
    Jowar = "Crop_Jowar"
    Linseed = "Crop_Linseed"
    Maize = "Crop_Maize"
    Onion = "Crop_Onion"
    Rice = "Crop_Rice"
    Sesamum = "Crop_Sesamum"
    Wheat = "Crop_Wheat"


def maharashtra_dict(area: int | float, district: District, season: Season, crop: Crop):
    mh_dict = {
        "area": 0,
        District.AKOLA.value: 0,
        District.AMRAVATI.value: 0,
        District.AURANGABAD.value: 0,
        District.BEED.value: 0,
        District.BHANDARA.value: 0,
        District.BULDHANA.value: 0,
        District.CHANDRAPUR.value: 0,
        District.DHULE.value: 0,
        District.GADCHIROLI.value: 0,
        District.GONDIA.value: 0,
        District.HINGOLI.value: 0,
        District.JALGAON.value: 0,
        District.JALNA.value: 0,
        District.KOLHAPUR.value: 0,
        District.LATUR.value: 0,
        District.MUMBAI.value: 0,
        District.NAGPUR.value: 0,
        District.NANDED.value: 0,
        District.NANDURBAR.value: 0,
        District.NASHIK.value: 0,
        District.OSMANABAD.value: 0,
        District.PALGHAR.value: 0,
        District.PARBHANI.value: 0,
        District.PUNE.value: 0,
        District.RAIGAD.value: 0,
        District.RATNAGIRI.value: 0,
        District.SANGLI.value: 0,
        District.SATARA.value: 0,
        District.SINDHUDURG.value: 0,
        District.SOLAPUR.value: 0,
        District.THANE.value: 0,
        District.WARDHA.value: 0,
        District.WASHIM.value: 0,
        District.YAVATMAL.value: 0,
        Season.Kharif.value: 0,
        Season.Rabi.value: 0,
        Season.Summer.value: 0,
        Season.WholeYear.value: 0,
        Crop.Bajra.value: 0,
        Crop.Cotton.value: 0,
        Crop.Jowar.value: 0,
        Crop.Linseed.value: 0,
        Crop.Maize.value: 0,
        Crop.Onion.value: 0,
        Crop.Rice.value: 0,
        Crop.Sesamum.value: 0,
        Crop.Wheat.value: 0,
    }
    mh_dict["area"] = area
    mh_dict[district.value] = 1
    mh_dict[season.value] = 1
    mh_dict[crop.value] = 1
    data = list(mh_dict.values())
    input_arr = np.array(data)
    return input_arr


def predict(area: int | float, district: District, season: Season, crop: Crop):
    arr = maharashtra_dict(area, district, season, crop)
    result = model.predict([arr])
    return result


print(predict(31500, District.NANDED, Season.Rabi, Crop.Wheat))
