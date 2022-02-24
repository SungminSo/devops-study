# NACL 설정하기

## AWS 인스턴스 보안 설정 방법
- NACL : stateless
- Security Group : stateful  

## Security Group
- Inbound/Outbound 정보를 가지고 있음
- Inbound로 80번 포트가 열려있고, Outbound는 none으로 모두 닫혀있는 경우, 80번 포트로 들어온 request는 해당 트래픽이 기억되기 때문에 outbound가 none일지라도 response가 나갈 수 있음

## NACL
- Security Group과 마찬가지로 Inbound/Outbound 정보를 가지고 있음
- Inbound로 80번 포트가 열려있고, Outbound는 none으로 모두 닫혀있는 경우, 80번 포트로 들어온 request는 outbound가 모두 닫혀있기 때문에 response가 나갈 수 없음
- Security Group보다는 조금 더 엄격하게 적용된다고 볼 수 있음
- Inbound/Outbound 규칙에서 규칙번호는 우선순위의 의미를 가짐(숫자가 작을수록 우선순위가 높음)
- Outbound 규칙에서 포트 범위를 1024 ~ 65535로 주는 이유는 request->reponse 하는 쪽에서 사용하는 임시 포트의 범위에 해당하기 때문