from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/get-download")
async def get_download(videoId: str):
    youtube_url = f"https://www.youtube.com/watch?v={videoId}"
    target_api = "https://rapidapi.com"
    
    headers = {
        "x-rapidapi-key": "03bd2a143emshccdb36e550193fdp1cb1afjsnbaee8adb9e88", # Make sure your real key is here
        "x-rapidapi-host": "youtube-mp3-download3.p.rapidapi.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept": "application/json"
    }
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(target_api, params={"yt": youtube_url}, headers=headers, timeout=30.0)
            
            # Read the raw text directly before trying to turn it into JSON
            raw_text = response.text
            
            try:
                # If it's standard JSON format, send it right down to the phone
                return response.json()
            except Exception:
                # If the provider sent raw text or a message instead, safely output it without crashing
                return {
                    "error": "The RapidAPI provider returned text instead of a JSON data link.",
                    "status_code": response.status_code,
                    "server_said": raw_text[:500] # Captures the exact message
                }
                
        except Exception as e:
            return {"error": "Proxy network connection error", "details": str(e)}
