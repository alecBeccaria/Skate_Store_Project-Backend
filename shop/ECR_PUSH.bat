:: For Single image push
:: docker build -t item_get_search:1.0 .

:: To Test local image
:: docker run -d -p 9001:8080 --name performer_lambda performer_lambda:1



:: Docker fun stuff
docker compose up -d

:: Check Login
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 249804032116.dkr.ecr.us-east-1.amazonaws.com/skate_ecommerce


::Tag and push to ECR
docker tag item_get:1.0 249804032116.dkr.ecr.us-east-1.amazonaws.com/skate_ecommerce:Item_Get
docker tag item_get_all:1.0 249804032116.dkr.ecr.us-east-1.amazonaws.com/skate_ecommerce:Item_Get_All
docker tag item_get_category:1.0 249804032116.dkr.ecr.us-east-1.amazonaws.com/skate_ecommerce:Item_Get_Category
docker tag item_get_search:1.0 249804032116.dkr.ecr.us-east-1.amazonaws.com/skate_ecommerce:Item_Get_Search
docker tag item_post:1.0 249804032116.dkr.ecr.us-east-1.amazonaws.com/skate_ecommerce:Item_Post
docker tag item_delete:1.0 249804032116.dkr.ecr.us-east-1.amazonaws.com/skate_ecommerce:Item_Delete
docker tag item_put:1.0 249804032116.dkr.ecr.us-east-1.amazonaws.com/skate_ecommerce:Item_Put


docker push 249804032116.dkr.ecr.us-east-1.amazonaws.com/skate_ecommerce:Item_Get
docker push 249804032116.dkr.ecr.us-east-1.amazonaws.com/skate_ecommerce:Item_Get_All
docker push 249804032116.dkr.ecr.us-east-1.amazonaws.com/skate_ecommerce:Item_Get_Category
docker push 249804032116.dkr.ecr.us-east-1.amazonaws.com/skate_ecommerce:Item_Get_Search
docker push 249804032116.dkr.ecr.us-east-1.amazonaws.com/skate_ecommerce:Item_Post
docker push 249804032116.dkr.ecr.us-east-1.amazonaws.com/skate_ecommerce:Item_Delete
docker push 249804032116.dkr.ecr.us-east-1.amazonaws.com/skate_ecommerce:Item_Put