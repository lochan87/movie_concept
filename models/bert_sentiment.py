from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

try:
    tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
    bert_model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
except Exception as e:
    print(f"Error loading BERT model: {e}")
    exit(1)

def analyze_sentiment(text):
    try:
        # Tokenize the input text
        inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        
        # Get the output logits from the model (no gradient computation needed)
        with torch.no_grad():
            outputs = bert_model(**inputs)
        
        # Extract logits (raw output scores)
        logits = outputs.logits
        
        # Get the predicted class ID by selecting the maximum value (which corresponds to the highest probability)
        predicted_class_id = torch.argmax(logits).item()
        
        # Check the class label
        # Assuming the model has 3 classes: 0 = Negative, 1 = Neutral, 2 = Positive
        if predicted_class_id == 0:
            return "negative"
        elif predicted_class_id == 1:
            return "neutral"
        elif predicted_class_id == 2:
            return "positive"
        else:
            return "unknown"  # In case there's an unexpected class ID
        
    except Exception as e:
        print(f"Sentiment analysis error: {e}")
        return "error"
