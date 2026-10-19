from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

@app.get("/get-download")
async def get_download(videoId: str):
    youtube_url = f"https://www.youtube.com/watch?v={videoId}"
    
    # Updated direct routing endpoint path
    target_api = "https://rapidapi.com"
    
    # Clean parameters block structure
    query_params = {
        "yt": youtubeUrl
    }
    
    headers = {
        "x-rapidapi-key": "YOUR_ACTUAL_RAPIDAPI_KEY_HERE", # Put your exact key here
        "x-rapidapi-host": "youtube-mp3-download3.p.rapidapi.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept": "application/json"
    }
    
    async with httpx.AsyncClient() as client:
        try:
            # Separating parameters explicitly eliminates standard DNS lookup errors
            response = await client.get(target_api, params=query_params, headers=headers, timeout=30.0)
            if response.status_code == 200:
                return response.json()
            else:
                raise HTTPException(status_code=response.status_code, detail=f"Server returned error code: {response.status_code}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
