from typing import ClassVar

from connection_data import area_doors_unpackable
from door_logic import canOpen
from item_data import items_unpackable, Items
from loadout import Loadout
from logicInterface import AreaLogicType, LocationLogicType, LogicInterface
from logic_shortcut import LogicShortcut

# TODO: There are a bunch of places where where Expert logic needed energy tanks even if they had Varia suit.
# Need to make sure everything is right in those places. 
# (They will probably work right when they're combined like this,
#  but they wouldn't have worked right when casual was separated from expert.)

# TODO: There are also a bunch of places where casual used icePod, where expert only used Ice. Is that right?

(
    CraterR, SunkenNestL, RuinedConcourseBL, RuinedConcourseTR, CausewayR,
    SporeFieldTR, SporeFieldBR, OceanShoreR, EleToTurbidPassageR, PileAnchorL,
    ExcavationSiteL, WestCorridorR, FoyerR, ConstructionSiteL, AlluringCenoteR,
    FieldAccessL, TransferStationR, CellarR, SubbasementFissureL,
    WestTerminalAccessL, MezzanineConcourseL, VulnarCanyonL, CanyonPassageR,
    ElevatorToCondenserL, LoadingDockSecurityAreaL, ElevatorToWellspringL,
    NorakBrookL, NorakPerimeterTR, NorakPerimeterBL, VulnarDepthsElevatorEL,
    VulnarDepthsElevatorER, HiveBurrowL, SequesteredInfernoL,
    CollapsedPassageR, MagmaPumpL, ReservoirMaintenanceTunnelR, IntakePumpR,
    ThermalReservoir1R, GeneratorAccessTunnelL, ElevatorToMagmaLakeR,
    MagmaPumpAccessR, FieryGalleryL, RagingPitL, HollowChamberR, PlacidPoolR,
    SporousNookL, RockyRidgeTrailL, TramToSuziIslandR
) = area_doors_unpackable

(
    Missile, Super, PowerBomb, Morph, Springball, Bombs, HiJump,
    Varia, GravitySuit, Wave, SpeedBooster, Spazer, Ice,
    Plasma, Screw, Charge, Grapple, SpaceJump, Energy, Xray, Reserve
) = items_unpackable

energy200 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 1
))

energy300 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 2
))
energy400 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 3
))
energy500 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 4
))
energy600 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 5
))
energy700 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 6
))
energy800 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 7
))
energy900 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 8
))
energy1000 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 9
))
energy1200 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve))  >= 11
))
energy1500 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve))  >= 14
))
hellrun2 = LogicShortcut(lambda loadout: (
    (energy300 in loadout) or
    (Varia in loadout)
))
hellrun3 = LogicShortcut(lambda loadout: (
    (energy400 in loadout) or
    (Varia in loadout)
))
hellrun4 = LogicShortcut(lambda loadout: (
    (energy500 in loadout) or
    (Varia in loadout)
))

missile10 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Missile) * 5 >= 10
))
missile15 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Missile) * 5 >= 15
))
missile25 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Missile) * 5 >= 25
))
missile40 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Missile) * 5 >= 40
))
missile60 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Missile) * 5 >= 60
))
super15 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Super) * 5 >= 15
))
super30 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Super) * 5 >= 30
))
powerBomb15 = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    loadout.count(Items.PowerBomb) *3 >= 15
))
canUseBombs = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    ((Bombs in loadout) or (PowerBomb in loadout))
))
canUsePB = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    (PowerBomb in loadout)
))
canBreakBlocks = LogicShortcut(lambda loadout: (
    #with bombs or screw attack, maybe without morph
    (canUseBombs in loadout) or
    (Screw in loadout)
))
pinkDoor = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    (
        (Missile in loadout) or
        (Super in loadout)
        )
))
canIBJ = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    (Bombs in loadout)
))
canSBJ = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    (Springball in loadout)
))
morphHop = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    (
        (Bombs in loadout) or
        (PowerBomb in loadout) or
        (Springball in loadout)
    )
))
canFly = LogicShortcut(lambda loadout: (
    (canIBJ in loadout) or
    (SpaceJump in loadout)
))
parlor = LogicShortcut(lambda loadout: (
    (Morph in loadout) or
    (SpeedBooster in loadout) or
    (Screw in loadout)
))
lowerOcean = LogicShortcut(lambda loadout: (
    ( #enter
        ( #from ocean
            (Super in loadout) and
            (Morph in loadout)
        ) or
        ( #parlor basement
            (pinkDoor in loadout) and
            (
                (canUseBombs in loadout) or #morph maze
                (
                    (Grapple in loadout) and #grapple crumbles
                    (Morph in loadout)
                )
            )
        ) or
        ( #climb
            (pinkDoor in loadout) and
            (GravitySuit in loadout) and
            (Morph in loadout)
        )
    ) and
    ( #return
        (Morph in loadout) or #bowling
        (
            (canFly in loadout) and #climb
            (canUseBombs in loadout)
        )
    )
))
gardensWest = LogicShortcut(lambda loadout: (
    ( #from gauntlet
        (Morph in loadout) and
        (Super in loadout)
    ) or
    ( #from parlor
        (parlor in loadout) and
        (
            (canFly in loadout) or
            (SpeedBooster in loadout)
        ) and
        (Super in loadout)
    ) or
    ( #from underworld central
        (parlor in loadout) and
        (pinkDoor in loadout) and
        (Grapple in loadout) and
        (canUsePB in loadout) and
        (hellrun3 in loadout)
    )
))
tetraRuins = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    (
        (canUseBombs in loadout) or
        (GravitySuit in loadout)
        #SpeedBooster speedkeep to return?
    )
))
btAtrium = LogicShortcut(lambda loadout: (
    (tetraRuins in loadout) and
    ( #enter
        (pinkDoor in loadout) or #front door
        (
            (canUseBombs in loadout) and #back door options
            (
                (
                    (canIBJ in loadout) and
                    (canUsePB in loadout)
                ) or
                (HiJump in loadout) or
                (Springball in loadout) or
                (SpaceJump in loadout) or
                (SpeedBooster in loadout)
            )
        )
    ) and
    ( #leave atrium
        (canUseBombs in loadout) or #lower left or right
        ( #upper left
            (Super in loadout) and
            (
                (canFly in loadout) or
                (SpeedBooster in loadout)
            )
        ) 
    )
))
variaElevator = LogicShortcut(lambda loadout: (
    (canUseBombs in loadout) and
    (
        ( #need a gray door, like BT
            (btAtrium in loadout) and
            (Bombs in loadout)
        ) or
        (pinkDoor in loadout) #or old Mother Brain gray door
    ) and
    ( #kill the pink pirate
        (Plasma in loadout) or
        (SpeedBooster in loadout)
    ) and 
    ( #pass the PB block at top of elevator
        (canUsePB in loadout) or
        (Xray in loadout)
    )
))
elevatorToSky = LogicShortcut(lambda loadout: (
    (variaElevator in loadout) and
    ( #pass the speed or wave blocks
        (SpeedBooster in loadout) or
        (
            (canFly in loadout) and
            (canUsePB in loadout) and
            (Wave in loadout)
        )   
    ) and
    ( #plus, it's a hellrun
        (hellrun4 in loadout) #idk   
    )

))
eternalHall = LogicShortcut(lambda loadout: (
    ( #from sky elevator
        (elevatorToSky in loadout) and
        (Missile in loadout) and
        (canUsePB in loadout)
    ) or
    ( #from toilet
        (canUsePB in loadout) and
        (Super in loadout) and
        (energy500 in loadout)
    ) or
    (
        ( #from gardens West
            (
                (gardensWest in loadout) and
                ( #lava dive
                    (energy300 in loadout) or
                    (GravitySuit in loadout) 
                )
            ) or
            ( #from underworld central
                (parlor in loadout) and
                (pinkDoor in loadout) and
                (Grapple in loadout) and
                (canUsePB in loadout) and
                (hellrun3 in loadout)
            )
            
        ) and
        ( #get in the front gates
            (canUseBombs in loadout) or
            (morphHop in loadout) or
            (SpeedBooster in loadout)
        ) and
        ( #get up the spike wall
            (SpeedBooster in loadout) or
            (canFly in loadout) or
            (Ice in loadout)
        ) and
        ( #get across the spikes
            (Grapple in loadout) or
            (SpaceJump in loadout) or
            (energy500 in loadout)
        )
    )
))
upperEternal = LogicShortcut(lambda loadout: (
    ( #from sky elevator
        (elevatorToSky in loadout) and
        (Missile in loadout)
    ) or
    ( #from toilet
        (canUsePB in loadout) and
        (Super in loadout) and
        (energy500 in loadout)
    ) or
    ( #from lower eternal hall
        (eternalHall in loadout) and
        (
            (canUsePB in loadout) or
            (canFly in loadout) or
            (HiJump in loadout) or
            (canSBJ in loadout) or
            (Ice in loadout) or
            (SpeedBooster in loadout)
        )
    )
))
kraid = LogicShortcut(lambda loadout: (
    (eternalHall in loadout) and
    (SpeedBooster in loadout) and
    (canUsePB in loadout) and
    (
        (Charge in loadout) or
        (Missile in loadout)
    ) and
    ( #lava dive escape
        (GravitySuit in loadout) or
        (energy300 in loadout)
    )
))
croc = LogicShortcut(lambda loadout: (
#copied from eternalHall, but doesn't need speed
    (Morph in loadout) and
    (
        (
            (gardensWest in loadout) and
            ( #lava dive
                (energy300 in loadout) or
                (GravitySuit in loadout) 
            )
        ) or
        ( #from underworld central
            (parlor in loadout) and
            (pinkDoor in loadout) and
            (Grapple in loadout) and
            (canUsePB in loadout) and
            (hellrun3 in loadout)
        )
    ) and
    ( #kill croc
        (hellrun3 in loadout) and
        (
            (Missile in loadout) or
            (Charge in loadout)
        ) and
        (
            (GravitySuit in loadout) or
            (energy400 in loadout) # a guess
        )
    )
))
businessCenter = LogicShortcut(lambda loadout: (
    (parlor in loadout) and 
    (pinkDoor in loadout) and
    ( #get in to business center
        (Super in loadout) or
        (
            (canUsePB in loadout) or
            (Grapple in loadout)
        )
    ) and
    ( #be able to leave business center!
        (canUsePB in loadout) or
        (
            (Super in loadout) and
            (energy300 in loadout) and
            (canUseBombs in loadout)
        ) or
        (
            (Varia in loadout) and
            (SpaceJump in loadout) and
            (canUseBombs in loadout)
        )
    )
))
underworldCentral = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    (pinkDoor in loadout) and
    (canUseBombs in loadout) and
    (Varia in loadout) and #eyyyyyy
    (
        (Grapple in loadout) or
        (Super in loadout)
    )
))
ln = LogicShortcut(lambda loadout: (
    ( #front and back doors to LN
        (canUsePB in loadout) or
        (Wave in loadout)
    ) and
    ( #get there first
        (
            (underworldCentral in loadout) and
            (energy300 in loadout)
        ) or
        (
            (canUsePB in loadout) and
            (pinkDoor in loadout) and
            (Varia in loadout)
        )
    )

))
command = LogicShortcut(lambda loadout: (
    (Missile in loadout) and # for Phantoon 
    ( # protection for Phantoon
        (Varia in loadout) or
        (GravitySuit in loadout) or
        (energy300 in loadout)
    ) and
    (
        ( # from Eternal L
            (upperEternal in loadout) and
            (Super in loadout)
        ) or
        ( # from Eternal R
            (upperEternal in loadout) and
            (canUsePB in loadout)
        ) or
        (elevatorToSky in loadout)  # varia elevator side
    )
))
sky = LogicShortcut(lambda loadout: (
    ( #get there
        (command in loadout) or
        (variaElevator in loadout)
    ) and
    (       
        (Wave in loadout) or
        (
            (SpeedBooster in loadout) and
            (canUsePB in loadout) and
            (canFly in loadout)
        )
    )
))
draygon = LogicShortcut(lambda loadout: (
    (sky in loadout) and
    (canUsePB in loadout) and
    (energy300 in loadout) and
    (
        (Grapple in loadout) or
        (
            (Plasma in loadout) and
            (Charge in loadout)
        )
    )   
))
gt = LogicShortcut(lambda loadout: (
    (
        (eternalHall in loadout) and
        (canUsePB in loadout)
    ) or
    (
        (canUsePB in loadout) and
        (Super in loadout)
    )
))

area_logic: AreaLogicType = {
    "Early": {
        # using SunkenNestL as the hub for this area, so we don't need a path from every door to every other door
        # just need at least a path with sunken nest to and from every other door in the area
        ("CraterR", "SunkenNestL"): lambda loadout: (
            True
        ),
        ("SunkenNestL", "CraterR"): lambda loadout: (
            True
        ),
        ("SunkenNestL", "RuinedConcourseBL"): lambda loadout: (
            True
        ),
        ("SunkenNestL", "RuinedConcourseTR"): lambda loadout: (
            True
            # TODO: Expert needs energy and casual doesn't? And Casual can do it with supers, but expert can't?
        ),   
    },
}


location_logic: LocationLogicType = {
    "Crater Missile": lambda loadout: (
        True
    ),
    "Parlor Morph Ball": lambda loadout: (
        (Morph in loadout) or
        (SpeedBooster in loadout) or
        (Screw in loadout)

    ),
    "Charge Beam": lambda loadout: (
        (tetraRuins in loadout)
    ),
    "Bombs": lambda loadout: (
        (btAtrium in loadout)
    ),
    "Varia Suit": lambda loadout: (
        (canUseBombs in loadout)
    ),
    "Grapple Beam": lambda loadout: (
        (lowerOcean in loadout) and
        (hellrun2 in loadout) and #heyyyy
        (
            (Grapple in loadout) or
            (canFly in loadout)
        ) #ish
    ),
    "Kraid Reward Power Bomb": lambda loadout: (
        (kraid in loadout)
    ),
    "Speed Booster": lambda loadout: (
        (command in loadout) and
        (SpeedBooster in loadout) and
        (energy400 in loadout)
    ),
    "Springball": lambda loadout: (
        (canUsePB in loadout) and
        (
            ( #from below tube
                (GravitySuit in loadout) or
                (Ice in loadout) or
                (Super in loadout)
            ) or
            ( #through botwoon *barf
                (btAtrium in loadout) and
                (super15 in loadout) and
                (energy300 in loadout) and
                (Grapple in loadout)   
            )
        )
    ),
    "Gravity Suit": lambda loadout: (
        (gt in loadout) and
        (Varia in loadout) and
        (Springball in loadout) and
        (
            (super15 in loadout) or
            (Charge in loadout)
        )
    ),
    "Wave Beam": lambda loadout: (
        (ln in loadout) and
        (energy300 in loadout) and
        ( # exit
            (Wave in loadout) or # wave entry
            ( #acid entry
                (GravitySuit in loadout) or
                (SpaceJump in loadout)
            )
        )
        #same as wave beam energy
    ),
    "First Energy Tank": lambda loadout: (
        (tetraRuins in loadout)
    ),
    "Bomb Torizo Atrium Missile": lambda loadout: (
        (btAtrium in loadout)
    ),
    "Bomb Torizo Atrium Energy Tank": lambda loadout: (
        (btAtrium in loadout)
    ),
    "Bomb Torizo Alcoon Missile": lambda loadout: (
        (btAtrium in loadout)
    ),
    "Varia Hidden Missile": lambda loadout: (
        (canUseBombs in loadout)
    ),
    "Parlor West Missile": lambda loadout: (
        (canBreakBlocks in loadout) or
        (SpeedBooster in loadout)
    ),
    "HiJump": lambda loadout: (
        (canUsePB in loadout)
    ),
    "Parlor West Energy Tank": lambda loadout: (
        (pinkDoor in loadout) and
        (canUsePB in loadout)
    ),
    "Parlor West Ceiling Pair Hidden Missile": lambda loadout: (
        (Morph in loadout) and #needs morph
        (pinkDoor in loadout) and
        (
            (canFly in loadout) or
            (SpeedBooster in loadout)
        )
    ),
    "Parlor West Ceiling Pair Open Missile": lambda loadout: (
        (parlor in loadout) and #matches, but doesn't need morph
        (pinkDoor in loadout) and
        (
            (canFly in loadout) or
            (SpeedBooster in loadout)
        )
    ),
    "Parlor Basement Ceiling Missile": lambda loadout: (
        (lowerOcean in loadout)
    ),
    "Old Mother Brain Missile": lambda loadout: (
        (lowerOcean in loadout)
    ),
    "Tetra Billy Mays Missile": lambda loadout: (
        (tetraRuins in loadout) and
        (pinkDoor in loadout)
    ),
    "Tetra Billy Mays Hidden Missile": lambda loadout: (
        (tetraRuins in loadout) and
        (pinkDoor in loadout)
    ),
    "Tetra Reserve Tank": lambda loadout: (
        #same as Tetra Reserve Chozo plus Supers
        (Super in loadout) and
        (tetraRuins in loadout) and
        (
            (pinkDoor in loadout) or
            (btAtrium in loadout)
        ) and
        (
            (canFly in loadout) or
            (
                (SpeedBooster in loadout) and
                (energy200 in loadout)
            )
        )
    ),
    "Tetra Reserve Super Missile": lambda loadout: (
        #same as Tetra Reserve Chozo plus Supers
        (Super in loadout) and
        (tetraRuins in loadout) and
        (
            (pinkDoor in loadout) or
            (btAtrium in loadout)
        ) and
        (
            (canFly in loadout) or
            (
                (SpeedBooster in loadout) and
                (energy200 in loadout)
            )
        )
    ),
    "Tetra Reserve Chozo Missile": lambda loadout: (
        (tetraRuins in loadout) and
        (
            (pinkDoor in loadout) or
            (btAtrium in loadout)
        ) and
        (
            (canFly in loadout) or
            (
                (SpeedBooster in loadout) and
                (energy200 in loadout)
            )
        )
    ),
    "Xray": lambda loadout: (
        (canUsePB in loadout) and
        (btAtrium in loadout) and
        (
            (canFly in loadout) or
            (Springball in loadout) or
            (SpeedBooster in loadout) or
            (HiJump in loadout)
        )
    ),
    "Retro Blue Hidden Power Bomb": lambda loadout: (
        (gardensWest in loadout) and
        (canUsePB in loadout)
    ),
    "Retro Blue Chozo Missile": lambda loadout: (
        (gardensWest in loadout) and
        (Morph in loadout)
    ),
    "Retro Blue Ceiling Energy Tank": lambda loadout: (
        (gardensWest in loadout) and
        (canUsePB in loadout)
    ),
    "Retro Blue Power Bomb": lambda loadout: (
        (pinkDoor in loadout) and
        (canUsePB in loadout) and
        (
            (Grapple in loadout) or
            (gardensWest in loadout)
        )
    ),
    "Retro Blue Hoppers Super Missile": lambda loadout: (
        (gardensWest in loadout) and
        (Morph in loadout) and
        (energy200 in loadout)
    ),
    "Eternal Hall Entry Gate Missile": lambda loadout: (
        (eternalHall in loadout)
    ),
    "Crater Energy Tank": lambda loadout: (
        (canBreakBlocks in loadout) and
        (Morph in loadout) and
        (
            (canFly in loadout) or
            (SpeedBooster in loadout)
            #maybe other ways
        )
    ),
    "Ocean Energy Tank": lambda loadout: (
        (pinkDoor in loadout) and
        (canUseBombs in loadout) and
        (SpeedBooster in loadout)
    ),
    "Tetra Speedlocked Energy Tank": lambda loadout: (
        (tetraRuins in loadout) and
        (
            (pinkDoor in loadout) or
            (btAtrium in loadout)
        ) and
        (SpeedBooster in loadout) and
        (morphHop in loadout)
    ),
    "Tetra Mask Missile": lambda loadout: (
        (tetraRuins in loadout)
    ),
    "Screw Attack": lambda loadout: (
        ( #get there
            (command in loadout) or
            # maybe update to sky elevator etc
            (
                (pinkDoor in loadout) and
                (canUseBombs in loadout) and
                (
                    (SpeedBooster in loadout) or
                    (Plasma in loadout)
                ) and
                (
                    (SpeedBooster in loadout) or
                    (
                        (Wave in loadout) and
                        (canUsePB in loadout) and
                        (canFly in loadout)
                    )
                )
            )
        ) and
        (
            (canIBJ in loadout) or
            (Springball in loadout)
        )
        # copied from Screw Reserve
    ),
    "High Command Left Side Super Missile": lambda loadout: (
        (command in loadout) and
        (
            (canFly in loadout) or
            (SpeedBooster in loadout) or
            (
                (GravitySuit in loadout) and
                (HiJump in loadout) #maybe
            )
        )
    ),
    "Robot Missile": lambda loadout: (
        (command in loadout)
    ),
    "High Command Evir Super Missile": lambda loadout: (
        (command in loadout) and
        (
            (Plasma in loadout) or
            (Screw in loadout)
        ) #more movement?
    ),
    "Plasma Beam": lambda loadout: (
        (command in loadout) and
        (
            (Plasma in loadout) or
            (Screw in loadout)
        ) and
        (canUsePB in loadout)
    ),
    "Eternal Pothole Missile": lambda loadout: (
        (upperEternal in loadout)
    ),
    "Eternal Easy Wall Missile": lambda loadout: (
        (eternalHall in loadout) and
        (Morph in loadout)
    ),
    "Eternal Top Floor Energy Tank": lambda loadout: (
        (upperEternal in loadout) and
        (canUsePB in loadout) and
        (energy600 in loadout)
    ),
    "Bubble Mountain Summit Missile": lambda loadout: (
        (upperEternal in loadout) and
        (Morph in loadout)
    ),
    "Ceres Dentist Super Missile": lambda loadout: (
        (kraid in loadout) and
        (energy400 in loadout)
    ),
    "Kraid Eye Power Bomb": lambda loadout: (
        (kraid in loadout) and
        (
            (canIBJ in loadout) or
            (Springball in loadout)
        )
    ),
    "BT Flyway Missile": lambda loadout: (
        (tetraRuins in loadout) and
        (
            (
                (canIBJ in loadout) and
                (canUsePB in loadout)
            ) or
            (SpeedBooster in loadout) or
            (
                (canBreakBlocks in loadout) and
                (
                    (HiJump in loadout) or
                    (Springball in loadout) or
                    (SpaceJump in loadout)
                )
            ) or
            (
                (canUseBombs in loadout) and
                (pinkDoor in loadout)
            )
        )
            #related to btAtrium but might not need canUseBombs
    ),
    "West Parlor Pink Super Missile": lambda loadout: (
        (canUseBombs in loadout) and
        (Super in loadout)
    ),
    "Grapple Energy Tank": lambda loadout: (
        (lowerOcean in loadout) and
        (hellrun2 in loadout) and #heyyyy
        (Grapple in loadout)
        #mostly copied from grapple
    ),
    "Green Cavern Super Missile": lambda loadout: (
        (gardensWest in loadout) and
        (
            (canFly in loadout) or
            (SpeedBooster in loadout)
        )
    ),
    "Crocomire Energy Tank": lambda loadout: (
        (croc in loadout)
    ),
    "Ice Beam": lambda loadout: (
        (croc in loadout)
    ),
    "Cathedral Reserve Tank": lambda loadout: (
        (canUsePB in loadout) and
        (pinkDoor in loadout) and
        (
            (Grapple in loadout) or
            (Super in loadout) 
        )
    ),
    "Underworld Cavern Maze Inside Missile": lambda loadout: (
        (underworldCentral in loadout) and
        (canFly in loadout) and #probably
        (
            (canIBJ in loadout) or
            (Springball in loadout)
        )

    ),
    "Underworld Cavern Maze Top Missile": lambda loadout: (
        (underworldCentral in loadout) and
        (canFly in loadout) and #probably
        (
            (canIBJ in loadout) or
            (Springball in loadout)
        )
    ),
    "Gravity Super Missile": lambda loadout: (
        (gt in loadout) and
        (Varia in loadout) and
        (Springball in loadout) and
        (
            (super15 in loadout) or
            (Charge in loadout)
        )
    ),
    "Plasma Pirates Energy Tank": lambda loadout: (
        (gt in loadout) and
        (canUsePB in loadout) and
        (Super in loadout) and
        (Plasma in loadout)
    ),
    "Bomb Torizo Attic Super Missile": lambda loadout: (
        (btAtrium in loadout) and
        (Super in loadout) and
        (
            (canFly in loadout) or
            (SpeedBooster in loadout)
        )
    ),
    "Screw Reserve Tank": lambda loadout: (
        ( #get there
            (command in loadout) or
            (
                (pinkDoor in loadout) and
                (canUseBombs in loadout) and
                (
                    (SpeedBooster in loadout) or
                    (Plasma in loadout)
                ) and
                (
                    (SpeedBooster in loadout) or
                    (
                        (Wave in loadout) and
                        (canUsePB in loadout) and
                        (canFly in loadout)
                    )
                )
            )
        ) and
        (
            (canIBJ in loadout) or
            (Springball in loadout)
        )
    ),
    "Sky Metroids West Missile": lambda loadout: (
        (sky in loadout)
    ),
    "Sky Top Hoppers Power Bomb": lambda loadout: (
        (sky in loadout)
    ),
    "Sky Kihunter Spark Super Missile": lambda loadout: (
        (sky in loadout) and
        (SpeedBooster in loadout)
    ),
    "Space Jump Power Bomb": lambda loadout: (
        (draygon in loadout)
    ),
    "Space Jump Super Missile": lambda loadout: (
        (draygon in loadout)
    ),
    "Space Jump": lambda loadout: (
        (draygon in loadout)
    ),
    "Grapple Puzzle Reserve Tank": lambda loadout: (
        (sky in loadout) and
        (canUsePB in loadout) and
        (SpaceJump in loadout) and
        (Super in loadout)
    ),
    "Grapple Puzzle Power Bomb": lambda loadout: (
        (sky in loadout) and
        (canUsePB in loadout) and
        (SpaceJump in loadout)
    ),
    "Spazer": lambda loadout: (
        (command in loadout) and
        (SpeedBooster in loadout) and
        (
            (Grapple in loadout) or
            (energy200 in loadout)
        )
    ),
    "LN Phony Chozo Energy Tank": lambda loadout: (
        (ln in loadout)
    ),
    "LN Crescent Missile": lambda loadout: (
        (Varia in loadout) and
        ( #from ocean
            (
                (canUsePB in loadout) and
                (pinkDoor in loadout)
            ) or
            (
                (underworldCentral in loadout) and
                (energy300 in loadout)
            )
        )
    ),
    "Wave Beam Energy Tank": lambda loadout: (
        (ln in loadout) and
        ( # exit
            (Wave in loadout) or # wave entry
            ( #acid entry
                (GravitySuit in loadout) or
                (SpaceJump in loadout)
            )
        )

    ),
    "Sky East Green Stairs Super Missile": lambda loadout: (
        (sky in loadout) and
        (canUsePB in loadout) and
        (Super in loadout) and
        (SpaceJump in loadout) and
        (HiJump in loadout)
    ),
    "Sky Low Metroids Power Bomb": lambda loadout: (
        (sky in loadout) and
        (canUsePB in loadout) and
        (SpaceJump in loadout) and
        (HiJump in loadout) and
        (Super in loadout)
    ),
    "Business Center B1 Power Bomb": lambda loadout: (
        (canUsePB in loadout) and
        (pinkDoor in loadout) and
        (energy300 in loadout) and
        (
            (Grapple in loadout) or
            (Super in loadout) 
        ) #copied from cathedral
    ),
    "Business Center B2 Missile": lambda loadout: (
        (businessCenter in loadout)
    ),
    "Business Center B3 Hidden Missile": lambda loadout: (
        (businessCenter in loadout) and
        (Super in loadout)
    ),
    "Business Center B3 Super Missile": lambda loadout: (
        (businessCenter in loadout) and
        (Super in loadout) and
        (
            (canFly in loadout) or
            (canUsePB in loadout)
        )
    ),
    "Business Center B3 Missile": lambda loadout: (
        (businessCenter in loadout) and
        (Super in loadout) and
        (
            (canFly in loadout) or
            (canUsePB in loadout)
        )
    ),
    "Underworld Vertigo Super Missile": lambda loadout: (
        #simple version
        (
            (businessCenter in loadout) and
            (Varia in loadout) and
            (SpaceJump in loadout) and
            (canUseBombs in loadout)
        ) or
        (
            (underworldCentral in loadout) and
            (canUsePB in loadout)
        )
    ),
    "Business Center B5 Super Missile": lambda loadout: (
        (
            (businessCenter in loadout) and
            (Super in loadout)
        ) or
        (
            (underworldCentral in loadout) and 
            (pinkDoor in loadout) and
            (Grapple in loadout) and
            (energy300 in loadout) and
            (canUseBombs in loadout)
        ) # copied from B5 Lower
    ),
    "Eternal Desgeega Missile": lambda loadout: (
        (upperEternal in loadout)
    ),
    "Underworld Orb Hangout Power Bomb": lambda loadout: (
        (pinkDoor in loadout) and
        (canUsePB in loadout) and
        (
            (Grapple in loadout) or
            (Super in loadout)
        ) # this is copied from underworld central, no varia, needs PB
    ),
    "Underworld Donut Hole Missile": lambda loadout: (
        (underworldCentral in loadout)
    ),
    "Underworld Donut Top Right Power Bomb": lambda loadout: (
        (underworldCentral in loadout) and
        (canUsePB in loadout)
    ),
    "Gravity Kihunters Power Bomb": lambda loadout: (
        (gt in loadout) and
        (Varia in loadout) and
        (Springball in loadout) and
        (
            (super15 in loadout) or
            (Charge in loadout)
        )
    ),
    "Eternal Power Pit Power Bomb": lambda loadout: (
        (eternalHall in loadout) and
        (canUsePB in loadout)
    ),
    "Shiny Acid Energy Tank": lambda loadout: (
        (energy500 in loadout) and
        (
            (
                (upperEternal in loadout) and
                (canUsePB in loadout)
            ) or
            (
                (canUsePB in loadout) and
                (Super in loadout)
            )
        )
    ),
    "Business Center B5 Lower Missile": lambda loadout: (
        (
            (businessCenter in loadout) and
            (Super in loadout)
        ) or
        (
            (underworldCentral in loadout) and 
            (pinkDoor in loadout) and
            (Grapple in loadout) and
            (energy300 in loadout) and
            (canUseBombs in loadout)
        ) #borrowed from business center, super-less route

    ),
    "Coliseum Super Missile": lambda loadout: (
        (tetraRuins in loadout) and
        (Super in loadout) and
        (   #and survive
            (Grapple in loadout) or
            (SpaceJump in loadout) or
            (energy500 in loadout)
        )
    ),
    "Wave Acid Escape Missile": lambda loadout: (
        (ln in loadout) and
        (energy300 in loadout) and
        ( # exit
            (Wave in loadout) or # wave entry
            ( #acid entry
                (GravitySuit in loadout) or
                (SpaceJump in loadout)
            )
        )
        #same as wave beam energy
    ),
    "Wave Chambers Power Bomb": lambda loadout: (
        (ln in loadout)
    ),
    "Wave Desgeega Vault Super Missile": lambda loadout: (
        (ln in loadout) and
        (
            (canFly in loadout) or
            (SpeedBooster in loadout)
        )
    ),
    "Climb Missile": lambda loadout: (
        (Morph in loadout) and
        (pinkDoor in loadout) and
        (
            ( #traditional
                (canUseBombs in loadout) and
                (canFly in loadout)
            ) or
            ( #moat
                (GravitySuit in loadout) or
                (
                    (HiJump in loadout) and
                    (Springball in loadout) #can be more precise
                )
            )
        )
    ),
    "High Command East Closet Missile": lambda loadout: (
        (command in loadout) and
        (canUsePB in loadout)
    ),
    "High Command East Vault Missile": lambda loadout: (
        (command in loadout) # doesn't need phantoon though
    ),
    "Eternal Ripper Basement Power Bomb": lambda loadout: (
        (eternalHall in loadout) and
        (Super in loadout) and
        (canUsePB in loadout)
    ),

}


class Expert(LogicInterface):
    area_logic: ClassVar[AreaLogicType] = area_logic
    location_logic: ClassVar[LocationLogicType] = location_logic

    @staticmethod
    def can_fall_from_spaceport(loadout: Loadout) -> bool:
        return True
