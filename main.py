import pandas as pd
import streamlit as st
import plotly.express as px
@st.cache_data
def load_data():
    df=pd.read_csv('netflix_titles.csv')
    df["date_added"]=pd.to_datetime(df["date_added"],errors='coerce')
    df["year_added"]=df["date_added"].dt.year
    return df
st.set_page_config(page_title="Netflix Dashboard",layout="wide")
st.title("Netflix dashboard")
df=load_data()
#st.write(df)
st.sidebar.header("Dashboard Filter")
type_filter=st.sidebar.multiselect("Select Content Type",
                                   options=df["type"].dropna().unique(),
                                   default=df["type"].dropna().unique())
country_filter=st.sidebar.multiselect("Select Country",
                                      options=df["country"].dropna().unique())
rating_filter=st.sidebar.multiselect("Select rating",
                                      options=df["rating"].dropna().unique())
year_filter=st.sidebar.slider("Select release year",
                              (int)(df["release_year"].min()),(int)(df["release_year"].max()),(2000,2021))
fil_df=df[df["type"].isin(type_filter)]
#st.write(fil_df)
if country_filter:
    fil_df=fil_df[fil_df["country"].isin(country_filter)]
if rating_filter:
    fil_df=fil_df[fil_df["rating"].isin(rating_filter)]
if year_filter:
    fil_df = fil_df[(fil_df["release_year"] >= year_filter[0]) & (fil_df["release_year"] <= year_filter[1])]
#st.write(fil_df)
st.subheader("Key Matrics")
col1, col2, col3, col4 = st.columns(4)
total=len(fil_df)
movies= len(fil_df[fil_df["type"]=="Movie"])
tvshows= len(fil_df[fil_df["type"]=="TV Show"])
countries= fil_df["country"].nunique()
col1.metric("Total Titles",total)
col2.metric("Movies",movies)
col3.metric("TV Shows",tvshows)
col4.metric("Countries ",countries)
st.divider()
col1 ,col2 = st.columns(2)
with col1:
    st.subheader("Movie VS TV Shows")
    res=fil_df["type"].value_counts()
    fig=px.pie(names=res.index,values=res.values,color_discrete_sequence=px.colors.sequential.Reds)
    st.plotly_chart(fig,width ="stretch")
with col2:
    st.subheader("Content Over years")
    res1=fil_df["year_added"].value_counts().sort_index()
    fig=px.line(x=res1.index,y=res1.values,markers=True)
    fig.update_layout(xaxis_title="year_added",yaxis_title="count")
    st.plotly_chart(fig,width ="stretch")
st.divider()
col1,col2= st.columns(2)
with col1:
    st.subheader("Top Content Producing Countries")
    cnt_counts=fil_df["country"].value_counts().head(10)
    fig=px.bar(x=cnt_counts.values,y=cnt_counts.index,color=cnt_counts.values,color_continuous_scale="Reds")
    st.plotly_chart(fig,width="stretch")
with col2:
    st.subheader("Rating Distribution")
    rat_counts=fil_df["rating"].value_counts()
    fig=px.bar(x=rat_counts.index,y=rat_counts.values,color=rat_counts.values,color_continuous_scale="reds")
    st.plotly_chart(fig,width="stretch")
st.divider()
st.subheader("Top Geners")
#st.write(fil_df)
geners=fil_df["listed_in"].str.split(",").explode()
#st.write(geners.value_counts())
gencnt=geners.value_counts()
fig=px.bar(x=gencnt.index,y=gencnt.values,color=gencnt.values,color_continuous_scale="reds")
st.plotly_chart(fig,width="stretch")

st.divider()
st.subheader("Global Distribution of Contents")
cnt_values=fil_df["country"].dropna().str.split(",").explode().str.strip().replace(" ",pd.NA).dropna().value_counts().reset_index(name="count")
cnt_values.columns=["country","count"]
#fig=px.choropleth(cnt_values,locations="country",color="count",locationmode="country names",color_continuous_scale="Reds",range_color=(0,cnt_values['count'].max()))
#st.plotly_chart(fig,width="stretch")
#st.write(cnt_values.head(10))
fig = px.choropleth(
    data_frame=cnt_values,
    locations="country",
    color="count",
    hover_name="country",
    locationmode="country names",
    projection="natural earth",
    color_continuous_scale="Reds"
)

fig.update_geos(showcoastlines=True, showframe=False)
st.plotly_chart(fig, use_container_width=True)

st.divider()
st.subheader("Dataset Preview")
txtsrc=st.text_input("Enter title to search")
if txtsrc:
    fil_df=fil_df[fil_df["title"].str.contains(txtsrc,case=False)]
st.write(fil_df)