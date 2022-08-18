# AWS CodeCommit

## AWS CodeCommit
- Github와 유사한 VCS
	- git 기반의 리포지토리 호스팅 
- S3에 모든 코드를 암호화(AWS KMS)하여 저장
- IAM 인증으로 push/pul에 대한 권한 관리

## CodeCommit 사용방법
1. IAM 유저 생성
	- "CodeCommit" 관련 정책 설정 필요
2. 보안 자격 증명에서 awscodecommit에 대한 https 키 설정
3. 로컬에 aws-cli 설치 및 configure
4. codeCommit 서비스 들어가서 리포지토리 생성
5. 로컬에서 git clone