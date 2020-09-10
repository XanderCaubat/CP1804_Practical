"""
CP1404/CP5632 Practical 05
Hexadecimal colour lookup
Xander Dino Caubat
"""
HEX_COLOUR_CODE = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "BlanchedAlmond": "#ffebcd",
                   "BlueViolet": "#8a2be2", "CadetBlue": " #5f9ea0", "DarkGoldenrod": "#b8860b",
                   "DarkGreen": "#006400", "DarkOrchid": "#9932cc", "FloralWhite": "#fffaf0", "Black": "#000000"}
print(HEX_COLOUR_CODE)

colour_code = input("Enter colour name: ")
while colour_code.lower() != "":
    print(" The code for \"{}\" is {}".format(colour_code, HEX_COLOUR_CODE.get(colour_code)))
    colour_code = input("Enter short state: ")