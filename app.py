!pip install Cython==0.28.5
import Cython
import pickle
import streamlit as st
 
# loading the trained model
pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction (aon,daily_decr90,rental90,last_rech_date_ma,
       last_rech_date_da, last_rech_amt_ma, cnt_ma_rech30,
       fr_ma_rech30, sumamnt_ma_rech30, medianamnt_ma_rech30,
       medianmarechprebal30, cnt_ma_rech90, fr_ma_rech90,
       sumamnt_ma_rech90, medianamnt_ma_rech90, medianmarechprebal90,
       cnt_da_rech30, fr_da_rech30, cnt_da_rech90, fr_da_rech90,
       maxamnt_loans30, cnt_loans90, amnt_loans90, maxamnt_loans90,
       medianamnt_loans90, payback30, payback90, month, day):
  

    prediction = classifier.predict( 
        [[aon, daily_decr90, rental90, last_rech_date_ma,last_rech_date_da, last_rech_amt_ma, cnt_ma_rech30,fr_ma_rech30, sumamnt_ma_rech30,
               medianamnt_ma_rech30,medianmarechprebal30, cnt_ma_rech90, fr_ma_rech90,sumamnt_ma_rech90, medianamnt_ma_rech90,medianmarechprebal90,
               cnt_da_rech30, fr_da_rech30, cnt_da_rech90, fr_da_rech90,
               maxamnt_loans30, cnt_loans90, amnt_loans90, maxamnt_loans90,
               medianamnt_loans90, payback30, payback90, month, day]])
    if prediction == 0:
      pred = 'Rejected'
    else:
      pred = 'Approved'
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:#00FFFF;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Micro-Credit Defaulter Model</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    aon = st.number_input("age on cellular network in days") 
    daily_decr90 = st.number_input("Daily amount spent from main account, averaged over last 90 days (in Indonesian Rupiah)")
    rental90 = st.number_input("Average main account balance over last 90 days") 
    last_rech_date_ma = st.number_input("Number of days till last recharge of main account")
    last_rech_date_da = st.number_input("Number of days till last recharge of data account") 
    last_rech_amt_ma = st.number_input("Amount of last recharge of main account (in Indonesian Rupiah)")
    cnt_ma_rech30 = st.number_input("Number of times main account got recharged in last 30 days") 
    fr_ma_rech30 = st.number_input("Frequency of main account recharged in last 30 days")
    sumamnt_ma_rech30 = st.number_input("Total amount of recharge in main account over last 30 days (in Indonesian Rupiah)") 
    medianamnt_ma_rech30 = st.number_input("Median of amount of recharges done in main account over last 30 days at user level (in Indonesian Rupiah)")
    medianmarechprebal30 = st.number_input("Median of main account balance just before recharge in last 30 days at user level (in Indonesian Rupiah)")
    cnt_ma_rech90 = st.number_input("Number of times main account got recharged in last 90 days")
    fr_ma_rech90 = st.number_input("Frequency of main account recharged in last 90 days")
    sumamnt_ma_rech90 = st.number_input("Total amount of recharge in main account over last 90 days (in Indonasian Rupiah)")
    medianamnt_ma_rech90 = st.number_input("Median of amount of recharges done in main account over last 90 days at user level (in Indonasian Rupiah)")
    medianmarechprebal90 = st.number_input('Median of main account balance just before recharge in last 90 days at user level (in Indonasian Rupiah)')
    cnt_da_rech30=	st.number_input('Number of times data account got recharged in last 30 days')
    fr_da_rech30=	st.number_input('Frequency of data account recharged in last 30 days')
    cnt_da_rech90	=st.number_input('Number of times data account got recharged in last 90 days')
    fr_da_rech90=	st.number_input('Frequency of data account recharged in last 90 days')
    maxamnt_loans30=	st.number_input('maximum amount of loan taken by the user in last 30 days')
    cnt_loans90	=st.number_input('Number of loans taken by user in last 90 days')
    amnt_loans90=	st.number_input('Total amount of loans taken by user in last 90 days')
    maxamnt_loans90=	st.number_input('maximum amount of loan taken by the user in last 90 days')
    medianamnt_loans90=	st.number_input('Median of amounts of loan taken by the user in last 90 days')
    payback30=	st.number_input('Average payback time in days over last 30 days')
    payback90=	st.number_input('Average payback time in days over last 90 days')
    month=st.number_input('Month')
    day=st.number_input('day')
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(aon, daily_decr90, rental90, last_rech_date_ma,last_rech_date_da, last_rech_amt_ma, cnt_ma_rech30,fr_ma_rech30, sumamnt_ma_rech30,
               medianamnt_ma_rech30,medianmarechprebal30, cnt_ma_rech90, fr_ma_rech90,sumamnt_ma_rech90, medianamnt_ma_rech90,medianmarechprebal90,
               cnt_da_rech30, fr_da_rech30, cnt_da_rech90, fr_da_rech90,
               maxamnt_loans30, cnt_loans90, amnt_loans90, maxamnt_loans90,
               medianamnt_loans90, payback30, payback90, month, day) 
        st.success('Your loan is {}'.format(result))
     
if __name__=='__main__': 
    main()
