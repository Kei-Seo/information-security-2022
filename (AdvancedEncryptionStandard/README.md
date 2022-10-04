AES (Advanced Encryption Standard)
• DES를 대체하기 위한 차세대 암호 표준
• 2001년 선정 (NIST-FIPS-197, ISO/IEC 18033-3)
• 당시 경쟁자들
• Rijndael  최종 선정
• MARS, RC6, Serpent, Twofish

• 블록암호를 이용한 암호 통신기 완성하기
  - 이미 구현된 것들
  - 네트워크 코드 (소켓 등…)
  - 서버 (암호화 잘 되고 있는지…)
  - 구현 해야 하는 것들
  - 입력 처리기 뒷단  메세지 송/수신 전에 해야하는 암호화 처리
  - AES 암복호화 코드 (직접구현 x, 라이브러리 사용!)
  - pyCryptodome: pip install pycryptodome
