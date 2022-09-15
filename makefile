deploy-external-api:
	cd external-api; cp -R ../.git git_folder; gcloud builds submit --tag "gcr.io/${GCP_PROJECT}/external-api"; rm -rf git_folder
	gcloud run deploy external-api --region=us-central1 --image gcr.io/${GCP_PROJECT}/external-api --update-env-vars ROOKOUT_TOKEN=${ROOKOUT_TOKEN},ROOKOUT_LABELS="env:prod"

deploy-orders-service:
	cd orders-service; cp -R ../.git git_folder;  gcloud builds submit --tag gcr.io/${GCP_PROJECT}/orders-service; rm -rf ./git_folder
	gcloud run deploy orders-service --region=us-central1 --image gcr.io/${GCP_PROJECT}/orders-service --update-env-vars ROOKOUT_TOKEN=${ROOKOUT_TOKEN},ROOKOUT_LABELS="env:prod"

deploy-inventory-service:
	cd inventory-service; cp -R ../.git git_folder;  gcloud builds submit --tag gcr.io/${GCP_PROJECT}/inventory-service; rm -rf ./git_folder
	gcloud run deploy inventory-service --region=us-central1 --image gcr.io/${GCP_PROJECT}/inventory-service --update-env-vars ROOKOUT_TOKEN=${ROOKOUT_TOKEN},ROOKOUT_LABELS="env:prod"

deploy-shipping-service:
	cd shipping-service; cp -R ../.git git_folder;  gcloud builds submit --tag gcr.io/${GCP_PROJECT}/shipping-service; rm -rf ./git_folder
	gcloud run deploy shipping-service --region=us-central1 --image gcr.io/${GCP_PROJECT}/shipping-service --update-env-vars ROOKOUT_TOKEN=${ROOKOUT_TOKEN},ROOKOUT_LABELS="env:prod"

deploy-all:
	make deploy-orders-service deploy-inventory-service deploy-shipping-service deploy-external-api