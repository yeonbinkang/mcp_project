from flask import Flask, request, jsonify
import requests
from mcp.server.fastmcp import FastMCP

JETBOT_IP = "192.168.0.119"  # JetBot의 IP 주소
JETBOT_PORT = 5000  # JetBot Flask 서버 포트
JETBOT_EXECUTE_ENDPOINT = f"http://{JETBOT_IP}:{JETBOT_PORT}/execute"

mcp = FastMCP(
    "JetBot Controller",
    instructions="사용자의 자연어 명령을 기반으로 JetBot을 제어하는 코드를 생성하고 실행합니다.",
    host="0.0.0.0",
    port=8005
)

@mcp.tool()
def move_forward(duration: float, speed: float = 0.5) -> str:
    code = (
        f"from jetbot import Robot\n"
        f"import time\n"
        f"robot = Robot()\n"
        f"robot.forward({speed})\n"
        f"time.sleep({duration})\n"
        f"robot.stop()"
    )
    return execute_jetbot_code(code)

@mcp.tool()
def move_backward(duration: float, speed: float = 0.5) -> str:
    code = (
        f"from jetbot import Robot\n"
        f"import time\n"
        f"robot = Robot()\n"
        f"robot.backward({speed})\n"
        f"time.sleep({duration})\n"
        f"robot.stop()"
    )
    return execute_jetbot_code(code)

@mcp.tool()
def turn_left(duration: float, speed: float = 0.5) -> str:
    code = (
        f"from jetbot import Robot\n"
        f"import time\n"
        f"robot = Robot()\n"
        f"robot.left({speed})\n"
        f"time.sleep({duration})\n"
        f"robot.stop()"
    )
    return execute_jetbot_code(code)

@mcp.tool()
def turn_right(duration: float, speed: float = 0.5) -> str:
    code = (
        f"from jetbot import Robot\n"
        f"import time\n"
        f"robot = Robot()\n"
        f"robot.right({speed})\n"
        f"time.sleep({duration})\n"
        f"robot.stop()"
    )
    return execute_jetbot_code(code)

def execute_jetbot_code(code: str) -> str:
    try:
        response = requests.post(
            JETBOT_EXECUTE_ENDPOINT,
            json={"code": code},
            timeout=10
        )
        result = response.json()
        return f"JetBot 응답: {result}"
    except requests.exceptions.RequestException as e:
        return f"JetBot 전송 실패: {str(e)}"

if __name__ == "__main__":
    mcp.run()
