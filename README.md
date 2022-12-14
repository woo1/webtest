postgres local install : https://postgresapp.com/ <br>
비밀번호 및 접속 설정 : https://hgko1207.github.io/2020/09/11/postgresql-2/

## 1. password setting
// postgres 계정으로 접속 <br>
su - postgres psql

// 비밀번호 설정 <br>
\password postgres

// 방화벽 개방 <br>
firewall-cmd --permanent --zone=public --add-port=5432/tcp <br>
firewall-cmd --reload <br>

postgresql.conf <br>
listen_addresses = '*'

<br>
테이블명 소문자 안하면 FROM "TABLE_ID"