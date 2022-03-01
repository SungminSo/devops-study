# VPC endpoint

- private 서브넷에 있는 인스턴스를 위한 서비스
- 두가지 종류(gateway / interface endpoint)가 있음
- NAT gateway를 통해서 S3나 dynanoDB에 접근해도 됨
	- 가능하긴 하지만 되도록이면 그 방법은 안쓰는게 좋음
	- 그 이유는 트래픽이 외부에 노출이 되기 때문
	- 보안상의 이유로 트래픽 노출은 안하는게 좋음

## gateway endpoint
- S3나 DynanoDB에 연결하기 위한 VPC endpoint 유형
- 생성 시 public 라우팅 테이블에 `vpce`라는 prefix를 달고 있는 대상이 하나 생성됨
- 라우팅 테이블에 대상이 추가된것의 의미는 S3나 DynanoDB에 접근하는 트래픽은 VPC endpoint를 통해서 연결하겠다는 의미
- NAT gateway를 사용하는 경우 vpc endpoint 대상 아래에 생성해야 우선순위를 알맞게 사용할 수 있음
	
