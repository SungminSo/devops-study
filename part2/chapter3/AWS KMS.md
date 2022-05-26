# AWS KMS

## 데이터 암호화
### client-side 암호화
- '내'갸 직접 암호화 키 관리
- 암호화 키 관리툴로 AWS의 KMS(Key Management Service)를 사용할 수 있음

### server-side 암호화  	
- AWS가 알아서 서버에 저장된 데이터를 암호화
- 암호화 키를 자동으로 관리
	- AWS의 KMS가 자동으로 사용됨
- S3, RDS, DynamoDB, Redshift 등은 모두 암호화 기능을 기본으로 갖추고 있음


## KMS (Key Management Service)
- AWS의 encryption key(암호화 키)를 관리해주는 서비스
- 관리하는 암호화 키는 CMK(Customer Master Key)라고 부름
	- CMK는 region 설정이 필수 -> CMK는 각 리전별 KMS에서 관리됨
	- CMK를 통해서는 최대 4KB의 데이터만 암호화 가능
	- 더 큰 데이터를 암호화 할때는 CMK가 아닌 data key 활용
- CMK를 HSMs(Hardware Security Modules)라는 저장소에 저장
- HSMs에 있는 CMK를 활용하기 위해 KMS API 사용
- AWS Cloudtrail로 누가 어떤 Key를 어떻게 사용했는지 로그 남김
- KMS는 CMK만 관리하고 data key는 관리하지 않음
- data key는 CMK를 통해서만 생성 가능하고, 하나의 CMK로 여러개의 data key 생성 가능
- 즉, 큰 데이터 암호화 시 CMK에서 Encryption algorithm을 통해서 data key를 2개 생성(plaintext data key와 encrypted data key)
- plaintext data key를 활용해서 암호화하고, 암호화가 완료되면 해당 plaintext data key는 삭제
- 이후에 복호화 시에는 encrypted data key로 바로 복호화 할 수는 없고, CMK를 통해서 encrypted data key를 다시 plaintext data key로 바꿔준 후 데이터 복호화


## KMS 활용 실습
- 키 구성 시 키 유형은 `대칭`인것이 조금 더 편함
- 키 권한에서 사용자는 데이터 복호화만 가능하고, 관리자는 그 외의 모든 기능도 사용가능
- 코드내에서 외부에 노출되면 안되는 문자열(ex. boto3 access key/secret key) 등을 암호화해서 코드 또는 해당 서버 어딘가에 저장하고, 사용할 때 복호화해서 사용