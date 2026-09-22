gen:
	cd gen_glyphs; dub build; cd ..
	mkdir -p glyphs fonts
	./gen_glyphs/gen_glyphs
	python3 scripts/create_font.py data/munia-dot-info.json
	python3 scripts/import_glyphs.py Munia-Dot-Regular.sfd glyphs.json

install:
	cp fonts/Munia-Dot-Regular.otf ~/.fonts/; fc-cache -f
