# Route53 도메인 등록과 DNS의 동작원리

## 도메인 등록 프로세스
- 등록자 -> 등록대행자(Route53 등) -> 등록소 (Top level domain) -> ICANN (Root name server)

## DNS 동작원리
- ex. fast-devops.com
1. pc에서 local DNS 서버로 요청
2. local DNS 서버에서 해결되지 않을 경우 ICANN (Root name server)로 요청 
3. `.com`으로 등록소(Top level domain) 판단해서 해당 DNS 서버로 요청하게끔 응답
4. 해당 등록소에서 DNS server 확인 및 ip 주소 local DNS 서버에 캐싱한 후 클라이언트에게 응답

## Route 53을 활용한 http 설정
1. ec2 인스턴스가 타깃으로 잡힌 타깃그룹 생성
2. 해당 타깃그룹을 로드밸런서의 리스너에 연결
	- 로드밸런서를 연결하는 가장 큰 이유는 사용자가 http 기본포트로 서버에 접속할 수 있도록 하기 위함(사용자는 포트를 모르기 때문에)

## Route 53을 활용한 https 설정
1. http와는 다르게 서버 보안인증서 필요
2. ACM에서 인증서 발급받은 후 Route 53과 연결
	- DNS 검증방식으로 했을 경우 CNAME 유형의 레코드 추가됨
3. 로드밸런서 리스너에서 443 포트의 리스너 추가
	- 여기서 인증서는 2번에서 발급받은 인증서 사용