FROM public.ecr.aws/lambda/python:3.6
COPY lambda.py ${LAMBDA_TASK_ROOT}
CMD [ "lambda.handler" ]