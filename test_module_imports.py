import requests
import json
import time
import os
import asyncio
import random
import multiprocessing
import colorama
from tiktok_downloader import downloader
from TikTokApi import TikTokApi
from moviepy.editor import VideoFileClip, clips_array, ImageClip, CompositeVideoClip, vfx

def test_imports():
    try:
        print("requests version:", requests.__version__)
        print("json module imported successfully")
        print("time module imported successfully")
        print("os module imported successfully")
        print("asyncio module imported successfully")
        print("random module imported successfully")
        print("multiprocessing module imported successfully")
        colorama.init(autoreset=True)
        print("colorama imported and initialized successfully")
        print("tiktok_downloader imported successfully")
        api = TikTokApi()
        print("TikTokApi instantiated successfully")
        print("moviepy imported successfully")
        print("All modules imported and tested successfully")
    except Exception as e:
        print("Error during import or test:", e)

if __name__ == "__main__":
    test_imports()
