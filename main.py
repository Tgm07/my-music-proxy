from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

@app.get("/get-download")
async def get_download(videoId: str):
    # This generates the clean URL layout expected by the API converter system
    youtube_url = f"https://www.youtube.com/watch?v={videoId}"
    
    # Target endpoint path mapping
    target_api = "https://rapidapi.com"
    
    headers = {
        "x-rapidapi-key": "03bd2a143emshccdb36e550193fdp1cb1afjsnbaee8adb9e88", # Paste your exact key string right inside these quotes
        "x-rapidapi-host": "youtube-mp3-download3.p.rapidapi.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "application/json"
    }
    
    async with httpx.AsyncClient() as client:
        try:
            # Passing the parameter explicitly as a clean dictionary map prevents network routing failures
            response = await client.get(target_api, params={"yt": youtube_url}, headers=headers, timeout=30.0)
            
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": f"API returned code {response.status_code}", "details": response.text[:200]}
                
        except Exception as e:
            return {"error": "Proxy server network exception", "details": str(e)}
