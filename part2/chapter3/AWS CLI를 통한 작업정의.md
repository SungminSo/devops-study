# AWS CLI를 통한 작업정의


## aws 자격증명
- aws configure
- aws ecr get-login --no-include-email --region ap-northeast-2
    
## aws ecr 레포지토리 생성
- aws ecr create-repository --repository-name _hello-world_ --region ap-northeast-2
    
## aws iam role 생성
- role에 대한 정보가 담긴 json
	- ```
	{
	    "Version": "2012-10-17",
	    "Statement": [
	        {
	            "Sid": "',
	            "Effect": "Allow",
	            "Principal": {
	                "Service" "ecs-tasks.amazonaws.com"
	            },
	            "Action": "sts:AssumeRole"
	        }
	    ]
	}
	```
- iam 생성
	- aws iam create-role --role-name _ecsTaskExecutionRole_ --assume-role-policy-document _file://ecs-tasks-trust-policy.json_
- 현재 사용하고 있는 user에 연결
	- aws iam attach-role-policy -role-name _ecsTaskExecutionRole_ --policy-arn arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy
    
## aws ecs 클러스터 생성
- 클러스터 생성
	- aws ecs create-cluster --cluster-name _cli-fargate_
	- 옵션으로 cluster-name만 주더라도 default로 fargate 유형으로 클러스터 생성
-  작업 정의 등록
	- aws ecs register-task-definition --cli-input-json _file://$HOME/tasks/fargate-task.json_
	-  ```
	 _file://$HOME/tasks/fargate-task.json_
	{
	    "family": "sample-fargate", 
	    "networkMode": "awsvpc", 
	    "executionRoleArn": "ecsTaskRole",
	    "containerDefinitions": [
	        {
	            "name": "fargate-app", 
	            "image": "public.ecr.aws/docker/library/httpd:latest", 
	            "portMappings": [
	                {
	                    "containerPort": 80, 
	                    "protocol": "tcp"
	                }
	            ], 
	            "essential": true, 
	            "entryPoint": [
	                "sh",
			"-c"
	            ], 
	        }
	    ], 
	    "requiresCompatibilities": [
	        "FARGATE"
	    ], 
	    "cpu": "256", 
	    "memory": "512"
	}
	 ```
      
## aws ecs 클러스터 서비스 생성	
- 프라이빗 서브넷 사용
	- aws ecs create-service --cluster _cli-fargate_ --service-name _cli-fargate-service_ --task-definition _sample-fargate:1_ --desired-count 1 --launch-type "FARGATE" --network-configuration "awsvpcConfiguration={subnets=[subnet-abcd1234],securityGroups=[sg-abcd1234]}"
- 퍼블릭 서브넷 사용
	- aws ecs create-service --cluster _cli-fargate_ --service-name _cli-fargate-service_--task-definition _sample-fargate:1_ --desired-count 1 --launch-type "FARGATE" --network-configuration "awsvpcConfiguration={subnets=[subnet-abcd1234],securityGroups=[sg-abcd1234],assignPublicIp=ENABLED}" 

## aws ecs 클러스터 서비스 삭제
- aws ecs delete-service --cluster _cli-fargate_ --service _cli-fargate-service_ --force
	
	 