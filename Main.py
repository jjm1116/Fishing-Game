import random
import time

class Fish:
    def __init__(self, name, price, catch_chance, category):
        self.name = name
        self.price = price
        self.base_price = price
        self.catch_chance = catch_chance  # Probability of catching this fish (0-1 scale)
        self.category = category  # Category of the fish (e.g., Common, Rare, etc.)
        self.weight = round(random.uniform(1, 20), 2)  # Randomized weight in kilograms
        self.price = self.base_price  # Final price after applying mutation

    def apply_mutation(self, mutation_name, multiplier):
        """Apply a mutation to this fish, modifying its price."""
        self.mutation = mutation_name
        self.price = round(self.base_price * multiplier, 2)

    def clone(self):
        """Create a copy of the fish to apply mutations without affecting the original."""
        return Fish(self.name, self.base_price, self.catch_chance, self.category)

    def __str__(self):
        mutation_info = f" ({self.mutation})" if self.mutation else ""
        return (f"{self.name}{mutation_info} (Worth: ${self.price}, Weight: {self.weight}kg, "
                f"Category: {self.category}, Catch Chance: {self.catch_chance * 100}%)")

class Rod:
    def __init__(self, name, cost, catch_rate):
        self.name = name
        self.cost = cost
        self.catch_rate = catch_rate  # Probability of catching a fish (0-1 scale)

    def __str__(self):
        return f"{self.name} (Cost: ${self.cost}, Catch Rate: {self.catch_rate * 100}%)"

class FishingGame:
    def __init__(self):
        self.fish_types = [
            Fish("Seaweed", 16, 0.2, "Trash"),
            Fish("Destroyed Fossil", 17, 0.2, "Trash"),
            Fish("Bone", 16, 0.2, "Trash"),
            Fish("Boot", 17, 0.2, "Trash"),
            Fish("Log", 18, 0.2, "Trash"),
            Fish("Rock", 10, 0.2, "Trash"),
            Fish("Driftwood", 12, 0.25, "Trash"),
            Fish("Stalactite", 20, 0.25, "Trash"),
            Fish("Scrap Metal", 15, 0.2, "Trash"),
            Fish("Ice", 16, 0.02, "Trash"),
            Fish("Tire", 20, 0.2, "Trash"),
            Fish("Basalt", 15, 0.25, "Trash"),
            Fish("Fungal Cluster", 15, 0.25, "Trash"),
            Fish("Sand Dollar", 30, 0.1, "Common"),
            Fish("Sea Bass", 30, 0.1, "Common"),
            Fish("Trout", 30, 0.1, "Common"),
            Fish("Largemouth Bass", 30, 0.1, "Common"),
            Fish("Pollock", 30, 0.1, "Common"),
            Fish("Porgy", 30, 0.1, "Common"),
            Fish("Mackerel", 30, 0.1, "Common"),
            Fish("Minnow", 30, 0.1, "Common"),
            Fish("Horseshoe crab", 30, 0.1, "Common"),
            Fish("Gudgeon ", 30, 0.1, "Common"),
            Fish("Grayling", 30, 0.1, "Common"),
            Fish("Sardine", 30, 0.1, "Common"),
            Fish("Mullet", 30, 0.1, "Common"),
            Fish("Smallmouth Bass", 30, 0.15, "Common"),
            Fish("Swamp Bass", 30, 0.15, "Common"),
            Fish("Mussel", 30, 0.25, "Common"),
            Fish("Spiderfish", 30, 0.15, "Common"),
            Fish("Cladoselache", 30, 0.15, "Common"),
            Fish("Piranha", 30, 0.15, "Common"),
            Fish("Deep-Sea Dragonfish", 30, 0.15, "Common"),
            Fish("Slate Tuna", 30, 0.15, "Common"),
            Fish("Sweetfish", 30, 0.15, "Common"),
            Fish("Night Shrimp", 30, 0.15, "Common"),
            Fish("Shortfin Make Shark", 30, 0.15, "Common"),
            Fish("Bream", 30, 0.1, "Common"),
            Fish("Chub", 30, 0.2, "Common"),
            Fish("Bluegill", 30, 0.1, "Common"),
            Fish("Sockeye salmon", 30, 0.15, "Common"),
            Fish("Pearl", 30, 0.1, "Common"),
            Fish("Glassfish", 30, 0.1, "Common"),
            Fish("Deep-sea Hatchetfish", 30, 0.23, "Common"),
            Fish("Perch", 30, 0.15, "Common"),
            Fish("Herring", 30, 0.15, "Common"),
            Fish("Shrimp", 30, 0.2, "Common"),
            Fish("Red Drum", 30, 0.15, "Common"),
            Fish("White Perch", 30, 0.15, "Common"),
            Fish("Anchovy", 30, 0.2, "Common"),
            Fish("Red Snapper", 30, 0.15, "Common"),
            Fish("Gazerfish", 30, 0.15, "Common"),
            Fish("Corsair Grouper", 30, 0.1, "Common"),
            Fish("Walleye", 75, 0.1, "Uncommon"),
            Fish("Arctic Char", 75, 0.1, "Uncommon"),
            Fish("Starfish", 75, 0.1, "Uncommon"),
            Fish("Galleon Goliath", 75, 0.1, "Uncommon"),
            Fish("Onychodos", 75, 0.1, "Uncommon"),
            Fish("Buccanner Barracuda", 75, 0.1, "Uncommon"),
            Fish("Crab", 75, 0.1, "Uncommon"),
            Fish("Prawn", 75, 0.1, "Uncommon"),
            Fish("Salmon", 75, 0.1, "Uncommon"),
            Fish("Magma Tang", 75, 0.1, "Uncommon"),
            Fish("Carp", 75, 0.1, "Uncommon"),
            Fish("Burbot", 75, 0.1, "Uncommon"),
            Fish("Fish Barrel", 75, 0.1, "Uncommon"),
            Fish("Coral Geode", 75, 0.1, "Uncommon"),
            Fish("Amberjack", 75, 0.1, "Uncommon"),
            Fish("Yellowfin Tuna", 75, 0.1, "Uncommon"),
            Fish("Oyster", 75, 0.1, "Uncommon"),
            Fish("Common Crate", 75, 0.1, "Uncommon"),
            Fish("Brine Shrimp", 75, 0.1, "Uncommon"),
            Fish("Chinfish", 75, 0.1, "Uncommon"),
            Fish("Pumpkinseed", 75, 0.1, "Uncommon"),
            Fish("Barracuda", 75, 0.1, "Uncommon"),
            Fish("Goldfish", 75, 0.1, "Uncommon"),
            Fish("Phantom Ray", 75, 0.1, "Uncommon"),
            Fish("Butterfly Fish", 75, 0.1, "Uncommon"),
            Fish("Scallop", 75, 0.1, "Uncommon"),
            Fish("Grey Carp", 75, 0.1, "Uncommon"),
            Fish("Pale Tang", 75, 0.1, "Uncommon"),
            Fish("White Bass", 75, 0.1, "Uncommon"),
            Fish("Bait Crate", 75, 0.1, "Uncommon"),
            Fish("Longtail Bass", 75, 0.1, "Uncommon"),
            Fish("Blackfish", 75, 0.1, "Uncommon"),
            Fish("Anomalocaris", 75, 0.1, "Uncommon"),
            Fish("Blue Tang", 75, 0.1, "Uncommon"),
            Fish("Clownfish", 75, 0.1, "Uncommon"),
            Fish("Cod", 75, 0.1, "Uncommon"),
            Fish("Red Tang", 75, 0.1, "Uncommon"),
            Fish("Bowfin", 75, 0.1, "Uncommon"),
            Fish("Tempest Ray", 75, 0.1, "Uncommon"),
            Fish("Abyss Snapper", 75, 0.1, "Uncommon"),
            Fish("Lingcod", 200, 0.08, "Unusual"),
            Fish("Lobster ", 200, 0.08, "Unusual"),
            Fish("Gilded Pearl", 200, 0.08, "Unusual"),
            Fish("Cockatoo Squid", 200, 0.08, "Unusual"),
            Fish("Palaeoniscus", 200, 0.08, "Unusual"),
            Fish("Skipjack Tuna", 200, 0.08, "Unusual"),
            Fish("Three-eyed Fish", 200, 0.08, "Unusual"),
            Fish("Snook", 200, 0.08, "Unusual"),
            Fish("Redeye bass", 200, 0.08, "Unusual"),
            Fish("Hyneria", 200, 0.08, "Unusual"),
            Fish("Flounder", 200, 0.08, "Unusual"),
            Fish("Xiphactinus", 200, 0.08, "Unusual"),
            Fish("Scurvy Sailfish", 200, 0.08, "Unusual"),
            Fish("Angelfish", 200, 0.08, "Unusual"),
            Fish("Bluefish", 200, 0.08, "Unusual"),
            Fish("Trumpetfish", 200, 0.08, "Unusual"),
            Fish("Globbe Jellyfish", 200, 0.08, "Unusual"),
            Fish("Acanthodii", 200, 0.08, "Unusual"),
            Fish("Eel", 200, 0.08, "Unusual"),
            Fish("Depths Octopus ", 200, 0.08, "Unusual"),
            Fish("Ribbon Eel ", 200, 0.08, "Unusual"),
            Fish("Clam", 200, 0.08, "Unusual"),
            Fish("Birgeria", 200, 0.08, "Unusual"),
            Fish("Frilled Shark ", 200, 0.08, "Unusual"),
            Fish("Rockstar Hermit Crab", 200, 0.08, "Unusual"),
            Fish("Swamp Scallop", 200, 0.08, "Unusual"),
            Fish("Luminescent Minnow ", 200, 0.08, "Unusual"),
            Fish("Ember Snapper", 200, 0.08, "Unusual"),
            Fish("Chinook Salmon", 200, 0.08, "Unusual"),
            Fish("Fangborn Gar", 200, 0.08, "Unusual"),
            Fish("Ember Perch", 200, 0.08, "Unusual"),
            Fish("Cutlass fish", 200, 0.08, "Unusual"),
            Fish("Glacier  Pike", 200, 0.08, "Unusual"),
            Fish("Pike", 200, 0.08, "Unusual"),
            Fish("Rose Pearl", 200, 0.08, "Unusual"),
            Fish("Yellow Boxfish", 200, 0.08, "Unusual"),
            Fish("Squid ", 200, 0.08, "Unusual"),
            Fish("Nurse Shark", 200, 0.08, "Unusual"),
            Fish("Hollyscale Trout", 200, 0.08, "Unusual"),
            Fish("Crystal Carp", 200, 0.08, "Unusual"),
            Fish("Vortex Barracuda", 200, 0.08, "Unusual"),
            Fish("Whirlpool Marlin", 200, 0.08, "Unusual"),
            Fish("Napoleon Fish", 500, 0.07, "Rare"),
            Fish("Sturgeon", 500, 0.07, "Rare"),
            Fish("Swordfish", 500, 0.07, "Rare"),
            Fish("Hallucigenia", 500, 0.07, "Rare"),
            Fish("Bluefin Tuna", 500, 0.07, "Rare"),
            Fish("Stingray", 500, 0.07, "Rare"),
            Fish("Phanerorhynchus", 400, 0.07, "Rare"),
            Fish("Goblin Shark", 700, 0.05, "Rare"),
            Fish("Abyssacuda", 500, 0.07, "Rare"),
            Fish("Spider Crab", 500, 0.07, "Rare"),
            Fish("Cobia", 500, 0.07, "Rare"),
            Fish("Catfish", 500, 0.07, "Rare"),
            Fish("Cursed Eel", 500, 0.07, "Rare"),
            Fish("Lapisjack", 500, 0.07, "Rare"),
            Fish("Alligator Gar", 500, 0.07, "Rare"),
            Fish("Mauve Pearl", 500, 0.07, "Rare"),
            Fish("Black Dragon Fish", 400, 0.07, "Rare"),
            Fish("Pyrogrub", 500, 0.07, "Rare"),
            Fish("Mushgrove Crab", 500, 0.07, "Rare"),
            Fish("Carbon Crate", 300, 0.08, "Rare"),
            Fish("Voidfin Mahi", 500, 0.07, "Rare"),
            Fish("King Oyster", 500, 0.07, "Rare"),
            Fish("Mahi Mahi", 500, 0.07, "Rare"),
            Fish("Sea Urchin", 500, 0.07, "Rare"),
            Fish("Pufferfish", 500, 0.07, "Rare"),
            Fish("Banditfish", 500, 0.07, "Rare"),
            Fish("Suckermouth Catfish", 150, 0.09, "Rare"),
            Fish("Volcanic Geode", 400, 0.07, "Rare"),
            Fish("Arapaima", 400, 0.07, "Rare"),
            Fish("Cookiecutter Shark ", 500, 0.07, "Rare"),
            Fish("Sailfish", 500, 0.07, "Rare"),
            Fish("Anglerfish", 400, 0.07, "Rare"),
            Fish("Halibut", 500, 0.07, "Rare"),
            Fish("Coelacanth", 400, 0.07, "Rare"),
            Fish("Reefrunner Snapper", 500, 0.07, "Rare"),
            Fish("Quality Bait Crate", 600, 0.07, "Rare"),
            Fish("Marsh Gar", 500, 0.07, "Rare"),
            Fish("Dweller Catfish", 550, 0.07, "Rare"),
            Fish("Keeper's Guardian", 500, 0.07, "Rare"),
            Fish("Small Spine Chimera", 3000, 0.05, "Legendary"),
            Fish("Midnight  Axolotl", 1000, 0.05, "Legendary"),
            Fish("Rabbitfish", 700, 0.05, "Legendary"),
            Fish("Brine Phantom", 3000, 0.05, "Legendary"),
            Fish("Leedsichthys", 3000, 0.05, "Legendary"),
            Fish("Moon Wood", 3000, 0.05, "Legendary"),
            Fish("Void Wood", 3000, 0.05, "Legendary"),
            Fish("Polar Alligator", 3000, 0.05, "Legendary"),
            Fish("Golden Smallmouth Bass", 3000, 0.05, "Legendary"),
            Fish("Diplurus", 3000, 0.05, "Legendary"),
            Fish("Ancient Wood", 3000, 0.05, "Legendary"),
            Fish("Deep Pearl", 3000, 0.05, "Legendary"),
            Fish("Flying Fish", 3000, 0.05, "Legendary"),
            Fish("Sawfish", 3000, 0.05, "Legendary"),
            Fish("Axolotl", 3000, 0.05, "Legendary"),
            Fish("Umbral Shark", 3800, 0.05, "Legendary"),
            Fish("Nautilus", 3000, 0.05, "Legendary"),
            Fish("Crown Bass", 3000, 0.05, "Legendary"),
            Fish("Ginsu Shark", 3000, 0.05, "Legendary"),
            Fish("Shipwreck Barracuda", 3000, 0.05, "Legendary"),
            Fish("Barbed Shark", 3000, 0.05, "Legendary"),
            Fish("Frostjaw Cod", 3000, 0.05, "Legendary"),
            Fish("Wiifish", 3000, 0.05, "Legendary"),
            Fish("Dunkleosteus", 3000, 0.05, "Legendary"),
            Fish("Dolphin", 3000, 0.05, "Legendary"),
            Fish("Olm", 3000, 0.05, "Legendary"),
            Fish("Sun fish", 3000, 0.05, "Legendary"),
            Fish("Pond Emperor", 1670, 0.05, "Legendary"),
            Fish("Obsidian Salmon", 3000, 0.05, "Legendary"),
            Fish("Dumbo Octopus", 1500, 0.05, "Legendary"),
            Fish("Moonfish", 2000, 0.05, "Legendary"),
            Fish("Bull Shark", 3500, 0.04, "Legendary"),
            Fish("Alligator", 3270, 0.045, "Legendary"),
            Fish("Borealis Snapper", 3000, 0.05, "Legendary"),
            Fish("Frigit Antlers", 3000, 0.05, "Legendary"),
            Fish("Whiptail Catfish", 3000, 0.05, "Legendary"),
            Fish("Rubber Ducky", 3000, 0.05, "Legendary"),
            Fish("Floppy", 3000, 0.05, "Legendary"),
            Fish("Ancient Eel", 3000, 0.05, "Legendary"),
            Fish("Frozen Fangfish", 3000, 0.05, "Legendary"),
            Fish("Coral Emperor", 3300, 0.04, "Legendary"),
            Fish("Captain's Goldfish", 5000, 0.03, "Mythical"),
            Fish("Oarfish", 5000, 0.03, "Mythical"),
            Fish("Meg's Fang", 5000, 0.05, "Mythical"),
            Fish("Helicoprion", 5000, 0.02, "Mythical"),
            Fish("Spectral Serpent", 5000, 0.03, "Mythical"),
            Fish("Mutated Shark", 5000, 0.04, "Mythical"),
            Fish("Amblypterus", 5000, 0.03, "Mythical"),
            Fish("Mosasaurus", 5000, 0.04, "Mythical"),
            Fish("Sea Snake", 4500, 0.06, "Mythical"),
            Fish("Golden Seahorse", 5000, 0.04, "Mythical"),
            Fish("Mythic Fish", 5000, 0.07, "Mythical"),
            Fish("Whisker Bill", 5000, 0.04, "Mythical"),
            Fish("Emperor Jellyfish", 5000, 0.03, "Mythical"),
            Fish("Meg's Spine", 5000, 0.5, "Mythical"),
            Fish("Sea Turtle", 5000, 0.03, "Mythical"),
            Fish("Barreleye Fish", 5000, 0.01, "Mythical"),
            Fish("Isonade", 5000, 0.02, "Mythical"),
            Fish("Voltfish", 5000, 0.06, "Mythical"),
            Fish("Aurora Pearl", 5000, 0.04, "Mythical"),
            Fish("Obsidian Swordfish", 5000, 0.05, "Mythical"),
            Fish("Ringle", 5000, 0.007, "Mythical"),
            Fish("Sea Mine", 5000, 0.01, "Mythical"),
            Fish("Manta Ray", 5000, 0.00, "Mythical"),
            Fish("Whale Shark", 5000, 0.001, "Mythical"),
            Fish("Sea Pickle", 5000, 0.001, "Mythical"),
            Fish("Great Hammerhead Shark", 5000, 0.001, "Mythical"),
            Fish("Great White Shark", 5000, 0.001, "Mythical"),
            Fish("Inferno Wood", 5000, 0.001, "Mythical"),
            Fish("Colossal Squid", 5000, 0.001, "Mythical"),
            Fish("Handfish", 5000, 0.001, "Mythical"),
            Fish("Glacierfish", 5000, 0.001, "Mythical"),
            Fish("Lepidotes", 5000, 0.001, "Mythical"),
            Fish("Glacier Glowfish", 5000, 0.001, "Mythical"),
            Fish("Void Angler", 5000, 0.001, "Mythical"),
            Fish("Megaladon", 20000, 0.08, "Exotic"),
            Fish("Ancient Megaladon", 40000, 0.01, "Exotic"),
            Fish("Phantom Megaladon", 50000, 0.009, "Exotic"),
            Fish("Ancient Depth Serpent", 15000, 0.075, "Exotic"),
            Fish("Molten Banshee", 19000, 0.04, "Exotic"),
            Fish("Golden Sea Pearl", 9000, 0.01, "Exotic"),
            Fish("The Depths Key", 4000, 0.01, "Exotic"),
            Fish("Treble Bass", 9000, 0.0001, "Exotic"),
            Fish("Kraken", 20000, 0.009, "Exotic"),
            Fish("Long Pike", 20000, 0.0002, "Secret"),
            Fish("Banana", 20000, 0.0002, "Secret"),
            Fish("Mustard", 20000, 0.0002, "Secret"),
            Fish("FISCH", 20000, 0.0002, "Secret"),
            Fish("Ancient Kraken", 400000, 0.0002, "Secret"),
            Fish("Lurkerfish", 50000, 0.005, "Limited"),
            Fish("Ghoulfish", 50000, 0.004, "Limited"),
            Fish("Zombiefish", 50000, 0.004, "Limited"),
            Fish("Nessie", 50000, 0.0009, "Limited"),
            Fish("Candy Fish", 50000, 0.00, "Limited"),
            Fish("Skelefish", 50000, 0.006, "Limited"),
            Fish("Turkey", 50000, 0.007, "Limited"),
            Fish("Icicle", 50000, 0.008, "Limited"),
            Fish("Olmdeer", 50000, 0.007, "Limited"),
            Fish("Cookie", 50000, 0.007, "Limited"),
            Fish("Supreme Present", 50000, 0.006, "Limited"),
            Fish("Gingerbread Fish", 50000, 0.008, "Limited"),
            Fish("Ornament Fish", 50000, 0.006, "Limited"),
            Fish("Santa Salmon", 50000, 0.008, "Limited"),
            Fish("Glass Of Milk", 50000, 0.007, "Limited"),
            Fish("Santa Pufferfish", 50000, 0.006, "Limited"),
            Fish("Festive Bait Crate", 50000, 0.008, "Limited"),
            Fish("Basic Present", 50000, 0.008, "Limited"),
            Fish("Northstar Serpent", 50000, 0.005, "Limited"),
            Fish("Unique Present", 50000, 0.0007, "Limited"),
            Fish("Candy Cane Carp", 50000, 0.006, "Limited"),
            Fish("Snowflake Flounder", 50000, 0.007, "Limited"),
            Fish("Eternal FrostWhale", 50000, 0.005, "Limited"),

            
        ]

        self.mutations = {
            " ": 0, 
            "Big": 1.5, "Giant": 2.3, "Shiny": 1.85, "Sparkling": 1.85, "Aurora": 6.5,
            "Aureolin": 5, "Aurulent": 5, "Subspace": 5, "Heavenly": 5, "Mythical": 4.5,
            "Aureate": 4, "Sunken": 4, "Greedy": 4, "Nuclear": 4, "Firework": 3.5,
            "Abyssal": 3.5, "Revitalized": 3.5, "Atlantean": 3, "Aurelian": 3, "Blighted": 3,
            "Sleet": 2.4, "Anomalous": 2.5, "Aurous": 2, "Fossilized": 2.5, "Solarblaze": 2.5,
            "Lunar": 2.5, "Celestial": 2, "Midas": 2, "Purified": 2, "Crystallized": 1.75,
            "Glossy": 1.6, "Silver": 1.6, "Mosaic": 1.5, "Hexed": 1.5, "Electric": 1.45,
            "Scorched": 1.3, "Darkened": 1.3, "Translucent": 1.3, "Frozen": 1.3, "Negative": 1.3,
            "Seasonal": 2.5, "Albino": 1.1, "Amber": 0.5,
        }



        self.rod_types = [
            Rod("Training Rod", 300, 0.2),
            Rod("Plastic Rod", 900, 0.2),
            Rod("Carbon Rod", 2000, 0.3),
            Rod("Long Rod", 4500, 0.4),
            Rod("Fast Rod", 4500, 0.45),
            Rod("Lucky Rod", 5250, 0.5),
            Rod("Steady Rod", 7000, 0.55),
            Rod("Fortune Rod", 12750, 0.4),
            Rod("Rapid Rod", 14000, 0.35),
            Rod("Nocturnal Rod", 11000, 0.4),
            Rod("Aurora Rod", 90000, 0.55),
            Rod("Rod of the Depths", 750000, 0.7),
            Rod("Magnet Rod", 15000, 0.45),
            Rod("King's Rod", 120000, 0.7),
            Rod("Destiny Rod", 190000, 0.82),
            Rod("Midas Rod", 55000, 0.55),
            Rod("Mythical Rod", 110000, 0.57),
            Rod("Reinforced Rod", 20000, 0.3),
            Rod("Trident Rod", 150000, 0.8),
            Rod("Scurvy Rod", 50000, 0.4),
            Rod("Phoenix Rod", 40000, 0.4),
            Rod("Stone Rod", 3000, 0.2),
            Rod("Heaven's Rod", 1750000, 0.8),
            Rod("Summit Rod", 300000, 0.7),
            Rod("Avalanche Rod", 35000, 0.65),
            Rod("Ice Warper's Rod", 65000, 0.55),
            Rod("Crystallized Rod", 35000, 0.5),
            Rod("Arctic Rod", 25000, 0.6),
            Rod("Magma Rod", 9000, 0.4),
            Rod("Fungal Rod", 7000, 0.3),
            Rod("No-Life Rod", 0, 0.85),
            Rod("Sunken Rod", 10000, 0.7),
            Rod("Firework Rod", 15000, 0.5),
            Rod("Rod of the Exalted one", 750000, 0.8),
            Rod("Rod of the Forgotten Fang", 150000, 1),
            Rod("Rod of the Eternal King", 100000, 0.9),
            Rod("Celestial Rod", 70000, 0.85),
            Rod("Riptide Rod", 60000, 0.57),
            Rod("Seasons Rod", 50000, 0.53),
            Rod("Resourceful Rod", 30000, 0.45),
            Rod("Wisdom Rod", 10000, 0.3),
            Rod("Precision Rod", 20000, 0.43),
            Rod("Haunted Rod", 10000, 0.6),
            Rod("Relic Rod", 65000, 0.75),
            Rod("Buddy Bond Rod", 10000, 0.5),
            Rod("Candy Cane Rod", 1500, 0.5),
            Rod("Krampus's Rod", 75000, 0.7),
            Rod("Astral Rod", 1000, 0.3),
            Rod("Event Horizon Rod", 20000, 0.3),
            Rod("Antler Rod", 15000, 0.5),
            Rod("North-Star Rod", 15450, 0.5),
            Rod("Fischer's Rod", 10000, 0.5),
            Rod("Frost Warden's Rod", 15000, 0.5),
            Rod("Fischmas Rod", 25000, 0.7),
            Rod("Frostfire Rod", 50000, 0.7),
            Rod("Seraphic Rod", 0, 500),
            Rod("Soveriegn Doombringer", 100000000, 500),
            Rod("Dev Rod", 100000000, 500),
            Rod("Executive Rod", 100000000, 500),
            Rod("Evil Pitchfork of Devil's Peril", 100000000, 500),
            Rod("Rex Ubranum", 100000000, 500),
        ]

        self.current_rod = self.rod_types[0]
        self.money = 50
        self.inventory = []
        self.fishing_attempts = 0  # Counter to track fishing attempts
        self.bestiary = {fish.name: 0 for fish in self.fish_types}  # Track fish caught

    def display_fish(self):
        print("\nAvailable Fish:")
        for fish in self.fish_types:
            print(f"- {fish}")

    def display_rods(self):
        print("\nAvailable Rods:")
        for rod in self.rod_types:
            print(f"- {rod}")

    def shop_screen(self):
        print("\n--- Fishing Rod Shop ---")
        print("Available Rods:")
        affordable_rods = [rod for rod in self.rod_types if rod.cost > self.current_rod.cost and rod.cost <= self.money]

        if not affordable_rods:
            print("No affordable upgrades available at the moment.")
            return

        for i, rod in enumerate(affordable_rods, 1):
            print(f"{i}. {rod}")

        print("Enter the number of the rod you want to buy, or press 0 to exit the shop.")
        choice = input("Choose a rod: ")

        if choice == "0":
            print("Exiting the shop.")
            return

        try:
            choice = int(choice) - 1
            if 0 <= choice < len(affordable_rods):
                selected_rod = affordable_rods[choice]
                self.current_rod = selected_rod
                self.money -= selected_rod.cost
                print(f"Successfully upgraded to {selected_rod.name}!")
            else:
                print("Invalid choice. Returning to the menu.")
        except ValueError:
            print("Invalid input. Returning to the menu.")

    def fish(self):
        print("\nCasting your line...")
        self.fishing_attempts += 1  # Increment fishing attempts

        # Check if the player has reached 500 fishing attempts
        if self.fishing_attempts == 500:
            self.current_rod = next(rod for rod in self.rod_types if rod.name == "No-Life Rod")
            print("Congratulations! You have unlocked the No-Life Rod for reaching 500 fishing attempts!")

        if self.fishing_attempts == 1000:
            self.current_rod = next(rod for rod in self.rod_types if rod.name == "Seraphic Rod")
            print("Congratulations! You have unlocked the Seraphic Rod for reaching 500 fishing attempts!")

        if random.random() <= self.current_rod.catch_rate:
            available_fish = [fish for fish in self.fish_types if random.random() <= fish.catch_chance]
            if available_fish:
                caught_fish = random.choice(available_fish)

                mutation, multiplier = random.choice(list(self.mutations.items()))
                caught_fish.apply_mutation(mutation, multiplier)

                self.inventory.append(caught_fish)
                self.bestiary[caught_fish.name] += 1
                print(f"You caught a {caught_fish.name} weighing {caught_fish.weight}kg worth ${caught_fish.price}!")
            else:
                print("No fish were biting today.")
        else:
            print("No luck this time.")

    def sell_fish(self):
        if not self.inventory:
            print("\nYou have no fish to sell.")
            return

        print("\nSelling all fish...")
        total_value = sum(fish.price for fish in self.inventory)
        self.money += total_value
        self.inventory = []
        print(f"You sold all your fish for ${total_value}!")

    def show_inventory(self):
        print("\nInventory:")
        if self.inventory:
            for fish in self.inventory:
                print(f"- {fish}")
        else:
            print("(Empty)")

    def show_bestiary(self):
        print("\n--- Bestiary ---")
        total_caught = sum(self.bestiary.values())  # Total fish caught
        unique_fish_caught = sum(1 for count in self.bestiary.values() if count > 0)  # Unique fish types caught
        total_fish_types = len(self.bestiary)  # Total available fish types
        percentage_types_caught = (unique_fish_caught / total_fish_types * 100) if total_fish_types > 0 else 0

        print(f"Total Fish Caught: {total_caught}")
        print(f"Unique Fish Types Caught: {unique_fish_caught}/{total_fish_types} ({percentage_types_caught:.2f}%)\n")
        print("Caught Fish Details:")

        for fish_name, count in self.bestiary.items():
            if count > 0:
                percentage = (count / total_caught * 100) if total_caught > 0 else 0
                print(f"- {fish_name}: {count} caught ({percentage:.2f}%)")

        print(f"\nTotal Fish Types Caught: {unique_fish_caught}/{total_fish_types} ({percentage_types_caught:.2f}%)")



    def show_status(self):
        print("\n--- Current Status ---")
        print(f"Money: ${self.money}")
        print(f"Current Rod: {self.current_rod}")
        print(f"Fishing Attempts: {self.fishing_attempts}")
        print("Fish Caught:")
        for fish_name, count in self.bestiary.items():
            print(f"- {fish_name}: {count}")
        print("Inventory:")
        if self.inventory:
            for fish in self.inventory:
                print(f"- {fish}")
        else:
            print("(Empty)")

    def main_menu(self):
        while True:
            print("\n--- Fishing Game Menu ---")
            print("1. Go Fishing")
            print("2. Show Inventory")
            print("3. Sell Fish")
            print("4. Show Bestiary")
            print("5. Visit Shop")
            print("6. Show Status")
            print("0. Exit Game")

            choice = input("Choose an option: ")

            if choice == "1":
                self.fish()
            elif choice == "2":
                self.show_inventory()
            elif choice == "3":
                self.sell_fish()
            elif choice == "4":
                self.show_bestiary()
            elif choice == "5":
                self.shop_screen()
            elif choice == "6":
                self.show_status()
            elif choice == "0":
                print("Thanks for playing the Fishing Game!")
                break
            else:
                print("Invalid option. Please try again.")

class MegFishingGame:
    def __init__(self):
        # ... (Other initializations remain unchanged)
        self.typing_challenge_words = [
            "Megaladon", "No-Life", "Exotic", "Phantom", "Fisch"
        ]
        self.typing_game_attempts = 0  # Counter to track typing attempts

    def start_typing_challenge(self):
        """Start the typing challenge when a Megaladon is caught."""
        print("\nA Megaladon is on the line! Type the words correctly to catch it!\n")
        
        # Select 5 random words for the challenge
        challenge_words = random.sample(self.typing_challenge_words, 5)
        challenge_words_str = " ".join(challenge_words)
        print(f"Words to type: {challenge_words_str}")
        
        # Allow the player 3 attempts to type all the words correctly
        attempts = 0
        while attempts < 3:
            user_input = input("Type the words correctly: ").strip()
            if user_input == challenge_words_str:
                print("\nCongratulations! You caught the Megaladon!")
                return True  # Successful catch
            else:
                print("\nIncorrect! Try again.")
                attempts += 1
        
        print("\nYou failed to type the words correctly. The Megaladon got away!")
        return False  # Failed catch

    def fish(self):
        print("\nCasting your line...")
        self.fishing_attempts += 1  # Increment fishing attempts

        # Check if the player has reached 500 fishing attempts
        if self.fishing_attempts == 500:
            self.current_rod = next(rod for rod in self.rod_types if rod.name == "No-Life Rod")
            print("Congratulations! You have unlocked the No-Life Rod for reaching 500 fishing attempts!")

        if random.random() <= self.current_rod.catch_rate:
            available_fish = [fish for fish in self.fish_types if random.random() <= fish.catch_chance]
            if available_fish:
                caught_fish = random.choice(available_fish)

                # Check if the fish caught is a Megaladon
                if caught_fish.name == "Megaladon":
                    if not self.start_typing_challenge():
                        return  # If the player fails, no fish is added

                mutation, multiplier = random.choice(list(self.mutations.items()))
                caught_fish.apply_mutation(mutation, multiplier)

                self.inventory.append(caught_fish)
                self.bestiary[caught_fish.name] += 1
                print(f"You caught a {caught_fish.name} weighing {caught_fish.weight}kg worth ${caught_fish.price}!")
            else:
                print("No fish were biting today.")
        else:
            print("No luck this time.")


if __name__ == "__main__":
    game = FishingGame()
    game.main_menu()
