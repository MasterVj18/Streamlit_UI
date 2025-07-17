# sensor_app.py
import streamlit as st
import asyncio
import websockets

SERVER_IP = "192.168.1.3"  # <-- Change this to your Base Station IP
SERVER_PORT = 8765

async def send_alert(alert_msg):
    uri = f"ws://{SERVER_IP}:{SERVER_PORT}"
    try:
        async with websockets.connect(uri) as websocket:
            await websocket.send(f"ALERT::{alert_msg}")
            st.success(f"✅ Sent: {alert_msg}")
    except Exception as e:
        st.error(f"❌ Failed to send: {e}")

def run_async_task(coro):
    """Helper to run asyncio tasks in Streamlit safely"""
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(coro)
        loop.close()
    except Exception as e:
        st.error(f"⚠️ Async Error: {e}")

# Streamlit UI
st.title("📱 Sensor App")
st.write("Send alert messages to machine.")

alerts = ["Wear seatbelt", "Proximity alert", "Idle time", "Sleepy operator"]

for alert in alerts:
    if st.button(alert):
        run_async_task(send_alert(alert))
