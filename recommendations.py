# AI 종류: ChatGPT
# AI 사용 목적: 9팀 항공편 맞춤 공항 안내 프로그램의 설계 및 구현
# 사용한 AI 프롬프트: 이거 팀프로젝트 발표인데 8페이지에 나와있는 12주차 13주차 완성해야하는데 팀원을 역할 분담해서 각자 맡을 코드(파이썬으로만)를 주고 구현 까지 할 수 있는 코드를 짜주고 팀원(전재균,김기범,최민호,장태현)에게 각각 코드를 줘 그리고 우리 팀 깃허브의 커밋해서 통합하는 방법까지 알려줘
# 추가 AI 프롬프트: 그럼 시설 추천도 넣어줘 우리 팀프로젝트 파악해서 코드 다시 짜줘
# 추가 AI 사용 목적: 터미널·검색대 방향별 시연 시설 추천
# AI 요청자: 장태현
# AI 사용 날짜: 2026-11-23

"""김기범 담당 — 혼잡도 판정과 주변 시설 추천."""


def congestion_level(wait_time):
    if wait_time < 10:
        return "원활"
    if wait_time < 15:
        return "보통"
    return "혼잡"


# 발표용 예시 데이터. 실제 매장 위치나 운영 시간은 공항 안내를 확인한다.
# 각 항목은 (시설명, 종류, 예시 위치) 순서다.
FACILITIES_BY_CHECKPOINT = {
    ("제1여객터미널", "동편 보안검색대"): [
        ("카페", "음료", "보안검색 전 동편"),
        ("편의점", "편의", "보안검색 전 동편"),
    ],
    ("제1여객터미널", "서편 보안검색대"): [
        ("카페", "음료", "보안검색 전 서편"),
        ("푸드코트", "식사", "보안검색 전 서편"),
    ],
    ("제2여객터미널", "동편 보안검색대"): [
        ("한국전통문화센터", "문화", "보안검색 후"),
        ("면세구역 카페", "음료", "보안검색 후"),
        ("푸드코트", "식사", "보안검색 후"),
    ],
    ("제2여객터미널", "서편 보안검색대"): [
        ("카페", "음료", "보안검색 전 서편"),
        ("식당", "식사", "보안검색 전 서편"),
    ],
}


def recommended_facilities(flight):
    if flight.wait_time < 15:
        return []

    location = (flight.terminal, flight.checkpoint)
    facility_details = FACILITIES_BY_CHECKPOINT.get(location, [])
    allowed_names = set(flight.facilities)
    return [
        f"{category} · {name} ({area})"
        for name, category, area in facility_details
        if name in allowed_names
    ]
