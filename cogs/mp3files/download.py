import json
import requests

def main():
    with open('/home/ami/src/venv/ADPhi-Bot/cogs/songs.json') as f:
        data = json.load(f)['songs']
    for x in range(1,11):
        doc = requests.get(data[x]['http'])
        name = f"{data[x]['name']}.mp3"
        with open(name, 'wb') as f:
            f.write(doc.content)

if __name__ == '__main__':
    main()



