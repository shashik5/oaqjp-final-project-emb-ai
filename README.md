# Emotion Detector

## Project Overview
An AI-based web application for detecting emotions in text using the **IBM Watson NLP** library. Built with Python and Flask, this application analyzes input text and returns emotion scores for anger, disgust, fear, joy, and sadness — along with the dominant emotion.

## Project Structure
```
EmotionDetector/
├── EmotionDetection/
│   ├── __init__.py            # Package init — imports emotion_detector
│   └── emotion_detection.py   # Core emotion detection function
├── templates/
│   └── index.html             # Web UI
├── server.py                  # Flask web server
├── test_emotion_detection.py  # Unit tests
├── requirements.txt           # Python dependencies
└── README.md
```

## Tasks Completed
| Task | Description |
|------|-------------|
| Task 1 | Cloned project repository |
| Task 2 | Created emotion detection application using Watson NLP library |
| Task 3 | Formatted the output to include individual scores and dominant emotion |
| Task 4 | Packaged as `EmotionDetection` Python package |
| Task 5 | Unit tests with `unittest` covering all 5 emotions + blank input |
| Task 6 | Web deployment via Flask on port 5000 |
| Task 7 | Error handling for blank input (HTTP 400) |
| Task 8 | Static code analysis with `pylint` (10/10 score) |

## Setup & Installation

### Prerequisites
- Python 3.8+
- pip

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run the Application
```bash
python server.py
```
Then navigate to [http://localhost:5000](http://localhost:5000).

### Run Unit Tests
```bash
python -m pytest test_emotion_detection.py -v
# or
python -m unittest test_emotion_detection.py -v
```

### Run Static Code Analysis
```bash
pylint server.py
```

## API Endpoint
```
GET /emotionDetector?textToAnalyze=<your text>
```

**Example Response:**
```
For the given statement, the system response is 'anger': 0.006, 'disgust': 0.002, 
'fear': 0.011, 'joy': 0.985 and 'sadness': 0.005. The dominant emotion is joy.
```

## Technologies Used
- **IBM Watson NLP** — Emotion prediction API
- **Python 3** — Core language
- **Flask** — Web framework
- **unittest / pytest** — Testing
- **pylint** — Static code analysis
