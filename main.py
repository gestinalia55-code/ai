# RUN IN GOOGLE COLAB - Modern Chat UI
import ipywidgets as widgets
from IPython.display import display, HTML
import random
from datetime import datetime

# Styling modern
style = """
<style>
.chat-container {
    max-width: 800px;
    margin: 20px auto;
    border-radius: 15px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}
.chat-message {
    margin: 15px 0;
    padding: 15px;
    border-radius: 20px;
    color: white;
    max-width: 70%;
}
.user-message {
    background: rgba(255,255,255,0.2);
    margin-left: auto;
    border-bottom-right-radius: 5px;
}
.ai-message {
    background: rgba(255,255,255,0.1);
    border-bottom-left-radius: 5px;
}
.quick-actions {
    display: flex;
    gap: 10px;
    margin: 20px 0;
}
.action-btn {
    background: rgba(255,255,255,0.2);
    border: none;
    padding: 10px 15px;
    border-radius: 25px;
    color: white;
    cursor: pointer;
}
</style>
"""

display(HTML(style))

class ModernChatAI:
    def __init__(self):
        self.name = "Nova"
        self.responses = {
            'greeting': ["👋 Halo! Saya Nova AI yang modern!", "🤖 Hai! Siap membantu dengan style!"],
            'time': [f"🕒 Sekarang {datetime.now().strftime('%H:%M')}"],
            'joke': ["😆 Kenapa AI tidak pernah sakit? Karena selalu ada di cloud!"],
            'default': ["✨ Itu pertanyaan menarik! Saya masih berkembang nih."]
        }
    
    def get_response(self, text):
        text = text.lower()
        if any(word in text for word in ['halo', 'hai']):
            return random.choice(self.responses['greeting'])
        elif 'jam' in text:
            return random.choice(self.responses['time'])
        elif 'lucu' in text:
            return random.choice(self.responses['joke'])
        else:
            return random.choice(self.responses['default'])

# Initialize
ai = ModernChatAI()
chat_history = widgets.Output()
input_text = widgets.Text(placeholder="Ketik pesan Anda...")
send_btn = widgets.Button(description="Kirim", button_style='primary')

def on_send_click(b):
    user_msg = input_text.value
    if user_msg:
        with chat_history:
            display(HTML(f'<div class="chat-message user-message">👤 {user_msg}</div>'))
            ai_msg = ai.get_response(user_msg)
            display(HTML(f'<div class="chat-message ai-message">🤖 {ai_msg}</div>'))
        input_text.value = ''

send_btn.on_click(on_send_click)

# Quick actions
quick_actions = widgets.HBox([
    widgets.Button(description="🕒 Waktu", layout=widgets.Layout(width='auto')),
    widgets.Button(description="😄 Joke", layout=widgets.Layout(width='auto')),
    widgets.Button(description="🤖 Perkenalan", layout=widgets.Layout(width='auto'))
])

def on_quick_action(b):
    if b.description == "🕒 Waktu":
        msg = "jam berapa"
    elif b.description == "😄 Joke":
        msg = "cerita lucu"
    else:
        msg = "hai"
    
    with chat_history:
        display(HTML(f'<div class="chat-message user-message">👤 {msg}</div>'))
        ai_msg = ai.get_response(msg)
        display(HTML(f'<div class="chat-message ai-message">🤖 {ai_msg}</div>'))

for btn in quick_actions.children:
    btn.on_click(on_quick_action)

# Display everything
display(HTML('<div class="chat-container">'))
display(HTML('<h2 style="color: white; text-align: center;">💬 Nova AI Modern</h2>'))
display(quick_actions)
display(chat_history)
display(widgets.HBox([input_text, send_btn]))
display(HTML('</div>'))