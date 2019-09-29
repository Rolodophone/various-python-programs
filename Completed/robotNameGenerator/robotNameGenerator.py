"""
Not my program!
This was taken and modified for my use from https://www.fantasynamegenerators.com/robot-names.php
"""


nameList = []


names1 = ["Adept", "Advanced", "Artificial", "Automated", "Automatic", "Autonomous", "Bio-Electrionic", "Bionic", "Compact", "Computerized", "Conscious", "Cybernated", "Cybernetic", "Digital", "Dynamic", "Efficient", "Electronic", "Essential", "Exceptional", "Experimental", "Extra-Terrestrial", "Extraterrestial", "Extreme", "General", "Generic", "Global", "High-Powered", "Highpowered", "Humanoid", "Independent", "Integrated", "Intelligent", "Main", "Mechanical", "Mechanized", "Motorized", "Neohuman", "Nuclear", "Perceptive", "Personal", "Preliminary", "Primary", "Prime", "Primitive", "Programmed", "Rational", "Reactive", "Responsive", "Robotic", "Secondary", "Self-Aware", "Self-Regulaing", "Self-Reliant", "Self-Sufficient", "Sensitive", "Sensory", "Solar", "Strategic", "Super", "Supreme", "Synchronized", "Temporary", "Ultimate", "Unified", "Universal"]
names2 = ["Air Defense", "Air Safety", "Airplane Control", "Algorithm", "Analysis", "Animal Control", "Animal Handling", "Animal Protection", "Assassination", "Base Protection", "Battle", "Bodyguard", "Bomb Disposal", "Care", "Caretaker", "Construction", "Contamination", "Cultivation", "Data Analyzing", "Data Collection", "Data Destruction", "Data Protection", "Decoding", "Demolition", "Detection", "Diplomacy", "Docking", "Domination", "Education", "Emergency Repair", "Emergency Response", "Emergency", "Emulation", "Encoding", "Encryption", "Enforcer", "Engineering", "Eradication", "Escort", "Evacuation", "Evasion", "Examination", "Excevation", "Excretion", "Expedition", "Exploration", "Farming", "Fire Fighting", "First Aid", "Flora and Fauna", "Garbage Disposal", "Guidance", "Harvesting", "Home Protection", "Human Control", "Human Protection", "Human Training", "Infiltration", "Info Analyzing", "Info Collection", "Information", "Inspection", "Instruction", "Instructor", "Invasion", "Lab Partner", "Laboratorium", "Life Emulation", "Life Protection", "Life Simulation", "Lifeform Detection", "Management", "Mapping", "Medical", "Mining", "Network Defense", "Neutralization", "Nullification", "Observer", "Ocean Exploration", "Oceanic Navigation", "Operating", "Operation", "Peacekeeping", "Personal Protection", "Pilot", "Piloting", "Planet Defence", "Planet Examination", "Planet Exploration", "Planet Survey", "Planetary Analysis", "Planetary Expedition", "Probe", "Processor", "Protection", "Recording", "Regulation", "Repairation", "Riot Control", "Robot Control", "Sabotage", "Safety Guard", "Safety", "Sanitation", "Science", "Servant", "Shepherd", "Simulation", "Space Expedition", "Space Exploration", "Space Navigation", "Spacecraft Defense", "Supervision", "Teaching", "Termination", "Terraforming", "Translation", "Transportation", "Travel", "Troubleshooting", "Unit Response", "Usher", "Utility", "Vegetation", "War Domination", "War Management", "War", "Waste Collection", "Waste Disposal"]
names3 = ["Android", "Automaton", "Bot", "Cyborg", "Device", "Droid", "Drone", "Emulator", "Entity", "Golem", "Juggernaut", "Machine", "Prototype", "Robot", "Technician", "Technology"]
for name1 in names1:
    for name2 in names2:
        for name3 in names3:
            nameList.append("{} {} {}\n".format(name1, name2, name3))


names4 = ["01010010 (R in binary)", "Alpha", "Andromeda", "Andy Roid", "Anne Droid", "Ash", "Auto", "Axel", "Azerty", "Beta", "Bit", "Bolt", "Booker", "Boomer", "Bracer", "Brainstorm", "Brobot", "Bult", "Buttons", "Cabe", "Clank", "Cole", "Combot", "Copper", "Core", "Corion", "Corius", "Crowby", "Curious", "Cyb", "Cybel", "Cyd", "Cyl", "Cylinder", "Data", "Devi", "Dot", "Dotty", "Drillbit", "Dustie", "Earl", "Experiment", "Fiber", "Gadget", "Gage", "Gear", "Gearz", "Gere", "Gigabit", "Golem", "Greez", "Grezzer", "Hammer", "Jet", "Jin", "Kitt", "Knave", "Led", "Mace", "Mach", "Max", "Mecha", "Mechan", "Mechi", "Micro", "Mig", "Norbit", "Nozzle", "Otis", "Plex", "Plexi", "Plier", "Prime", "Proto", "Qwerty", "Ranger", "Ratcher", "Ratchet", "Rob Bitt", "Rob Bott", "Rob Oto", "Robbie", "Robert", "Roberto", "Rubber", "Rust", "Rusty", "Sark", "Scrap", "Scrappie", "Scrappy", "Screwie", "Scythe", "Scyther", "Shrimp", "Silver", "Skip", "Socket", "Sona", "Spanner", "Spark", "Sparkle", "Sparky", "Spencer", "Spirit", "Spud", "Spudnik", "Sterling", "Talus", "Tech", "Tera", "Terra", "Test", "Tin", "Tink", "Tinker", "Tobor", "Tracker", "Twobit", "Wire"]
for name4 in names4:
    nameList.append(name4 + "\n")

names5 = ["a", "e", "i", "o", "u"]
names6 = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
names7 = ["a", "e", "i", "o", "u", "", "", "", ""]
names8 = ["b", "c", "d", "f", "g", "h", "x", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "x", "x", "y", "z", "", "", "", "", "", "", "", "", "", ""]
names9 = ["x", "tron", "roid", "ator", "oid", "", "", "", "", "", "", ""]
for name5 in names5:
    for name6 in names6:
        for name7 in names7:
            for name8 in names8:
                for name9 in names9:
                    newName = name5 + name6 + name7 + name8 + name9 + "\n"
                    if not newName in nameList:            # for removing duplicates
                        nameList.append(newName)


with open("robots.txt", "w") as robotsFile:
    robotsFile.writelines(nameList)
