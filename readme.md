# Ultraleap Streamlit

A Streamlit app for interfacing with Ultraleap camera using the Leap Motion SDK and viewing live feeds from the leap camera.

## Requirements

- Python 3.8
- LeapDeveloperKit_4.1.0
- The following files from the Leap Motion SDK must be present:
    - `Leap.dll`
    - `Leap.py`
    - `LeapPython.pyd`

> **Note:** These files are wrappers over the base Leap C SDK and are dependent on version 4.1.0.

## Setup Instructions

1. **Clone this repository:**
     ```bash
     git clone https://github.com/MJshah001/ultraleap_streamlit.git
     ```

     ```bash
     cd ultraleap_streamlit
     ```

2. **Create a virtual environment** (optional but recommended):
     ```bash
     python -m venv venv
     ```

3. **Activate the virtual environment:**
     - On Windows:
         ```bash
         venv\Scripts\activate
         ```
     - On macOS/Linux:
         ```bash
         source venv/bin/activate
         ```

4. **Install dependencies:**
     ```bash
     pip install -r requirements.txt
     ```

     If You see any errors in above command then pip might be outdated:
     
     Upgrade pip with:
    
     
     ```bash
     python -m pip install --upgrade pip setuptools wheel
     ```
     and then :
     ```bash
     pip install -r requirements.txt
     ```

5. **Run the Streamlit app:**
     ```bash
     streamlit run app.py
     ```

## Notes

- Ensure the Leap Motion SDK files (`Leap.dll`, `Leap.py`, `LeapPython.pyd`) are accessible in your project directory or Python path.

