from EmotionDetection.emotion_detection import emotion_detector
import unittest
class TestEmotionDetection(unittest.TestCase):
    def test_joy(self):
        res = emotion_detector("I am glad this happened")
        self.assertEqual(res.get('dominant_emotion',None),'joy')
    def test_anger(self):
        res = emotion_detector("I am really mad about this")
        self.assertEqual(res.get('dominant_emotion',None),'anger')
    def test_disgust(self):
        res = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(res.get('dominant_emotion',None),'disgust')
    def test_sadness(self):
        res = emotion_detector("I am so sad about this")
        self.assertEqual(res.get('dominant_emotion',None),'sadness')
    def test_fear(self):
        res = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(res.get('dominant_emotion',None),'fear')
if __name__ == '__main__':
    unittest.main()