# AWS 네트워킹의 동작원리

## VPC 특징
- 계정 생성 시 default VPC 생성됨
- 서브넷 구성 가능
- 보안 설정(IP block, inbound/outbound 설정) 가능
- VPC peering 가능
- IP 대역 지정 가능
- 하나의 Region으로 확장 불가능 => 하나의 Region에 종속됨

## VPC 구성요소
- **Availability Zone (AZ)**
	- AWS가 운영하는 데이터센터
	- 각 리전에 종속되어 있는 요소
	- 자연재해, 인재 등으로 인해 서비스가 중단되는 것을 막기위해 각 AZ는 일정 거리 이상 떨어져있고, 하나의 리전은 2개 이상의 AZ로 구성됨
- **Subnet(CIDR)**
	- 하나의 AZ에서만 생성가능하고, 하나의 AZ안에서는 여러개의 subnet 생성 가능
	- private / public subnet으로 구분됨
- **Internet Gateway**
	- VPC 내부의 IP 주소를 배정받은 서비스들과 외부 인터넷과의 매개체
	- private subnet은 IGW로 연결하지 않음
	- 프로세스: internet <-> Internet Gateway <-> Router <-> VPC Subnet(public)
- **Route Table**
	- 트래픽이 어디로 가야할지 알려주는 테이블
	- VPC 생성 시 자동으로 생성됨
	- 10.0.0.0/16 -> local로 연결됨
	- 0.0.0.0/16 -> IGW로 연결됨
- **NACL(Network Access Control List) / security group**
	- VPC 서브넷과 서비스 인스턴스의 보안 설정
	- NACL -> stateless / SG -> stateful
	- access block(특정 ip만 차단)은 NACL에서만 가능
	- SG는 VPC 내에서의 설정값으로 봐도됨
	- 프로세스: internet <-> Internet Gateway <-> Router <-> Route Table <-> NACL <-> (SG <->) VPC subnet(public)
- **NAT (Network Address Translation) instance / NAT gateway**
	- public subnet과 private subnet의 차이점은 IGW 연결 유무
	- private subnet에는 보통 DB 인스턴스, 또는 보안적으로 중요한 것들을 위치시킴
	- private subnet 내의 인스턴스에 내에서 특정 서비스 또는 라이브러리를 받아야하는 경우 등이 생기기 때문에 인터넷 연결이 필요한 경우가 있음. 그런 경우 public subnet을 통해 우회해서 외부 인터넷과 연결하게 됨
	- public subnet을 통해 우회해서 외부 인터넷과 연결하는 방법이 크게 두가지가 있음 -> NAT gateway / NAT Instance
	- NAT Instance는 public subnet 내에 있는 EC2 인스턴스
	- NAT Gateway는 public subnet을 통한 우회를 위해 AWS에서 제공하는 서비스
	- 프로세스(NAT Gateway): private subnet EC2 -> NACL -> Route Table -> Router -> Route Table -> NACL -> public subnet(NAT Gateway) -> NACL -> Route Table -> Router -> Internet Gateway -> internet
	- bastion host
		- vpc 외부에서 private subnet 내부에 접근하기 위한 방법(ex. 관리자가 서버에 접근해야하는 경우)
		- NAT Gateway와는 반대로 외부 인터넷 -> private subnet 방향
- **VPC endpoint**
	- VPC endpoint를 통해 AWS 서비스 및 VPC endpoint 서비스에 비공개로 연결할 수 있음
	- VPC의 인스턴스는 서비스의 리소스와 통신하는데 public ip 주소가 필요하지 않고, VPC와 기타 서비스 간의 트래픽은 amazon 네트워크를 벗어나지 않을 수 있음 
	- private subnet의 경우는 amazon 네트워크 내에 격리된 공간인데, 그 상황에서도 aws의 다양한 서비스들(== 외부 인터넷 접근)에 연결할 수 있도록 지원하는 서비스
	- **Interface Endpoint** : private ip를 만들어 서비스로 연결해줌 (SQS, SNS, Kinesis, Sagemaker 등 지원)
	- **Gateway Endpoint** : 라우팅 테이블에서 경로의 대상으로 지정하여 사용 (S3, Dynamodb 지원)

