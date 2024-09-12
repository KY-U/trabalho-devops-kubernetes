kubectl delete -f k8s/mysql-init-config.yaml
kubectl delete -f k8s/mysql-deployment.yaml
kubectl delete -f k8s/mysql-service.yaml
kubectl delete -f k8s/backend-deployment.yaml
kubectl delete -f k8s/backend-service.yaml
kubectl delete -f k8s/frontend-deployment.yaml
kubectl delete -f k8s/frontend-service.yaml
kubectl delete -f k8s/ingress.yaml
kubectl delete -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.11.2/deploy/static/provider/cloud/deploy.yaml

kubectl delete all --all