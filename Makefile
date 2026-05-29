SOURCES=$(shell python3 scripts/read-config.py --sources )
FAMILY=$(shell python3 scripts/read-config.py --family )

help:
	@echo "###"
	@echo "# Build targets for $(FAMILY)"
	@echo "###"
	@echo
	@echo "  make build:  Builds the fonts and places them in the fonts/ directory"
	@echo "  make test:   Tests the fonts with fontspector"
	@echo "  make proof:  Creates HTML proof documents in the proof/ directory"
	@echo "  make images: Creates PNG specimen images in the documentation/ directory"
	@echo

build: build.stamp

venv: venv/touchfile

venv-pixel: venv-pixel/touchfile

customize: venv
	. venv/bin/activate; python3 scripts/customize.py

build.stamp: venv venv-pixel sources/config-Geist.yaml $(SOURCES)
	rm -rf fonts geist-font geist-font.zip
	# Geist Pixel uses a virtual master, which the released gftools in
	# requirements.txt can't build (it fails with "No final targets"). Build it
	# with the dev gftools in venv-pixel that has the virtual-master fix;
	# everything else uses venv.
	@for config in sources/config*.yaml; do \
		if [ "$$config" = "sources/config-GeistPixel.yaml" ]; then \
			( . venv-pixel/bin/activate && gftools builder "$$config" ); \
		else \
			( . venv/bin/activate && gftools builder "$$config" ); \
		fi; \
	done
	# Geist Pixel's static instances and webfonts are hand-exported from Glyphs
	# and committed (buildStatic:false means gftools only builds the variable, so
	# the clean `rm -rf fonts` above drops them). Restore the committed assets the
	# release zip and npm package consume.
	git checkout -- fonts/GeistPixel/otf fonts/GeistPixel/ttf fonts/GeistPixel/webfonts
	$(MAKE) copy-npm-fonts
	$(MAKE) create-release-zip
	touch build.stamp

copy-npm-fonts:
	# Clear any pre-existing build artifacts
	rm -rf packages/next/dist/fonts
	# Copy over the relevant font files
	mkdir -p packages/next/dist/fonts/geist-sans packages/next/dist/fonts/geist-mono packages/next/dist/fonts/geist-pixel
	cp fonts/Geist/ttf/*.ttf packages/next/dist/fonts/geist-sans/
	cp fonts/Geist/webfonts/*.woff2 packages/next/dist/fonts/geist-sans/
	cp fonts/Geist/variable/*.ttf packages/next/dist/fonts/geist-sans/
	cp fonts/GeistMono/ttf/*.ttf packages/next/dist/fonts/geist-mono/
	cp fonts/GeistMono/webfonts/*.woff2 packages/next/dist/fonts/geist-mono/
	cp fonts/GeistMono/variable/*.ttf packages/next/dist/fonts/geist-mono/
	cp fonts/GeistPixel/webfonts/*.woff2 packages/next/dist/fonts/geist-pixel/
	# Apparently there is a naming mismatch between the font files for npm distribution and the actual font files,
	# so we need to rename them to the correct names.
	cd packages/next/dist/fonts/geist-sans && \
		mv Geist-ExtraLight.ttf Geist-UltraLight.ttf && \
		mv Geist-ExtraLight.woff2 Geist-UltraLight.woff2 && \
		mv Geist-ExtraBold.ttf Geist-UltraBlack.ttf && \
		mv Geist-ExtraBold.woff2 Geist-UltraBlack.woff2 && \
		mv 'Geist[wght].ttf' Geist-Variable.ttf && \
		mv 'Geist[wght].woff2' Geist-Variable.woff2
	cd packages/next/dist/fonts/geist-mono && \
		mv GeistMono-ExtraLight.ttf GeistMono-UltraLight.ttf && \
		mv GeistMono-ExtraLight.woff2 GeistMono-UltraLight.woff2 && \
		mv GeistMono-ExtraBold.ttf GeistMono-UltraBlack.ttf && \
		mv GeistMono-ExtraBold.woff2 GeistMono-UltraBlack.woff2 && \
		mv 'GeistMono[wght].ttf' GeistMono-Variable.ttf && \
		mv 'GeistMono[wght].woff2' GeistMono-Variable.woff2

create-release-zip:
	mkdir -p geist-font
	cp -r fonts/* geist-font/
	cp documentation/DESCRIPTION.en_us.html geist-font/ || true
	cp documentation/article/ARTICLE.en_us.html geist-font/ || true
	cp OFL.txt geist-font/
	zip -r geist-font.zip geist-font
	rm -rf geist-font

venv/touchfile: requirements.txt
	test -d venv || python3 -m venv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/touchfile

# Geist Pixel's virtual-master support only exists in an unreleased gftools dev
# build (Simon Cozens' fix). Pin the exact commit for reproducibility; revisit
# once it ships in an official gftools release and we can fold it into venv.
GFTOOLS_PIXEL_REF = 47ec3706b

venv-pixel/touchfile: Makefile
	test -d venv-pixel || python3 -m venv venv-pixel
	. venv-pixel/bin/activate; pip install "gftools @ git+https://github.com/googlefonts/gftools@$(GFTOOLS_PIXEL_REF)"
	touch venv-pixel/touchfile

test: build.stamp
	which fontspector || (echo "fontspector not found. Please install it with 'cargo install fontspector'." && exit 1)
	TOCHECK=$$(find fonts/Geist/variable -type f 2>/dev/null); mkdir -p out/ out/fontspector; fontspector --profile googlefonts -l warn --full-lists --succinct --html out/fontspector/GeistVF-fontspector-report.html --ghmarkdown out/fontspector/GeistVF-fontspector-report.md --badges out/badges $$TOCHECK  || echo '::warning file=sources/config-Geist.yaml,title=fontspector failures::The fontspector QA check reported errors in your font. Please check the generated report.'
	TOCHECK=$$(find fonts/Geist/ttf -type f 2>/dev/null); mkdir -p out/ out/fontspector; fontspector --profile googlefonts -l warn --full-lists --succinct --html out/fontspector/Geist-fontspector-report.html --ghmarkdown out/fontspector/Geist-fontspector-report.md --badges out/badges $$TOCHECK  || echo '::warning file=sources/config-Geist.yaml,title=fontspector failures::The fontspector QA check reported errors in your font. Please check the generated report.'
	TOCHECK=$$(find fonts/GeistMono/variable -type f 2>/dev/null); mkdir -p out/ out/fontspector; fontspector --profile googlefonts -l warn --full-lists --succinct --html out/fontspector/GeistMonoVF-fontspector-report.html --ghmarkdown out/fontspector/GeistMonoVF-fontspector-report.md --badges out/badges $$TOCHECK  || echo '::warning file=sources/config-GeistMono.yaml,title=fontspector failures::The fontspector QA check reported errors in your font. Please check the generated report.'
	TOCHECK=$$(find fonts/GeistMono/ttf -type f 2>/dev/null); mkdir -p out/ out/fontspector; fontspector --profile googlefonts -l warn --full-lists --succinct --html out/fontspector/GeistMono-fontspector-report.html --ghmarkdown out/fontspector/GeistMono-fontspector-report.md --badges out/badges $$TOCHECK  || echo '::warning file=sources/config-GeistMono.yaml,title=fontspector failures::The fontspector QA check reported errors in your font. Please check the generated report.'
	TOCHECK=$$(find fonts/GeistPixel/ttf -type f 2>/dev/null); mkdir -p out/ out/fontspector; fontspector --profile googlefonts -l warn --full-lists --succinct --html out/fontspector/GeistPixel-fontspector-report.html --ghmarkdown out/fontspector/GeistPixel-fontspector-report.md --badges out/badges $$TOCHECK  || echo '::warning file=sources/config-GeistPixel.yaml,title=fontspector failures::The fontspector QA check reported errors in your font. Please check the generated report.'

proof: venv build.stamp
	TOCHECK=$$(find fonts/Geist/variable -type f 2>/dev/null); if [ -z "$$TOCHECK" ]; then TOCHECK=$$(find fonts/Geist/ttf -type f 2>/dev/null); fi ; . venv/bin/activate; mkdir -p out/ out/proof; diffenator2 proof $$TOCHECK -o out/proof

images: venv $(DRAWBOT_OUTPUT)

%.png: %.py build.stamp
	. venv/bin/activate; python3 $< --output $@

clean:
	rm -rf venv venv-pixel
	find . -name "*.pyc" -delete

update-project-template:
	npx update-template https://github.com/googlefonts/googlefonts-project-template/

update: venv
	venv/bin/pip install --upgrade pip-tools
	# See https://pip-tools.readthedocs.io/en/latest/#a-note-on-resolvers for
	# the `--resolver` flag below.
	venv/bin/pip-compile --upgrade --verbose --resolver=backtracking requirements.in
	venv/bin/pip-sync requirements.txt

	git commit -m "Update requirements" requirements.txt
	git push
