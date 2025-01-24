import requests
import json
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk  # PIL (Pillow) library is used to handle images
from io import BytesIO

# Function to fetch and update the price
def update_price():
    try:
        # Fetch data from XMR Live feed API
        response = requests.get('https://api.diadata.org/v1/assetQuotation/Monero/0x0000000000000000000000000000000000000000')
        data = response.json()

        # Extract Price and Volume data
        price = data['Price']
        volume = data['VolumeYesterdayUSD']

        # Update the price and volume labels
        price_label.config(text=f"${price:,.2f}")
        volume_label.config(text=f"Volume: ${volume:,.0f}")
    except requests.exceptions.RequestException as e:
        # Handle any error from the request (e.g., network issue)
        print(f"Error fetching data: {e}")
        price_label.config(text="Error")
        volume_label.config(text="Error")

    # Call this function again after 1000 ms (1 second)
    root.after(1000, update_price)

# Set up the main window
root = tk.Tk()
root.title("Monero Price & Volume")
root.geometry("500x300")  # Width x Height of the window
root.config(bg="#1e1e1e")  # Dark background color

# Load the Monero logo image from the root of the repository
logo_path = "monero.png"
logo_image = Image.open(logo_path)
logo_image = logo_image.resize((50, 50))
logo_tk = ImageTk.PhotoImage(logo_image)

# Create a frame to contain the widgets
frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(pady=20)  # Add some padding

# Display the Monero logo
logo_label = tk.Label(frame, image=logo_tk, bg="#1e1e1e")
logo_label.grid(row=0, column=0, padx=10, pady=10)

# Create the price label with large font
price_label = tk.Label(frame, text="Loading...", font=("Helvetica", 30, "bold"), fg="#f2a900", bg="#1e1e1e")
price_label.grid(row=0, column=1, padx=50, pady=50)

# Create the volume label with smaller font
volume_label = tk.Label(frame, text="Volume: Loading...", font=("Helvetica", 14), fg="#f2a900", bg="#1e1e1e")
volume_label.grid(row=1, column=1, padx=10, pady=10)

# Add a small footer with "Powered by diadata.org"
footer_label = tk.Label(root, text="Powered by CRZYCYBR. Follow on YT for 64 Core XMR Miner Build", font=("Helvetica", 10), fg="#777777", bg="#1e1e1e")
footer_label.pack(side=tk.BOTTOM, pady=10)

# Start the price update loop
update_price()

# Start the Tkinter main loop
root.mainloop()
