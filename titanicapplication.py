import streamlit as st
import pickle
 
#Set the title and Display an Image for Branding
st.title('Titanic Survival Prediction App!')
st.image('Titanic_Image.jpeg', caption = 'Predict Survival on the Titanic')
 
#Load the pretrained model
with open('titanicpickle2.pkl', 'rb') as pickleFile:
    model = pickle.load(pickleFile)
 
#Function to Make Prediction
def PredictionFunction(Pclass, Sex, Age, SibSp, Parch, Fare, Embarked):
    try:
        prediction = model.predict([[Pclass, Sex, Age, SibSp, Parch, Fare, Embarked]])
        return 'Survived' if prediction[0] == 1 else 'Did not Survived'
    except Exception as e:
        return f'Error:{str(e)}'
 
#Sidebar for Instructions
st.sidebar.header('How to Use!')
st.sidebar.markdown("""
1. Enter the Passenger Details in the Form.
2. Click 'Predict' to See the Survival Result.
3. Adjust Values to Test Different Scenarios.
""")
st.sidebar.info('Example: A 30 years old male, 3rd class, $20 fare, travelinga alone from port Southempton.')
 
#Main Input Form
def main():
    st.subheader('Enter Passenger Details:')
    col1, col2 = st.columns(2)
    #Organize inputs in columns
    with col1:
        Pclass = st.selectbox('Passenger Class:', options = [1,2,3], format_func = lambda X: f'class{X}')
        Sex = st.radio("Sex:" , options = ['male', 'female'])
        Age = st.slider('Age:', min_value=0, max_value=100, value=30)
    with col2:
        SibSp = st.slider('Siblings/Spouses Abroad:', min_value=0, max_value=10, value=0)
        Parch = st.slider('Parents/Children Aboard:', min_value=0, max_value=10, value=0)

        Fare = st.slider('Fare($):', min_value=0.0, max_value=500.0, value=50.0, step=0.1)
        Embarked = st.radio('Port of Embarkation:', options=['C','Q','S'], format_func = lambda X : f'port{X}')

    #convert categorical inputs to numeric values
    Sex = 1 if Sex == 'female' else 0
    Embarked = {'C':0, 'Q':1, 'S':2}[Embarked]
    
    #Button for prediction
    if st.button('predict'):
        result = PredictionFunction(Pclass, Sex, Age, SibSp, Parch, Fare, Embarked)
        st.markdown(f'###{result}')
        st.balloons()
 
#Run the main function
if __name__ == '__main__':
    main()
 
