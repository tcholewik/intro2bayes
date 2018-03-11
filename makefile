output/presentation.html: notebook/presentation.ipynb
	nbpresent -i $< -o $@
