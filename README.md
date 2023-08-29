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
      - name: Install Go
        uses: actions/setup-go@v1
        with:
          go-version: ${{ matrix.go-version }}
      - name: Build binary
        run: |
          cd example && CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -v -a -o main main.go && zip deployment.zip main
      - name: default deploy
        uses: appleboy/lambda-action@master
        with:
          aws_access_key_id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws_secret_access_key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws_region: ${{ secrets.AWS_REGION }}
          function_name: gorush
          zip_file: example/deployment.zip
          memory_size: 128
          timeout: 10
          handler: foobar
          role: arn:aws:iam::xxxxxxxxxxx:role/test1234
          runtime: python11.x
```
