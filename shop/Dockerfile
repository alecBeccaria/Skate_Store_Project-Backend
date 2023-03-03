FROM public.ecr.aws/lambda/python:3.9

#Copys files over
COPY ./Item_Get_Search.py ${LAMBDA_TASK_ROOT}
COPY ./requirements.txt .

#Installs dependencies
RUN pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

#This makes it the entry point
#CMD ["app.lambda_handler"]
CMD ["Item_Get_Search.lambda_handler"]