deploy-external-api:
	cd external-api; gcloud builds submit --tag gcr.io/rookoutdev/external-api
	gcloud run deploy external-api --region=us-central1 --image gcr.io/${GCP_PROJECT}/external-api

deploy-orders-service:
	cd orders-service; gcloud builds submit --tag gcr.io/rookoutdev/orders-service
	gcloud run deploy orders-service --region=us-central1 --image gcr.io/${GCP_PROJECT}/orders-service

deploy-inventory-service:
	cd inventory-service; gcloud builds submit --tag gcr.io/rookoutdev/inventory-service
	gcloud run deploy inventory-service --region=us-central1 --image gcr.io/${GCP_PROJECT}/inventory-service

deploy-shipping-service:
	cd shipping-service; gcloud builds submit --tag gcr.io/rookoutdev/shippgin-service
	gcloud run deploy shipping-service --region=us-central1 --image gcr.io/${GCP_PROJECT}/shippgin-service

deploy-all:
	make deploy-orders-service deploy-inventory-service deploy-shipping-service deploy-external-api