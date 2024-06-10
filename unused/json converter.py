import csv
import json
import os

def csv_to_custom_json(csv_file_path, json_file_path,desc):
    # Read the first row from the CSV file
    with open(csv_file_path, mode='r',encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file,delimiter="|")
        data = [row for row in csv_reader]  
    
    #JSON structure
    entry=[]
    for row in data:
        
        if len(row) == 1:
            s_entry = [
                {"description": desc},
                row
            ]
            entry.append(s_entry)
    # Read existing data from the JSON file if it exists
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as json_file:
            existing_data = json.load(json_file)
    else:
        existing_data = []
    
    # add new entry to the already stored entry
    existing_data.extend(entry)

    # Write the updated data back to the JSON file
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(existing_data, json_file, ensure_ascii=False, indent=4)

# Example usage
csv_file_path = 'data\\real reviews\\air purifier.csv'  # CSV file path -> the data
json_file_path = 'llm data.json'  # JSON file path
instructuion = "เขียนรีวิวเกี่ยวกับสินค้านี้ จากรายละเอียดสินค้า เเละ ตัวอย่างรีวิวที่ให้"
description = "เหมียวระเบิด หรือแมวระเบิด บอร์ดเกมปาร์ตี้สุดฮิตที่สร้างมาสำหรับทาสแมว การเล่นบอร์ดเกมนี้จะมีลักษณะคล้ายเกม UNO (อูโน่) และมีการเดิมพันการเล่นแบบรัสเชียนรูเล็ตต์ โดยจะมีกองการ์ดให้ผู้เล่นผลัดกันจั่วและเล่นการ์ด จนกว่าจะเจอเหมียวระเบิด เพราะหากเจอระเบิดเมื่อไรคุณจะต้องระเบิดตัวตายและออกจากเกมทันทีนอกจากว่าจะมีการ์ดปลดระเบิดที่จะช่วยชีวิตให้อยู่ต่อและสามารถกำหนดชะตาชีวิตได้ว่าการ์ดระเบิดครั้งต่อไปจะอยู่ตรงไหนในกอง เพื่อให้ผู้เล่นคนต่อไปได้ลุ้นในการเปิดการ์ด ความสนุกพาหัวร้อนของเกมไม่ได้มีแค่นี้ เพราะจะมีการ์ดความสามารถพิเศษพลังแมวเหมียวที่จะช่วยหลีกเลี่ยงเหมียวระเบิดได้อีก ไม่ว่าจะเป็น การ์ดข้าม การ์ดโจมตี การ์ดห้าม การ์ดช่วยหน่อย การดสับกอง การ์ดดูอนาคต และการ์ดแมวที่อยู่เดี่ยวๆจะไม่มีประโยชน์อะไร แต่หากอยู่เป็นคู่ หรือเก็บจำนวนตามคอมโบพิเศษก็เล่นได้อย่างสนุกมากขึ้น ต้องพยายามไม่ให้โดนระเบิดตาย และเหลือรอดเป็นคนสุดท้ายเพื่อเป็นผู้ชนะ บอร์ดเกมนี้เหมาะกับเป็นบอร์ดเกมเล่นกับเพื่อน เน้นการบลัฟ หักหลัง รับประกันว่าเป็นบอร์ดเกมสนุก กติกาที่ไม่ยุ่งยากที่ควรได้ลองเล่น"
csv_to_custom_json(csv_file_path, json_file_path,description)