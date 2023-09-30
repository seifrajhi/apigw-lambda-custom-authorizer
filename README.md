# Amazon API Gateway REST API with Lambda Token Authorizer

API with a mapping template that enriches the request with additional data from Lambda Token Authorizer.

The serverless template deploys an Amazon API Gateway REST API endpoint that uses a Lambda Token Authorizer for access control.

If the request to the endpoint does not include a 'authorizationToken' header, the Lambda Authorizer will not be invoked and API Gateway will return a 401 Forbidden.
If the request to the endpoint includes a 'authorizationToken' header, the Lambda Authorizer will be invoked and its response will depend on the value of the 'authorizationToken' header.
If the value of 'authorizationToken' header is 'unauthorized', API Gateway will return a 401 Unauthorized error.
If the value of 'authorizationToken' header is 'Bearer deny', API Gateway will return a 403 error.
Only if the value of 'authorizationToken' header is 'Bearer allow', API Gateway will successfully invoke the Lambda integration and return a 200.
For any other case, API Gateway will return a 500 error.


:rotating_light: :warning: Under the API Key Source section in the Settings pane for API Gateway console, choose AUTHORIZER from the drop-down list. Save changes and then you need to redeploy your service 

## Install Serverless CLI

https://www.serverless.com/framework/docs/getting-started/

## Contributing

```
# Invoke chronos locally
serverless invoke local --function hello_world

# Install Deps
npm install serverless-offline --save-dev


# Run offline locally
serverless offline start
```

## To deploy funtion from local

```
# Deploy functions from local
sls deploy --aws-profile "dev"

# Remove the functions on current context
sls remove --aws-profile "dev"
```

