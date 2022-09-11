deploy-orders-service:
	cd orders-service; gcloud builds submit --tag gcr.io/rookoutdev/orders-service
	gcloud run deploy orders-service --region=us-central1 --image gcr.io/rookoutdev/orders-service

deploy-inventory-service:
	cd inventory-service; gcloud builds submit --tag gcr.io/rookoutdev/inventory-service
	gcloud run deploy inventory-service --region=us-central1 --image gcr.io/rookoutdev/inventory-service

deploy-shipping-service:
	cd shipping-service; gcloud builds submit --tag gcr.io/rookoutdev/shippgin-service
	gcloud run deploy shipping-service --region=us-central1 --image gcr.io/rookoutdev/shippgin-service

