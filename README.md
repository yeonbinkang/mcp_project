# 📦 설치 방법

### ✅ 1. 저장소 클론

```bash
git clone https://github.com/yeonbinkang/mcp_project.git
cd langgraph-mcp-agents
```

---

### ✅ 2. 가상환경 생성 및 패키지 설치 (uv 사용)

```bash
uv venv
uv pip install -r requirements.txt
```

> 🔍 **Windows 사용자**는 다음 명령어로 가상환경을 활성화하세요:

```powershell
.venv\Scripts\activate
```

> 💡 Mac 또는 Linux 사용자는 아래 명령어를 사용하세요:

```bash
source .venv/bin/activate
```

---

### ✅ 3. 환경변수 설정 파일 `.env` 만들기

`.env.example` 파일을 참고하여 `.env` 파일을 생성하고, 다음과 같이 API 키를 설정하세요:

```
ANTHROPIC_API_KEY=your_anthropic_api_key
OPENAI_API_KEY=your_openai_api_key  # (선택 사항)
TAVILY_API_KEY=your_tavily_api_key  # (선택 사항)

LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_API_KEY=your_langsmith_api_key
LANGSMITH_PROJECT=your_langsmith_project
```

> 🔐 `.env` 파일은 외부에 노출되지 않도록 `.gitignore`에 추가하는 것을 잊지 마세요.

---

# 🚀 사용 방법

### ✅ Streamlit 앱 실행

```bash
streamlit run app.py
```

앱이 실행되면 브라우저가 자동으로 열리며 인터페이스가 표시됩니다.  
이제 LLM과 MCP agent 기반 기능을 직접 테스트해볼 수 있습니다.
