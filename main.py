from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

@app.get("/get-download")
async def get_download(videoId: str):
    # This high-performance provider expects the raw video URL as a query target parameter
    youtube_url = f"https://www.youtube.com/watch?v={videoId}"
    target_api = "https://youtube-mp310.p.rapidapi.com/download/mp3"
    
    headers = {
        "x-rapidapi-key": "03bd2a143emshccdb36e550193fdp1cb1afjsnbaee8adb9e88", # Paste your exact RapidAPI key here
        "x-rapidapi-host": "youtube-mp310.p.rapidapi.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept": "application/json"
    }
    
    async with httpx.AsyncClient() as client:
        try:
            # Dispatch the request safely to the new endpoint
            response = await client.get(target_api, params={"url": youtube_url}, headers=headers, timeout=30.0)
            
            if response.status_code == 200:
                data = response.json()
                
                # Check for the key specific to this new API's structural layout
                if "downloadUrl" in data:
                    return {"mp3_url": data["downloadUrl"]}
                elif "mp3_url" in data:
                    return {"mp3_url": data["mp3_url"]}
                else:
                    return {"error": "Unexpected data format from new provider", "raw": data}
            else:
                return {"error": f"New API returned error code {response.status_code}", "details": response.text[:200]}
                
        except Exception as e:
            return {"error": "Proxy network exception", "details": str(e)}
