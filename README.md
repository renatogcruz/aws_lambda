# AWS Lambda

#### GitHub Action | [AWS Lambda Deploy](https://github.com/marketplace/actions/aws-lambda-deploy) | lambda-action

[GitHub Action](https://docs.github.com/en/actions) for deploying Lambda code to an existing function

![infra](https://github.com/renatogcruz/aws_lambda/assets/32683908/d487eaaa-1f7c-4ed8-83ae-587f88148988)

#### Usage

Upload zip file to AWS Lambda function.

```
name: deploy to lambda
on: [push]
jobs:

  deploy_zip:
    name: deploy lambda function
    runs-on: ubuntu-latest
    strategy:
      matrix:
        go-version: [1.13.x]
    steps:
      - name: checkout source code
        uses: actions/checkout@v1      
      - name: Generate Zip
        run: |
          zip deployment.zip *.py
      - name: default deploy
        uses: appleboy/lambda-action@master
        with:
          aws_access_key_id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws_secret_access_key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws_region: ${{ secrets.AWS_REGION }}
          function_name: primeirFuncao
          zip_file: deployment.zip
```
---

Reference:

- https://github.com/alura-cursos/aws-lambda-alura
