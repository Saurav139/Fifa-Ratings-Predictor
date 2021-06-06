 
import pickle
import streamlit as st
import pandas as pd
import numpy as np
from icrawler.builtin import GoogleImageCrawler

# loading the trained model
pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)
fifa_age_vs_overall=pd.read_csv("FIFA_stats.csv")
@st.cache()

def check_position(fifa_age_vs_overall,position,fifa_version):
    if fifa_version=="FIFA 22":
        if position == "Overall":
            final_pred= fifa_age_vs_overall[["current_player_name","age_22","overall_22_predicted"]].sort_values(by="overall_22_predicted",ascending=False).head(10)
            final_pred.columns=["PLAYER","AGE","OVERALL PREDICTION"]
            return final_pred
        elif position == "Forwards":
            forwards=fifa_age_vs_overall[fifa_age_vs_overall["player_position"]=="Forward"]
            final_pred= forwards[["current_player_name","age_22","overall_22_predicted"]].sort_values(by="overall_22_predicted",ascending=False).head(10)
            final_pred.columns=["PLAYER","AGE","OVERALL PREDICTION"]
            return final_pred
        elif position == "Midfielders":
            mids=fifa_age_vs_overall[fifa_age_vs_overall["player_position"]=="Midfielder"]
            final_pred= mids[["current_player_name","age_22","overall_22_predicted"]].sort_values(by="overall_22_predicted",ascending=False).head(10)
            final_pred.columns=["PLAYER","AGE","OVERALL PREDICTION"]
            return final_pred
        elif position == "Defenders":
            defenders=fifa_age_vs_overall[fifa_age_vs_overall["player_position"]=="Defender"]
            final_pred= defenders[["current_player_name","age_22","overall_22_predicted"]].sort_values(by="overall_22_predicted",ascending=False).head(10)
            final_pred.columns=["PLAYER","AGE","OVERALL PREDICTION"]
            return final_pred
        elif position == "Goalkeepers":
            gks=fifa_age_vs_overall[fifa_age_vs_overall["player_position"]=="Goalkeeper"]
            final_pred= gks[["current_player_name","age_22","overall_22_predicted"]].sort_values(by="overall_22_predicted",ascending=False).head(10)
            final_pred.columns=["PLAYER","AGE","OVERALL PREDICTION"]
            return final_pred
    elif fifa_version=="FIFA 23":
        if position == "Overall":
            final_pred= fifa_age_vs_overall[["current_player_name","age_23","overall_23_predicted"]].sort_values(by="overall_23_predicted",ascending=False).head(10)
            final_pred.columns=["PLAYER","AGE","OVERALL PREDICTION"]
            return final_pred
        elif position == "Forwards":
            forwards=fifa_age_vs_overall[fifa_age_vs_overall["player_position"]=="Forward"]
            final_pred= forwards[["current_player_name","age_23","overall_23_predicted"]].sort_values(by="overall_23_predicted",ascending=False).head(10)
            final_pred.columns=["PLAYER","AGE","OVERALL PREDICTION"]
            return final_pred
        elif position == "Midfielders":
            mids=fifa_age_vs_overall[fifa_age_vs_overall["player_position"]=="Midfielder"]
            final_pred= mids[["current_player_name","age_23","overall_23_predicted"]].sort_values(by="overall_23_predicted",ascending=False).head(10)
            final_pred.columns=["PLAYER","AGE","OVERALL PREDICTION"]
            return final_pred
        elif position == "Defenders":
            defenders=fifa_age_vs_overall[fifa_age_vs_overall["player_position"]=="Defender"]
            final_pred= defenders[["current_player_name","age_23","overall_23_predicted"]].sort_values(by="overall_23_predicted",ascending=False).head(10)
            final_pred.columns=["PLAYER","AGE","OVERALL PREDICTION"]
            return final_pred
        elif position == "Goalkeepers":
            gks=fifa_age_vs_overall[fifa_age_vs_overall["player_position"]=="Goalkeeper"]
            final_pred= gks[["current_player_name","age_23","overall_23_predicted"]].sort_values(by="overall_23_predicted",ascending=False).head(10)
            final_pred.columns=["PLAYER","AGE","OVERALL PREDICTION"]
            return final_pred
    elif fifa_version=="FIFA 24":
        if position == "Overall":
            final_pred= fifa_age_vs_overall[["current_player_name","age_24","overall_24_predicted"]].sort_values(by="overall_24_predicted",ascending=False).head(10)
            final_pred.columns=["PLAYER","AGE","OVERALL PREDICTION"]
            return final_pred
        elif position == "Forwards":
            forwards=fifa_age_vs_overall[fifa_age_vs_overall["player_position"]=="Forward"]
            final_pred= forwards[["current_player_name","age_24","overall_24_predicted"]].sort_values(by="overall_24_predicted",ascending=False).head(10)
            final_pred.columns=["PLAYER","AGE","OVERALL PREDICTION"]
            return final_pred
        elif position == "Midfielders":
            mids=fifa_age_vs_overall[fifa_age_vs_overall["player_position"]=="Midfielder"]
            final_pred= mids[["current_player_name","age_24","overall_24_predicted"]].sort_values(by="overall_24_predicted",ascending=False).head(10)
            final_pred.columns=["PLAYER","AGE","OVERALL PREDICTION"]
            return final_pred
        elif position == "Defenders":
            defenders=fifa_age_vs_overall[fifa_age_vs_overall["player_position"]=="Defender"]
            final_pred= defenders[["current_player_name","age_24","overall_24_predicted"]].sort_values(by="overall_24_predicted",ascending=False).head(10)
            final_pred.columns=["PLAYER","AGE","OVERALL PREDICTION"]
            return final_pred
        elif position == "Goalkeepers":
            gks=fifa_age_vs_overall[fifa_age_vs_overall["player_position"]=="Goalkeeper"]
            final_pred= gks[["current_player_name","age_24","overall_24_predicted"]].sort_values(by="overall_24_predicted",ascending=False).head(10)
            final_pred.columns=["PLAYER","AGE","OVERALL PREDICTION"]
            return final_pred
        

def prediction(fifa_version,fifa_age_vs_overall,position):
    from sklearn.preprocessing import RobustScaler
    scaler = RobustScaler()
    if fifa_version == "FIFA 22":
        X_22=fifa_age_vs_overall[["age_22","overall_21_predicted"]]
        X_22=scaler.fit_transform(X_22)
        y_pred_22=classifier.predict(X_22)
        y_pred_22=np.round(y_pred_22,2)
        fifa_age_vs_overall["overall_22_predicted"]=y_pred_22
        final_pred=check_position(fifa_age_vs_overall,position,fifa_version)
        return final_pred
        
    if fifa_version == "FIFA 23":
        X_22=fifa_age_vs_overall[["age_22","overall_21_predicted"]]
        X_22=scaler.fit_transform(X_22)
        y_pred_22=classifier.predict(X_22)
        y_pred_22=np.round(y_pred_22,2)
        fifa_age_vs_overall["overall_22_predicted"]=y_pred_22

        X_23=fifa_age_vs_overall[["age_23","overall_22_predicted"]]
        X_23=scaler.fit_transform(X_23)
        y_pred_23=classifier.predict(X_23)
        y_pred_23=np.round(y_pred_23,2)
        fifa_age_vs_overall["overall_23_predicted"]=y_pred_23
        final_pred=check_position(fifa_age_vs_overall,position,fifa_version)
        return final_pred
        
    if fifa_version == "FIFA 24":
        X_22=fifa_age_vs_overall[["age_22","overall_21_predicted"]]
        X_22=scaler.fit_transform(X_22)
        y_pred_22=classifier.predict(X_22)
        y_pred_22=np.round(y_pred_22,2)
        fifa_age_vs_overall["overall_22_predicted"]=y_pred_22    

        X_23=fifa_age_vs_overall[["age_23","overall_22_predicted"]]
        X_23=scaler.fit_transform(X_23)
        y_pred_23=classifier.predict(X_23)
        y_pred_23=np.round(y_pred_23,2)
        fifa_age_vs_overall["overall_23_predicted"]=y_pred_23
    
        X_24=fifa_age_vs_overall[["age_24","overall_23_predicted"]]
        X_24=scaler.fit_transform(X_24)
        y_pred_24=classifier.predict(X_24)
        y_pred_24=np.round(y_pred_24,2)
        fifa_age_vs_overall["overall_24_predicted"]=y_pred_24
        
        final_pred=check_position(fifa_age_vs_overall,position,fifa_version)
        return final_pred
def download_images(result):
    for player in result["PLAYER"]:
            google_crawler = GoogleImageCrawler(storage={'root_dir': 'images/'+player})
            google_crawler.crawl(keyword=player,max_num=2)
def display_images(result):
    for i,player in zip(range(len(result)),result["PLAYER"]):
        age=result["AGE"][i]
        rating=result["OVERALL PREDICTION"][i]
        player_text= "# "+player
        age="** "+"AGE : {} ".format(age) + " **"
        ratings="** "+"RATINGS : {} ".format(rating)+ " **"
        try:
            
            st.image('images/'+player+"/000002.jpg",width=250)
            st.markdown(player_text)
            st.markdown(age)
            st.markdown(ratings)
    
                
        except:
            
            st.image('images/'+player+"/000001.jpg",width=250)
            st.markdown(player_text)
            st.markdown(age)
            st.markdown(ratings)
            
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:red;padding:13px"> 
    <h1 style ="color:black;text-align:center;">FIFA Ratings predictor ML App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
    fifa_version = st.selectbox('FIFA Version',("FIFA 22","FIFA 23","FIFA 24"))
    position = st.selectbox('Position',("Overall","Forwards","Midfielders","Defenders","Goalkeepers"))
    
    if st.button("Predict"): 
        result = prediction(fifa_version,fifa_age_vs_overall,position)
        result=result.reset_index()
        st.success("Top 10 rated players in {} ({})".format(fifa_version,position))
        download_images(result)
        display_images(result)
        
        
        
            
if __name__=='__main__': 
    main()
