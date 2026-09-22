#!/usr/bin/env python3
"""
"""
import sys
import json

import fontforge


def build_font(data):
    font = fontforge.font()

    font.fontname   = data["ps_name"]
    font.familyname = data["family"]
    font.fullname   = data["full_name"]
    font.weight     = data["style"]
    font.version    = data["version"]
    font.copyright  = data["copyright"]
    font.comment    = data["description"]
    font.fontlog    = ""
    font.sfntRevision = float(data["version"])

    font.encoding = "UnicodeFull"
    font.em       = data["em"]
    font.ascent   = data["ascent"]
    font.descent  = data["descent"]

    font.italicangle = 0.0
    font.upos        = -418
    font.uwidth      = 140
    font.strokewidth = 0

    font.is_quadratic = True

    font.hasvmetrics = False

    # OS/2 table
    font.os2_version   = 4
    font.os2_weight    = 400
    font.os2_width     = 5
    font.os2_fstype    = 0
    font.os2_vendor    = data["vendor_id"]
    font.os2_family_class = 0

    font.os2_panose = (2, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    font.os2_typoascent   = data["ascent"]
    font.os2_typodescent  = -data["descent"]
    font.os2_typolinegap  = 0
    font.os2_winascent    = data["ascent"]
    font.os2_windescent   = data["descent"]
    font.os2_winascent_add  = 0
    font.os2_windescent_add = 0
    font.os2_typoascent_add  = 0
    font.os2_typodescent_add = 0
    font.hhea_ascent   = data["ascent"]
    font.hhea_descent  = -data["descent"]
    font.hhea_linegap  = 0
    font.hhea_ascent_add  = 0
    font.hhea_descent_add = 0

    font.os2_stylemap = 0x40
    font.os2_use_typo_metrics = True

    font.os2_subxsize   = int(data["em"] * 0.65)
    font.os2_subysize   = int(data["em"] * 0.70)
    font.os2_subxoff    = 0
    font.os2_subyoff    = int(data["em"] * 0.14)
    font.os2_supxsize   = int(data["em"] * 0.65)
    font.os2_supysize   = int(data["em"] * 0.70)
    font.os2_supxoff    = 0
    font.os2_supyoff    = int(data["em"] * 0.48)
    font.os2_strikeypos  = int(data["em"] * 0.26)
    font.os2_strikeysize = 50
    font.macstyle = 0

    # sfnt names
    lang = "English (US)"
    names = [
        ("Copyright",      data["copyright"]),
        ("Family",         data["family"]),
        ("SubFamily",      data["style"]),
        ("UniqueID",       f"{data["version"]};{data["vendor_id"]};{data["ps_name"]}"),
        ("Fullname",       data["full_name"]),
        ("Version",        f"Version {data["version"]}"),
        ("PostScriptName", data["ps_name"]),
        ("Manufacturer",   data["designer"]),
        ("Designer",       data["designer"]),
        ("Descriptor",     data["description"]),
        ("Vendor URL",     data["vendor_url"]),
        ("Designer URL",   data["designer_url"]),
        ("License",        data["license"]),
        ("License URL",    data["license_url"]),
    ]
    for key, value in names:
        font.appendSFNTName(lang, key, value)

    font.os2_codepages    = (1, 0)
    font.os2_unicoderanges = (1, 0, 0, 0)

    return font


def main():
    data_file = sys.argv[1]
    data = json.load(open(data_file))
    font = build_font(data)

    sfd_path = f"{data["ps_name"]}.sfd"
    font.save(sfd_path)
    font.close()


if __name__ == "__main__":
    main()
