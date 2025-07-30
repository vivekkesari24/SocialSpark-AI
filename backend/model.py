from transformers import pipeline, set_seed
import re
import random

generator = pipeline('text-generation', model='gpt2')
set_seed(42)

def clean_caption(text, max_words=15):
    text = text.strip().split("\n")[0]
    text = re.split(r'[.!?]', text)[0]
    words = text.split()
    return " ".join(words[:max_words])

def append_hashtags(text, hashtags):
    tag_line = " ".join(random.sample(hashtags, min(2, len(hashtags))))
    return f"{text} {tag_line}" if not any(tag in text for tag in hashtags) else text

def generate_captions(theme, tone, mood, platform, hashtags):
    prompt = (
        f"Write a short, {tone.lower()} and {mood.lower()} Instagram caption about {theme.lower()} "
        f"with emojis and fun vibes. Keep it under 20 words."
    )

    results = generator(
        prompt,
        max_new_tokens=30,
        num_return_sequences=5,
        do_sample=True,
        temperature=1.0,
        top_k=50,
        pad_token_id=50256
    )

    captions = []
    for res in results:
        text = res['generated_text'].replace(prompt, "").strip()
        short_caption = clean_caption(text)
        caption = append_hashtags(short_caption, hashtags)
        captions.append(caption)

    return captions
