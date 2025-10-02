import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI Backend!"}

@app.get("/api/hello")
def hello():
    return {"message": "Hello from the backend API!"}

@app.get("/api/events")
def get_events():
    # In a production app, load from a database or CMS
    events = [
        {"id": 1, "date": "2025-10-10", "title": "Fall Seed Swap", "time": "10:00 AM", "location": "Co-op Garden"},
        {"id": 2, "date": "2025-10-15", "title": "Compost 101 Workshop", "time": "6:00 PM", "location": "Community Center"},
        {"id": 3, "date": "2025-10-22", "title": "Harvest Box Pick-up", "time": "5:00 PM", "location": "Warehouse Bay 3"},
        {"id": 4, "date": "2025-11-05", "title": "Cover Crops & Soil Health", "time": "6:30 PM", "location": "Learning Farm"},
    ]
    return {"events": events}

@app.get("/api/instagram")
def get_instagram_posts():
    # For production: integrate Instagram Basic Display API and cache results
    posts = [
        {
            "url": "https://www.instagram.com/p/CxU9O1CqkzM/",
            "img": "https://images.unsplash.com/photo-1542838132-92c53300491e?q=80&w=1200&auto=format&fit=crop",
            "alt": "Farm fresh greens",
        },
        {
            "url": "https://www.instagram.com/p/CxU9O1CqkzM/",
            "img": "https://images.unsplash.com/photo-1463062511209-f7aa591fa72f?q=80&w=1200&auto=format&fit=crop",
            "alt": "Community garden bed",
        },
        {
            "url": "https://www.instagram.com/p/CxU9O1CqkzM/",
            "img": "https://images.unsplash.com/photo-1464226184884-fa280b87c399?q=80&w=1200&auto=format&fit=crop",
            "alt": "Compost turning",
        },
        {
            "url": "https://www.instagram.com/p/CxU9O1CqkzM/",
            "img": "https://images.unsplash.com/photo-1615485737651-6f4b7700f9b2?q=80&w=1200&auto=format&fit=crop",
            "alt": "Harvest box assortment",
        },
        {
            "url": "https://www.instagram.com/p/CxU9O1CqkzM/",
            "img": "https://images.unsplash.com/photo-1511690656952-34342bb7c2f2?q=80&w=1200&auto=format&fit=crop",
            "alt": "Seedlings in trays",
        },
        {
            "url": "https://www.instagram.com/p/CxU9O1CqkzM/",
            "img": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?q=80&w=1200&auto=format&fit=crop",
            "alt": "Colorful veggies",
        },
    ]
    return {"posts": posts}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
