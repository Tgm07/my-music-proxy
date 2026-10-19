from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

@app.get("/get-download")
async def get_download(videoId: str):
    # This acts like a secure backend tunnel using server data center credentials
    youtube_url = f"https://www.youtube.com/watch?v={videoId}"
    target_api = f"https://rapidapi.com{youtube_url}"
    
    headers = {
        "x-rapidapi-key": "YOUR_ACTUAL_RAPIDAPI_KEY_HERE", # Replace this text with your exact key string
        "x-rapidapi-host": "://rapidapi.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept": "application/json"
    }
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(target_api, headers=headers, timeout=30.0)
            # If the server returned clean data, forward it straight to the mobile app
            if response.status_code == 200:
                return response.json()
            else:
                raise HTTPException(status_code=response.status_code, detail="Proxy failed to fetch link")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
