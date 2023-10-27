import json
import shutil

import uvicorn
from Pensieve.old.app import create_app
import threading
from pathlib import Path

import subprocess


def main():
    # Load configuration
    config_path = Path("config.json")

    if not config_path.exists():
        default_config_path = Path("Pensieve/resources/default_config.json")
        shutil.copyfile(default_config_path, config_path)

    config: dict
    with open(config_path, "r") as config_file:
        config = json.load(config_file)

    # Start up web gui server
    uv_config = uvicorn.Config(create_app, factory=True, port=5000, log_level="info")
    uv_server = uvicorn.Server(uv_config)
    def launch_web_server():
        uv_server.run()

    t = threading.Thread(target=launch_web_server)
    t.start()

    # Launch web browser for gui
    print("launching chrome")
    chrome = subprocess.Popen(["Pensieve\\resources\\chromium\\chrome.exe", "--app=http://127.0.0.1:5000/static/index.html"])

    try:
        chrome.wait()
    except KeyboardInterrupt:
        exit(-1)

    print("chrome killed")
    uv_server.shutdown()
    exit(0)


if __name__ == "__main__":
    main()
