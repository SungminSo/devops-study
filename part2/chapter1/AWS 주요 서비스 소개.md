# AWS 주요 서비스 소개

1. **가상 컴퓨팅 서비스**
	- EC2(elastic) : 사양과 크기를 조절할 수 있는 컴퓨팅 서비스
	- Lightsail : 가상화 프라이빗 서버
		- EC2랑 비슷하지만 프라이빗에 좀더 초점이 있다고 보면 됨
	- Auto Scaling : 서버의 특정 조건에 따라 서버를 추가/삭제할 수 있게 하는 서비스
	- Workspaces : 사내 pc를 가상화로 구성하여, 문서를 개인 pc에 보관하는 것이 아니라 서버에 보관하게 하는 서비스
		- dropbox를 가상으로 지원해주는 서비스라고 보면 됨

2. **네트워킹 서비스**
	- Route 53 : DNS 웹서비스
		- 도메인 구입을 간편하게 할 수 있음
	- VPC : 가상 네트워크를 클라우드 내에 생성/구성
	- Direct Connect : On-premise 인프라와 aws를 연결하는 네트워킹 서비스
	- ELB : 부하 분산(로드 밸런싱) 서비스
		- Auto Scaling과 비슷하게 부하를 분산해주지만, 차이점은 Auto Scaling은 서버를 여러대 생성해서 부하를 분산시키는 방식이고, ELB는 네트워킹 방식을 통해서 부하를 분산시킴

3. **스토리지/데이터베이스 서비스**
	- S3 : 여러가지 파일을 형식에 상관없이 저장
	- RDS : 가상 SQL DB 서비스
	- DynamoDB : 가상 NoSQL DB 서비스
	- ElastiCache : in-memory 기반의 cache 서비스

4. **데이터 분석 & AI 서비스**
	- Redshift : 데이터 분석에 특화된 스토리지 시스템
	- EMR : 대량의 데이터를 효율적으로 가공 및 처리
		- mapReduce 방식으로 처리
	- Sagemaker : 머신 러닝 & 데이터분석을 위한 클라우드 환경 제공
		- jupyter notebook같은 환경 제공