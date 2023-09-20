deploy:
	chmod +x start_paella_app.sh && ./start_paella_app.sh

destroy:
	chmod +x clean_paella_app.sh && ./clean_paella_app.sh

test:
	curl -X POST -H "Content-Type: application/json" -d @input.json http://localhost:30007/paella
