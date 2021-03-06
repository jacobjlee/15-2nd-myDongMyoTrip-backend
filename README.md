
## ⛩ My Dongmyo Trip ( 마이동묘트립 )

- [마이리얼트립] https://www.myrealtrip.com/
- 기업 소개: 마이리얼트립은 여행을 떠나기 위해 필요한 모든 것을 쉽고, 빠르게 검색하고 예약할 수 있는 국내 최고의 자유여행 플랫폼입니다. 항공권, 숙박, 에어텔 상품을 비롯하여 전세계 680여개 도시 20,000여개의 현지 투어&티켓 상품을 제공하고 있습니다.

## 👨‍👩‍👧‍👦 팀원

힙스터의 성지 동묘 앞에서 위벤저스 결성!

- Front-end: 김해인(PM), 이하영, 안미현
- Back-end: 우혁준, 이주형

## 📅 개발 기간

- 기간: 2020.12.28 ~ 2021.01.08 (11일)

## 🧑‍💻 적용 기술

- Front-end: React.js, React(CRA), React-router, Styled-Components, Hooks
- Back-end: Django, Python, MySQL, jwt, bcrypt, AWS
- communication: Git, Trello, Slack

## 💁‍♀️ 구현 기능

### Front-end

#### 회원가입, 로그인

- 이메일인증 회원가입, 로그인, 이용약관 체크박스 구현
- 카카오를 통한 회원가입, 로그인
- 로그인 성공시 메인페이지로 이동

#### 헤더 및 메인페이지

- 로그인시 헤더가 로그아웃으로 바뀌는 동적라우팅
- 특정 페이지에는 다른 버젼의 헤더 렌더링
- 슬라이더 라이브러리를 사용한 메인페이지 구현

#### 항공권

- 슬라이더 라이브러리 사용한 항공권 메인페이지 레이아웃 구현
- 백엔드 데이터를 통한 항공권 도시선택 메뉴 구현
- 날짜 라이브러리 사용
- 기본 성인 1명 기준 최대 9명 예약가능 인원수 체크박스 구현
- 백엔드 데이터를 이용한 항공권 리스트
- 쿼리스트링을 이용한 항공권 필터기능

#### 숙소

- 숙소 메인페이지 레이아웃 완벽구현
- 백엔드 데이터를 이용한 숙소 리스트페이지 구현
- 상단 메뉴 날짜선택창, 인원수 체크박스 구현
- 쿼리스트링을 통한 좌측 모든 필터기능 구현
- 하단 페이지네이션 구현
- 백엔드 데이터를 이용한 숙소 상세페이지 구현
- 상단 메뉴 날짜 선택창, 인원수 체크박스 구현
- 지도보기 클릭시 새탭으로 보기 구현
- 상세정보 더보기 구현
- 위시리스트 모달창 좋아요 클릭기능
- 숙소 선택시 모달창에 정보 업데이트 기능 구현

#### 의외 부가적인 기술

- styled component 사용시 globalStyles.js , theme,js 를 통한 통일적인 레이아웃 구현

### Back-end

#### 회원가입
- 정규표현식 유효성 검사 모듈화 한 것을 import하여 사용
- Bcrypt로 비밀번호 암호화, JWT로 토큰 인가 구현
- SMTP를 이용한 회원가입 이메일 인증 구현

#### 로그인 
- 카카오 소셜 로그인

#### 항공권 리스트
- 날짜별 목록 반환하는 항공권 리스트 API 구현
- 쿼리 스트링으로 다중 필터링, 정렬, 검색 구현

#### 숙소 리스트
- 숙소 리스트페이지 모든 필터기능 구현
- select_related 와 prefetch_related를 사용한 데이터 참조
- Limit과 offset를 사용한 pagenation 구현

#### 숙소 상세 
- 숙소 상세페이지 구현
- 숙소 상세 페이지 필터 구현
- Path Parameter를 선언해 RESTful API 구현
- Query string parameter 구현

## 🎥 영상

[클로닝 동영상](https://youtu.be/Ni-htqkWnf4)

## 💎 레퍼런스

- 이 프로젝트는 [MyRealTrip](https://www.myrealtrip.com/) 사이트를 참조하여 학습목적으로 만들었습니다.
- 실무수준의 프로젝트이지만 학습용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.
- 이 프로젝트에서 사용하고 있는 사진 일부분은 위코드에서 구매한 것 이므로 해당 프로젝트 외부인이 사용할 수 없습니다.
