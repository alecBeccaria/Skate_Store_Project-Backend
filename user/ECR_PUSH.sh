#! /bin/bash
# For Single image push
# docker build -t user_get:1.0 .

# To Test local image
# docker run -d -p 9001:8080 --name performer_lambda performer_lambda:1



# Docker fun stuff
docker compose up -d

# Check Login
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 249804032116.dkr.ecr.us-east-1.amazonaws.com/skate_ecommerce


# Tag and push to ECR
docker tag user_get:1.0 249804032116.dkr.ecr.us-east-1.amazonaws.com/skate_ecommerce:User_Get
docker tag user_post:1.0 249804032116.dkr.ecr.us-east-1.amazonaws.com/skate_ecommerce:User_Post
docker tag user_delete:1.0 249804032116.dkr.ecr.us-east-1.amazonaws.com/skate_ecommerce:User_Delete
docker tag user_put:1.0 249804032116.dkr.ecr.us-east-1.amazonaws.com/skate_ecommerce:User_Put


docker push 249804032116.dkr.ecr.us-east-1.amazonaws.com/skate_ecommerce:User_Get
docker push 249804032116.dkr.ecr.us-east-1.amazonaws.com/skate_ecommerce:User_Post
docker push 249804032116.dkr.ecr.us-east-1.amazonaws.com/skate_ecommerce:User_Delete
docker push 249804032116.dkr.ecr.us-east-1.amazonaws.com/skate_ecommerce:User_Put