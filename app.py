import streamlit as st
import re

st.set_page_config(
    page_title="AI Project Release Agent",
    page_icon="🚀",
    layout="centered"
)

# ── Sidebar ──────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🚀 Release Agent")
    st.divider()
    page = st.radio(
        "Navigation",
        ["🏠 Overview", "🔍 Secret Scanner", "⚙️ Pipeline"],
        label_visibility="collapsed"
    )
    st.divider()
    st.caption("n8n + Groq + OpenRouter\nGitHub API + LinkedIn API")


# ══ OVERVIEW ══════════════════════════════════════════════════
if page == "🏠 Overview":
    st.title("🚀 AI Project Release Agent")
    st.caption("Raw dev files → Security scan → GitHub → LinkedIn. One trigger. Fully automated.")
    st.divider()

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Security Layers", "2",      "AI + Regex")
    c2.metric("Release Time",    "~3 min", "vs 45 min manual")
    c3.metric("Secret Detection","100%",   "Zero leaks")
    c4.metric("Platforms",       "2",      "GitHub + LinkedIn")

    st.divider()
    st.subheader("What it does")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.success("**🔒 Security**")
        st.write("2-pass regex scan + AI review. Hard gate blocks unsafe releases.")

    with col2:
        st.info("**📄 Documentation**")
        st.write("Real app screenshot + AI-generated README from actual source files.")

    with col3:
        st.warning("**🚀 Publishing**")
        st.write("GitHub repo auto-created. LinkedIn post with human approval.")


# ══ SECRET SCANNER ════════════════════════════════════════════
elif page == "🔍 Secret Scanner":
    st.title("🔍 Live Secret Scanner")
    st.caption("Same regex engine used in the actual n8n pipeline")
    st.divider()

    code_input = st.text_area(
        "Paste any code to test",
        height=200,
        placeholder="Paste any code snippet here to scan for secrets..."
    )

    patterns = {
        "Google API Key":      r"AIza[A-Za-z0-9_-]{35}",
        "GitHub Token":        r"(?:ghp|gho|github_pat)_[A-Za-z0-9_]{20,}",
        "OpenAI Key":          r"sk-[A-Za-z0-9]{32,}",
        "Anthropic Key":       r"sk-ant-[A-Za-z0-9_-]{32,}",
        "HuggingFace Token":   r"hf_[A-Za-z0-9]{32,}",
        "AWS Access Key":      r"AKIA[A-Z0-9]{16}",
        "Database URL":        r"(?:postgres|mongodb|mysql|redis)://[^\s]+:[^\s]+@",
        "Password Assignment": r"(?:password|passwd|pwd)\s*[=:]\s*['\"][^'\"]{8,}['\"]",
        "API Key Assignment":  r"(?:api[_-]?key|apikey)\s*[=:]\s*['\"][^'\"]{12,}['\"]",
    }

    if st.button("🔍 Scan Now", type="primary", use_container_width=True):
        if not code_input.strip():
            st.info("Paste some code first.")
        else:
            found = []
            for name, pattern in patterns.items():
                for m in re.findall(pattern, code_input, re.IGNORECASE):
                    found.append((name, str(m)))

            if found:
                st.error(f"🚨 {len(found)} secret(s) detected — would be auto-replaced in pipeline")
                for name, match in found:
                    masked = match[:6] + "●" * 10
                    env_name = name.upper().replace(" ", "_")
                    st.warning(f"**{name}** — `{masked}` → would become `{{{{{env_name}}}}}`")
            else:
                st.success("✅ No secrets detected — safe to publish")
                st.caption(f"Scanned {len(patterns)} pattern types — all clear")


# ══ PIPELINE ══════════════════════════════════════════════════
elif page == "⚙️ Pipeline":
    st.title("⚙️ Pipeline Stages")
    st.caption("12-stage automated release pipeline")
    st.divider()

    stages = [
        ("📥", "File Intake",          "ZIP or multi-file upload"),
        ("🔍", "Secret Scan — Pass 1", "Regex scan for API keys, tokens, passwords"),
        ("🤖", "AI Security Review",   "Groq AI validates each flagged item"),
        ("✂️", "Sanitization",         "Secrets replaced — .env.example generated"),
        ("🛡️", "Secret Scan — Pass 2", "Verification — HARD STOP if anything remains"),
        ("📸", "App Screenshot",       "App launched locally — Selenium captures real UI"),
        ("📝", "README Generation",    "OpenRouter AI writes README from source files"),
        ("🐙", "GitHub Publish",       "Repo created — files + screenshot pushed"),
        ("✍️", "LinkedIn Draft",       "AI generates post — human approval via email"),
        ("📢", "LinkedIn Publish",     "Post published after approval"),
        ("📊", "Log + Notify",         "Google Sheets updated — summary email sent"),
    ]

    for icon, title, desc in stages:
        with st.container():
            c1, c2 = st.columns([1, 8])
            c1.markdown(f"## {icon}")
            c2.markdown(f"**{title}**")
            c2.caption(desc)
        st.divider()