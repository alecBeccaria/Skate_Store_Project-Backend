:: For Single image push
:: docker build -t admin_post:1.0 .

:: To Test local image
:: docker run -d -p 9001:8080 --name performer_lambda performer_lambda:1



:: Docker fun stuff
docker compose up -d

:: Check Login
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 249804032116.dkr.ecr.us-east-1.amazonaws.com/skate_ecommerce


::Tag and push to ECR
docker tag admin_get:1.0 249804032116.dkr.ecr.us-east-1.amazonaws.com/skate_ecommerce:Admin_Get
docker tag admin_post:1.0 249804032116.dkr.ecr.us-east-1.amazonaws.com/skate_ecommerce:Admin_Post
docker tag admin_delete:1.0 249804032116.dkr.ecr.us-east-1.amazonaws.com/skate_ecommerce:Admin_Delete
docker tag admin_put:1.0 249804032116.dkr.ecr.us-east-1.amazonaws.com/skate_ecommerce:Admin_Put


docker push 249804032116.dkr.ecr.us-east-1.amazonaws.com/skate_ecommerce:Admin_Get
docker push 249804032116.dkr.ecr.us-east-1.amazonaws.com/skate_ecommerce:Admin_Post
docker push 249804032116.dkr.ecr.us-east-1.amazonaws.com/skate_ecommerce:Admin_Delete
docker push 249804032116.dkr.ecr.us-east-1.amazonaws.com/skate_ecommerce:Admin_Put