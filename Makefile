install_packages: ## Install python requirements
	pip install -r requirements.txt

project: install_packages build

build: clean load_users load_data

clean: ## Clean sandbox images,cache,static and database
	# Remove media
	-rm -rf public/media/images
	-rm -rf public/media/cache
	-rm -rf public/static
	-rm -f db.sqlite3
	# Create database
	python manage.py migrate

load_users: ## Load user data into sandbox
	python manage.py loaddata outlet/fixtures/auth.json

load_data: ## Import fixtures and collect static
	# Import some fixtures. Order is important as JSON fixtures include primary keys
	python manage.py loaddata outlet/fixtures/child_products.json
	python manage.py oscar_import_catalogue outlet/fixtures/*.csv
	python manage.py oscar_import_catalogue_images outlet/fixtures/images.tar.gz
	python manage.py oscar_populate_countries --initial-only
	python manage.py loaddata outlet/fixtures/pages.json outlet/fixtures/ranges.json outlet/fixtures/offers.json
	python manage.py loaddata outlet/fixtures/orders.json
	python manage.py clear_index --noinput
	python manage.py update_index catalogue
	python manage.py thumbnail cleanup
	python manage.py collectstatic --noinput

lint: ## Run flake8 and isort checks
	flake8 outlet/
	isort -c -q --diff outlet/

#######################
# Translations Handling
#######################
extract_translations: ## Extract strings and create source .po files
	cd src/oscar; django-admin.py makemessages -a

compile_translations: ## Compile translation files and create .mo files
	cd src/oscar; django-admin.py compilemessages

######################
# Project Management
######################
clean_project: ## Remove files not in source control
	find . -type f -name "*.pyc" -delete
	rm -rf nosetests.xml coverage.xml htmlcov *.egg-info *.pdf dist violations.txt
