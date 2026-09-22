import sys
import json

import fontforge

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print ("USAGE: import_glyph_from_svg.py <sfd/font file> <glyphs JSON file>")
    else:
        data = json.load(open(sys.argv[2]))
        font = fontforge.open(sys.argv[1])

        glyph = font.createChar(-1, "space")
        glyph.clear()
        glyph.left_side_bearing = 50
        glyph.right_side_bearing = 50
        glyph.width = 600

        for glyph_data in data:
            glyph = font.createChar(-1, glyph_data["name"])
            glyph.clear()
            glyph.importOutlines("glyphs/" + glyph_data["name"] + ".svg", scale=False)
            glyph.left_side_bearing = glyph_data.get("lbearing", 50)
            glyph.right_side_bearing = glyph_data.get("rbearing", 50)

            glyph = font.createChar(-1, glyph_data["name"] + ".ss01")
            glyph.clear()
            glyph.importOutlines("glyphs/" + glyph_data["name"] + ".ss01.svg", scale=False)
            glyph.left_side_bearing = glyph_data.get("lbearing", 50)
            glyph.right_side_bearing = glyph_data.get("rbearing", 50)

            # glyph.width = 500

        # Apply the features
        font.mergeFeature("alt.fea")

        font.save(sys.argv[1])
        flags  = ("opentype", "dummy-dsig", "round", "apple")
        font_name = sys.argv[1].replace(".sfd",".otf")
        font.generate(font_name, flags=flags)
        font.close()
