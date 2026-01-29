SOURCES=$(shell python3.10 scripts/read-config.py --sources )
FAMILY=$(shell python3.10 scripts/read-config.py --family )

help:
	@echo "###"
	@echo "# Build targets for $(FAMILY)"
	@echo "###"
	@echo
	@echo "  make build:  Builds the fonts and places them in the fonts/ directory"
	@echo "  make test:   Tests the fonts with fontbakery"
	@echo "  make proof:  Creates HTML proof documents in the proof/ directory"
	@echo "  make images: Creates PNG specimen images in the documentation/ directory"
	@echo

build: build.stamp

venv: venv/touchfile

venv-test: venv-test/touchfile

customize: venv
	. venv/bin/activate; python3.10 scripts/customize.py

build.stamp: venv sources/config-Geist.yaml $(SOURCES)
	rm -rf fonts geist-font geist-font.zip
	(for config in sources/config*.yaml; do . venv/bin/activate; gftools builder $$config; done)
	$(MAKE) copy-npm-fonts
	$(MAKE) create-release-zip
	touch build.stamp

copy-npm-fonts:
	# Clear any pre-existing build artifacts
	rm -rf packages/next/dist/fonts
	# Copy over the relevant font files
	mkdir -p packages/next/dist/fonts/geist-sans packages/next/dist/fonts/geist-mono
	cp fonts/Geist/ttf/*.ttf packages/next/dist/fonts/geist-sans/
	cp fonts/Geist/webfonts/*.woff2 packages/next/dist/fonts/geist-sans/
	cp fonts/Geist/variable/*.ttf packages/next/dist/fonts/geist-sans/
	cp fonts/GeistMono/ttf/*.ttf packages/next/dist/fonts/geist-mono/
	cp fonts/GeistMono/webfonts/*.woff2 packages/next/dist/fonts/geist-mono/
	cp fonts/GeistMono/variable/*.ttf packages/next/dist/fonts/geist-mono/
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
	test -d venv || python3.10 -m venv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/touchfile

venv-test/touchfile: requirements-test.txt
	test -d venv-test || python3.10 -m venv venv-test
	. venv-test/bin/activate; pip install -Ur requirements-test.txt
	touch venv-test/touchfile

test: venv-test build.stamp
	TOCHECK=$$(find fonts/Geist/variable -type f 2>/dev/null); if [ -z "$$TOCHECK" ]; then TOCHECK=$$(find fonts/Geist/ttf -type f 2>/dev/null); fi ; . venv-test/bin/activate; mkdir -p out/ out/fontbakery; fontbakery check-googlefonts -l WARN --full-lists --succinct --badges out/badges --html out/fontbakery/Geist-fontbakery-report.html --ghmarkdown out/fontbakery/Geist-fontbakery-report.md $$TOCHECK  || echo '::warning file=sources/config-Geist.yaml,title=Fontbakery failures::The fontbakery QA check reported errors in your font. Please check the generated report.'
	TOCHECK=$$(find fonts/GeistMono/variable -type f 2>/dev/null); if [ -z "$$TOCHECK" ]; then TOCHECK=$$(find fonts/GeistMono/ttf -type f 2>/dev/null); fi ; . venv-test/bin/activate; mkdir -p out/ out/fontbakery; fontbakery check-googlefonts -l WARN --full-lists --succinct --badges out/badges --html out/fontbakery/GeistMono-fontbakery-report.html --ghmarkdown out/fontbakery/GeistMono-fontbakery-report.md $$TOCHECK  || echo '::warning file=sources/config-GeistMono.yaml,title=Fontbakery failures::The fontbakery QA check reported errors in your font. Please check the generated report.'

proof: venv build.stamp
	TOCHECK=$$(find fonts/Geist/variable -type f 2>/dev/null); if [ -z "$$TOCHECK" ]; then TOCHECK=$$(find fonts/Geist/ttf -type f 2>/dev/null); fi ; . venv/bin/activate; mkdir -p out/ out/proof; diffenator2 proof $$TOCHECK -o out/proof
	TOCHECK=$$(find fonts/Geist/variable -type f 2>/dev/null); if [ -z "$$TOCHECK" ]; then TOCHECK=$$(find fonts/GeistMono/ttf -type f 2>/dev/null); fi ; . venv/bin/activate; mkdir -p out/ out/proof; diffenator2 proof $$TOCHECK -o out/proof

%.png: %.py build.stamp
	. venv/bin/activate; python3.10 $< --output $@

clean:
	rm -rf venv
	find . -name "*.pyc" -delete

update-project-template:
	npx update-template https://github.com/googlefonts/googlefonts-project-template/

update: venv venv-test
	venv/bin/pip install --upgrade pip-tools
	# See https://pip-tools.readthedocs.io/en/latest/#a-note-on-resolvers for
	# the `--resolver` flag below.
	venv/bin/pip-compile --upgrade --verbose --resolver=backtracking requirements.in
	venv/bin/pip-sync requirements.txt

	venv-test/bin/pip install --upgrade pip-tools
	venv-test/bin/pip-compile --upgrade --verbose --resolver=backtracking requirements-test.in
	venv-test/bin/pip-sync requirements-test.txt

	git commit -m "Update requirements" requirements.txt requirements-test.txt
	git push
