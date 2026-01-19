import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Rishana Abubacker | Senior Data Analyst",
    page_icon="📊",
    layout="wide"
)

# ---------------- HEADER ----------------
st.title("Rishana Abubacker")
st.subheader("Senior Data Analyst | Product, Business & GenAI Analytics")

st.markdown("""
Senior Data Analyst with 4+ years of experience turning complex, high-volume data into
clear, actionable insights that drive business, product, and customer decisions.

Delivered analytics across **60+ engagements for Tier-1 clients**, supporting global
Consumer and Healthcare brands. Specialized in **SQL-driven analytics, automation,
dashboarding, and LLM-powered insight extraction**.
""")

st.markdown("---")

# ---------------- METRICS ----------------
col1, col2, col3, col4 = st.columns(4)
col1.metric("Experience", "4+ Years")
col2.metric("Tier-1 Engagements", "60+")
col3.metric("Data Scale", "30M+ Records")
col4.metric("Decision Velocity", "↑ 40%")

st.markdown("---")

# ---------------- SKILLS ----------------
st.header("🧠 Core Skills")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
**Data Analysis & SQL**
- Advanced SQL (CTEs, window functions, complex joins)
- Exploratory data analysis & root cause analysis
- Metric ownership (NPS, churn, sentiment)
- Hypothesis-driven analysis
""")

with col2:
    st.markdown("""
**Tools & Advanced Analytics**
- Python for automation & data processing
- Tableau dashboards & KPI frameworks
- LLM prompt engineering for insight extraction
- Competitor benchmarking & investor analytics
""")

st.markdown("---")

# ---------------- EXPERIENCE ----------------
st.header("💼 Experience Summary")

st.markdown("""
As a Senior Data Analyst, I work closely with consultants, investors, product teams,
and CX leaders to support data-backed decision-making at scale.

**Key responsibilities include:**
- Owning analytics across NPS, customer support tickets, reviews, and feedback
- Building SQL-driven pipelines and Tableau dashboards
- Conducting churn and root-cause deep dives
- Delivering competitor benchmarking for investment decisions
- Applying LLM-powered insight extraction to scale qualitative analysis
- Automating workflows, improving efficiency by ~60%
""")

st.markdown("---")

# ---------------- PROJECTS ----------------
st.header("🧩 Flagship Projects")

with st.expander("📊 NPS & Customer Sentiment Analytics Platform", expanded=True):
    st.markdown("""
**Problem**  
Lack of a unified view of customer sentiment across surveys, reviews, and support tickets.

**Approach**
- SQL pipelines consolidating NPS, review text, and ticket data
- Tableau dashboards tracking sentiment drivers and trends
- Root cause analysis of dissatisfaction drivers

**Impact**
- 5–30% reduction in customer negativity
- ~40% faster decision-making
""")

with st.expander("🔁 Customer Churn & Retention Deep Dive"):
    st.markdown("""
**Problem**  
Unclear drivers of customer churn and retention risks.

**Approach**
- Advanced SQL analysis of customer interactions
- Identification of high-impact churn indicators
- Stakeholder collaboration on retention initiatives

**Impact**
- Supported ~20% churn reduction initiatives
""")

with st.expander("📈 Competitor Benchmarking for Investors"):
    st.markdown("""
**Problem**  
Need for data-backed competitive benchmarking.

**Approach**
- Comparative dashboards across competing brands
- Review and sentiment analysis
- Risk and opportunity identification

**Impact**
- Informed investment and due-diligence decisions
""")

with st.expander("🛠 Product Improvement Prioritization"):
    st.markdown("""
**Problem**  
Fragmented customer feedback limited product prioritization.

**Approach**
- SQL-based mapping of issues to product features
- Frequency, sentiment, and trend analysis

**Impact**
- Informed product improvements for ~60% of consumer clients
""")

st.markdown("---")

# ---------------- IMPACT ----------------
st.header("🚀 Impact & Outcomes")

st.markdown("""
- 📉 5–30% reduction in customer negativity  
- 🔁 ~20% churn reduction (initiative-supported)  
- 🧠 Product improvements for ~60% of clients  
- 🚀 40% improvement in decision velocity  
- 🤖 50%+ reduction in manual qualitative analysis using LLMs  
""")

st.markdown("---")

# ---------------- CONTACT ----------------
st.header("📬 Let’s Connect")

st.markdown("""
- **LinkedIn:** https://www.linkedin.com/in/rishana-abubacker-54045713b/
- **Email:** rishanaabubacker.abc@gmail.com
""")

st.caption("Open to Senior Data Analyst, BI Engineer, and Product Analytics roles.")
