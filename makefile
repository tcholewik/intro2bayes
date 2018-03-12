reveal_path = "./src/reveal.js"
build_slides = jupyter nbconvert $< --to slides 

output/presentation.slides.html: notebook/presentation.ipynb dependencies rise_presenter ./src/reveal.js
	echo "Building presentation"
	$(build_slides) --output-dir ./output --reveal-prefix $(reveal_path)

present: notebook/presentation.ipynb
	$(build_slides) --post serve

dependencies:
	echo "Installing python dependencies"
	pip install jupyter RISE

rise_presenter:
	jupyter nbextension install rise --py --sys-prefix
	jupyter nbextension enable  rise --py --sys-prefix

./src/reveal.js:
	echo "Downloading reveal.js to $(reveal_path)"
	git clone https://github.com/hakimel/reveal.js.git $(reveal_path)

clean:
	echo "Removing presentation outputs"
	rm output/presentation.slides.html
	echo "Removing reveal.js"
	rm $(reveal_path)
