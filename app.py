# app.py
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from mock_data import MockDataGenerator

def render_overview_tab(mock_data):
    col1, col2 = st.columns(2)
    
    # Daily trends chart
    daily_data = mock_data.generate_daily_data()
    with col1:
        fig = go.Figure()
        fig.add_trace(
            go.Scatter(
                x=daily_data['date'],
                y=daily_data['impressions'],
                name='Impressions',
                line=dict(color='blue')
            )
        )
        fig.add_trace(
            go.Scatter(
                x=daily_data['date'],
                y=daily_data['clicks'],
                name='Clicks',
                line=dict(color='green'),
                yaxis='y2'
            )
        )
        fig.update_layout(
            title='Daily Performance Trends',
            yaxis=dict(title='Impressions'),
            yaxis2=dict(title='Clicks', overlaying='y', side='right')
        )
        st.plotly_chart(fig, use_container_width=True)

    # Campaign performance chart
    with col2:
        campaign_data = mock_data.generate_campaign_data()
        fig = px.bar(
            campaign_data,
            x='campaign_name',
            y=['clicks', 'conversions'],
            title='Campaign Performance Overview',
            barmode='group'
        )
        st.plotly_chart(fig, use_container_width=True)

def render_keywords_tab(mock_data):
    keyword_data = mock_data.generate_keyword_data()
    
    # Keyword performance chart
    fig = px.scatter(
        keyword_data,
        x='impressions',
        y='clicks',
        size='conversions',
        color='quality_score',
        hover_data=['keyword', 'match_type', 'ctr'],
        title='Keyword Performance'
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Keyword table
    st.dataframe(keyword_data)

def render_ads_tab(mock_data):
    ad_data = mock_data.generate_ad_data()
    
    # Ad performance chart
    fig = go.Figure(data=[
        go.Bar(name='Clicks', x=ad_data['headline'], y=ad_data['clicks']),
        go.Bar(name='Conversions', x=ad_data['headline'], y=ad_data['conversions'])
    ])
    fig.update_layout(title='Ad Performance', barmode='group')
    st.plotly_chart(fig, use_container_width=True)
    
    # Ad details
    for _, row in ad_data.iterrows():
        with st.expander(row['headline']):
            col1, col2 = st.columns(2)
            with col1:
                st.metric("CTR", f"{row['ctr']}%")
                st.metric("Clicks", row['clicks'])
            with col2:
                st.metric("Conversions", row['conversions'])
                st.metric("Status", row['status'])

def render_audiences_tab(mock_data):
    audience_data = mock_data.generate_audience_data()
    
    # Audience size bubble chart
    fig = px.scatter(
        audience_data,
        x='impressions',
        y='conversions',
        size='size',
        color='clicks',
        hover_data=['audience', 'cost'],
        title='Audience Performance'
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Audience metrics
    st.dataframe(audience_data)

def render_benchmarks_tab(mock_data):
    benchmark_data = mock_data.generate_benchmark_data()
    
    # Benchmark comparison chart
    fig = go.Figure()
    for col in ['account_value', 'industry_avg', 'top_performer']:
        fig.add_trace(go.Bar(
            name=col.replace('_', ' ').title(),
            x=benchmark_data['metric'],
            y=benchmark_data[col]
        ))
    fig.update_layout(title='Performance Benchmarks', barmode='group')
    st.plotly_chart(fig, use_container_width=True)

def render_campaign_tab(mock_data):
    campaign_data = mock_data.generate_campaign_data()
    
    # Campaign scatter plot
    fig = px.scatter(
        campaign_data,
        x='cost',
        y='conversions',
        size='clicks',
        color='quality_score',
        hover_data=['campaign_name', 'ctr', 'conv_rate'],
        title='Campaign Performance Matrix'
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Campaign metrics table
    st.dataframe(campaign_data)

def render_competitor_tab(mock_data):
    competitor_data = mock_data.generate_competitor_data()
    
    fig = px.scatter(
        competitor_data,
        x='overlap_rate',
        y='outranking_share',
        size='top_of_page_rate',
        color='position_above_rate',
        hover_data=['competitor'],
        title='Competitor Analysis'
    )
    st.plotly_chart(fig, use_container_width=True)

def render_recommendations_tab(mock_data):
    recommendations = mock_data.generate_recommendations()
    
    for rec in recommendations:
        with st.expander(f"{rec['priority']} Priority - {rec['category']}"):
            st.write(f"Description: {rec['description']}")
            st.write(f"Potential Impact: {rec['impact']}")
            st.write(f"Status: {rec['status']}")

def main():
    st.set_page_config(page_title="Google Ads Account Audit Demo", layout="wide")
    
    mock_data = MockDataGenerator()
    
    st.title("Google Ads Account Audit Demo")
    st.subheader("Account: Demo Account - Last 30 Days")
    
    # Metrics row
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Spend", "$12,345", "+10%")
    with col2:
        st.metric("Conversions", "456", "+15%")
    with col3:
        st.metric("CTR", "2.4%", "-1%")
    with col4:
        st.metric("Quality Score", "7.5", "+0.5")
    
    # All tabs
    tabs = st.tabs([
        "Overview",
        "Campaigns",
        "Keywords",
        "Ads",
        "Audiences",
        "Competitors",
        "Benchmarks",
        "Recommendations"
    ])
    
    with tabs[0]:
        render_overview_tab(mock_data)
    with tabs[1]:
        render_campaign_tab(mock_data)
    with tabs[2]:
        render_keywords_tab(mock_data)
    with tabs[3]:
        render_ads_tab(mock_data)
    with tabs[4]:
        render_audiences_tab(mock_data)
    with tabs[5]:
        render_competitor_tab(mock_data)
    with tabs[6]:
        render_benchmarks_tab(mock_data)
    with tabs[7]:
        render_recommendations_tab(mock_data)

if __name__ == "__main__":
    main()