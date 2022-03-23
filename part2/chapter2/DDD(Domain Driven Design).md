# DDD(Domain Driven Design)

- 기획자, 마케터, 개발자, 디자이너의 관점이 각각 다르기 때문에 의사소통 시 차이가 있을 수 밖에 없음
	- 소프트웨어 개발과 도메인, 모델과의 불일치 발생
	- 기획과 개발의 불일치 발생

## DDD
- 보편언어 사용
	- 도메인에 대한 어휘를 이해관계자(기획자, 개발자 등)들이 공통적으로 이해할 수 있도록 정의
- 모델 주도 설계
	- 도메인 분석과 설계의 간극을 최소화
	- 분석/설계/구현의 모든 단계를 관통하는 하나의 모델 유지
	- 모델과 코드를 동일하게 만들자

### 전략적 설계
- 비즈니스의 상황(context)에 맞게 설계
- 모든 context를 이벤트 스토밍을 통해서 공유
- 각 context를 그룹핑(Bounded Context)
- 컨택스트 매핑을 통해서 Bounded context 간의 관계 정의
- 결과물: 도메인 모델(서비스를 추상화한 설계도)

### 전술적 설계
- 전략적 설계보다 더 상세한 부분 모델링
- Model driven design
- Aggregate pattern
	- aggregate: 서로 관련이 있는 도메인 모델들의 집합
- 계층형 아키텍처를 통한 도메인 모델 분리
- 도메인 이벤트를 통해 도메인을 보다 명확히 모델링
