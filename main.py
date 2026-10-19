from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

@app.get("/get-download")
async def get_download(videoId: str):
    youtube_url = f"https://youtube.com{videoId}"
    target_api = "https://rapidapi.com"
    
    headers = {
        "x-rapidapi-key": "03bd2a143emshccdb36e550193fdp1cb1afjsnbaee8adb9e88", # Paste your exact RapidAPI key here
        "x-rapidapi-host": "://rapidapi.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept": "application/json"
    }
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(target_api, params={"url": youtube_url}, headers=headers, timeout=30.0)
            
            if response.status_code == 200:
                data = response.json()
                
                # Check for the provider's actual raw download link keys
                if "downloadUrl" in data:
                    return {"mp3_url": data["downloadUrl"]}
                elif "download_url" in data:
                    return {"mp3_url": data["download_url"]}
                elif "link" in data:
                    return {"mp3_url": data["link"]}
                else:
                    raise HTTPException(status_code=500, detail="Could not extract download key mapping from provider data.")
            else:
                raise HTTPException(status_code=response.status_code, detail="Provider server connection failure")
                
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
