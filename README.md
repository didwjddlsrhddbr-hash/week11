# (성적 CSV 검사)




  README 여섯 항목 양식입니다. (실습 PPT 28쪽 · 학습지 ⑤와 같은 순서)
  1. 이 파일의 이름을 README.md 로 바꾼 뒤 아래 칸을 채웁니다.
  2. <!-- 로 시작하는 설명은 다 채운 뒤 지웁니다.
  3. 명령은 직접 실행해 보고, 실제로 나온 결과만 적습니다.
  4. 공개 저장소이므로 학번·연락처는 적지 않습니다. (학번은 학습지에만)
  5. 각 칸의 내용은 설명이 끝나는 줄 아래 빈 줄에 적습니다. (설명 안에 쓰면 GitHub에 보이지 않습니다)

  판정 기준: 처음 보는 사람이 이 문서만 보고 실행과 테스트를 할 수 있는가.
  (게시 후 새 폴더에 clone해 이 문서대로 직접 실행해 봅니다)


## ① 무엇을 하나요 (What · 현재 상태)



  성적CSV를 읽어 유효한 점수 목록, 제외한 행의 기록을 반환. + 지금 되는 것 - 0~100 정수 점수 검증, 따옴표 안 쉼표가 든 이름(`"최,네번"`) 처리, 빈 줄 무시, 같은 이름 모두 보관, 없는 파일은 `FileNotFoundError`, 제목 줄만 있는 파일은 빈 목록 반환/ 안 되는 것 - 평균·학점 계산은 아직 하지 않는다.
  

## ② 왜 만들었나요 (Why)


  여러 명의 성적을 기준에 맞는 지 검사하여 유효 데이터와 제외된 데이터의 제외 이유를 확인하기 위해 제작.

## ③ 어떻게 쓰나요 (How)


python --version
python -m pip install --user -U pytest~=7.0 pytest-cov
set PYTEST_DISABLE_PLUGIN_AUTOLOAD=1
python load_scores.py scores.csv

예상 결과: (예상 결과: 유효 5개 / 제외 5개)

## ④ 어떻게 테스트하나요


python -m pytest test_load_scores.py -v → 12 passed
test_bug_A.py·test_bug_B.py는 find_max 버그를 찾아 2개, 1개 찾아 실패
test_bug_A.py·test_bug_B.py는 AI 최초 응답을 보존한 비교용 파일이다.

test_bug_A.py·test_bug_B.py는 AI 최초 응답을 보존한 비교용 파일이다.

## ⑤ 파일 구성

| load_scores.py | (CSV를 읽어 (kept, skipped)를 돌려주는 함수)|
| scores.csv · empty.csv · weird.csv |예제 데이터 (정상 / 제목 줄만 있는 파일 / 잘못된 행이 섞인 파일)|
| test_load_scores.py |기본 테스트 (보강 1개 포함 12개)  ||
| bug3_logic.py · test_bug_A.py · test_bug_B.py | AI 실험용 find_max(일부러 버그 있음)와 AI가 만든 테스트 원본 |
| prompts.txt | AI 실험에 쓴 요청문 
|LICENSE gitignore 라이선스 / Git이 추적하지 않을 파일 목록

## ⑥ 만든 사람과 AI 사용

- 만든 사람 : (이름 또는 GitHub 아이디)
- 사용한 AI 도구·모델 : VS Code Copilot Chat (대화형)
- AI에게 도움받은 부분 : test_bug_A, test_bug_B(코드를 준 A, 명세를 준 B)
- 내가 직접 판단·확인한 부분 : AI가 만든 테스트의 기대값을 명세와 대조, 기본 테스트 test_load_scores.py를 직접 실행해 12 passed 확인

## 라이선스

MIT License (LICENSE 파일 참고)