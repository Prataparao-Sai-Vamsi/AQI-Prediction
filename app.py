import pickle
import streamlit as st
pickle_in = open("random_forest_regression_model.pkl","rb")
random_forest_regressor=pickle.load(pickle_in)
def welcome():
 return "welcome all"
def predict_AQI(Average_Temperature,Maximum_Temperature,Minimum_Temperature,Atm_pressure_at_sea_level,Average_wind_speed):
 
 
 prediction=random_forest_regressor.predict([[ Average_Temperature,Maximum_Temperature,Minimum_Temperature, Atm_pressure_at_sea_level,Average_wind_speed]])
 print(prediction)
 return prediction
def main():
 st.title("Hyderabad AQI prediction")
 html_temp = """
 <div style="background-color:green;padding:20px"\>
 <h2 style="color:white;text-align:center;">AQI prediction ML App </h2>
 </div>
 """
 st.markdown(html_temp,unsafe_allow_html=True)
 Average_Temperature= st.text_input("Average_Temperature ",0)
 Maximum_Temperature = st.text_input("Maximum_Temperature ",0)
 Minimum_Temperature = st.text_input("Minimum_Temperature ",0)
 Atm_pressure_at_sea_level = st.text_input("Atm_pressure_at_sea_level ",0)
 Average_wind_speed = st.text_input("Average_wind_speed",0)
 result=""
 if st.button("Predict"):
 	result=predict_AQI(Average_Temperature,Maximum_Temperature,Minimum_Temperature,Atm_pressure_at_sea_level,Average_wind_speed)
 st.success('The AQI is {}'.format(result))
 if st.button("About"):
 	st.text("Lets Learn")
 	st.text("Built with Streamlit")
if __name__=='__main__':
 main()
