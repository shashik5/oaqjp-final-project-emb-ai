"""
Unit tests for the emotion_detector function.
Uses unittest.mock to avoid live API calls.
"""
import unittest
from unittest.mock import patch, MagicMock
from EmotionDetection.emotion_detection import emotion_detector


def make_mock_response(emotion_scores, status_code=200):
    """Helper to create a mock requests.Response with emotion data."""
    mock_resp = MagicMock()
    mock_resp.status_code = status_code
    mock_resp.json.return_value = {
        'emotionPredictions': [
            {
                'emotion': emotion_scores
            }
        ]
    }
    return mock_resp


class TestEmotionDetector(unittest.TestCase):
    """Unit tests for emotion_detector function."""

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_joy_emotion(self, mock_post):
        """Test that a joyful statement returns 'joy' as dominant emotion."""
        mock_post.return_value = make_mock_response({
            'anger': 0.006, 'disgust': 0.002, 'fear': 0.011,
            'joy': 0.985, 'sadness': 0.005
        })
        result = emotion_detector('I am glad this happened')
        self.assertEqual(result['dominant_emotion'], 'joy')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_anger_emotion(self, mock_post):
        """Test that an angry statement returns 'anger' as dominant emotion."""
        mock_post.return_value = make_mock_response({
            'anger': 0.901, 'disgust': 0.024, 'fear': 0.032,
            'joy': 0.008, 'sadness': 0.035
        })
        result = emotion_detector('I am really angry at this')
        self.assertEqual(result['dominant_emotion'], 'anger')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_disgust_emotion(self, mock_post):
        """Test that a disgusting statement returns 'disgust' as dominant emotion."""
        mock_post.return_value = make_mock_response({
            'anger': 0.042, 'disgust': 0.876, 'fear': 0.015,
            'joy': 0.004, 'sadness': 0.063
        })
        result = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result['dominant_emotion'], 'disgust')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_sadness_emotion(self, mock_post):
        """Test that a sad statement returns 'sadness' as dominant emotion."""
        mock_post.return_value = make_mock_response({
            'anger': 0.018, 'disgust': 0.009, 'fear': 0.041,
            'joy': 0.007, 'sadness': 0.925
        })
        result = emotion_detector('I am really sad about this')
        self.assertEqual(result['dominant_emotion'], 'sadness')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_fear_emotion(self, mock_post):
        """Test that a fearful statement returns 'fear' as dominant emotion."""
        mock_post.return_value = make_mock_response({
            'anger': 0.051, 'disgust': 0.013, 'fear': 0.832,
            'joy': 0.012, 'sadness': 0.092
        })
        result = emotion_detector('I am scared I will lose my job')
        self.assertEqual(result['dominant_emotion'], 'fear')

    def test_blank_input(self):
        """Test that blank input returns None for all fields without API call."""
        result = emotion_detector('')
        self.assertIsNone(result['dominant_emotion'])
        self.assertIsNone(result['anger'])
        self.assertIsNone(result['disgust'])
        self.assertIsNone(result['fear'])
        self.assertIsNone(result['joy'])
        self.assertIsNone(result['sadness'])

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_status_400_returns_none(self, mock_post):
        """Test that a 400 response returns all None values."""
        mock_post.return_value = make_mock_response({}, status_code=400)
        result = emotion_detector('some invalid text')
        self.assertIsNone(result['dominant_emotion'])
        self.assertIsNone(result['anger'])


if __name__ == '__main__':
    unittest.main()
