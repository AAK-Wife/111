from flask import request

from constants import SANDBOX_JSON_PATH, SANDBOX_TEMP_JSON_PATH, SANDBOX_TABLE_URL
from utils import read_json, write_json, decrypt_battle_data
from core.function.update import updateData


def createGame():
    null = None
    true = True
    false = False
    sandbox = {
        "template": {
            "SANDBOX_V2": {
                "sandbox_1": {
                    "status": {
                        "ver": 1,
                        "state": 1,
                        "ts": 1700000000,
                        "isRift": false,
                        "isGuide": false,
                        "exploreMode": false
                    },
                    "base": {
                        "baseLv": 6,
                        "upgradeProgress": [
                            [
                                0,
                                1
                            ]
                        ],
                        "trapLimit": {},
                        "portableUnlock": true,
                        "outpostUnlock": true,
                        "repairDiscount": 0,
                        "bossKill": []
                    },
                    "main": {
                        "game": {
                            "mapId": "sandbox_1_main_0",
                            "day": 1,
                            "maxDay": 0,
                            "ap": 2,
                            "maxAp": 2
                        },
                        "map": {
                            "season": {
                                "type": 0,
                                "remain": 18,
                                "total": 18
                            },
                            "zone": {
                                "z_1_2": {
                                    "state": 1,
                                    "weather": 0
                                },
                                "z_1_4": {
                                    "state": 1,
                                    "weather": 0
                                },
                                "z_1_3": {
                                    "state": 1,
                                    "weather": 0
                                },
                                "z_1_1": {
                                    "state": 1,
                                    "weather": 0
                                },
                                "z_1_0": {
                                    "state": 1,
                                    "weather": 0
                                }
                            },
                            "node": {
                                "nB32E": {
                                    "zone": "z_1_0",
                                    "type": 1,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -140,
                                            189
                                        ],
                                        "adj": [
                                            "n3259",
                                            "n8340",
                                            "n6368"
                                        ],
                                        "depth": 0
                                    },
                                    "stageId": "sandbox_1_27",
                                    "weatherLv": 0
                                },
                                "n12B9": {
                                    "zone": "z_1_0",
                                    "type": 14,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -102,
                                            -96
                                        ],
                                        "adj": [],
                                        "depth": 0
                                    },
                                    "stageId": "sandbox_1_32",
                                    "weatherLv": 0
                                },
                                "n8340": {
                                    "zone": "z_1_0",
                                    "type": 2,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -283.58728,
                                            508.190674
                                        ],
                                        "adj": [
                                            "n88A8",
                                            "nB32E"
                                        ],
                                        "depth": 1
                                    },
                                    "stageId": "sandbox_1_26",
                                    "weatherLv": 0
                                },
                                "n88A8": {
                                    "zone": "z_1_1",
                                    "type": 5,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -718,
                                            452
                                        ],
                                        "adj": [
                                            "n8340",
                                            "n2259"
                                        ],
                                        "depth": 2
                                    },
                                    "stageId": "sandbox_1_01",
                                    "weatherLv": 0
                                },
                                "n35C1": {
                                    "zone": "z_1_1",
                                    "type": 6,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -751,
                                            142
                                        ],
                                        "adj": [
                                            "n3259",
                                            "nCFA1"
                                        ],
                                        "depth": 2
                                    },
                                    "stageId": "sandbox_1_09",
                                    "weatherLv": 0
                                },
                                "n2259": {
                                    "zone": "z_1_1",
                                    "type": 6,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -1122,
                                            181
                                        ],
                                        "adj": [
                                            "n20CB",
                                            "n88A8"
                                        ],
                                        "depth": 3
                                    },
                                    "stageId": "sandbox_1_56",
                                    "weatherLv": 0
                                },
                                "n20CB": {
                                    "zone": "z_1_1",
                                    "type": 5,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -1599,
                                            -57
                                        ],
                                        "adj": [
                                            "n97C7",
                                            "n2259",
                                            "n3740"
                                        ],
                                        "depth": 4
                                    },
                                    "stageId": "sandbox_1_38",
                                    "weatherLv": 0
                                },
                                "n97C7": {
                                    "zone": "z_1_1",
                                    "type": 6,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -1517,
                                            -299
                                        ],
                                        "adj": [
                                            "n20CB",
                                            "nD54F"
                                        ],
                                        "depth": 5
                                    },
                                    "stageId": "sandbox_1_54",
                                    "weatherLv": 0
                                },
                                "nD54F": {
                                    "zone": "z_1_1",
                                    "type": 6,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -1732,
                                            -434
                                        ],
                                        "adj": [
                                            "n97C7",
                                            "n9EF3",
                                            "nED84"
                                        ],
                                        "depth": 6
                                    },
                                    "stageId": "sandbox_1_55",
                                    "weatherLv": 0
                                },
                                "nB55F": {
                                    "zone": "z_1_1",
                                    "type": 5,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -2011,
                                            -144
                                        ],
                                        "adj": [
                                            "n07D6",
                                            "nA226",
                                            "nE038"
                                        ],
                                        "depth": 9
                                    },
                                    "stageId": "sandbox_1_38",
                                    "weatherLv": 0
                                },
                                "nA226": {
                                    "zone": "z_1_1",
                                    "type": 3,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -2135,
                                            -442.999969
                                        ],
                                        "adj": [
                                            "nB55F",
                                            "nED84"
                                        ],
                                        "depth": 8
                                    },
                                    "stageId": "sandbox_1_72",
                                    "weatherLv": 0
                                },
                                "n07D6": {
                                    "zone": "z_1_1",
                                    "type": 4,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -2274,
                                            -292
                                        ],
                                        "adj": [
                                            "nB55F"
                                        ],
                                        "depth": 10
                                    },
                                    "stageId": "sandbox_1_64",
                                    "weatherLv": 0
                                },
                                "n0446": {
                                    "zone": "z_1_1",
                                    "type": 8,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -2246,
                                            -1218
                                        ],
                                        "adj": [
                                            "nA659"
                                        ],
                                        "depth": 9
                                    },
                                    "stageId": "sandbox_1_28",
                                    "weatherLv": 0
                                },
                                "nA659": {
                                    "zone": "z_1_1",
                                    "type": 5,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -1970.00012,
                                            -997.3706
                                        ],
                                        "adj": [
                                            "n0446",
                                            "nED84",
                                            "n8375"
                                        ],
                                        "depth": 8
                                    },
                                    "stageId": "sandbox_1_39",
                                    "weatherLv": 0
                                },
                                "nED84": {
                                    "zone": "z_1_1",
                                    "type": 3,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -1834.99988,
                                            -772.000061
                                        ],
                                        "adj": [
                                            "nA659",
                                            "nA226",
                                            "nEFA5",
                                            "nD54F"
                                        ],
                                        "depth": 7
                                    },
                                    "stageId": "sandbox_1_80",
                                    "weatherLv": 0
                                },
                                "nEFA5": {
                                    "zone": "z_1_1",
                                    "type": 10,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -1456,
                                            -1040
                                        ],
                                        "adj": [
                                            "nED84",
                                            "n81E8"
                                        ],
                                        "depth": 7
                                    },
                                    "stageId": "sandbox_1_70",
                                    "weatherLv": 0
                                },
                                "n81E8": {
                                    "zone": "z_1_1",
                                    "type": 5,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -1121,
                                            -876
                                        ],
                                        "adj": [
                                            "nEFA5",
                                            "nCA3B"
                                        ],
                                        "depth": 6
                                    },
                                    "stageId": "sandbox_1_40",
                                    "weatherLv": 0
                                },
                                "n9EF3": {
                                    "zone": "z_1_1",
                                    "type": 5,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -1471,
                                            -582
                                        ],
                                        "adj": [
                                            "n607D",
                                            "nD54F",
                                            "n3740"
                                        ],
                                        "depth": 5
                                    },
                                    "stageId": "sandbox_1_40",
                                    "weatherLv": 0
                                },
                                "n3259": {
                                    "zone": "z_1_0",
                                    "type": 2,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -442.199036,
                                            12.4334812
                                        ],
                                        "adj": [
                                            "n35C1",
                                            "nB32E"
                                        ],
                                        "depth": 1
                                    },
                                    "stageId": "sandbox_1_24",
                                    "weatherLv": 0
                                },
                                "n6368": {
                                    "zone": "z_1_0",
                                    "type": 2,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            168.191132,
                                            23.1137753
                                        ],
                                        "adj": [
                                            "nD7CE",
                                            "nB32E"
                                        ],
                                        "depth": 1
                                    },
                                    "stageId": "sandbox_1_25",
                                    "weatherLv": 0
                                },
                                "nD7CE": {
                                    "zone": "z_1_1",
                                    "type": 9,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            229.000015,
                                            -248.000031
                                        ],
                                        "adj": [
                                            "n2D12",
                                            "n6368",
                                            "n9096"
                                        ],
                                        "depth": 2
                                    },
                                    "stageId": "sandbox_1_69",
                                    "weatherLv": 0
                                },
                                "n2D12": {
                                    "zone": "z_1_1",
                                    "type": 3,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -139,
                                            -311
                                        ],
                                        "adj": [
                                            "nD7CE",
                                            "nBEB8"
                                        ],
                                        "depth": 3
                                    },
                                    "stageId": "sandbox_1_74",
                                    "weatherLv": 0
                                },
                                "nDEF4": {
                                    "zone": "z_1_2",
                                    "type": 9,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -405.000031,
                                            -1495.7
                                        ],
                                        "adj": [
                                            "n71D1"
                                        ],
                                        "depth": 14
                                    },
                                    "stageId": "sandbox_1_70",
                                    "weatherLv": 0
                                },
                                "n9096": {
                                    "zone": "z_1_1",
                                    "type": 5,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -28.0000038,
                                            -628
                                        ],
                                        "adj": [
                                            "n22B0",
                                            "nD7CE",
                                            "nD2FB"
                                        ],
                                        "depth": 3
                                    },
                                    "stageId": "sandbox_1_38",
                                    "weatherLv": 0
                                },
                                "nCA3B": {
                                    "zone": "z_1_1",
                                    "type": 6,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -786,
                                            -713
                                        ],
                                        "adj": [
                                            "n22B0",
                                            "nDDDC",
                                            "nF586",
                                            "n81E8"
                                        ],
                                        "depth": 5
                                    },
                                    "stageId": "sandbox_1_55",
                                    "weatherLv": 0
                                },
                                "n22B0": {
                                    "zone": "z_1_1",
                                    "type": 6,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -408.939972,
                                            -738
                                        ],
                                        "adj": [
                                            "n9096",
                                            "nCA3B",
                                            "nBEB8"
                                        ],
                                        "depth": 4
                                    },
                                    "stageId": "sandbox_1_56",
                                    "weatherLv": 0
                                },
                                "n607D": {
                                    "zone": "z_1_1",
                                    "type": 9,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -1205.4,
                                            -713
                                        ],
                                        "adj": [
                                            "n9EF3",
                                            "n14BC"
                                        ],
                                        "depth": 6
                                    },
                                    "stageId": "sandbox_1_71",
                                    "weatherLv": 0
                                },
                                "n14BC": {
                                    "zone": "z_1_1",
                                    "type": 4,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -976.8,
                                            -539
                                        ],
                                        "adj": [
                                            "n607D"
                                        ],
                                        "depth": 7
                                    },
                                    "stageId": "sandbox_1_62",
                                    "weatherLv": 0
                                },
                                "nBEB8": {
                                    "zone": "z_1_1",
                                    "type": 9,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -387,
                                            -507.000031
                                        ],
                                        "adj": [
                                            "nF586",
                                            "n2D12",
                                            "n22B0"
                                        ],
                                        "depth": 4
                                    },
                                    "stageId": "sandbox_1_69",
                                    "weatherLv": 0
                                },
                                "nF586": {
                                    "zone": "z_1_1",
                                    "type": 5,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -500,
                                            -374
                                        ],
                                        "adj": [
                                            "nBEB8",
                                            "nDDDC",
                                            "nCA3B"
                                        ],
                                        "depth": 5
                                    },
                                    "stageId": "sandbox_1_37",
                                    "weatherLv": 0
                                },
                                "n3740": {
                                    "zone": "z_1_1",
                                    "type": 9,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -1139,
                                            -358
                                        ],
                                        "adj": [
                                            "n20CB",
                                            "nDDDC",
                                            "nCFA1",
                                            "n9EF3"
                                        ],
                                        "depth": 4
                                    },
                                    "stageId": "sandbox_1_70",
                                    "weatherLv": 0
                                },
                                "nCFA1": {
                                    "zone": "z_1_1",
                                    "type": 5,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -884,
                                            -101
                                        ],
                                        "adj": [
                                            "n3740",
                                            "n35C1"
                                        ],
                                        "depth": 3
                                    },
                                    "stageId": "sandbox_1_41",
                                    "weatherLv": 0
                                },
                                "nDDDC": {
                                    "zone": "z_1_1",
                                    "type": 6,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -749,
                                            -245
                                        ],
                                        "adj": [
                                            "nF586",
                                            "nCA3B",
                                            "n3740"
                                        ],
                                        "depth": 5
                                    },
                                    "stageId": "sandbox_1_54",
                                    "weatherLv": 0
                                },
                                "n32FD": {
                                    "zone": "z_1_4",
                                    "type": 4,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -1795.00012,
                                            328
                                        ],
                                        "adj": [
                                            "nE038",
                                            "n8667",
                                            "nFE3F"
                                        ],
                                        "depth": 11
                                    },
                                    "stageId": "sandbox_1_62",
                                    "weatherLv": 0
                                },
                                "nFE3F": {
                                    "zone": "z_1_4",
                                    "type": 5,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -1485,
                                            197
                                        ],
                                        "adj": [
                                            "n8667",
                                            "n32FD"
                                        ],
                                        "depth": 12
                                    },
                                    "stageId": "sandbox_1_03",
                                    "weatherLv": 0
                                },
                                "n8667": {
                                    "zone": "z_1_4",
                                    "type": 7,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -1438,
                                            507.000031
                                        ],
                                        "adj": [
                                            "nFE3F",
                                            "n32FD",
                                            "n4CDF"
                                        ],
                                        "depth": 12
                                    },
                                    "stageId": "sandbox_1_19",
                                    "weatherLv": 0
                                },
                                "n4CDF": {
                                    "zone": "z_1_4",
                                    "type": 3,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -1856,
                                            547
                                        ],
                                        "adj": [
                                            "n8667",
                                            "nAD10",
                                            "nAB42"
                                        ],
                                        "depth": 13
                                    },
                                    "stageId": "sandbox_1_77",
                                    "weatherLv": 0
                                },
                                "nAD10": {
                                    "zone": "z_1_4",
                                    "type": 5,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -1374,
                                            715
                                        ],
                                        "adj": [
                                            "n4CDF",
                                            "n6ECA",
                                            "n8734"
                                        ],
                                        "depth": 14
                                    },
                                    "stageId": "sandbox_1_45",
                                    "weatherLv": 0
                                },
                                "nAB42": {
                                    "zone": "z_1_4",
                                    "type": 9,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -2072,
                                            751
                                        ],
                                        "adj": [
                                            "n4CDF",
                                            "n7A2B",
                                            "n6ECA",
                                            "n0D60"
                                        ],
                                        "depth": 14
                                    },
                                    "stageId": "sandbox_1_71",
                                    "weatherLv": 0
                                },
                                "nE038": {
                                    "zone": "z_1_1",
                                    "type": 12,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -1908,
                                            90
                                        ],
                                        "adj": [
                                            "n32FD",
                                            "nB55F"
                                        ],
                                        "depth": 10
                                    },
                                    "stageId": "sandbox_1_14",
                                    "weatherLv": 0
                                },
                                "n7A2B": {
                                    "zone": "z_1_4",
                                    "type": 5,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -2187.05347,
                                            592.5775
                                        ],
                                        "adj": [
                                            "nAB42"
                                        ],
                                        "depth": 15
                                    },
                                    "stageId": "sandbox_1_04",
                                    "weatherLv": 0
                                },
                                "n6ECA": {
                                    "zone": "z_1_4",
                                    "type": 5,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -1596.9989,
                                            847
                                        ],
                                        "adj": [
                                            "nAB42",
                                            "nAD10",
                                            "n7CB1"
                                        ],
                                        "depth": 15
                                    },
                                    "stageId": "sandbox_1_03",
                                    "weatherLv": 0
                                },
                                "n8734": {
                                    "zone": "z_1_4",
                                    "type": 5,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -1219,
                                            854
                                        ],
                                        "adj": [
                                            "nAD10",
                                            "n6632",
                                            "nEE32"
                                        ],
                                        "depth": 15
                                    },
                                    "stageId": "sandbox_1_52",
                                    "weatherLv": 0
                                },
                                "n6632": {
                                    "zone": "z_1_4",
                                    "type": 6,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -1425,
                                            1007
                                        ],
                                        "adj": [
                                            "n8734",
                                            "n7CB1",
                                            "n663B"
                                        ],
                                        "depth": 16
                                    },
                                    "stageId": "sandbox_1_13",
                                    "weatherLv": 0
                                },
                                "n7CB1": {
                                    "zone": "z_1_4",
                                    "type": 5,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -1882,
                                            1203
                                        ],
                                        "adj": [
                                            "n6632",
                                            "n6ECA",
                                            "n0D60",
                                            "n3E46"
                                        ],
                                        "depth": 16
                                    },
                                    "stageId": "sandbox_1_05",
                                    "weatherLv": 0
                                },
                                "n0D60": {
                                    "zone": "z_1_4",
                                    "type": 6,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -1999,
                                            1056
                                        ],
                                        "adj": [
                                            "nAB42",
                                            "n7CB1",
                                            "n3DB9"
                                        ],
                                        "depth": 15
                                    },
                                    "stageId": "sandbox_1_09",
                                    "weatherLv": 0
                                },
                                "nEE32": {
                                    "zone": "z_1_4",
                                    "type": 7,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -1359,
                                            1332
                                        ],
                                        "adj": [
                                            "n8734",
                                            "n5D41"
                                        ],
                                        "depth": 16
                                    },
                                    "stageId": "sandbox_1_22",
                                    "weatherLv": 0
                                },
                                "n663B": {
                                    "zone": "z_1_4",
                                    "type": 5,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -1471,
                                            1159
                                        ],
                                        "adj": [
                                            "n6632"
                                        ],
                                        "depth": 17
                                    },
                                    "stageId": "sandbox_1_49",
                                    "weatherLv": 0
                                },
                                "n5D41": {
                                    "zone": "z_1_4",
                                    "type": 9,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -1477,
                                            1459.00012
                                        ],
                                        "adj": [
                                            "nEE32",
                                            "n3E46"
                                        ],
                                        "depth": 17
                                    },
                                    "stageId": "sandbox_1_70",
                                    "weatherLv": 0
                                },
                                "n3E46": {
                                    "zone": "z_1_4",
                                    "type": 3,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -1685.00122,
                                            1639
                                        ],
                                        "adj": [
                                            "n7CB1",
                                            "n5D41",
                                            "n542E",
                                            "nD5FB"
                                        ],
                                        "depth": 17
                                    },
                                    "stageId": "sandbox_1_73",
                                    "weatherLv": 0
                                },
                                "n542E": {
                                    "zone": "z_1_4",
                                    "type": 5,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -2037.00012,
                                            1575
                                        ],
                                        "adj": [
                                            "n3E46",
                                            "n3DB9"
                                        ],
                                        "depth": 17
                                    },
                                    "stageId": "sandbox_1_51",
                                    "weatherLv": 0
                                },
                                "n3DB9": {
                                    "zone": "z_1_4",
                                    "type": 7,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -2114,
                                            1375
                                        ],
                                        "adj": [
                                            "n542E",
                                            "n0D60"
                                        ],
                                        "depth": 16
                                    },
                                    "stageId": "sandbox_1_67",
                                    "weatherLv": 0
                                },
                                "nD5FB": {
                                    "zone": "z_1_4",
                                    "type": 5,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -1765.05359,
                                            1811.57764
                                        ],
                                        "adj": [
                                            "n3E46",
                                            "n12CF"
                                        ],
                                        "depth": 18
                                    },
                                    "stageId": "sandbox_1_52",
                                    "weatherLv": 0
                                },
                                "n12CF": {
                                    "zone": "z_1_4",
                                    "type": 7,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -1445.05359,
                                            2086.57764
                                        ],
                                        "adj": [
                                            "nD5FB"
                                        ],
                                        "depth": 19
                                    },
                                    "stageId": "sandbox_1_20",
                                    "weatherLv": 0
                                },
                                "n10AD": {
                                    "zone": "z_1_2",
                                    "type": 4,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -1865,
                                            -1684
                                        ],
                                        "adj": [
                                            "nEA6F"
                                        ],
                                        "depth": 12
                                    },
                                    "stageId": "sandbox_1_65",
                                    "weatherLv": 0
                                },
                                "nA1C6": {
                                    "zone": "z_1_2",
                                    "type": 10,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -1712.00012,
                                            -1903.00012
                                        ],
                                        "adj": [
                                            "nEA6F"
                                        ],
                                        "depth": 12
                                    },
                                    "stageId": "sandbox_1_70",
                                    "weatherLv": 0
                                },
                                "nEA6F": {
                                    "zone": "z_1_2",
                                    "type": 6,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -1481,
                                            -1764
                                        ],
                                        "adj": [
                                            "n6831",
                                            "n4121",
                                            "n10AD",
                                            "nA1C6",
                                            "n1B64",
                                            "nA1CE",
                                            "n3809"
                                        ],
                                        "depth": 11
                                    },
                                    "stageId": "sandbox_1_60",
                                    "weatherLv": 0
                                },
                                "n4121": {
                                    "zone": "z_1_2",
                                    "type": 5,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -1740.3833,
                                            -1453.7428
                                        ],
                                        "adj": [
                                            "n8375",
                                            "nEA6F"
                                        ],
                                        "depth": 10
                                    },
                                    "stageId": "sandbox_1_02",
                                    "weatherLv": 0
                                },
                                "n8375": {
                                    "zone": "z_1_1",
                                    "type": 12,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -1834.99988,
                                            -1199.99988
                                        ],
                                        "adj": [
                                            "n4121",
                                            "nA659"
                                        ],
                                        "depth": 9
                                    },
                                    "stageId": "sandbox_1_63",
                                    "weatherLv": 0
                                },
                                "nE095": {
                                    "zone": "z_1_2",
                                    "type": 9,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -1131.4,
                                            -1103.4
                                        ],
                                        "adj": [
                                            "n3809",
                                            "n6831"
                                        ],
                                        "depth": 13
                                    },
                                    "stageId": "sandbox_1_71",
                                    "weatherLv": 0
                                },
                                "n6831": {
                                    "zone": "z_1_2",
                                    "type": 6,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -1462,
                                            -1286
                                        ],
                                        "adj": [
                                            "nEA6F",
                                            "nE095"
                                        ],
                                        "depth": 12
                                    },
                                    "stageId": "sandbox_1_50",
                                    "weatherLv": 0
                                },
                                "n3809": {
                                    "zone": "z_1_2",
                                    "type": 5,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -1019.38336,
                                            -1481.50134
                                        ],
                                        "adj": [
                                            "nEA6F",
                                            "nE095",
                                            "n4B29",
                                            "n71D1"
                                        ],
                                        "depth": 12
                                    },
                                    "stageId": "sandbox_1_44",
                                    "weatherLv": 0
                                },
                                "nA1CE": {
                                    "zone": "z_1_2",
                                    "type": 6,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -1113,
                                            -1799
                                        ],
                                        "adj": [
                                            "nEA6F",
                                            "n6829",
                                            "n1B64"
                                        ],
                                        "depth": 12
                                    },
                                    "stageId": "sandbox_1_09",
                                    "weatherLv": 0
                                },
                                "n2BA6": {
                                    "zone": "z_1_2",
                                    "type": 7,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -935.3833,
                                            -2188.225
                                        ],
                                        "adj": [
                                            "n1B64",
                                            "n0FB8"
                                        ],
                                        "depth": 13
                                    },
                                    "stageId": "sandbox_1_23",
                                    "weatherLv": 0
                                },
                                "n1B64": {
                                    "zone": "z_1_2",
                                    "type": 5,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -1350,
                                            -1949
                                        ],
                                        "adj": [
                                            "nEA6F",
                                            "n2BA6",
                                            "nA1CE"
                                        ],
                                        "depth": 12
                                    },
                                    "stageId": "sandbox_1_40",
                                    "weatherLv": 0
                                },
                                "n6829": {
                                    "zone": "z_1_2",
                                    "type": 5,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -543,
                                            -1935
                                        ],
                                        "adj": [
                                            "n71D1",
                                            "nA1CE",
                                            "n0FB8"
                                        ],
                                        "depth": 13
                                    },
                                    "stageId": "sandbox_1_42",
                                    "weatherLv": 0
                                },
                                "n0FB8": {
                                    "zone": "z_1_2",
                                    "type": 5,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -386,
                                            -2066
                                        ],
                                        "adj": [
                                            "n2BA6",
                                            "n71D1",
                                            "nC69C",
                                            "n6829"
                                        ],
                                        "depth": 14
                                    },
                                    "stageId": "sandbox_1_02",
                                    "weatherLv": 0
                                },
                                "nC69C": {
                                    "zone": "z_1_2",
                                    "type": 9,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -251.683289,
                                            -1795.38708
                                        ],
                                        "adj": [
                                            "n0FB8",
                                            "n9C6A",
                                            "nF5F6",
                                            "n71D1"
                                        ],
                                        "depth": 14
                                    },
                                    "stageId": "sandbox_1_69",
                                    "weatherLv": 0
                                },
                                "n9C6A": {
                                    "zone": "z_1_2",
                                    "type": 5,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            151.58,
                                            -1967
                                        ],
                                        "adj": [
                                            "nC69C",
                                            "n6C8E"
                                        ],
                                        "depth": 15
                                    },
                                    "stageId": "sandbox_1_43",
                                    "weatherLv": 0
                                },
                                "n98EF": {
                                    "zone": "z_1_2",
                                    "type": 7,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            677,
                                            -1569.7
                                        ],
                                        "adj": [
                                            "n6C8E"
                                        ],
                                        "depth": 17
                                    },
                                    "stageId": "sandbox_1_68",
                                    "weatherLv": 0
                                },
                                "nF5F6": {
                                    "zone": "z_1_2",
                                    "type": 3,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            155.000015,
                                            -1733
                                        ],
                                        "adj": [
                                            "nC69C",
                                            "n6C8E"
                                        ],
                                        "depth": 15
                                    },
                                    "stageId": "sandbox_1_75",
                                    "weatherLv": 0
                                },
                                "nA1AD": {
                                    "zone": "z_1_2",
                                    "type": 3,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            630,
                                            -1334
                                        ],
                                        "adj": [
                                            "nF294"
                                        ],
                                        "depth": 18
                                    },
                                    "stageId": "sandbox_1_78",
                                    "weatherLv": 0
                                },
                                "nF294": {
                                    "zone": "z_1_2",
                                    "type": 6,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            282,
                                            -1250
                                        ],
                                        "adj": [
                                            "nAB04",
                                            "nA1AD"
                                        ],
                                        "depth": 17
                                    },
                                    "stageId": "sandbox_1_57",
                                    "weatherLv": 0
                                },
                                "nAB04": {
                                    "zone": "z_1_2",
                                    "type": 5,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            391,
                                            -950
                                        ],
                                        "adj": [
                                            "n74C3",
                                            "nF294",
                                            "n2AF0",
                                            "n9B77"
                                        ],
                                        "depth": 16
                                    },
                                    "stageId": "sandbox_1_02",
                                    "weatherLv": 0
                                },
                                "n42D8": {
                                    "zone": "z_1_3",
                                    "type": 8,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            1005.5,
                                            -721
                                        ],
                                        "adj": [
                                            "n2D0A"
                                        ],
                                        "depth": 22
                                    },
                                    "stageId": "sandbox_1_30",
                                    "weatherLv": 0
                                },
                                "n74C3": {
                                    "zone": "z_1_2",
                                    "type": 3,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -139.982086,
                                            -1191
                                        ],
                                        "adj": [
                                            "n4244",
                                            "n9542",
                                            "nAB04"
                                        ],
                                        "depth": 15
                                    },
                                    "stageId": "sandbox_1_76",
                                    "weatherLv": 0
                                },
                                "n4244": {
                                    "zone": "z_1_2",
                                    "type": 6,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -90,
                                            -1318
                                        ],
                                        "adj": [
                                            "nF0F5",
                                            "n74C3"
                                        ],
                                        "depth": 15
                                    },
                                    "stageId": "sandbox_1_58",
                                    "weatherLv": 0
                                },
                                "nF0F5": {
                                    "zone": "z_1_2",
                                    "type": 9,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -437,
                                            -1362
                                        ],
                                        "adj": [
                                            "n4B29",
                                            "n4244"
                                        ],
                                        "depth": 14
                                    },
                                    "stageId": "sandbox_1_71",
                                    "weatherLv": 0
                                },
                                "n9542": {
                                    "zone": "z_1_2",
                                    "type": 5,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -410,
                                            -900
                                        ],
                                        "adj": [
                                            "n4B29",
                                            "n74C3"
                                        ],
                                        "depth": 14
                                    },
                                    "stageId": "sandbox_1_42",
                                    "weatherLv": 0
                                },
                                "n4B29": {
                                    "zone": "z_1_2",
                                    "type": 6,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -762,
                                            -999.4
                                        ],
                                        "adj": [
                                            "n3809",
                                            "n9542",
                                            "nF0F5"
                                        ],
                                        "depth": 13
                                    },
                                    "stageId": "sandbox_1_59",
                                    "weatherLv": 0
                                },
                                "nD2FB": {
                                    "zone": "z_1_1",
                                    "type": 4,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            0,
                                            -826
                                        ],
                                        "adj": [
                                            "n9096"
                                        ],
                                        "depth": 4
                                    },
                                    "stageId": "sandbox_1_64",
                                    "weatherLv": 0
                                },
                                "n71D1": {
                                    "zone": "z_1_2",
                                    "type": 6,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            -595,
                                            -1624
                                        ],
                                        "adj": [
                                            "n3809",
                                            "n6829",
                                            "n0FB8",
                                            "nC69C",
                                            "nDEF4"
                                        ],
                                        "depth": 13
                                    },
                                    "stageId": "sandbox_1_57",
                                    "weatherLv": 0
                                },
                                "n6C8E": {
                                    "zone": "z_1_2",
                                    "type": 9,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            542.5998,
                                            -1832
                                        ],
                                        "adj": [
                                            "n9C6A",
                                            "nF5F6",
                                            "n98EF"
                                        ],
                                        "depth": 16
                                    },
                                    "stageId": "sandbox_1_69",
                                    "weatherLv": 0
                                },
                                "n9B77": {
                                    "zone": "z_1_2",
                                    "type": 8,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            616.5998,
                                            -1125.99988
                                        ],
                                        "adj": [
                                            "nAB04"
                                        ],
                                        "depth": 17
                                    },
                                    "stageId": "sandbox_1_29",
                                    "weatherLv": 0
                                },
                                "n2AF0": {
                                    "zone": "z_1_2",
                                    "type": 12,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            567,
                                            -719
                                        ],
                                        "adj": [
                                            "n80F5",
                                            "nAB04"
                                        ],
                                        "depth": 17
                                    },
                                    "stageId": "sandbox_1_15",
                                    "weatherLv": 0
                                },
                                "n80F5": {
                                    "zone": "z_1_3",
                                    "type": 7,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            362,
                                            -586
                                        ],
                                        "adj": [
                                            "n6AB0",
                                            "n2AF0"
                                        ],
                                        "depth": 18
                                    },
                                    "stageId": "sandbox_1_18",
                                    "weatherLv": 0
                                },
                                "n6AB0": {
                                    "zone": "z_1_3",
                                    "type": 6,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            790,
                                            -535
                                        ],
                                        "adj": [
                                            "n80F5",
                                            "n3899",
                                            "n2423",
                                            "nBAFC"
                                        ],
                                        "depth": 19
                                    },
                                    "stageId": "sandbox_1_61",
                                    "weatherLv": 0
                                },
                                "n3899": {
                                    "zone": "z_1_3",
                                    "type": 5,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            780,
                                            -963
                                        ],
                                        "adj": [
                                            "n2D0A",
                                            "n6AB0",
                                            "nB251"
                                        ],
                                        "depth": 20
                                    },
                                    "stageId": "sandbox_1_48",
                                    "weatherLv": 0
                                },
                                "nB251": {
                                    "zone": "z_1_3",
                                    "type": 4,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            1177,
                                            -1177.4
                                        ],
                                        "adj": [
                                            "n3899"
                                        ],
                                        "depth": 21
                                    },
                                    "stageId": "sandbox_1_64",
                                    "weatherLv": 0
                                },
                                "n2D0A": {
                                    "zone": "z_1_3",
                                    "type": 6,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            1177,
                                            -888.999939
                                        ],
                                        "adj": [
                                            "n3899",
                                            "n42D8"
                                        ],
                                        "depth": 21
                                    },
                                    "stageId": "sandbox_1_53",
                                    "weatherLv": 0
                                },
                                "n6695": {
                                    "zone": "z_1_3",
                                    "type": 5,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            1536,
                                            -935.999939
                                        ],
                                        "adj": [
                                            "nCC82",
                                            "nC10F"
                                        ],
                                        "depth": 26
                                    },
                                    "stageId": "sandbox_1_03",
                                    "weatherLv": 0
                                },
                                "nCF3F": {
                                    "zone": "z_1_3",
                                    "type": 8,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            1602.05957,
                                            -1071.37061
                                        ],
                                        "adj": [
                                            "n5536",
                                            "n740B"
                                        ],
                                        "depth": 27
                                    },
                                    "stageId": "sandbox_1_31",
                                    "weatherLv": 0
                                },
                                "n5536": {
                                    "zone": "z_1_3",
                                    "type": 10,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            1557.97144,
                                            -1335.89893
                                        ],
                                        "adj": [
                                            "nCF3F"
                                        ],
                                        "depth": 28
                                    },
                                    "stageId": "sandbox_1_69",
                                    "weatherLv": 0
                                },
                                "n740B": {
                                    "zone": "z_1_3",
                                    "type": 3,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            1919.49353,
                                            -846.521545
                                        ],
                                        "adj": [
                                            "nCF3F",
                                            "n9AE0"
                                        ],
                                        "depth": 26
                                    },
                                    "stageId": "sandbox_1_74",
                                    "weatherLv": 0
                                },
                                "n9AE0": {
                                    "zone": "z_1_3",
                                    "type": 5,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            2040,
                                            -601
                                        ],
                                        "adj": [
                                            "n740B",
                                            "nDFEC",
                                            "n1AA7"
                                        ],
                                        "depth": 25
                                    },
                                    "stageId": "sandbox_1_46",
                                    "weatherLv": 0
                                },
                                "nDFEC": {
                                    "zone": "z_1_3",
                                    "type": 6,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            1879.00012,
                                            -388
                                        ],
                                        "adj": [
                                            "n9AE0",
                                            "n1AA7",
                                            "nCC82"
                                        ],
                                        "depth": 25
                                    },
                                    "stageId": "sandbox_1_58",
                                    "weatherLv": 0
                                },
                                "nCC82": {
                                    "zone": "z_1_3",
                                    "type": 5,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            1698,
                                            -533.4964
                                        ],
                                        "adj": [
                                            "nDFEC",
                                            "n6695",
                                            "nC10F"
                                        ],
                                        "depth": 26
                                    },
                                    "stageId": "sandbox_1_01",
                                    "weatherLv": 0
                                },
                                "nC10F": {
                                    "zone": "z_1_3",
                                    "type": 9,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            1442,
                                            -664
                                        ],
                                        "adj": [
                                            "n6695",
                                            "nA317",
                                            "nCC82"
                                        ],
                                        "depth": 25
                                    },
                                    "stageId": "sandbox_1_71",
                                    "weatherLv": 0
                                },
                                "nA317": {
                                    "zone": "z_1_3",
                                    "type": 5,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            1489.63513,
                                            -348.3266
                                        ],
                                        "adj": [
                                            "nC10F",
                                            "nE57A"
                                        ],
                                        "depth": 24
                                    },
                                    "stageId": "sandbox_1_48",
                                    "weatherLv": 0
                                },
                                "n1AA7": {
                                    "zone": "z_1_3",
                                    "type": 7,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            1897.44946,
                                            -231.493286
                                        ],
                                        "adj": [
                                            "n9AE0",
                                            "nDFEC",
                                            "nE57A"
                                        ],
                                        "depth": 24
                                    },
                                    "stageId": "sandbox_1_66",
                                    "weatherLv": 0
                                },
                                "nE57A": {
                                    "zone": "z_1_3",
                                    "type": 3,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            1529.31409,
                                            -63.9588356
                                        ],
                                        "adj": [
                                            "n1AA7",
                                            "nA317",
                                            "n403F"
                                        ],
                                        "depth": 23
                                    },
                                    "stageId": "sandbox_1_73",
                                    "weatherLv": 0
                                },
                                "n403F": {
                                    "zone": "z_1_3",
                                    "type": 6,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            1456,
                                            171
                                        ],
                                        "adj": [
                                            "n7F77",
                                            "n8BFF",
                                            "nE57A",
                                            "n3BA7"
                                        ],
                                        "depth": 22
                                    },
                                    "stageId": "sandbox_1_09",
                                    "weatherLv": 0
                                },
                                "n427C": {
                                    "zone": "z_1_3",
                                    "type": 5,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            1177,
                                            -44
                                        ],
                                        "adj": [
                                            "nBAFC"
                                        ],
                                        "depth": 21
                                    },
                                    "stageId": "sandbox_1_47",
                                    "weatherLv": 0
                                },
                                "nBAFC": {
                                    "zone": "z_1_3",
                                    "type": 6,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            1027,
                                            -240.000015
                                        ],
                                        "adj": [
                                            "n427C",
                                            "n6AB0",
                                            "n7F77"
                                        ],
                                        "depth": 20
                                    },
                                    "stageId": "sandbox_1_10",
                                    "weatherLv": 0
                                },
                                "n2423": {
                                    "zone": "z_1_3",
                                    "type": 9,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            1040,
                                            -389
                                        ],
                                        "adj": [
                                            "n6AB0",
                                            "nE03B"
                                        ],
                                        "depth": 20
                                    },
                                    "stageId": "sandbox_1_69",
                                    "weatherLv": 0
                                },
                                "nE03B": {
                                    "zone": "z_1_3",
                                    "type": 5,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            1215,
                                            -523
                                        ],
                                        "adj": [
                                            "n2423"
                                        ],
                                        "depth": 21
                                    },
                                    "stageId": "sandbox_1_03",
                                    "weatherLv": 0
                                },
                                "n7F77": {
                                    "zone": "z_1_3",
                                    "type": 6,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            956.000061,
                                            79.5
                                        ],
                                        "adj": [
                                            "nBAFC",
                                            "n403F",
                                            "n8BFF",
                                            "n6B1D"
                                        ],
                                        "depth": 21
                                    },
                                    "stageId": "sandbox_1_12",
                                    "weatherLv": 0
                                },
                                "n6B1D": {
                                    "zone": "z_1_3",
                                    "type": 5,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            938.534058,
                                            308.5852
                                        ],
                                        "adj": [
                                            "n7F77",
                                            "n4A25",
                                            "nA6A1"
                                        ],
                                        "depth": 22
                                    },
                                    "stageId": "sandbox_1_45",
                                    "weatherLv": 0
                                },
                                "n8BFF": {
                                    "zone": "z_1_3",
                                    "type": 5,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            1326,
                                            338
                                        ],
                                        "adj": [
                                            "n403F",
                                            "n7F77"
                                        ],
                                        "depth": 22
                                    },
                                    "stageId": "sandbox_1_52",
                                    "weatherLv": 0
                                },
                                "n3BA7": {
                                    "zone": "z_1_3",
                                    "type": 6,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            1640.50012,
                                            467.999969
                                        ],
                                        "adj": [
                                            "n403F"
                                        ],
                                        "depth": 23
                                    },
                                    "stageId": "sandbox_1_11",
                                    "weatherLv": 0
                                },
                                "n6828": {
                                    "zone": "z_1_3",
                                    "type": 5,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            1582,
                                            803
                                        ],
                                        "adj": [
                                            "n4A25",
                                            "n9FD9"
                                        ],
                                        "depth": 24
                                    },
                                    "stageId": "sandbox_1_40",
                                    "weatherLv": 0
                                },
                                "n4A25": {
                                    "zone": "z_1_3",
                                    "type": 3,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            1284.62524,
                                            581.9311
                                        ],
                                        "adj": [
                                            "n6828",
                                            "n6B1D",
                                            "nA6A1"
                                        ],
                                        "depth": 23
                                    },
                                    "stageId": "sandbox_1_79",
                                    "weatherLv": 0
                                },
                                "nA6A1": {
                                    "zone": "z_1_3",
                                    "type": 9,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            1201,
                                            868.999939
                                        ],
                                        "adj": [
                                            "n4A25",
                                            "n6B1D"
                                        ],
                                        "depth": 23
                                    },
                                    "stageId": "sandbox_1_69",
                                    "weatherLv": 0
                                },
                                "n9FD9": {
                                    "zone": "z_1_3",
                                    "type": 7,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            1169,
                                            1302
                                        ],
                                        "adj": [
                                            "n6828"
                                        ],
                                        "depth": 25
                                    },
                                    "stageId": "sandbox_1_21",
                                    "weatherLv": 0
                                },
                                "n918E": {
                                    "zone": "z_1_1",
                                    "type": 13,
                                    "state": 2,
                                    "relate": {
                                        "pos": [
                                            95,
                                            335
                                        ],
                                        "adj": [],
                                        "depth": 0
                                    },
                                    "stageId": "sandbox_1_33",
                                    "weatherLv": 0
                                }
                            }
                        },
                        "stage": {
                            "node": {
                                "nB32E": {
                                    "id": "sandbox_1_27",
                                    "state": 0,
                                    "view": "",
                                    "action": [],
                                    "base": [
                                        {
                                            "key": "trap_446_xbfdtion",
                                            "pos": [
                                                12,
                                                14
                                            ],
                                            "hpRatio": 10000,
                                            "isDead": 0
                                        }
                                    ]
                                },
                                "n12B9": {
                                    "id": "sandbox_1_32",
                                    "state": 0,
                                    "view": "",
                                    "action": [],
                                    "port": [
                                        {
                                            "key": "trap_447_xbmcv",
                                            "pos": [
                                                7,
                                                11
                                            ],
                                            "hpRatio": 10000,
                                            "isDead": 0
                                        }
                                    ]
                                },
                                "n8340": {
                                    "id": "sandbox_1_26",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n88A8": {
                                    "id": "sandbox_1_01",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n35C1": {
                                    "id": "sandbox_1_09",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n2259": {
                                    "id": "sandbox_1_56",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n20CB": {
                                    "id": "sandbox_1_38",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n97C7": {
                                    "id": "sandbox_1_54",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "nD54F": {
                                    "id": "sandbox_1_55",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "nB55F": {
                                    "id": "sandbox_1_38",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "nA226": {
                                    "id": "sandbox_1_72",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n07D6": {
                                    "id": "sandbox_1_64",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n0446": {
                                    "id": "sandbox_1_28",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "nA659": {
                                    "id": "sandbox_1_39",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "nED84": {
                                    "id": "sandbox_1_80",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "nEFA5": {
                                    "id": "sandbox_1_70",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n81E8": {
                                    "id": "sandbox_1_40",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n9EF3": {
                                    "id": "sandbox_1_40",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n3259": {
                                    "id": "sandbox_1_24",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n6368": {
                                    "id": "sandbox_1_25",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "nD7CE": {
                                    "id": "sandbox_1_69",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n2D12": {
                                    "id": "sandbox_1_74",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "nDEF4": {
                                    "id": "sandbox_1_70",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n9096": {
                                    "id": "sandbox_1_38",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "nCA3B": {
                                    "id": "sandbox_1_55",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n22B0": {
                                    "id": "sandbox_1_56",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n607D": {
                                    "id": "sandbox_1_71",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n14BC": {
                                    "id": "sandbox_1_62",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "nBEB8": {
                                    "id": "sandbox_1_69",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "nF586": {
                                    "id": "sandbox_1_37",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n3740": {
                                    "id": "sandbox_1_70",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "nCFA1": {
                                    "id": "sandbox_1_41",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "nDDDC": {
                                    "id": "sandbox_1_54",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n32FD": {
                                    "id": "sandbox_1_62",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "nFE3F": {
                                    "id": "sandbox_1_03",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n8667": {
                                    "id": "sandbox_1_19",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n4CDF": {
                                    "id": "sandbox_1_77",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "nAD10": {
                                    "id": "sandbox_1_45",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "nAB42": {
                                    "id": "sandbox_1_71",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "nE038": {
                                    "id": "sandbox_1_14",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n7A2B": {
                                    "id": "sandbox_1_04",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n6ECA": {
                                    "id": "sandbox_1_03",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n8734": {
                                    "id": "sandbox_1_52",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n6632": {
                                    "id": "sandbox_1_13",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n7CB1": {
                                    "id": "sandbox_1_05",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n0D60": {
                                    "id": "sandbox_1_09",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "nEE32": {
                                    "id": "sandbox_1_22",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n663B": {
                                    "id": "sandbox_1_49",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n5D41": {
                                    "id": "sandbox_1_70",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n3E46": {
                                    "id": "sandbox_1_73",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n542E": {
                                    "id": "sandbox_1_51",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n3DB9": {
                                    "id": "sandbox_1_67",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "nD5FB": {
                                    "id": "sandbox_1_52",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n12CF": {
                                    "id": "sandbox_1_20",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n10AD": {
                                    "id": "sandbox_1_65",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "nA1C6": {
                                    "id": "sandbox_1_70",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "nEA6F": {
                                    "id": "sandbox_1_60",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n4121": {
                                    "id": "sandbox_1_02",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n8375": {
                                    "id": "sandbox_1_63",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "nE095": {
                                    "id": "sandbox_1_71",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n6831": {
                                    "id": "sandbox_1_50",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n3809": {
                                    "id": "sandbox_1_44",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "nA1CE": {
                                    "id": "sandbox_1_09",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n2BA6": {
                                    "id": "sandbox_1_23",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n1B64": {
                                    "id": "sandbox_1_40",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n6829": {
                                    "id": "sandbox_1_42",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n0FB8": {
                                    "id": "sandbox_1_02",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "nC69C": {
                                    "id": "sandbox_1_69",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n9C6A": {
                                    "id": "sandbox_1_43",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n98EF": {
                                    "id": "sandbox_1_68",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "nF5F6": {
                                    "id": "sandbox_1_75",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "nA1AD": {
                                    "id": "sandbox_1_78",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "nF294": {
                                    "id": "sandbox_1_57",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "nAB04": {
                                    "id": "sandbox_1_02",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n42D8": {
                                    "id": "sandbox_1_30",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n74C3": {
                                    "id": "sandbox_1_76",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n4244": {
                                    "id": "sandbox_1_58",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "nF0F5": {
                                    "id": "sandbox_1_71",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n9542": {
                                    "id": "sandbox_1_42",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n4B29": {
                                    "id": "sandbox_1_59",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "nD2FB": {
                                    "id": "sandbox_1_64",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n71D1": {
                                    "id": "sandbox_1_57",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n6C8E": {
                                    "id": "sandbox_1_69",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n9B77": {
                                    "id": "sandbox_1_29",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n2AF0": {
                                    "id": "sandbox_1_15",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n80F5": {
                                    "id": "sandbox_1_18",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n6AB0": {
                                    "id": "sandbox_1_61",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n3899": {
                                    "id": "sandbox_1_48",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "nB251": {
                                    "id": "sandbox_1_64",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n2D0A": {
                                    "id": "sandbox_1_53",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n6695": {
                                    "id": "sandbox_1_03",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "nCF3F": {
                                    "id": "sandbox_1_31",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n5536": {
                                    "id": "sandbox_1_69",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n740B": {
                                    "id": "sandbox_1_74",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n9AE0": {
                                    "id": "sandbox_1_46",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "nDFEC": {
                                    "id": "sandbox_1_58",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "nCC82": {
                                    "id": "sandbox_1_01",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "nC10F": {
                                    "id": "sandbox_1_71",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "nA317": {
                                    "id": "sandbox_1_48",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n1AA7": {
                                    "id": "sandbox_1_66",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "nE57A": {
                                    "id": "sandbox_1_73",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n403F": {
                                    "id": "sandbox_1_09",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n427C": {
                                    "id": "sandbox_1_47",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "nBAFC": {
                                    "id": "sandbox_1_10",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n2423": {
                                    "id": "sandbox_1_69",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "nE03B": {
                                    "id": "sandbox_1_03",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n7F77": {
                                    "id": "sandbox_1_12",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n6B1D": {
                                    "id": "sandbox_1_45",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n8BFF": {
                                    "id": "sandbox_1_52",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n3BA7": {
                                    "id": "sandbox_1_11",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n6828": {
                                    "id": "sandbox_1_40",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n4A25": {
                                    "id": "sandbox_1_79",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "nA6A1": {
                                    "id": "sandbox_1_69",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n9FD9": {
                                    "id": "sandbox_1_21",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                },
                                "n918E": {
                                    "id": "sandbox_1_33",
                                    "state": 0,
                                    "view": "",
                                    "action": []
                                }
                            }
                        },
                        "enemy": {
                            "enemyRush": {},
                            "rareAnimal": {}
                        },
                        "npc": {
                            "node": {},
                            "favor": {}
                        },
                        "report": {
                            "settle": null,
                            "daily": null
                        },
                        "event": {
                            "node": {},
                            "effect": []
                        }
                    },
                    "rift": null,
                    "riftInfo": {
                        "isUnlocked": false,
                        "randomRemain": 1,
                        "difficultyLvMax": -1,
                        "teamLv": 1,
                        "fixFinish": [],
                        "reservation": null,
                        "gameInfo": null,
                        "settleInfo": null
                    },
                    "quest": {
                        "pending": [],
                        "complete": []
                    },
                    "mission": {
                        "squad": []
                    },
                    "troop": {
                        "food": {},
                        "squad": [
                            {
                                "slots": [],
                                "tools": []
                            },
                            {
                                "slots": [],
                                "tools": []
                            },
                            {
                                "slots": [],
                                "tools": []
                            },
                            {
                                "slots": [],
                                "tools": []
                            },
                            {
                                "slots": [],
                                "tools": []
                            },
                            {
                                "slots": [],
                                "tools": []
                            },
                            {
                                "slots": [],
                                "tools": []
                            },
                            {
                                "slots": [],
                                "tools": []
                            }
                        ],
                        "usedChar": []
                    },
                    "cook": {
                        "drink": 280,
                        "extraDrink": 100,
                        "book": {
                            "sandbox_1_food_0": 0,
                            "sandbox_1_food_1": 0,
                            "sandbox_1_food_2": 0,
                            "sandbox_1_food_3": 0,
                            "sandbox_1_food_4": 0,
                            "sandbox_1_food_5": 0,
                            "sandbox_1_food_6": 0,
                            "sandbox_1_food_7": 0,
                            "sandbox_1_food_8": 0,
                            "sandbox_1_food_9": 0,
                            "sandbox_1_food_10": 0,
                            "sandbox_1_food_11": 0,
                            "sandbox_1_food_12": 0,
                            "sandbox_1_food_13": 0,
                            "sandbox_1_food_14": 0,
                            "sandbox_1_food_15": 0,
                            "sandbox_1_food_16": 0,
                            "sandbox_1_food_17": 0,
                            "sandbox_1_food_18": 0,
                            "sandbox_1_food_19": 0,
                            "sandbox_1_food_20": 0,
                            "sandbox_1_food_21": 0,
                            "sandbox_1_food_22": 0,
                            "sandbox_1_food_23": 0,
                            "sandbox_1_food_24": 0,
                            "sandbox_1_food_25": 0,
                            "sandbox_1_food_26": 0,
                            "sandbox_1_food_27": 0,
                            "sandbox_1_food_28": 0,
                            "sandbox_1_food_29": 0,
                            "sandbox_1_food_30": 0,
                            "sandbox_1_food_31": 0,
                            "sandbox_1_food_32": 0,
                            "sandbox_1_food_33": 0,
                            "sandbox_1_food_34": 0,
                            "sandbox_1_food_35": 0,
                            "sandbox_1_food_36": 0,
                            "sandbox_1_food_37": 0,
                            "sandbox_1_food_38": 0,
                            "sandbox_1_food_39": 0,
                            "sandbox_1_food_40": 0,
                            "sandbox_1_food_41": 0,
                            "sandbox_1_food_42": 0,
                            "sandbox_1_food_43": 0,
                            "sandbox_1_food_44": 0
                        },
                        "food": {
                            "f_1": {
                                "id": "sandbox_1_food_0",
                                "sub": [
                                    "sandbox_1_condiment",
                                    "sandbox_1_condiment"
                                ],
                                "count": 9999
                            },
                            "f_2": {
                                "id": "sandbox_1_food_1",
                                "sub": [
                                    "sandbox_1_condiment",
                                    "sandbox_1_condiment"
                                ],
                                "count": 9999
                            },
                            "f_3": {
                                "id": "sandbox_1_food_2",
                                "sub": [
                                    "sandbox_1_condiment",
                                    "sandbox_1_condiment"
                                ],
                                "count": 9999
                            },
                            "f_4": {
                                "id": "sandbox_1_food_3",
                                "sub": [
                                    "sandbox_1_condiment",
                                    "sandbox_1_condiment"
                                ],
                                "count": 9999
                            },
                            "f_5": {
                                "id": "sandbox_1_food_4",
                                "sub": [
                                    "sandbox_1_condiment",
                                    "sandbox_1_condiment"
                                ],
                                "count": 9999
                            },
                            "f_6": {
                                "id": "sandbox_1_food_5",
                                "sub": [
                                    "sandbox_1_condiment",
                                    "sandbox_1_condiment"
                                ],
                                "count": 9999
                            },
                            "f_7": {
                                "id": "sandbox_1_food_6",
                                "sub": [
                                    "sandbox_1_condiment",
                                    "sandbox_1_condiment"
                                ],
                                "count": 9999
                            },
                            "f_8": {
                                "id": "sandbox_1_food_7",
                                "sub": [
                                    "sandbox_1_condiment",
                                    "sandbox_1_condiment"
                                ],
                                "count": 9999
                            },
                            "f_9": {
                                "id": "sandbox_1_food_8",
                                "sub": [
                                    "sandbox_1_condiment",
                                    "sandbox_1_condiment"
                                ],
                                "count": 9999
                            },
                            "f_10": {
                                "id": "sandbox_1_food_9",
                                "sub": [
                                    "sandbox_1_condiment",
                                    "sandbox_1_condiment"
                                ],
                                "count": 9999
                            },
                            "f_11": {
                                "id": "sandbox_1_food_10",
                                "sub": [
                                    "sandbox_1_condiment",
                                    "sandbox_1_condiment"
                                ],
                                "count": 9999
                            },
                            "f_12": {
                                "id": "sandbox_1_food_11",
                                "sub": [
                                    "sandbox_1_condiment",
                                    "sandbox_1_condiment"
                                ],
                                "count": 9999
                            },
                            "f_13": {
                                "id": "sandbox_1_food_12",
                                "sub": [
                                    "sandbox_1_condiment",
                                    "sandbox_1_condiment"
                                ],
                                "count": 9999
                            },
                            "f_14": {
                                "id": "sandbox_1_food_13",
                                "sub": [
                                    "sandbox_1_condiment",
                                    "sandbox_1_condiment"
                                ],
                                "count": 9999
                            },
                            "f_15": {
                                "id": "sandbox_1_food_14",
                                "sub": [
                                    "sandbox_1_condiment",
                                    "sandbox_1_condiment"
                                ],
                                "count": 9999
                            },
                            "f_16": {
                                "id": "sandbox_1_food_15",
                                "sub": [
                                    "sandbox_1_condiment",
                                    "sandbox_1_condiment"
                                ],
                                "count": 9999
                            },
                            "f_17": {
                                "id": "sandbox_1_food_16",
                                "sub": [
                                    "sandbox_1_condiment",
                                    "sandbox_1_condiment"
                                ],
                                "count": 9999
                            },
                            "f_18": {
                                "id": "sandbox_1_food_17",
                                "sub": [
                                    "sandbox_1_condiment",
                                    "sandbox_1_condiment"
                                ],
                                "count": 9999
                            },
                            "f_19": {
                                "id": "sandbox_1_food_18",
                                "sub": [
                                    "sandbox_1_condiment",
                                    "sandbox_1_condiment"
                                ],
                                "count": 9999
                            },
                            "f_20": {
                                "id": "sandbox_1_food_19",
                                "sub": [
                                    "sandbox_1_condiment",
                                    "sandbox_1_condiment"
                                ],
                                "count": 9999
                            },
                            "f_21": {
                                "id": "sandbox_1_food_20",
                                "sub": [
                                    "sandbox_1_condiment",
                                    "sandbox_1_condiment"
                                ],
                                "count": 9999
                            },
                            "f_22": {
                                "id": "sandbox_1_food_21",
                                "sub": [
                                    "sandbox_1_condiment",
                                    "sandbox_1_condiment"
                                ],
                                "count": 9999
                            },
                            "f_23": {
                                "id": "sandbox_1_food_22",
                                "sub": [
                                    "sandbox_1_condiment",
                                    "sandbox_1_condiment"
                                ],
                                "count": 9999
                            },
                            "f_24": {
                                "id": "sandbox_1_food_23",
                                "sub": [
                                    "sandbox_1_condiment",
                                    "sandbox_1_condiment"
                                ],
                                "count": 9999
                            },
                            "f_25": {
                                "id": "sandbox_1_food_24",
                                "sub": [
                                    "sandbox_1_condiment",
                                    "sandbox_1_condiment"
                                ],
                                "count": 9999
                            },
                            "f_26": {
                                "id": "sandbox_1_food_25",
                                "sub": [
                                    "sandbox_1_condiment",
                                    "sandbox_1_condiment"
                                ],
                                "count": 9999
                            },
                            "f_27": {
                                "id": "sandbox_1_food_26",
                                "sub": [
                                    "sandbox_1_condiment",
                                    "sandbox_1_condiment"
                                ],
                                "count": 9999
                            },
                            "f_28": {
                                "id": "sandbox_1_food_27",
                                "sub": [
                                    "sandbox_1_condiment",
                                    "sandbox_1_condiment"
                                ],
                                "count": 9999
                            },
                            "f_29": {
                                "id": "sandbox_1_food_28",
                                "sub": [
                                    "sandbox_1_condiment",
                                    "sandbox_1_condiment"
                                ],
                                "count": 9999
                            },
                            "f_30": {
                                "id": "sandbox_1_food_29",
                                "sub": [
                                    "sandbox_1_condiment",
                                    "sandbox_1_condiment"
                                ],
                                "count": 9999
                            },
                            "f_31": {
                                "id": "sandbox_1_food_30",
                                "sub": [
                                    "sandbox_1_condiment",
                                    "sandbox_1_condiment"
                                ],
                                "count": 9999
                            },
                            "f_32": {
                                "id": "sandbox_1_food_31",
                                "sub": [
                                    "sandbox_1_condiment",
                                    "sandbox_1_condiment"
                                ],
                                "count": 9999
                            },
                            "f_33": {
                                "id": "sandbox_1_food_32",
                                "sub": [
                                    "sandbox_1_condiment",
                                    "sandbox_1_condiment"
                                ],
                                "count": 9999
                            },
                            "f_34": {
                                "id": "sandbox_1_food_33",
                                "sub": [
                                    "sandbox_1_condiment",
                                    "sandbox_1_condiment"
                                ],
                                "count": 9999
                            },
                            "f_35": {
                                "id": "sandbox_1_food_34",
                                "sub": [
                                    "sandbox_1_condiment",
                                    "sandbox_1_condiment"
                                ],
                                "count": 9999
                            },
                            "f_36": {
                                "id": "sandbox_1_food_35",
                                "sub": [
                                    "sandbox_1_condiment",
                                    "sandbox_1_condiment"
                                ],
                                "count": 9999
                            },
                            "f_37": {
                                "id": "sandbox_1_food_36",
                                "sub": [
                                    "sandbox_1_condiment",
                                    "sandbox_1_condiment"
                                ],
                                "count": 9999
                            },
                            "f_38": {
                                "id": "sandbox_1_food_37",
                                "sub": [
                                    "sandbox_1_condiment",
                                    "sandbox_1_condiment"
                                ],
                                "count": 9999
                            },
                            "f_39": {
                                "id": "sandbox_1_food_38",
                                "sub": [
                                    "sandbox_1_condiment",
                                    "sandbox_1_condiment"
                                ],
                                "count": 9999
                            },
                            "f_40": {
                                "id": "sandbox_1_food_39",
                                "sub": [
                                    "sandbox_1_condiment",
                                    "sandbox_1_condiment"
                                ],
                                "count": 9999
                            },
                            "f_41": {
                                "id": "sandbox_1_food_40",
                                "sub": [
                                    "sandbox_1_condiment",
                                    "sandbox_1_condiment"
                                ],
                                "count": 9999
                            },
                            "f_42": {
                                "id": "sandbox_1_food_41",
                                "sub": [
                                    "sandbox_1_condiment",
                                    "sandbox_1_condiment"
                                ],
                                "count": 9999
                            },
                            "f_43": {
                                "id": "sandbox_1_food_42",
                                "sub": [
                                    "sandbox_1_condiment",
                                    "sandbox_1_condiment"
                                ],
                                "count": 9999
                            },
                            "f_44": {
                                "id": "sandbox_1_food_43",
                                "sub": [
                                    "sandbox_1_condiment",
                                    "sandbox_1_condiment"
                                ],
                                "count": 9999
                            },
                            "f_45": {
                                "id": "sandbox_1_food_44",
                                "sub": [
                                    "sandbox_1_condiment",
                                    "sandbox_1_condiment"
                                ],
                                "count": 9999
                            }
                        }
                    },
                    "build": {
                        "book": {
                            "sandbox_1_building_1": 0,
                            "sandbox_1_building_2": 0,
                            "sandbox_1_building_3": 0,
                            "sandbox_1_building_4": 0,
                            "sandbox_1_building_5": 0,
                            "sandbox_1_building_6": 0,
                            "sandbox_1_building_7": 0,
                            "sandbox_1_building_8": 0,
                            "sandbox_1_building_9": 0,
                            "sandbox_1_building_10": 0,
                            "sandbox_1_building_11": 0,
                            "sandbox_1_building_12": 0,
                            "sandbox_1_building_13": 0,
                            "sandbox_1_building_14": 0,
                            "sandbox_1_building_15": 0,
                            "sandbox_1_building_16": 0,
                            "sandbox_1_building_17": 0,
                            "sandbox_1_building_18": 0,
                            "sandbox_1_building_19": 0,
                            "sandbox_1_building_20": 0,
                            "sandbox_1_building_21": 0,
                            "sandbox_1_building_22": 0,
                            "sandbox_1_building_23": 0,
                            "sandbox_1_building_24": 0,
                            "sandbox_1_building_25": 0,
                            "sandbox_1_building_26": 0,
                            "sandbox_1_building_27": 0,
                            "sandbox_1_building_28": 0,
                            "sandbox_1_building_29": 0,
                            "sandbox_1_building_30": 0,
                            "sandbox_1_building_31": 0,
                            "sandbox_1_building_32": 0,
                            "sandbox_1_building_33": 0,
                            "sandbox_1_building_34": 0,
                            "sandbox_1_building_35": 0,
                            "sandbox_1_building_36": 0,
                            "sandbox_1_animal_1": 0,
                            "sandbox_1_animal_2": 0,
                            "sandbox_1_animal_3": 0,
                            "sandbox_1_animal_4": 0,
                            "sandbox_1_animal_5": 0,
                            "sandbox_1_animal_6": 0,
                            "sandbox_1_animal_7": 0,
                            "sandbox_1_animal_8": 0,
                            "sandbox_1_animal_11": 0,
                            "sandbox_1_animal_12": 0,
                            "sandbox_1_animal_13": 0,
                            "sandbox_1_animal_14": 0,
                            "sandbox_1_animal_15": 0,
                            "sandbox_1_animal_16": 0,
                            "sandbox_1_animal_17": 0,
                            "sandbox_1_animal_18": 0,
                            "sandbox_1_tactical_1": 0,
                            "sandbox_1_tactical_2": 0,
                            "sandbox_1_tactical_3": 0,
                            "sandbox_1_tactical_4": 0,
                            "sandbox_1_tactical_5": 0,
                            "sandbox_1_tactical_6": 0,
                            "sandbox_1_tactical_7": 0,
                            "sandbox_1_tactical_8": 0,
                            "sandbox_1_tactical_9": 0,
                            "sandbox_1_tactical_10": 0,
                            "sandbox_1_tactical_11": 0,
                            "sandbox_1_tactical_12": 0,
                            "sandbox_1_tactical_13": 0,
                            "sandbox_1_tactical_14": 0,
                            "sandbox_1_tactical_15": 0,
                            "sandbox_1_tactical_16": 0,
                            "sandbox_1_tactical_17": 0,
                            "sandbox_1_tactical_18": 0,
                            "sandbox_1_tactical_19": 0,
                            "sandbox_1_tactical_20": 0,
                            "sandbox_1_tactical_21": 0,
                            "sandbox_1_tactical_22": 0,
                            "sandbox_1_tactical_23": 0,
                            "sandbox_1_tactical_24": 0,
                            "sandbox_1_tactical_25": 0,
                            "sandbox_1_tactical_26": 0,
                            "sandbox_1_tactical_27": 0,
                            "sandbox_1_tactical_28": 0,
                            "sandbox_1_tactical_29": 0,
                            "sandbox_1_tactical_30": 0
                        },
                        "building": {
                            "sandbox_1_building_1": 9999,
                            "sandbox_1_building_2": 9999,
                            "sandbox_1_building_3": 9999,
                            "sandbox_1_building_4": 9999,
                            "sandbox_1_building_5": 9999,
                            "sandbox_1_building_6": 9999,
                            "sandbox_1_building_7": 9999,
                            "sandbox_1_building_8": 9999,
                            "sandbox_1_building_9": 9999,
                            "sandbox_1_building_10": 9999,
                            "sandbox_1_building_11": 9999,
                            "sandbox_1_building_12": 9999,
                            "sandbox_1_building_13": 9999,
                            "sandbox_1_building_14": 9999,
                            "sandbox_1_building_15": 9999,
                            "sandbox_1_building_16": 9999,
                            "sandbox_1_building_17": 9999,
                            "sandbox_1_building_18": 9999,
                            "sandbox_1_building_19": 9999,
                            "sandbox_1_building_20": 9999,
                            "sandbox_1_building_21": 9999,
                            "sandbox_1_building_22": 9999,
                            "sandbox_1_building_23": 9999,
                            "sandbox_1_building_24": 9999,
                            "sandbox_1_building_25": 9999,
                            "sandbox_1_building_26": 9999,
                            "sandbox_1_building_27": 9999,
                            "sandbox_1_building_28": 9999,
                            "sandbox_1_building_29": 9999,
                            "sandbox_1_building_30": 9999,
                            "sandbox_1_building_31": 9999,
                            "sandbox_1_building_32": 9999,
                            "sandbox_1_building_33": 9999,
                            "sandbox_1_building_34": 9999,
                            "sandbox_1_building_35": 9999,
                            "sandbox_1_building_36": 9999
                        },
                        "tactical": {
                            "sandbox_1_tactical_1": 9999,
                            "sandbox_1_tactical_2": 9999,
                            "sandbox_1_tactical_3": 9999,
                            "sandbox_1_tactical_4": 9999,
                            "sandbox_1_tactical_5": 9999,
                            "sandbox_1_tactical_6": 9999,
                            "sandbox_1_tactical_7": 9999,
                            "sandbox_1_tactical_8": 9999,
                            "sandbox_1_tactical_9": 9999,
                            "sandbox_1_tactical_10": 9999,
                            "sandbox_1_tactical_11": 9999,
                            "sandbox_1_tactical_12": 9999,
                            "sandbox_1_tactical_13": 9999,
                            "sandbox_1_tactical_14": 9999,
                            "sandbox_1_tactical_15": 9999,
                            "sandbox_1_tactical_16": 9999,
                            "sandbox_1_tactical_17": 9999,
                            "sandbox_1_tactical_18": 9999,
                            "sandbox_1_tactical_19": 9999,
                            "sandbox_1_tactical_20": 9999,
                            "sandbox_1_tactical_21": 9999,
                            "sandbox_1_tactical_22": 9999,
                            "sandbox_1_tactical_23": 9999,
                            "sandbox_1_tactical_24": 9999,
                            "sandbox_1_tactical_25": 9999,
                            "sandbox_1_tactical_26": 9999,
                            "sandbox_1_tactical_27": 9999,
                            "sandbox_1_tactical_28": 9999,
                            "sandbox_1_tactical_29": 9999,
                            "sandbox_1_tactical_30": 9999
                        },
                        "animal": {
                            "sandbox_1_animal_1": 9999,
                            "sandbox_1_animal_2": 9999,
                            "sandbox_1_animal_3": 9999,
                            "sandbox_1_animal_4": 9999,
                            "sandbox_1_animal_5": 9999,
                            "sandbox_1_animal_6": 9999,
                            "sandbox_1_animal_7": 9999,
                            "sandbox_1_animal_8": 9999,
                            "sandbox_1_animal_11": 9999,
                            "sandbox_1_animal_12": 9999,
                            "sandbox_1_animal_13": 9999,
                            "sandbox_1_animal_14": 9999,
                            "sandbox_1_animal_15": 9999,
                            "sandbox_1_animal_16": 9999,
                            "sandbox_1_animal_17": 9999,
                            "sandbox_1_animal_18": 9999
                        }
                    },
                    "bag": {
                        "material": {},
                        "craft": []
                    },
                    "tech": {
                        "token": 0,
                        "cent": 0,
                        "unlock": [
                            "sandbox_1_tech_1",
                            "sandbox_1_tech_2",
                            "sandbox_1_tech_3",
                            "sandbox_1_tech_4",
                            "sandbox_1_tech_5",
                            "sandbox_1_tech_6",
                            "sandbox_1_tech_7",
                            "sandbox_1_tech_8",
                            "sandbox_1_tech_9",
                            "sandbox_1_tech_10",
                            "sandbox_1_tech_11",
                            "sandbox_1_tech_12",
                            "sandbox_1_tech_13",
                            "sandbox_1_tech_14",
                            "sandbox_1_tech_15",
                            "sandbox_1_tech_16",
                            "sandbox_1_tech_17",
                            "sandbox_1_tech_18",
                            "sandbox_1_tech_19",
                            "sandbox_1_tech_20",
                            "sandbox_1_tech_21",
                            "sandbox_1_tech_22",
                            "sandbox_1_tech_23",
                            "sandbox_1_tech_24",
                            "sandbox_1_tech_25",
                            "sandbox_1_tech_26",
                            "sandbox_1_tech_27",
                            "sandbox_1_tech_28",
                            "sandbox_1_tech_29",
                            "sandbox_1_tech_30",
                            "sandbox_1_tech_31",
                            "sandbox_1_tech_32",
                            "sandbox_1_tech_33",
                            "sandbox_1_tech_34",
                            "sandbox_1_tech_35",
                            "sandbox_1_tech_36",
                            "sandbox_1_tech_37",
                            "sandbox_1_tech_38",
                            "sandbox_1_tech_39",
                            "sandbox_1_tech_40",
                            "sandbox_1_tech_41",
                            "sandbox_1_tech_42",
                            "sandbox_1_tech_43",
                            "sandbox_1_tech_44",
                            "sandbox_1_tech_45",
                            "sandbox_1_tech_46",
                            "sandbox_1_tech_47",
                            "sandbox_1_tech_48",
                            "sandbox_1_tech_49",
                            "sandbox_1_tech_50",
                            "sandbox_1_tech_51",
                            "sandbox_1_tech_52",
                            "sandbox_1_tech_53",
                            "sandbox_1_tech_54"
                        ]
                    },
                    "bank": {
                        "book": [],
                        "coin": {}
                    },
                    "buff": {
                        "rune": {
                            "global": [
                                "sandbox_1_craft_1",
                                "sandbox_1_craft_2",
                                "sandbox_1_craft_3",
                                "sandbox_1_craft_4",
                                "sandbox_1_tech_factory_max_hp_lv1",
                                "sandbox_1_tech_factory_def_lv1",
                                "sandbox_1_tech_factory_max_hp_lv2",
                                "sandbox_1_tech_factory_def_lv2",
                                "sandbox_1_tech_factory_max_hp_lv3",
                                "sandbox_1_tech_factory_damage_resistance",
                                "sandbox_1_tech_battle_factory_def",
                                "sandbox_1_tech_battle_factory_magic_resist",
                                "sandbox_1_tech_battle_factory_def_ability_lv1",
                                "sandbox_1_tech_battle_factory_def_ability_lv2",
                                "sandbox_1_tech_atkspeed_down",
                                "sandbox_1_tech_speed_down",
                                "sandbox_1_tech_wrkwrk_speed_lv1",
                                "sandbox_1_tech_wrkwrk_atkwood_lv1",
                                "sandbox_1_tech_wrkwrk_speed_lv2",
                                "sandbox_1_tech_wrkwrk_atkstone_lv1",
                                "sandbox_1_tech_wrkwrk_atkspeed",
                                "sandbox_1_tech_wrkwrk_atkiron_lv1",
                                "sandbox_1_tech_wrkwrk_atkiron_lv2",
                                "sandbox_1_tech_wrkwrk_atkwood_lv2",
                                "sandbox_1_tech_wrkwrk_atkstone_lv2",
                                "sandbox_1_tech_wfato_live_lv1",
                                "sandbox_1_tech_wfato_live_lv2",
                                "sandbox_1_tech_wfato_live_lv3",
                                "sandbox_1_tech_rain_lv1",
                                "sandbox_1_tech_rain_lv2",
                                "sandbox_1_tech_hot_lv1",
                                "sandbox_1_tech_hot_lv2",
                                "sandbox_1_tech_wind_lv1",
                                "sandbox_1_tech_wind_lv2",
                                "sandbox_1_tech_finish_view_lv1",
                                "sandbox_1_tech_finish_view_lv2",
                                "sandbox_1_tech_view_around",
                                "sandbox_1_tech_finish_view_lv3",
                                "sandbox_1_tech_show_enemy"
                            ],
                            "node": {},
                            "char": {}
                        }
                    },
                    "archive": {
                        "save": [],
                        "nextLoadTs": 0,
                        "loadTimes": 0,
                        "loadTs": 1700000000
                    },
                    "supply": {
                        "unlock": false,
                        "enable": false,
                        "slotCnt": 0,
                        "char": []
                    },
                    "shop": {
                        "unlock": false,
                        "day": 0,
                        "slots": []
                    },
                    "month": {
                        "rushPass": []
                    }
                }
            }
        },
        "isClose": false
    }

    write_json(sandbox, SANDBOX_JSON_PATH)
    data = {
        "playerDataDelta": {
            "modified": {
                "sandboxPerm": sandbox
            },
            "deleted": {}
        }
    }

    return data


def setSquad():
    sandbox = read_json(SANDBOX_JSON_PATH)

    request_json = request.json

    sandbox["template"]["SANDBOX_V2"]["sandbox_1"]["troop"]["squad"][request_json["index"]] = {
        "slots": request_json["slots"],
        "tools": request_json["tools"]
    }

    write_json(sandbox, SANDBOX_JSON_PATH)
    data = {
        "playerDataDelta": {
            "modified": {
                "sandboxPerm": sandbox
            },
            "deleted": {}
        }
    }

    return data


def battleStart():
    request_json = request.json

    sandboxTemp = read_json(SANDBOX_TEMP_JSON_PATH)

    sandboxTemp["currentNodeId"] = request_json["nodeId"]

    write_json(sandboxTemp, SANDBOX_TEMP_JSON_PATH)

    return {
        "battleId": "abcdefgh-1234-5678-a1b2c3d4e5f6",
        "isEnemyRush": False,
        "shinyAnimal": {},
        "playerDataDelta": {
            "modified": {},
            "deleted": {}
        }
    }


def battleFinish():
    request_json = request.json

    sandboxTemp = read_json(SANDBOX_TEMP_JSON_PATH)

    node_id = sandboxTemp["currentNodeId"]

    sandbox = read_json(SANDBOX_JSON_PATH)

    if "building" not in sandbox["template"]["SANDBOX_V2"]["sandbox_1"]["main"]["stage"]["node"][node_id]:
        sandbox["template"]["SANDBOX_V2"]["sandbox_1"]["main"]["stage"]["node"][node_id]["building"] = []

    for i in request_json["sandboxV2Data"]["placedItems"]:
        if i["value"]["hpRatio"]:
            sandbox["template"]["SANDBOX_V2"]["sandbox_1"]["main"]["stage"]["node"][node_id]["building"].append(
                {
                    "key": i["key"]["itemId"],
                    "pos": [
                        i["key"]["position"]["row"],
                        i["key"]["position"]["col"]
                    ],
                    "hpRatio": 10000,
                    "dir": i["value"]["direction"]
                }
            )
        else:
            for j in range(len(sandbox["template"]["SANDBOX_V2"]["sandbox_1"]["main"]["stage"]["node"][node_id]["building"])):
                k = sandbox["template"]["SANDBOX_V2"]["sandbox_1"]["main"]["stage"]["node"][node_id]["building"][j]
                if k["pos"][0] == i["key"]["position"]["row"] and k["pos"][1] == i["key"]["position"]["col"]:
                    sandbox["template"]["SANDBOX_V2"]["sandbox_1"]["main"]["stage"]["node"][node_id]["building"].pop(
                        j)
                    break

    write_json(sandbox, SANDBOX_JSON_PATH)
    data = {
        "success": True,
        "rewards": [],
        "randomRewards": [],
        "costItems": [],
        "isEnemyRush": False,
        "enemyRushCount": [],
        "playerDataDelta": {
            "modified": {
                "sandboxPerm": sandbox
            },
            "deleted": {}
        }
    }

    return data


def homeBuildSave():
    sandbox_table = updateData(SANDBOX_TABLE_URL)
    sandbox = read_json(SANDBOX_JSON_PATH)

    request_json = request.json

    node_id = request_json["nodeId"]

    if "building" not in sandbox["template"]["SANDBOX_V2"]["sandbox_1"]["main"]["stage"]["node"][node_id]:
        sandbox["template"]["SANDBOX_V2"]["sandbox_1"]["main"]["stage"]["node"][node_id]["building"] = []

    for i in request_json["operation"]:
        if i["type"] == 1:
            building_id = i["buildingId"]
            sandbox["template"]["SANDBOX_V2"]["sandbox_1"]["main"]["stage"]["node"][node_id]["building"].append(
                {
                    "key": building_id,
                    "pos": [
                        i["pos"]["row"],
                        i["pos"]["col"]
                    ],
                    "hpRatio": 10000,
                    "dir": i["dir"]
                }
            )
            building_buff = f"{building_id}_buff"
            if building_buff in sandbox_table["detail"]["SANDBOX_V2"]["sandbox_1"]["runeDatas"]:
                sandbox["template"]["SANDBOX_V2"]["sandbox_1"]["buff"]["rune"]["global"].append(
                    building_buff
                )
        elif i["type"] == 3:
            for j in range(len(sandbox["template"]["SANDBOX_V2"]["sandbox_1"]["main"]["stage"]["node"][node_id]["building"])):
                k = sandbox["template"]["SANDBOX_V2"]["sandbox_1"]["main"]["stage"]["node"][node_id]["building"][j]
                if k["pos"][0] == i["pos"]["row"] and k["pos"][1] == i["pos"]["col"]:
                    building_id = k["key"]
                    building_buff = f"{building_id}_buff"
                    if building_buff in sandbox_table["detail"]["SANDBOX_V2"]["sandbox_1"]["runeDatas"]:
                        sandbox["template"]["SANDBOX_V2"]["sandbox_1"]["buff"]["rune"]["global"].remove(
                            building_buff
                        )
                    sandbox["template"]["SANDBOX_V2"]["sandbox_1"]["main"]["stage"]["node"][node_id]["building"].pop(
                        j
                    )
                    break

    write_json(sandbox, SANDBOX_JSON_PATH)
    data = {
        "playerDataDelta": {
            "modified": {
                "sandboxPerm": sandbox
            },
            "deleted": {}
        }
    }

    return data


def settleGame():
    sandbox = read_json(SANDBOX_JSON_PATH)

    null = None
    true = True
    false = False
    data = {
        "playerDataDelta": {
            "modified": {
                "sandboxPerm": {
                    "template": {
                        "SANDBOX_V2": {
                            "sandbox_1": {
                                "base": {
                                    "baseLv": 0,
                                    "upgradeProgress": [],
                                    "trapLimit": {},
                                    "portableUnlock": false,
                                    "outpostUnlock": false,
                                    "repairDiscount": 0,
                                    "bossKill": []
                                },
                                "main": {
                                    "game": {
                                        "mapId": "",
                                        "day": 0,
                                        "maxDay": 0,
                                        "ap": 0,
                                        "maxAp": 0
                                    },
                                    "map": {
                                        "season": {
                                            "type": 0,
                                            "remain": 0,
                                            "total": 0
                                        }
                                    },
                                    "report": {
                                        "settle": null,
                                        "daily": null
                                    },
                                    "event": {
                                        "node": {},
                                        "effect": []
                                    }
                                },
                                "buff": {
                                    "rune": {
                                        "global": [],
                                        "node": {},
                                        "char": {}
                                    }
                                },
                                "riftInfo": {
                                    "isUnlocked": false,
                                    "randomRemain": 0,
                                    "difficultyLvMax": -1,
                                    "teamLv": 0,
                                    "fixFinish": [],
                                    "reservation": null,
                                    "gameInfo": null,
                                    "settleInfo": null
                                },
                                "quest": {
                                    "pending": [],
                                    "complete": []
                                },
                                "mission": {
                                    "squad": []
                                },
                                "troop": {
                                    "food": {},
                                    "squad": [
                                        {
                                            "slots": [],
                                            "tools": []
                                        },
                                        {
                                            "slots": [],
                                            "tools": []
                                        },
                                        {
                                            "slots": [],
                                            "tools": []
                                        },
                                        {
                                            "slots": [],
                                            "tools": []
                                        },
                                        {
                                            "slots": [],
                                            "tools": []
                                        },
                                        {
                                            "slots": [],
                                            "tools": []
                                        },
                                        {
                                            "slots": [],
                                            "tools": []
                                        },
                                        {
                                            "slots": [],
                                            "tools": []
                                        }
                                    ],
                                    "usedChar": []
                                },
                                "cook": {
                                    "drink": 0,
                                    "extraDrink": 0,
                                    "book": {},
                                    "food": {}
                                },
                                "bag": {
                                    "material": {},
                                    "craft": []
                                },
                                "tech": {
                                    "token": 8,
                                    "cent": 0,
                                    "unlock": []
                                },
                                "bank": {
                                    "book": [],
                                    "coin": {}
                                },
                                "archive": {
                                    "save": [],
                                    "nextLoadTs": 0,
                                    "loadTimes": 0,
                                    "loadTs": 0
                                },
                                "supply": {
                                    "unlock": false,
                                    "enable": false,
                                    "slotCnt": 0,
                                    "char": []
                                },
                                "shop": {
                                    "unlock": false,
                                    "day": 0,
                                    "slots": []
                                },
                                "status": {
                                    "ver": 1,
                                    "state": 0,
                                    "ts": 0,
                                    "isRift": false,
                                    "isGuide": false,
                                    "exploreMode": false
                                }
                            }
                        }
                    }
                }
            },
            "deleted": {
                "sandboxPerm": {
                    "template": {
                        "SANDBOX_V2": {
                            "sandbox_1": {
                                "main": {
                                    "map": {
                                        "node": [
                                            i for i in sandbox["template"]["SANDBOX_V2"]["sandbox_1"]["main"]["map"]["node"]
                                        ]
                                    },
                                    "stage": {
                                        "node": [
                                            i for i in sandbox["template"]["SANDBOX_V2"]["sandbox_1"]["main"]["stage"]["node"]
                                        ]
                                    },
                                    "enemy": {
                                        "enemyRush": [
                                            i for i in sandbox["template"]["SANDBOX_V2"]["sandbox_1"]["main"]["enemy"]["enemyRush"]
                                        ]
                                    }
                                },
                                "buff": {
                                    "rune": {
                                        "node": [
                                            i for i in sandbox["template"]["SANDBOX_V2"]["sandbox_1"]["buff"]["rune"]["node"]
                                        ],
                                        "char": [
                                            i for i in sandbox["template"]["SANDBOX_V2"]["sandbox_1"]["buff"]["rune"]["char"]
                                        ]
                                    }
                                },
                                "troop": {
                                    "food": [
                                        i for i in sandbox["template"]["SANDBOX_V2"]["sandbox_1"]["troop"]["food"]
                                    ]
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    sandbox = {
        "template": {
            "SANDBOX_V2": {
                "sandbox_1": {
                    "status": {
                        "ver": 1,
                        "state": 0,
                        "ts": 0,
                        "isRift": false,
                        "isGuide": false,
                        "exploreMode": false
                    },
                    "base": {
                        "baseLv": 0,
                        "upgradeProgress": [],
                        "trapLimit": {},
                        "portableUnlock": false,
                        "outpostUnlock": false,
                        "repairDiscount": 0,
                        "bossKill": []
                    },
                    "main": {
                        "game": {
                            "mapId": "",
                            "day": 0,
                            "maxDay": 0,
                            "ap": 0,
                            "maxAp": 0
                        },
                        "map": {
                            "season": {
                                "type": 0,
                                "remain": 0,
                                "total": 0
                            },
                            "zone": {},
                            "node": {}
                        },
                        "stage": {
                            "node": {}
                        },
                        "enemy": {
                            "enemyRush": {},
                            "rareAnimal": {}
                        },
                        "npc": {
                            "node": {},
                            "favor": {}
                        },
                        "report": {
                            "settle": null,
                            "daily": null
                        },
                        "event": {
                            "node": {},
                            "effect": []
                        }
                    },
                    "rift": null,
                    "riftInfo": {
                        "isUnlocked": false,
                        "randomRemain": 0,
                        "difficultyLvMax": -1,
                        "teamLv": 0,
                        "fixFinish": [],
                        "reservation": null,
                        "gameInfo": null,
                        "settleInfo": null
                    },
                    "quest": {
                        "pending": [],
                        "complete": []
                    },
                    "mission": {
                        "squad": []
                    },
                    "troop": {
                        "food": {},
                        "squad": [
                            {
                                "slots": [],
                                "tools": []
                            },
                            {
                                "slots": [],
                                "tools": []
                            },
                            {
                                "slots": [],
                                "tools": []
                            },
                            {
                                "slots": [],
                                "tools": []
                            },
                            {
                                "slots": [],
                                "tools": []
                            },
                            {
                                "slots": [],
                                "tools": []
                            },
                            {
                                "slots": [],
                                "tools": []
                            },
                            {
                                "slots": [],
                                "tools": []
                            }
                        ],
                        "usedChar": []
                    },
                    "cook": {
                        "drink": 0,
                        "extraDrink": 0,
                        "book": {},
                        "food": {}
                    },
                    "build": {
                        "book": {},
                        "building": {},
                        "tactical": {},
                        "animal": {}
                    },
                    "bag": {
                        "material": {},
                        "craft": []
                    },
                    "tech": {
                        "token": 6,
                        "cent": 0,
                        "unlock": []
                    },
                    "bank": {
                        "book": [],
                        "coin": {}
                    },
                    "buff": {
                        "rune": {
                            "global": [],
                            "node": {},
                            "char": {}
                        }
                    },
                    "archive": {
                        "save": [],
                        "nextLoadTs": 0,
                        "loadTimes": 0,
                        "loadTs": 0
                    },
                    "supply": {
                        "unlock": false,
                        "enable": false,
                        "slotCnt": 0,
                        "char": []
                    },
                    "shop": {
                        "unlock": false,
                        "day": 0,
                        "slots": []
                    },
                    "month": {
                        "rushPass": []
                    }
                }
            }
        }

    }

    write_json(sandbox, SANDBOX_JSON_PATH)

    return data


def eatFood():
    sandbox = read_json(SANDBOX_JSON_PATH)

    request_json = request.json

    char_inst_id = request_json["charInstId"]
    food_inst_id = request_json["foodInstId"]

    food = sandbox["template"]["SANDBOX_V2"]["sandbox_1"]["cook"]["food"][food_inst_id]

    sandbox["template"]["SANDBOX_V2"]["sandbox_1"]["troop"]["food"][str(char_inst_id)] = {
        "id": food["id"],
        "sub": food["sub"],
        "day": 6
    }

    buff = food["id"]

    sandbox_table = updateData(SANDBOX_TABLE_URL)

    if food["sub"] == [
        "sandbox_1_condiment",
        "sandbox_1_condiment"
    ]:
        if buff + "_x" in sandbox_table["detail"]["SANDBOX_V2"]["sandbox_1"]["runeDatas"]:
            buff += "_x"

    sandbox["template"]["SANDBOX_V2"]["sandbox_1"]["buff"]["rune"]["char"][str(char_inst_id)] = [
        buff
    ]

    write_json(sandbox, SANDBOX_JSON_PATH)
    data = {
        "playerDataDelta": {
            "modified": {
                "sandboxPerm": sandbox
            },
            "deleted": {}
        }
    }

    return data


def getNextEnemyRushId(sandbox):
    d = set()
    for e in sandbox["template"]["SANDBOX_V2"]["sandbox_1"]["main"]["enemy"]["enemyRush"]:
        d.add(int(e[3:]))
    i = 1
    while i in d:
        i += 1
    return f"er_{i}"


def addEnemyRush(sandbox, node_id, enemy_id):
    sandbox_table = updateData(SANDBOX_TABLE_URL)

    enemy_rush_id = getNextEnemyRushId(sandbox)

    enemy = []
    enemy_rush_type = 0

    enemy_rush_type_dict = {
        "NORMAL": 0,
        "ELITE": 1,
        "BOSS": 2,
        "BANDIT": 3,
        "RALLY": 4,
        "THIEF": 5,
        "MESSENGER": 6
    }

    flag = False
    for i in sandbox_table["detail"]["SANDBOX_V2"]["sandbox_1"]["rushEnemyData"]["rushEnemyGroupConfigs"]:
        for j in sandbox_table["detail"]["SANDBOX_V2"]["sandbox_1"]["rushEnemyData"]["rushEnemyGroupConfigs"][i]:
            if j["enemyGroupKey"] == enemy_id:
                for k in j["enemy"]:
                    enemy.append([k["count"], k["count"]])
                enemy_rush_type = enemy_rush_type_dict[i]
                flag = True
                break
        if flag:
            break

    sandbox["template"]["SANDBOX_V2"]["sandbox_1"]["main"]["enemy"]["enemyRush"][enemy_rush_id] = {
        "enemyRushType": enemy_rush_type,
        "groupKey": enemy_id,
        "state": 0,
        "day": 0,
        "path": [
            node_id
        ],
        "enemy": enemy,
        "badge": 0
    }


def monthBattleStart():
    return {
        "battleId": "abcdefgh-1234-5678-a1b2c3d4e5f6",
        "extraRunes": [
        ],
        "playerDataDelta": {
            "modified": {},
            "deleted": {}
        }
    }


def monthBattleFinish():
    request_json = request.json

    node_id = "n12B9"

    sandbox = read_json(SANDBOX_JSON_PATH)

    if "building" not in sandbox["template"]["SANDBOX_V2"]["sandbox_1"]["main"]["stage"]["node"][node_id]:
        sandbox["template"]["SANDBOX_V2"]["sandbox_1"]["main"]["stage"]["node"][node_id]["building"] = []

    for i in request_json["sandboxV2Data"]["placedItems"]:
        if i["value"]["hpRatio"]:
            sandbox["template"]["SANDBOX_V2"]["sandbox_1"]["main"]["stage"]["node"][node_id]["building"].append(
                {
                    "key": i["key"]["itemId"],
                    "pos": [
                        i["key"]["position"]["row"],
                        i["key"]["position"]["col"]
                    ],
                    "hpRatio": 10000,
                    "dir": i["value"]["direction"]
                }
            )
        else:
            for j in range(len(sandbox["template"]["SANDBOX_V2"]["sandbox_1"]["main"]["stage"]["node"][node_id]["building"])):
                k = sandbox["template"]["SANDBOX_V2"]["sandbox_1"]["main"]["stage"]["node"][node_id]["building"][j]
                if k["pos"][0] == i["key"]["position"]["row"] and k["pos"][1] == i["key"]["position"]["col"]:
                    sandbox["template"]["SANDBOX_V2"]["sandbox_1"]["main"]["stage"]["node"][node_id]["building"].pop(
                        j)
                    break

    write_json(sandbox, SANDBOX_JSON_PATH)
    return {
        "success": True,
        "firstPass": False,
        "enemyRushCount": [
            0,
            0
        ],
        "playerDataDelta": {
            "modified": {
                "sandboxPerm": sandbox
            },
            "deleted": {}
        }
    }


def exploreMode():
    request_json = request.json
    exploreMode = bool(request_json["open"])

    sandbox = read_json(SANDBOX_JSON_PATH)

    sandbox["template"]["SANDBOX_V2"]["sandbox_1"]["status"]["exploreMode"] = exploreMode

    exploreModeBuffs = ["normal_mode_buff1", "normal_mode_buff3"]

    if exploreMode:
        sandbox["template"]["SANDBOX_V2"]["sandbox_1"]["buff"]["rune"]["global"] += exploreModeBuffs
    else:
        for buff in exploreModeBuffs:
            if buff in sandbox["template"]["SANDBOX_V2"]["sandbox_1"]["buff"]["rune"]["global"]:
                sandbox["template"]["SANDBOX_V2"]["sandbox_1"]["buff"]["rune"]["global"].remove(
                    buff
                )

    write_json(sandbox, SANDBOX_JSON_PATH)

    data = {
        "playerDataDelta": {
            "modified": {
                "sandboxPerm": sandbox
            },
            "deleted": {}
        }
    }

    return data
