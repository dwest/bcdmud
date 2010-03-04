from sqlobject import *

class Player(SQLObject):
    """Player stats and other useful player info"""

    #SQL stored fields
    name = StringCol()
    level = IntCol()
    class = ForeignKey('Class')
    race = ForeignKey('Race')
    
    strength = IntCol()
    stamina = IntCol()
    intellect = IntCol()
    wisdom = IntCol()
    luck = IntCol()
    alignment = ForeignKey('Alignment')
    affinity = ForeignKey('Affinity')
    deity = ForeignKey('Deity')
    
    #Spells known by the player
    spells = MultipleJoin('KnownSpell')

    #Any non-magic ability known by the player
    abilities = MultipleJoin('KnownAbility')

    #water-walking, infravision, etc.
    passiveSkills = MultipleJoin('PassiveSkill')

    #transformation, blindness, curses, wereform, etc.
    status = MultipleJoin('Status')

    location = ForeignKey('PlayerLocation')
    inventory = ForeignKey('PlayerInventory')
    equipment = ForeignKey('PlayerEquipment')
    
