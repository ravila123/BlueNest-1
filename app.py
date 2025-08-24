import streamlit as st
import pandas as pd 
from db_funcs import *
from PIL import Image
import plotly.express as px
from datetime import date
import base64 

def color_df(val):
	if val == "Done":
		color = "green"
	elif val == "Doing":
		color = "orange"
	else:
		color = "red"

	return f'background-color: {color}'

st.set_page_config(
    page_title="BlueNest",
    page_icon="🐶",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Load sidebar image with caching to prevent reloading
@st.cache_data
def load_sidebar_image():
    bottom_img = Image.open('side art1.png')
    return bottom_img

bottom_image = load_sidebar_image()

# Function to convert image to base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Get base64 string of the wallpaper
wallpaper_base64 = get_base64_of_bin_file('to-do wallpaper.png')

# Custom CSS to use to-do wallpaper as background
st.markdown(f"""
<style>
    .stApp {{
        background-image: url("data:image/png;base64,{wallpaper_base64}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    
    .main-content {{
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(5px);
        border-radius: 15px;
        padding: 20px;
        margin: 20px 0;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        color: black !important;
    }}
    
    .main-title {{
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(10px);
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 20px;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.3);
        color: black !important;
    }}
    
    /* Make all text black except sidebar */
    .stApp * {{
        color: black !important;
    }}
    
    /* Blue title override - left aligned */
    .blue-title {{
        color: #1f77b4 !important;
        font-size: 2.5rem !important;
        font-weight: bold !important;
        text-align: left !important;
        margin-bottom: 1rem !important;
    }}
    
    /* Small "by Ravi" text */
    .by-author {{
        color: #666666 !important;
        font-size: 0.8rem !important;
        font-weight: normal !important;
        margin-left: 10px !important;
        vertical-align: baseline !important;
        position: relative !important;
        top: -0.2em !important;
    }}
    
    /* Sidebar text white */
    .sidebar .sidebar-content * {{
        color: white !important;
    }}
    
    .stSidebar * {{
        color: white !important;
    }}
    
    /* Specific overrides for form elements */
    .stTextInput > div > div > input {{
        color: white !important;
        background-color: rgba(0, 0, 0, 0.3) !important;
    }}
    
    .stSelectbox > div > div > div {{
        color: black !important;
    }}
    
    .stMarkdown {{
        color: black !important;
    }}
    
    .stSubheader {{
        color: black !important;
    }}
    
    /* Make Add New Task section text white */
    .add-task-section {{
        color: white !important;
    }}
    
    .add-task-section * {{
        color: white !important;
    }}
    
    /* Text input label white */
    .stTextInput label {{
        color: white !important;
    }}
    
    /* Form submit button styling */
    .stFormSubmitButton button {{
        background-color: rgba(255, 255, 255, 0.2) !important;
        color: white !important;
        border: 1px solid white !important;
    }}
    
    /* Stabilize sidebar images to prevent shaking */
    .stSidebar .element-container img {{
        width: 100% !important;
        height: auto !important;
        display: block !important;
        margin: 0 auto !important;
    }}
    
    /* Prevent sidebar layout shifts */
    .stSidebar {{
        min-width: 244px !important;
    }}
    
    /* Delete button styling - force no background */
    div[data-testid="column"]:nth-child(3) .stButton > button {{
        background: none !important;
        background-color: transparent !important;
        border: none !important;
        color: #ff4b4b !important;
        font-size: 14px !important;
        padding: 2px 4px !important;
        min-height: 20px !important;
        height: 20px !important;
        width: 20px !important;
        box-shadow: none !important;
        border-radius: 0 !important;
        line-height: 1 !important;
    }}
    
    div[data-testid="column"]:nth-child(3) .stButton > button:hover {{
        background: none !important;
        background-color: transparent !important;
        color: #d32f2f !important;
        transform: scale(1.1) !important;
        box-shadow: none !important;
    }}
    
    div[data-testid="column"]:nth-child(3) .stButton > button:focus {{
        background: none !important;
        background-color: transparent !important;
        box-shadow: none !important;
        outline: none !important;
    }}
    
    div[data-testid="column"]:nth-child(3) .stButton > button:active {{
        background: none !important;
        background-color: transparent !important;
        box-shadow: none !important;
    }}
</style>
""", unsafe_allow_html=True)

# Title with blue color - left aligned with small "by Ravi"
st.markdown('<h1 class="blue-title">🐶 BlueNest <span class="by-author">by Ravi</span></h1>', unsafe_allow_html=True)

# Sidebar
selected_user = st.sidebar.selectbox("Select User", ["Ravi", "Amitha"])
selected_date = st.sidebar.date_input("Select Date", value=date.today())
st.sidebar.image(bottom_image, use_container_width=True)
create_table()

# Add task section with white text (moved up)
st.markdown('<div class="add-task-section">', unsafe_allow_html=True)

with st.form("add_task_form", clear_on_submit=True):
	task = st.text_input(f"Add tasks to-do for {selected_user}")
	submitted = st.form_submit_button("Add Task")
	
	if submitted and task and task.strip():
		# Add task for the selected date (or today if today is selected)
		task_date = selected_date if selected_date else date.today()
		add_data(task, "ToDo", task_date)
		st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# Display tasks for selected date with checkboxes
if selected_date == date.today():
	st.subheader("Today's Tasks")
else:
	st.subheader(f"Tasks for {selected_date.strftime('%B %d, %Y')}")

selected_date_tasks = get_tasks_by_date(selected_date)

if selected_date_tasks:
	for i, (task_text, status, task_date) in enumerate(selected_date_tasks):
		col1, col2, col3 = st.columns([0.05, 0.9, 0.05])
		
		with col1:
			# Checkbox is checked if status is "Done"
			is_completed = status == "Done"
			checkbox_key = f"task_{i}_{task_text}_{selected_date}"
			completed = st.checkbox("", value=is_completed, key=checkbox_key)
			
		with col2:
			# Show task text with strikethrough if completed
			if completed:
				st.markdown(f"~~{task_text}~~")
				# Update status to Done if checkbox is checked
				if not is_completed:
					update_task_status(task_text, "Done")
			else:
				st.markdown(task_text)
				# Update status to ToDo if checkbox is unchecked
				if is_completed:
					update_task_status(task_text, "ToDo")
		
		with col3:
			# Delete button for each task
			delete_key = f"delete_{i}_{task_text}_{selected_date}"
			if st.button("🗑️", key=delete_key, help="Delete task"):
				delete_data(task_text)
				st.rerun()
else:
	if selected_date == date.today():
		st.info("No tasks for today. Add some tasks above!")
	else:
		st.info(f"No tasks found for {selected_date.strftime('%B %d, %Y')}.")


