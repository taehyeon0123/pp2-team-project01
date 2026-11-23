# AI 종류: ChatGPT
# AI 사용 목적: 9팀 항공편 맞춤 공항 안내 프로그램의 설계 및 구현
# 사용한 AI 프롬프트: 이거 팀프로젝트 발표인데 8페이지에 나와있는 12주차 13주차 완성해야하는데 팀원을 역할 분담해서 각자 맡을 코드(파이썬으로만)를 주고 구현 까지 할 수 있는 코드를 짜주고 팀원(전재균,김기범,최민호,장태현)에게 각각 코드를 줘 그리고 우리 팀 깃허브의 커밋해서 통합하는 방법까지 알려줘
# AI 요청자: 장태현
# AI 사용 날짜: 2026-11-23

"""장태현 담당 — 프로그램 실행, 모듈 통합, JSON 기록 저장."""
from datetime import datetime
import json
from pathlib import Path

HISTORY_FILE = Path(__file__).resolve().with_name("search_history.json")


def save_search(flight, level, facilities, history_file=HISTORY_FILE):
    if history_file.exists():
        with open(history_file, "r", encoding="utf-8") as file:
            history = json.load(file)
        if not isinstance(history, list):
            raise ValueError("기록 파일의 내용은 JSON 목록이어야 합니다.")
    else:
        history = []

    history.append({
        "searched_at": datetime.now().isoformat(timespec="seconds"),
        "number": flight.number,
        "airline": flight.airline,
        "destination": flight.destination,
        "terminal": flight.terminal,
        "checkpoint": flight.checkpoint,
        "wait_time": flight.wait_time,
        "congestion": level,
        "facilities": facilities,
    })

    # 기존 기록은 새 JSON을 모두 쓴 뒤에 교체한다.
    temporary_file = history_file.with_suffix(".tmp")
    with open(temporary_file, "w", encoding="utf-8") as file:
        json.dump(history, file, ensure_ascii=False, indent=2)
        file.write("\n")
    temporary_file.replace(history_file)


def main():
    import tkinter as tk

    from flights import load_sample_flights
    from gui import AirportGuideApp

    root = tk.Tk()
    AirportGuideApp(root, load_sample_flights(), save_search)
    root.mainloop()


if __name__ == "__main__":
    main()
