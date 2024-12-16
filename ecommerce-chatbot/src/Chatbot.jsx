import React, { useState } from "react";
import axios from "axios";

const Chatbot = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = { sender: "user", text: input };
    setMessages([...messages, userMessage]);

    try {
      const response = await axios.post("http://127.0.0.1:5000/api/chat", {
        message: input,
      });

      const botMessage = { sender: "bot", text: response.data.reply };
      setMessages((prev) => [...prev, botMessage]);
    } catch (error) {
      console.error("Error communicating with chatbot:", error);
    }
    setInput("");
  };

  return (
    <div className="app-container">
      <div className="chatbot">
        <div className="chat-header">Chatbot Assistant</div>
        <div className="chat-window">
          {messages.map((msg, idx) => (
            <div
              key={idx}
              className={`message-container ${
                msg.sender === "user" ? "message-user" : "message-bot"
              }`}
            >
              <div className={`message ${msg.sender}`}>{msg.text}</div>
            </div>
          ))}
        </div>
        <div className="input-area">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Type your message..."
            className="input-box"
          />
          <button onClick={sendMessage} className="send-button">
            Send
          </button>
        </div>
      </div>
    </div>
  );
};

export default Chatbot;
