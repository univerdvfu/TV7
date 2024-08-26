data_registers = {
    "device_type": {
        "registers":{
            "2.21": 0,
            "2.19": 0
        },
        "data_type":{
            "type":"unsigned_short",
            "bit": 1
        } 
       
    },
    "software_version": {
        "registers":{
            "2.21": 1,
            "2.19": 1
        },
         "data_type":{
            "type":"unsigned_short", 
            "bit": 1
        } 
    },
    "date_day": {
        "registers":{
            "2.21": 7816,
            "2.19": 3540
        },
         "data_type":{
            "type":"unsigned_short",
            "bit": 1
        } 
    },
    "date_hours": {
        "registers":{
            "2.21": 7817,
            "2.19": 3541
        },
         "data_type":{
            "type":"unsigned_short",
            "bit": 1
        } 
    },
    "date_minutes": {
        "registers":{
            "2.21": 7818,
            "2.19": 3542
        },
         "data_type":{
            "type":"unsigned_short",
            "bit": 1
        } 
    },
    "temp": {
        "registers":{
            "2.21": 7819,
            "2.19": 3543
        },
        "data_type":{
            "type":"float",
            "bit": 2
        } 
    },
    "pressure": {
        "registers":{
            "2.21": 7833,
            "2.19": 3555
        },
        "data_type":{
            "type":"float",
            "bit": 2
        }
    },
    "volume_consumption": {
        "registers":{
            "2.21": 7847,
            "2.19": 3567
        },
        "data_type":{
            "type":"float",
            "bit": 2
        }
    },
    "mass_consumption": {
        "registers":{
            "2.21": 7861,
            "2.19": 3579
        },
        "data_type":{
            "type":"float",
            "bit": 2
        }
    },
    "heat_flow": {
        "registers":{
            "2.21": 7875,
            "2.19": 3591
        },
        "data_type":{
            "type":"float",
            "bit": 2
        }
    },
    "enthalpy": {
        "registers":{
            "2.21": 7889,
            "2.19": 3603
        },
        "data_type":{
            "type":"float",
            "bit": 2
        }
    },
    "": {
        "registers":{
            "2.21": 7903,
            "2.19": 3615
        },
        "data_type":{
            "type":"float",
            "bit": 2
        }
    },
    "enthalpy_of_cold_water": {
        "registers":{
            "2.21": 7909,
            "2.19": 3619
        },
        "data_type":{
            "type":"float",
            "bit": 2
        }
    },
    "additional_parameter": {
        "registers":{
            "2.21": 7915,
            "2.19": 3623
        },
        "data_type":{
            "type":"float",
            "bit": 2
        }
    },
    "emergency_situation_p": {
        "registers":{
            "2.21": 7917,
            "2.19": 3625
        },
        "data_type":{
            "type":"unsigned_char",
            "bit": 1
        }
    },
    "two_position_input": {
        "registers":{
            "2.21": 7920,
            "2.19": None
        },
        "data_type":{
            "type":"bit_field",
            "bit": 1
        }
    },
    "emergency_situation_ti": {
        "registers":{
            "2.21": 7921,
            "2.19": 3628
        },
        "data_type":{
            "type":"unsigned_char",
            "bit": 1
        } 
    },
    "emergency_situation_ap": {
        "registers":{
            "2.21": 7924,
            "2.19": 3630
        },
        "data_type":{
            "type":"bit_field",
            "bit": 1
        }
    },
    "signs_of_events": {
        "registers":{
            "2.21": 7925,
            "2.19": 3631
        },
         "data_type":{
            "type":"unsigned_short",
            "bit": 1
        } 
    },
    "cold_water_temperature": {
        "registers":{
            "2.21": 7927,
            "2.19": 3633
        },
        "data_type":{
            "type":"float",
            "bit": 2
        }
    },
    "cold_water_pressure": {
        "registers":{
            "2.21": 7933,
            "2.19": 3637
        },
        "data_type":{
            "type":"float",
            "bit": 2
        }
    },
    "temperature_difference": {
        "registers":{
            "2.21": 7939,
            "2.19": 3641
        },
        "data_type":{
            "type":"float",
            "bit": 2
        }
    },
    "outdoor_air_temperature": {
        "registers":{
            "2.21": 7945,
            "2.19": 3645
        },
        "data_type":{
            "type":"float",
            "bit": 2
        }
    },
    "signs_of_empty_pipe": {
        "registers":{
            "2.21": 7951,
            "2.19": None
        },
        "data_type":{
            "type":"bit_field",
            "bit": 1
        }
    },
    "signs_reverse_through_pipes": {
        "registers":{
            "2.21": 7951,
            "2.19": None
        },
        "data_type":{
            "type":"bit_field",
            "bit": 1
        }
    },
    "situation_reverse_through_pipes": {
        "registers":{
            "2.21": 7952,
            "2.19": None
        },
        "data_type":{
            "type":"bit_field",
            "bit": 1
        }
    },
    "active_database": {
        "registers":{
            "2.21": 7953,
            "2.19": 3649
        },
        "data_type":{
            "type":"bit_field",
            "bit": 1
        }
    },
}
print(data_registers["device_type"]["registers"]["2.21"])


