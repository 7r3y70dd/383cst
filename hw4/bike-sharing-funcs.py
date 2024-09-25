import numpy as np
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/grbruns/cst383/master/lyft-2019-04.csv")
df.info()
df.isna().mean().sort_values()
df.dropna(inplace=True)
df['member_age'] = (2019 - df['member_birth_year']).astype(int)
df = df[df['member_age'] < 100]
age_groups = [18, 25, 35, 50, 100]
group_names = ['18-25', '25-35', '35-50', '>50']
df['age_group'] = pd.cut(df['member_age'], age_groups, labels=group_names).astype(object)
df.drop('month', axis=1, inplace=True)

class Problems:
    @staticmethod
    def prob_1(df):
        df['trip_min'] = (df['trip_duration_sec'] / 60).astype(int)
        return df
    
    @staticmethod
    def prob_2(df):
        df['start_station_id'] = df['start_station_id'].astype(int)
        return df
    
    @staticmethod
    def prob_3(df):
        df['end_station_id'] = df['end_station_id'].astype(int)
        return df
    
    @staticmethod
    def prob_4(df):
        df['route'] = df['start_station_id'].astype(str) + '->' + df['end_station_id'].astype(str)
        return df
    
    @staticmethod
    def prob_5(df):
        df['BART'] = df['start_station_name'].str.contains('BART') | df['end_station_name'].str.contains('BART')
        return df
    
    @staticmethod
    def prob_6(df):
        _x = df.shape[0]
        return _x
    
    @staticmethod
    def prob_7(df):
        _x = df.columns
        return _x
    
    @staticmethod
    def prob_8(df):
        _x = df['trip_min'].max() / 60
        return _x
    
    @staticmethod
    def prob_9(df):
        _x = df['trip_min'].median()
        return _x
    
    @staticmethod
    def prob_10(df):
        _x = df['member_age'].max()
        return _x
    
    @staticmethod
    def prob_11(df):
        _x = df['member_age'].min()
        return _x
    
    @staticmethod
    def prob_12(df):
        _x = df[['trip_min', 'member_age', 'member_gender', 'user_type']].head(10)
        return _x
    
    @staticmethod
    def prob_13(df):
        _x = df['user_type'].unique()
        return _x
    
    @staticmethod
    def prob_14(df):
        _x = (df['user_type'] == 'Subscriber').mean()
        return _x
    
    @staticmethod
    def prob_15(df):
        _x = (df['trip_min'] > 60).mean()
        return _x
    
    @staticmethod
    def prob_16(df):
        station_names = df['start_station_name'].unique()
        return station_names
    
    @staticmethod
    def prob_17(station_names):
        _x = (station_names.str.contains('Station')).mean()
        return _x
    
    @staticmethod
    def prob_18(df):
        _x = (df['end_station_name'].str.contains('Station')).mean()
        return _x
    
    @staticmethod
    def prob_19(df):
        _x = (df['BART']).mean()
        return _x
    
    @staticmethod
    def prob_20(df):
        _x = df['user_type'].value_counts()
        return _x
    
    @staticmethod
    def prob_21(df):
        _x = df['member_gender'].value_counts(normalize=True)
        return _x
    
    @staticmethod
    def prob_22(df):
        _x = df['age_group'].value_counts(normalize=True).sort_values(ascending=False)
        return _x
    
    @staticmethod
    def prob_23(df,group_names):
        _x = df['age_group'].value_counts(normalize=True).reindex(group_names)
        return _x
    
    @staticmethod
    def prob_24(df):
        _x = df['end_station_name'].value_counts().head(20)
        return _x
    
    @staticmethod
    def prob_25(df):
        _x = df['start_station_name'].value_counts().head(20)
        return _x
    
    @staticmethod
    def prob_26(df):
        _x = df.groupby(['start_station_name', 'end_station_name']).size().nlargest(20)
        return _x
    
    @staticmethod
    def prob_27(df):
        top_routes = df['route'].value_counts().nlargest(20).index
        return top_routes
    
    @staticmethod
    def prob_28(df):
        _x = df.groupby('age_group')['trip_min'].mean()
        return _x
    
    @staticmethod
    def prob_29(df):
        _x = df.groupby('age_group')['trip_min'].median()
        return _x
    
    @staticmethod
    def prob_30(df):
        _x = df.groupby('user_type')['member_age'].median()
        return _x
    
    @staticmethod
    def prob_31(df):
        _x = df.groupby('member_gender')['trip_min'].median()
        return _x
    
    @staticmethod
    def prob_32(df):
        _x = df.groupby(['member_gender', 'age_group'])['trip_min'].median()
        return _x
    
    @staticmethod
    def prob_33(df):
        _x = df.groupby('age_group')['trip_min'].agg(['mean', 'median'])
        return _x
    
    @staticmethod
    def prob_34(df):
        _x = df.groupby(df['end_station_name'].str.contains('Station'))['member_age'].median()
        return _x
    
    @staticmethod
    def prob_35(df):
        _x = df.groupby(df['end_station_name'].str.contains('BART'))['user_type'].apply(lambda x: (x == 'Subscriber').mean())
        return _x
    
    @staticmethod
    def prob_36(df,top_routes):
        df_top_routes = df[df['route'].isin(top_routes)]
        _x = df_top_routes.groupby('route')['trip_min'].median().sort_values(ascending=False)
        return _x
    
    @staticmethod
    def prob_37(df):
        _x = df.groupby(['user_type', 'age_group']).size() / len(df)
        return _x
    
