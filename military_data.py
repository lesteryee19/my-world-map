import json

# 假設這是你從軍事新聞 (如 USNI) 或開放數據中收集到的座標
# 你可以利用之前練習過的 Web Scraping 技術來自動更新這些數據
military_units = [
    {
        "name": "羅斯福號航空母艦 (USS Theodore Roosevelt)",
        "lat": 14.59, 
        "lng": 120.98, 
        "type": "Carrier",
        "status": "部署中",
        "description": "目前位於西太平洋區域"
    },
    {
        "name": "橫須賀海軍基地 (United States Fleet Activities Yokosuka)",
        "lat": 35.28, 
        "lng": 139.67, 
        "type": "Naval Base",
        "status": "常駐",
        "description": "美軍在遠東的主要海軍基地"
    },
    {
        "name": "雷根號航空母艦 (USS Ronald Reagan)",
        "lat": 35.29,
        "lng": 139.66,
        "type": "Carrier",
        "status": "維修中",
        "description": "目前停泊於橫須賀"
    }
]

# 將數據存成 JSON 檔案，讓 JavaScript 可以讀取
with open('military.json', 'w', encoding='utf-8') as f:
    json.dump(military_units, f, ensure_ascii=False, indent=4)

print("軍事數據已成功轉換為 JSON 格式！")