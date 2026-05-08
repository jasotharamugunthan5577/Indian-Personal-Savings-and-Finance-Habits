import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="WealthWise - Your Money Guide", page_icon="💰", layout="wide")

# =========================
# UNIQUE THEME DESIGN
# =========================
st.markdown("""
<style>
/* 🎨 Rich gradient background */
.stApp {
    background: linear-gradient(180deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    min-height: 100vh;
}

/* 💎 Glassmorphism cards */
.block-container {
    background: linear-gradient(145deg, rgba(255,255,255,0.08), rgba(255,255,255,0.02));
    backdrop-filter: blur(15px);
    padding: 30px;
    border-radius: 25px;
    border: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0 15px 35px rgba(0,0,0,0.4);
}

/* 🌈 Colorful headings */
h1 {
    background: linear-gradient(90deg, #e94560, #ffc947);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 900;
}
h2, h3 {
    color: #ffc947 !important;
    font-weight: 700;
}

/* 📝 Input styling */
.stNumberInput input, .stTextInput input, .stSelectbox div[data-role="selector"] {
    background: rgba(255,255,255,0.08) !important;
    border: 2px solid rgba(255,201,71,0.3) !important;
    border-radius: 15px !important;
    color: white !important;
    padding: 12px !important;
}
.stNumberInput input:focus {
    border-color: #ffc947 !important;
    box-shadow: 0 0 20px rgba(255,201,71,0.3) !important;
}

/* 🚀 Gradient button */
.stButton>button {
    background: linear-gradient(135deg, #e94560, #ff6b6b);
    color: white !important;
    font-weight: bold;
    border-radius: 30px;
    padding: 15px 40px;
    font-size: 18px;
    border: none;
    box-shadow: 0 6px 20px rgba(233,69,96,0.4);
    transition: all 0.3s ease;
}
.stButton>button:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 30px rgba(233,69,96,0.6);
}

/* 🏷️ Tab styling */
.stTabs [data-baseweb="tab-list"] {
    gap: 10px;
}
.stTabs [data-baseweb="tab"] {
    background: rgba(255,255,255,0.05);
    border-radius: 15px 15px 0 0;
    padding: 15px 25px;
    color: #b8c6db;
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #e94560, #ffc947) !important;
    color: white !important;
    font-weight: bold;
}

/* 📊 Metrics styling */
div[data-testid="stMetricValue"] {
    font-size: 28px !important;
    font-weight: bold;
}

/* 🎯 Alert styling */
.stAlert {
    border-radius: 15px;
    padding: 20px;
}

/* 🎪 Section titles */
.section-title {
    font-size: 24px;
    font-weight: 800;
    margin: 20px 0;
    color: #ffc947 !important;
}

/* 🌙 Hide streamlit branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# =========================
# LOGIN PAGE
# =========================
if "login" not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown("""
        <div style='text-align:center; padding:40px;'>
            <h1 style='font-size:60px; margin-bottom:10px;'>💎 WealthWise</h1>
            <h3 style='color:#ffc947 !important;'>Your Personal Money Manager</h3>
            <p style='color:#888; font-size:18px;'>Track • Save • Grow</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        user = st.text_input("👤 Username")
        pwd = st.text_input("🔑 Password", type="password")
        
        if st.button("✨ Login"):
            if user == "admin" and pwd == "admin":
                st.session_state.login = True
                st.rerun()
            else:
                st.error("Invalid credentials. Try: admin / admin")
        
        st.info("💡 Demo: admin / admin")
    st.stop()

# =========================
# MAIN APP WITH TABS
# =========================
st.markdown("""
<div style='text-align:center; padding:25px;'>
    <h1>💎 WealthWise Dashboard</h1>
    <p style='color:#b8c6db; font-size:20px;'>Your complete money overview at one place</p>
</div>
""", unsafe_allow_html=True)

# Create tabs
tab1, tab2, tab3, tab4 = st.tabs(["📝 Enter Details", "📊 Your Overview", "💡 Analysis", "🎯 Recommendations"])

# =========================
# TAB 1: INPUT FORM
# =========================
with tab1:
    st.markdown('<div class="section-title">💰 Monthly Income Details</div>', unsafe_allow_html=True)
    income = st.number_input("💵 Your Monthly Income (₹)", value=50000.0, min_value=0.0)
    
    st.markdown('<div class="section-title">🏠 Monthly Expenses</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        rent = st.number_input("🏠 House Rent (₹)", value=15000.0, min_value=0.0)
        loan = st.number_input("🏦 Loan EMI (₹)", value=5000.0, min_value=0.0)
        insurance = st.number_input("🛡️ Insurance Premium (₹)", value=2000.0, min_value=0.0)
        groceries = st.number_input("🛒 Groceries (₹)", value=8000.0, min_value=0.0)
        transport = st.number_input("🚗 Transport (₹)", value=3000.0, min_value=0.0)
    
    with col2:
        eating_out = st.number_input("🍔 Eating Out (₹)", value=4000.0, min_value=0.0)
        entertainment = st.number_input("🎬 Entertainment (₹)", value=3000.0, min_value=0.0)
        utilities = st.number_input("⚡ Utilities & Bills (₹)", value=2000.0, min_value=0.0)
        healthcare = st.number_input("🏥 Healthcare (₹)", value=1500.0, min_value=0.0)
        education = st.number_input("🎓 Education (₹)", value=2000.0, min_value=0.0)
    
    misc = st.number_input("🧾 Miscellaneous (₹)", value=3000.0, min_value=0.0)
    
    st.markdown("---")
    if st.button("💾 Save & Analyze"):
        total_expense = (rent + loan + insurance + groceries + transport +
                        eating_out + entertainment + utilities +
                        healthcare + education + misc)
        savings = income - total_expense
        percent = (savings / income * 100) if income else 0
        
        st.session_state.data = {
            "income": income,
            "expenses": total_expense,
            "savings": savings,
            "percent": percent,
            "categories": {
                "Rent": rent,
                "Loan": loan,
                "Insurance": insurance,
                "Groceries": groceries,
                "Transport": transport,
                "Eating Out": eating_out,
                "Entertainment": entertainment,
                "Utilities": utilities,
                "Healthcare": healthcare,
                "Education": education,
                "Others": misc
            }
        }
        st.success("✅ Details saved! Check the 'Your Overview' tab")

# =========================
# TAB 2: OVERVIEW WITH GRAPHS
# =========================
with tab2:
    if "data" not in st.session_state:
        st.info("📝 Please enter your details in the first tab first!")
    else:
        d = st.session_state.data
        
        st.markdown('<div class="section-title">💵 Quick Summary</div>', unsafe_allow_html=True)
        
        # Summary cards
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.metric("Total Income", f"₹{d['income']:,.0f}", delta_color="normal")
        with c2:
            st.metric("Total Expenses", f"₹{d['expenses']:,.0f}", delta_color="inverse")
        with c3:
            st.metric("Savings", f"₹{d['savings']:,.0f}", delta=f"{d['percent']:.1f}%")
        with c4:
            status = "✅ Good" if d['percent'] >= 20 else "⚠️ Needs Work"
            st.metric("Status", status)
        
        # Main message
        if d["savings"] > 0:
            st.success(f"🎉 Great! You're saving ₹{d['savings']} every month!")
        else:
            st.error(f"⚠️ You need ₹{abs(d['savings'])} more to balance your budget!")
        
        # ===== GRAPH 1: Expense Breakdown Pie =====
        st.markdown('<div class="section-title">🍩 Where Your Money Goes</div>', unsafe_allow_html=True)
        df = pd.DataFrame({
            "Category": list(d["categories"].keys()),
            "Amount": list(d["categories"].values())
        })
        
        fig1 = px.pie(df, names="Category", values="Amount", hole=0.5,
                      color_discrete_sequence=px.colors.qualitative.Pastel)
        fig1.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            font_color="white",
            legend=dict(orientation="h", y=-0.15)
        )
        st.plotly_chart(fig1, use_container_width=True)
        
        # ===== GRAPH 2: Bar Chart Comparison =====
        st.markdown('<div class="section-title">📊 Compare All Expenses</div>', unsafe_allow_html=True)
        
        fig2 = px.bar(df.sort_values("Amount", ascending=False), 
                      x="Category", y="Amount",
                      color="Amount",
                      color_continuous_scale="Sunset")
        fig2.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font_color="white",
            xaxis_title="",
            yaxis_title="Amount (₹)"
        )
        st.plotly_chart(fig2, use_container_width=True)
        
        # ===== GRAPH 3: Income vs Expense =====
        st.markdown('<div class="section-title">💰 Income vs Expenses</div>', unsafe_allow_html=True)
        
        ie_data = pd.DataFrame({
            "Type": ["Income", "Expenses"],
            "Amount": [d['income'], d['expenses']]
        })
        
        fig3 = px.bar(ie_data, x="Type", y="Amount", 
                      color="Type",
                      color_discrete_sequence=["#00d2ff", "#e94560"])
        fig3.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font_color="white"
        )
        st.plotly_chart(fig3, use_container_width=True)

# =========================
# TAB 3: ANALYSIS QUESTIONS
# =========================
with tab3:
    if "data" not in st.session_state:
        st.info("📝 Please enter your details first!")
    else:
        d = st.session_state.data
        
        st.markdown('<div class="section-title">📈 Financial Analysis</div>', unsafe_allow_html=True)
        
        # Question 1: Savings Percentage
        st.markdown("**❓ What percentage of income is being saved?**")
        
        col_g1, col_g2 = st.columns([2,1])
        with col_g1:
            # Donut chart for savings
            save_data = pd.DataFrame({
                "Type": ["Saved", "Spent"],
                "Amount": [d['savings'] if d['savings'] > 0 else 0, d['expenses']]
            })
            fig_savings = px.pie(save_data, values="Amount", names="Type",
                                 hole=0.5,
                                 color_discrete_sequence=["#00ff88", "#e94560"])
            fig_savings.update_layout(paper_bgcolor="rgba(0,0,0,0)", font_color="white")
            st.plotly_chart(fig_savings, use_container_width=True)
        
        with col_g2:
            st.markdown(f"""
            <div style='background:rgba(255,255,255,0.1); padding:20px; border-radius:15px;'>
                <h3 style='color:#00ff88 !important;'>{d['percent']:.1f}%</h3>
                <p style='color:#b8c6db;'>of income saved</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Question 2: Top 3 Expenses
        st.markdown("**❓ What are your top 3 expense categories?**")
        
        sorted_cats = sorted(d["categories"].items(), key=lambda x: x[1], reverse=True)[:3]
        
        col_top1, col_top2, col_top3 = st.columns(3)
        for i, (cat, amt) in enumerate(sorted_cats):
            with [col_top1, col_top2, col_top3][i]:
                st.metric(cat, f"₹{amt:,.0f}")
        
        # Horizontal bar for top 3
        top3_df = pd.DataFrame(sorted_cats, columns=["Category", "Amount"])
        fig_top3 = px.bar(top3_df, x="Amount", y="Category", orientation='h',
                          color="Amount", color_continuous_scale="Reds")
        fig_top3.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            font_color="white",
            height=200
        )
        st.plotly_chart(fig_top3, use_container_width=True)
        
        st.markdown("---")
        
        # Question 3: Budget Health
        st.markdown("**❓ Is the budget balanced?**")
        
        # Gauge chart
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=d['percent'],
            title={"text": f"Savings Rate: {d['percent']:.1f}%", "font": {"size": 20, "color": "white"}},
            gauge={
                "axis": {"range": [0, 50], "tickcolor": "white"},
                "bar": {"color": "#00ff88" if d['percent'] >= 20 else "#ffc947" if d['percent'] >= 10 else "#e94560"},
                "bgcolor": "rgba(255,255,255,0.1)",
            }
        ))
        fig_gauge.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            font_color="white",
            height=280
        )
        st.plotly_chart(fig_gauge, use_container_width=True)
        
        health_msg = "✅ Healthy" if d['percent'] >= 20 else "⚠️ Moderate" if d['percent'] >= 10 else "❌ Unhealthy"
        st.info(f"Budget Status: {health_msg}")
        
        st.markdown("---")
        
        # Question 4: Expense Distribution
        st.markdown("**❓ How are expenses distributed across categories?**")
        
        # Treemap
        fig_tree = px.treemap(df, path=["Category"], values="Amount",
                              color="Amount", color_continuous_scale="RdYlGn")
        fig_tree.update_layout(paper_bgcolor="rgba(0,0,0,0)", font_color="white")
        st.plotly_chart(fig_tree, use_container_width=True)

# =========================
# TAB 4: RECOMMENDATIONS
# =========================
with tab4:
    if "data" not in st.session_state:
        st.info("📝 Please enter your details first!")
    else:
        d = st.session_state.data
        
        st.markdown('<div class="section-title">💡 Personalized Suggestions</div>', unsafe_allow_html=True)
        
        # Create columns for tips
        tips_col1, tips_col2 = st.columns(2)
        
        with tips_col1:
            st.markdown("### 🎯 Based on your spending:")
            
            if d["percent"] < 10:
                st.error("📉 Your savings are low. Try the 50-30-20 rule: 50% needs, 30% wants, 20% savings!")
            
            if d["categories"]["Rent"] > d["income"] * 0.4:
                st.warning("🏠 Your rent is quite high (over 40% of income). Consider options to reduce it.")
            
            if d["categories"]["Eating Out"] > 3000:
                st.info("🍔 Eating out costs are high. Try cooking at home more often!")
            
            if d["categories"]["Entertainment"] > 4000:
                st.info("🎬 Look for free or cheaper entertainment options.")
        
        with tips_col2:
            st.markdown("### 🌟 Quick Wins:")
            
            if d["savings"] > 10000:
                st.success("💰 Great savings! Consider investing in mutual funds or FD.")
            
            if d["categories"]["Groceries"] > 8000:
                st.info("🛒 Try using cashback apps or buying in bulk.")
            
            if d["categories"]["Transport"] > 4000:
                st.info("🚗 Consider public transport or carpooling.")
            
            if d["savings"] <= 0:
                st.warning("📝 Make a strict budget and track every expense!")
        
        st.markdown("---")
        
        # Action items as visual checklist
        st.markdown("### ✅ Action Items")
        
        action_items = []
        if d["percent"] < 20:
            action_items.append({"Task": "Set up automatic savings", "Priority": "High"})
        if d["categories"]["Rent"] > d["income"] * 0.3:
            action_items.append({"Task": "Review rent options", "Priority": "Medium"})
        if d["categories"]["Eating Out"] > 2000:
            action_items.append({"Task": "Limit eating out to once a week", "Priority": "Low"})
        if d["savings"] > 5000:
            action_items.append({"Task": "Start investment journey", "Priority": "High"})
        
        if action_items:
            action_df = pd.DataFrame(action_items)
            fig_actions = px.bar(action_df, x="Priority", y="Task", 
                                 color="Priority",
                                 color_discrete_map={"High": "#e94560", "Medium": "#ffc947", "Low": "#00d2ff"})
            fig_actions.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",
                font_color="white",
                yaxis_title=""
            )
            st.plotly_chart(fig_actions, use_container_width=True)
        
        st.markdown("---")
        st.info("💡 Pro Tip: Review your spending weekly to stay on track!")

# =========================
# FOOTER
# =========================
st.markdown("---")
st.markdown("""
<div style='text-align:center; color:#666; padding:20px;'>
    <p>💎 WealthWise | Track • Save • Grow</p>
</div>
""", unsafe_allow_html=True)