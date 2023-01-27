init:
	pip install -r requirements.txt
run:
	export GOOGLE_APPLICATION_CREDENTIALS="/path/to/google_api_key.json"; \
	python main.py; \
	rm temp.jpg;

scraping:
	cd ./scraping ; \
	pwd ; \
	python get_cardlist_mons.py > mons.json; \
	python get_cardlist_magic.py > magic.json; \
	python get_cardlist_trap.py > trap.json;
	