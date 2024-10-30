# mock_data.py
import pandas as pd
import random
from datetime import datetime, timedelta

class MockDataGenerator:
    @staticmethod
    def generate_daily_data(days=30):
        dates = [(datetime.now() - timedelta(days=x)).strftime('%Y-%m-%d') for x in range(days)]
        return pd.DataFrame({
            'date': dates,
            'impressions': [random.randint(1000, 5000) for _ in range(days)],
            'clicks': [random.randint(50, 200) for _ in range(days)],
            'cost': [random.uniform(100, 500) for _ in range(days)],
            'conversions': [random.randint(5, 20) for _ in range(days)]
        })

    @staticmethod
    def generate_campaign_data():
        campaigns = ['Brand Campaign', 'Generic Search', 'Display Retargeting', 'Shopping']
        return pd.DataFrame({
            'campaign_name': campaigns,
            'impressions': [random.randint(10000, 50000) for _ in campaigns],
            'clicks': [random.randint(500, 2000) for _ in campaigns],
            'cost': [random.uniform(1000, 5000) for _ in campaigns],
            'conversions': [random.randint(50, 200) for _ in campaigns],
            'ctr': [random.uniform(1, 5) for _ in campaigns],
            'conv_rate': [random.uniform(2, 8) for _ in campaigns],
            'quality_score': [random.randint(5, 10) for _ in campaigns]
        })

    @staticmethod
    def generate_keyword_data():
        keywords = ['digital marketing', 'seo services', 'ppc management', 'social media marketing', 'web design']
        return pd.DataFrame({
            'keyword': keywords,
            'match_type': ['Exact', 'Phrase', 'Broad', 'Exact', 'Phrase'],
            'impressions': [random.randint(1000, 5000) for _ in keywords],
            'clicks': [random.randint(50, 200) for _ in keywords],
            'cost': [random.uniform(100, 500) for _ in keywords],
            'conversions': [random.randint(5, 20) for _ in keywords],
            'quality_score': [random.randint(1, 10) for _ in keywords],
            'ctr': [random.uniform(1, 5) for _ in keywords],
            'avg_position': [random.uniform(1, 4) for _ in keywords]
        })

    @staticmethod
    def generate_ad_data():
        headlines = ['Best Digital Marketing', 'Professional SEO Services', 'Expert PPC Management', 
                    'Social Media Experts', 'Web Design Solutions']
        return pd.DataFrame({
            'headline': headlines,
            'description': [f'Description for {h}' for h in headlines],
            'impressions': [random.randint(1000, 5000) for _ in headlines],
            'clicks': [random.randint(50, 200) for _ in headlines],
            'conversions': [random.randint(5, 20) for _ in headlines],
            'ctr': [random.uniform(1, 5) for _ in headlines],
            'status': ['Active', 'Active', 'Paused', 'Active', 'Paused']
        })

    @staticmethod
    def generate_audience_data():
        audiences = ['In-Market', 'Affinity', 'Custom Intent', 'Remarketing', 'Similar Audiences']
        return pd.DataFrame({
            'audience': audiences,
            'size': [random.randint(10000, 100000) for _ in audiences],
            'impressions': [random.randint(1000, 5000) for _ in audiences],
            'clicks': [random.randint(50, 200) for _ in audiences],
            'conversions': [random.randint(5, 20) for _ in audiences],
            'cost': [random.uniform(100, 500) for _ in audiences],
            'conv_rate': [random.uniform(1, 5) for _ in audiences]
        })

    @staticmethod
    def generate_competitor_data():
        competitors = ['Competitor A', 'Competitor B', 'Competitor C', 'Competitor D']
        return pd.DataFrame({
            'competitor': competitors,
            'overlap_rate': [random.uniform(0.2, 0.8) for _ in competitors],
            'position_above_rate': [random.uniform(0.1, 0.6) for _ in competitors],
            'top_of_page_rate': [random.uniform(0.3, 0.9) for _ in competitors],
            'outranking_share': [random.uniform(0.2, 0.7) for _ in competitors],
            'impression_share': [random.uniform(0.1, 0.5) for _ in competitors]
        })

    @staticmethod
    def generate_benchmark_data():
        metrics = ['CTR', 'CPC', 'Conv Rate', 'CPA', 'Impression Share', 'Quality Score']
        return pd.DataFrame({
            'metric': metrics,
            'account_value': [random.uniform(1, 5) for _ in metrics],
            'industry_avg': [random.uniform(1, 5) for _ in metrics],
            'top_performer': [random.uniform(3, 7) for _ in metrics]
        })

    @staticmethod
    def generate_recommendations():
        return [
            {
                'priority': 'High',
                'category': 'Budget',
                'description': 'Increase budget for high-performing campaign "Brand Campaign"',
                'impact': '+15% conversions',
                'status': 'New'
            },
            {
                'priority': 'High',
                'category': 'Keywords',
                'description': 'Add negative keywords to reduce irrelevant clicks',
                'impact': '-10% cost',
                'status': 'In Progress'
            },
            {
                'priority': 'Medium',
                'category': 'Ads',
                'description': 'Test new ad variations for better CTR',
                'impact': '+5% CTR',
                'status': 'New'
            },
            {
                'priority': 'Medium',
                'category': 'Bidding',
                'description': 'Adjust bid strategy for mobile devices',
                'impact': '+8% conversions',
                'status': 'New'
            },
            {
                'priority': 'Low',
                'category': 'Extensions',
                'description': 'Add more sitelink extensions',
                'impact': '+3% CTR',
                'status': 'New'
            }
        ]

    @staticmethod
    def generate_quality_score_distribution():
        scores = list(range(1, 11))
        return pd.DataFrame({
            'score': scores,
            'keywords': [random.randint(0, 100) for _ in scores]
        })