# Graph Theory Experiments - Streamlit App

A web-based interface to view and run Graph Theory experiments (1-11) with side-by-side comparison of NetworkX implementations vs Manual implementations.

## Features

- 🔗 **NetworkX Implementations**: Uses NetworkX library functions
- 🛠️ **Manual Implementations**: Custom implementations without NetworkX (NN versions)
- 📊 **Visual Outputs**: See matplotlib visualizations directly in the browser
- 📝 **Code View**: Expand code sections to review implementation details
- 🎯 **Easy Navigation**: Select experiments from sidebar

## Installation

1. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit app:
```bash
streamlit run streamlit_app.py
```

The app will open in your default browser at `http://localhost:8501`

## Available Experiments

- **Experiment 1-6, 7, 9, 10**: Each has NetworkX and Manual (NN) versions
- **Experiment 8**: NetworkX version only
- **Experiment 11**: Multiple variants (3 different implementations)

## How to Use

1. **Select an experiment** from the sidebar dropdown
2. **View the code** by clicking "View Code" expander
3. **Run the experiment** by clicking the "Run" button
4. **See outputs**: Visualizations and console output appear below the button

## File Structure

```
├── streamlit_app.py          # Main Streamlit application
├── requirements.txt          # Python dependencies
├── e1.py                     # Experiment 1 (NetworkX)
├── e1NN.py                   # Experiment 1 (Manual)
├── expt2.py, expt2NN.py      # Experiment 2
├── expt3.py, expt3NN.py      # Experiment 3
├── expt4.py, expt4NN.py      # Experiment 4
├── expt5.py, exp5NN.py       # Experiment 5
├── expt6.py, expt6Fn.py      # Experiment 6
├── expt7.py, expt7NN.py      # Experiment 7
├── expt8.py                  # Experiment 8
├── expt9.py, expt9NN.py      # Experiment 9
├── expt10.py, expt10NN.py    # Experiment 10
├── expt11(1).py              # Experiment 11 - Variant 1
├── expt11(2).py              # Experiment 11 - Variant 2
└── expt11(3).py              # Experiment 11 - Variant 3
```

## Notes

- Each experiment displays code and visualization side by side (where applicable)
- NetworkX versions use library functions for efficiency
- Manual (NN) versions build graphs from scratch without NetworkX
- Experiment 11 has multiple variants shown in expandable sections
- All outputs are captured and displayed in real-time
