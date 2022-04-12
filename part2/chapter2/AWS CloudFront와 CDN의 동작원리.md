# AWS CloudFront와 CDN의 동작원리

## CloudFront
- Cache + CDN
- 기본적으로는 Cache 서버
- Cache 서버는 전세계에 흩어져있는 인프라를 활용하기 때문에 추가적으로 CDN의 기능도 보유
- 웹서버의 비용을 감소시키며, 전 서계의 유저를 대상으로 고속으로 웹서비스를 제공하도록 하는 서비스

## CDN (Content Delivery Network)
- 전세계 어느 위치에서 접속하더라도 빠른 속도로 서비스할 수 있도록 하는 서비스
- 전세계에 흩어져있는 Edge Location(캐시 서버) 활용

## CloudFront를 활용한 Route 53 설정
- 기존 route 53의 라우팅 대상으로 elb를 넣었던것에서 수정
- 라우팅 대상을 elb에서 cloudfront로 변경
- cloudfront에서 원본 도메인으로 elb 선택
- cloudfront에서 캐시 동작 설정